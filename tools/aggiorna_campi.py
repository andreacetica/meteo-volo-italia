#!/usr/bin/env python3
"""Aggiorna l'archivio di aeroporti e aviosuperfici italiane dentro index.html.

Scarica i dati pubblici di OurAirports (pubblico dominio), tiene solo l'Italia,
applica le correzioni verificate di correzioni.json e riscrive la riga
`const AIRF=...;` in index.html.

Uso:  python3 tools/aggiorna_campi.py
"""
import csv, io, json, re, urllib.request, collections, datetime, pathlib

BASE = "https://raw.githubusercontent.com/davidmegginson/ourairports-data/main/"
ROOT = pathlib.Path(__file__).resolve().parent.parent


def get(name):
    with urllib.request.urlopen(BASE + name) as r:
        return list(csv.DictReader(io.StringIO(r.read().decode("utf-8"))))


def num(x):
    try:
        return round(float(x))
    except (TypeError, ValueError):
        return None


def main():
    ap = [r for r in get("airports.csv") if r["iso_country"] == "IT"
          and r["type"] in ("small_airport", "medium_airport", "large_airport")]
    ids = {r["id"] for r in ap}
    rw = collections.defaultdict(list)
    for r in get("runways.csv"):
        if r["airport_ref"] in ids and r["closed"] != "1":
            rw[r["airport_ref"]].append([r["le_ident"], r["he_ident"], num(r["length_ft"]), num(r["width_ft"]),
                                         r["surface"], num(r["le_heading_degT"]), num(r["le_elevation_ft"]),
                                         num(r["he_elevation_ft"])])
    fq = collections.defaultdict(list)
    for r in get("airport-frequencies.csv"):
        if r["airport_ref"] in ids:
            fq[r["airport_ref"]].append([r["type"], r["description"], r["frequency_mhz"]])
    out = []
    for r in ap:
        out.append({"c": r["icao_code"] or r["gps_code"] or r["ident"], "n": r["name"], "m": r["municipality"],
                    "t": r["type"][0], "la": round(float(r["latitude_deg"]), 5), "lo": round(float(r["longitude_deg"]), 5),
                    "e": int(float(r["elevation_ft"])) if r["elevation_ft"] else None,
                    "r": rw.get(r["id"], []), "f": fq.get(r["id"], []), "w": r["home_link"], "k": r["keywords"]})
    fixes = json.loads((ROOT / "correzioni.json").read_text(encoding="utf-8"))
    for a in out:
        if a["c"] in fixes:
            a.update({k: v for k, v in fixes[a["c"]].items() if not k.startswith("_")})
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    data = json.dumps(out, separators=(",", ":"), ensure_ascii=False)
    html, n = re.subn(r"^const AIRF=.*;$", lambda m: "const AIRF=" + data + ";", html, count=1, flags=re.M)
    assert n == 1, "riga const AIRF non trovata in index.html"
    html = re.sub(r"estratto del \d{2}/\d{2}/\d{4}", "estratto del " + datetime.date.today().strftime("%d/%m/%Y"), html)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"{len(out)} campi aggiornati in index.html")


if __name__ == "__main__":
    main()
