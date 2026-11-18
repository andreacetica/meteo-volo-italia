# ✈️ Meteo Volo Italia

**Meteo, vento in pista, limiti personali e navigazione VFR per oltre 650 aeroporti e aviosuperfici italiani.**
Gratuito, open source, senza registrazione. Funziona nel browser, anche da telefono.

👉 **Apri l'app: https://andreacetica.github.io/meteo-volo-italia/**

> ⚠️ **Non è uno strumento ufficiale né operativo.** Serve a prepararsi a terra. Prima di ogni volo consulta sempre le fonti ufficiali (Aeronautica Militare, ENAC/WebAAI, AIP, NOTAM), il gestore del campo e il tuo istruttore. La decisione di volare è solo del pilota.

---

## Cosa fa

**Il tuo campo base**
- Scegli il tuo campo tra **660 aeroporti e aviosuperfici italiani**: piste, orientamento, lunghezza, fondo, quota e frequenze, quando sono in archivio.
- Un **semaforo** (nei limiti / attenzione / fuori limiti) per l'ora scelta e per le prossime 3 ore, con alba e tramonto.
- **Vento** al suolo con raffiche, a 80 m (circuito), a circa 2.500 e 5.000 ft.
- **Componenti del vento** per ogni testata (frontale/in coda e traverso, anche con le raffiche) e pista consigliata.
- **Cielo e visibilità**: nubi basse, medie e alte, base nubi stimata, visibilità, pioggia.
- **Temperatura e pressione**: punto di rugiada, umidità, QNH approssimato, zero termico, instabilità.
- Tabella **ora per ora** per oggi, domani e dopodomani.
- **METAR e TAF** dei 3 aeroporti più vicini.

**Limiti per velivolo**
- Profili per **Tecnam P92** e **Cessna 172**, ognuno con i propri limiti personali (vento, raffiche, traverso, visibilità, base nubi, pioggia) e il traverso massimo dimostrato dal manuale.

**Navigazione (pianificazione a terra)**
- Costruisci la rotta sulla mappa come in un'app EFB: tocca per aggiungere un punto, trascina per spostarlo, tocca per eliminarlo.
- Cerca aeroporti e aviosuperfici per codice, nome o comune, oppure paesi.
- **Log di navigazione** per ogni tratta: rotta vera, distanza, vento in quota all'ora di passaggio, correzione di deriva, prua vera e magnetica, velocità al suolo, tempi, orari, carburante.
- Schede degli aeroporti in rotta con **vento previsto all'arrivo** e pista consigliata.
- Mappa topografica o satellite, livello **spazi aerei openAIP** (serve una chiave gratuita) ed esportazione della rotta in **GPX**.

## Come si usa

Apri il link dal computer o dal telefono. Su iPhone: Safari → **Condividi → Aggiungi alla schermata Home**.
Le impostazioni (campo base, limiti, velocità, consumo, chiave openAIP) restano salvate solo nel tuo browser.

## Da dove vengono i dati

| Dato | Fonte | Licenza |
|---|---|---|
| Previsioni meteo | [Open-Meteo](https://open-meteo.com) | CC BY 4.0 |
| Aeroporti, piste, frequenze | [OurAirports](https://ourairports.com) | pubblico dominio |
| METAR e TAF | [aviationweather.gov](https://aviationweather.gov) | pubblico dominio |
| Spazi aerei (facoltativo) | [openAIP](https://www.openaip.net) | con la chiave dell'utente |
| Mappe | Esri, OpenTopoMap | vedi i rispettivi termini |
| Mappa interattiva | [Leaflet](https://leafletjs.com) | BSD-2 |

I dati dei campi sono compilati da volontari e possono essere incompleti o sbagliati. Le correzioni verificate sono in [`correzioni.json`](correzioni.json), ognuna con la sua fonte. Orari, PPR, pendenza delle piste e circuiti **non** sono inclusi: per quelli fanno fede WebAAI (ENAC) e il gestore.

## Contribuire

Hai trovato un dato sbagliato sul tuo campo? Apri una [segnalazione](../../issues) indicando il campo, il dato corretto e **la fonte** (sito del gestore, AIP, WebAAI). Leggi [CONTRIBUTING.md](CONTRIBUTING.md).

Per aggiornare l'archivio dei campi:

```
python3 tools/aggiorna_campi.py
```

## Autore

Ideato da **Andrea Cetica**, pilota VDS all'Aero Club Serristori (Castiglion Fiorentino).

Licenza [MIT](LICENSE).

---

### English

**Meteo Volo Italia** is a free, open-source, browser-based VFR helper for Italian pilots: weather, runway wind components, personal minimums per aircraft and leg-by-leg route planning for 650+ Italian airports and airstrips. Not for operational use: always check official sources before flight.
