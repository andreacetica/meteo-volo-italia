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

**Il semaforo personale: meteo × velivolo × titolo × esperienza**
- **Velivolo**: profili per **Tecnam P92** e **Cessna 172**, ognuno con i propri limiti personali (vento, raffiche, traverso, visibilità, base nubi, pioggia) e il traverso massimo dimostrato dal manuale.
- **Titolo di volo**: **VDS basico** o **VDS avanzato**, con le regole del DPR 133/2010 art. 9: volo solo dall'alba al tramonto; per il basico quota massima 500 ft dal suolo (1.000 ft sabato, domenica e festività nazionali) e distanza di almeno 5 km dagli aeroporti.
- **Esperienza recente**: se non voli da più giorni di quanti decidi tu, i limiti di vento si riducono della percentuale che scegli, e il semaforo te lo dice.
- Il semaforo **spiega sempre il perché**.

**Navigazione (pianificazione a terra)**
- Costruisci la rotta sulla mappa come in un'app EFB: tocca per aggiungere un punto, trascina per spostarlo, tocca per eliminarlo.
- Cerca aeroporti e aviosuperfici per codice, nome o comune, oppure paesi.
- **Log di navigazione** per ogni tratta: rotta vera, distanza, vento in quota all'ora di passaggio, correzione di deriva, prua vera e magnetica, velocità al suolo, tempi, orari, carburante.
- Schede degli aeroporti in rotta con **vento previsto all'arrivo** e pista consigliata.
- **Profilo verticale** della rotta: terreno, quota di crociera, base nubi stimata, margine minimo sul terreno e, per il VDS basico, la linea della quota massima consentita.
- Per il VDS basico, **avviso se la rotta passa a meno di 5 km da un aeroporto**.
- **Windy** integrato (widget ufficiale) centrato sulla rotta: vento, raffiche, nuvole, pioggia, temperatura, pressione.
- Mappa topografica o satellite, livello **spazi aerei openAIP** (serve una chiave gratuita) ed esportazione della rotta in **GPX**.
- **Avviso zone sulla rotta**: con la chiave openAIP l'app segnala ATZ, CTR, TMA e zone P/R/D attraversate, in base al titolo (VDS basico o avanzato). Dati non ufficiali.
- **Checklist "Verifica su AIP e NOTAM"**: per ogni rotta dice quali sezioni dell'eAIP ENAV controllare (ENR 5.1, ENR 5.6, ENR 2, AD 2) e quali campi chiamare.

## Come si usa

Apri il link dal computer o dal telefono. Su iPhone: Safari → **Condividi → Aggiungi alla schermata Home**.
Le impostazioni (campo base, limiti, velocità, consumo, chiave openAIP) restano salvate solo nel tuo browser.

## Da dove vengono i dati

| Dato | Fonte | Licenza |
|---|---|---|
| Previsioni meteo | [Open-Meteo](https://open-meteo.com) | CC BY 4.0 |
| Aeroporti, piste, frequenze | [OurAirports](https://ourairports.com) | pubblico dominio |
| METAR e TAF | [aviationweather.gov](https://aviationweather.gov) | pubblico dominio |
| Spazi aerei e seconda scheda dei campi | [openAIP](https://www.openaip.net), CC BY-NC 4.0 | `data/openaip-it.js`, aggiornato ogni settimana da GitHub Actions (`tools/aggiorna_openaip.py`) |
| Livello spazi aerei sulla mappa (facoltativo) | openAIP | con la chiave dell'utente |
| Quote del terreno | [Open-Meteo Elevation](https://open-meteo.com) (Copernicus DEM) | CC BY 4.0 |
| Mappa meteo animata | widget ufficiale di [Windy.com](https://www.windy.com) | termini Windy |
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
