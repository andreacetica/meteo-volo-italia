#!/usr/bin/env python3
"""Scarica i dati openAIP dell'Italia (spazi aerei e campi) e scrive
data/openaip-it.js, letto dall'app senza bisogno di chiave.

Dati openAIP (https://www.openaip.net), licenza CC BY-NC 4.0:
uso non commerciale con attribuzione. Dati della comunità, non ufficiali.

Uso:  OPENAIP_API_KEY=la_tua_chiave python3 tools/aggiorna_openaip.py
"""
import json, os, urllib.request, datetime, pathlib, sys

API = "https://api.core.openaip.net/api"
KEY = os.environ.get("OPENAIP_API_KEY", "").strip()
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "openaip-it.js"

def get(what):
    """Scarica tutte le pagine di /airspaces o /airports per l'Italia."""
    out, page = [], 1
    while True:
        req = urllib.request.Request(f"{API}/{what}?country=IT&limit=1000&page={page}",
                                     headers={"x-openaip-api-key": KEY, "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            j = json.load(r)
        out += j.get("items", [])
        if page >= (j.get("totalPages") or 1):
            return out
        page += 1

def rnd(c):
    if isinstance(c, list):
        return [rnd(x) for x in c]
    return round(c, 5) if isinstance(c, float) else c

def lim(l):
    return {k: l.get(k) for k in ("value", "unit", "referenceDatum")} if l else None

def main():
    if not KEY:
        sys.exit("Manca la chiave: imposta il secret OPENAIP_API_KEY nel repository (Settings > Secrets and variables > Actions).")
    asp = get("airspaces")
    apt = get("airports")
    if not isinstance(asp, list) or not isinstance(apt, list) or len(asp) < 50 or len(apt) < 50:
        sys.exit("Dati openAIP inattesi: file non aggiornato.")
    A = [{"_id": a.get("_id"), "name": a.get("name"), "type": a.get("type"), "icaoClass": a.get("icaoClass"),
          "lowerLimit": lim(a.get("lowerLimit")), "upperLimit": lim(a.get("upperLimit")),
          "geometry": {"type": a["geometry"]["type"], "coordinates": rnd(a["geometry"]["coordinates"])}}
         for a in asp if a.get("geometry")]
    P = []
    for a in apt:
        if not a.get("geometry"):
            continue
        P.append({"name": a.get("name"), "icaoCode": a.get("icaoCode"), "type": a.get("type"),
                  "geometry": {"type": "Point", "coordinates": rnd(a["geometry"]["coordinates"])},
                  "elevation": a.get("elevation"), "ppr": a.get("ppr"), "private": a.get("private"),
                  "frequencies": [{k: f.get(k) for k in ("value", "unit", "type", "name")} for f in a.get("frequencies") or []],
                  "runways": [{"designator": r.get("designator"), "trueHeading": r.get("trueHeading"), "mainRunway": r.get("mainRunway"),
                               "dimension": r.get("dimension")} for r in a.get("runways") or []]})
    data = {"date": datetime.date.today().isoformat(), "asp": A, "apt": P}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("// Dati openAIP (www.openaip.net), CC BY-NC 4.0 - non ufficiali. Generato da tools/aggiorna_openaip.py\n"
                   "window.OAIP=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"Scritti {len(A)} spazi aerei e {len(P)} campi in {OUT}")

if __name__ == "__main__":
    main()
