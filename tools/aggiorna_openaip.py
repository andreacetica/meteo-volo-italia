#!/usr/bin/env python3
"""Scarica i dati openAIP dell'Italia (spazi aerei e campi) e scrive
data/openaip-it.js, letto dall'app senza bisogno di chiave.

Dati openAIP (https://www.openaip.net), licenza CC BY-NC 4.0:
uso non commerciale con attribuzione. Dati della comunità, non ufficiali.

Uso:  python3 tools/aggiorna_openaip.py
"""
import json, urllib.request, datetime, pathlib, sys

BUCKET = "https://storage.googleapis.com/29f98e10-a489-4c82-ae5e-489dbcd4912f"
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "openaip-it.js"

def get(name):
    with urllib.request.urlopen(f"{BUCKET}/{name}", timeout=120) as r:
        return json.load(r)

def rnd(c):
    if isinstance(c, list):
        return [rnd(x) for x in c]
    return round(c, 5) if isinstance(c, float) else c

def lim(l):
    return {k: l.get(k) for k in ("value", "unit", "referenceDatum")} if l else None

def main():
    asp = get("it_asp.json")
    apt = get("it_apt.json")
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
