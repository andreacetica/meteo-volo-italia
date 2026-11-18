# ✈️ Meteo Volo Italia

**Pianifica il volo VFR in Italia in tre passi: dove vai, con cosa e quando. Poi un semaforo unico ti dice se si può fare, per tutto il volo.**
Per piloti VDS e PPL. Gratuito, open source, senza registrazione. Funziona nel browser e si installa sul telefono come un'app.

👉 **Apri l'app: https://andreacetica.github.io/meteo-volo-italia/**

> ⚠️ **Non è uno strumento ufficiale né operativo.** Serve a prepararsi a terra. Prima di ogni volo consulta sempre le fonti ufficiali (Aeronautica Militare, ENAC/WebAAI, AIP, NOTAM), il gestore del campo e il tuo istruttore. La decisione di volare è solo del pilota.

---

## Come funziona

**① Dove vai**
- Scrivi il nome o il codice del campo e scegli dal menu a tendina, oppure tocca la mappa: il primo punto è la destinazione, i successivi diventano tappe. Spunta **ritorno** per l'andata e ritorno.
- Senza destinazione è un **giro attorno al tuo campo** (30 minuti, 1 ora o 2 ore).

**② Con cosa e quando**
- **Velivolo** (Tecnam P92, Cessna 172) e **titolo** legato al velivolo: VDS basico o avanzato per l'apparecchio VDS, LAPL(A) o PPL(A) per il velivolo certificato.
- **Finestra di volo**: una striscia con tutti gli orari di partenza del giorno, ogni mezz'ora, colorata in verde, giallo o rosso in base al meteo **lungo tutto il volo** (partenza, rotta, arrivo) e alla luce del giorno. Tocchi un orario e lo scegli. L'app ti dice anche quali sono le **partenze migliori**.
- La sera, a giornata finita, l'app propone da sola **domani**.
- **Quota**: con il VDS basico l'app segue il terreno (massimo 500 ft dal suolo, 1.000 ft nel fine settimana e nei festivi, dal terreno più alto entro 5 km); con gli altri titoli scegli una quota fissa.

**③ Si può fare?**
- Un **semaforo unico per tutto il volo**, con una riga per ogni controllo **nell'ordine in cui lo incontri**: partenza, zone attraversate (con miglia e minuti dalla partenza), meteo lungo la rotta, aeroporti entro 5 km (VDS basico), arrivo, luce del giorno.
- Tocchi una riga e si apre la spiegazione: per le zone, cos'è, i limiti di quota in parole semplici, dove sei tu rispetto alla zona e dove verificarla sull'AIP. La zona si evidenzia sulla mappa.
- **Meteo confrontato tra 4 modelli** (ICON-2I di ItaliaMeteo, ECMWF, ICON di DWD, Météo-France): conta il valore peggiore confermato da almeno due modelli, e se un modello prevede qualcosa di molto diverso (raffiche, temporali, nebbia, base nubi) compare un avviso.
- Tiene conto dei **tuoi limiti personali** per ogni velivolo e dell'**esperienza recente** (limiti ridotti se non voli da tempo).

**E poi**
- **Condividi il piano** con un link, per esempio su WhatsApp con l'istruttore o con chi vola con te: chi lo apre vede lo stesso volo, con lo stesso orario e lo stesso velivolo.
- **Stampa il piano** o salvalo in PDF, da tenere in volo.
- **Log di navigazione** (rotta, vento all'ora di passaggio, deriva, prua vera e magnetica, velocità al suolo, tempi, carburante con riserva) ed esportazione **GPX**.
- **Profilo verticale** con terreno, base nubi stimata e, per il VDS basico, la fascia in cui puoi volare.
- **Checklist prima di partire**: quali sezioni dell'eAIP ENAV e quali NOTAM controllare per quel volo.
- **Scheda di ogni campo**: piste, vento in pista, METAR e TAF, seconda fonte openAIP, contatti verificati e i tuoi appunti.
- Meteo del campo ora per ora, Windy integrato, METAR e TAF vicini.

## Come si usa

Apri il link dal computer o dal telefono e installala: su iPhone, in Safari, **Condividi → Aggiungi alla schermata Home**; su Android, dal menu del browser, **Installa app**.
Le impostazioni (campo base, limiti, velocità, consumo, appunti) restano salvate solo nel tuo browser.

## Da dove vengono i dati

| Dato | Fonte | Licenza |
|---|---|---|
| Previsioni meteo | [Open-Meteo](https://open-meteo.com) | CC BY 4.0 |
| Aeroporti, piste, frequenze | [OurAirports](https://ourairports.com) | pubblico dominio |
| METAR e TAF | [aviationweather.gov](https://aviationweather.gov) | pubblico dominio |
| Spazi aerei e seconda scheda dei campi | [openAIP](https://www.openaip.net), CC BY-NC 4.0 | `data/openaip-it.js`, aggiornato ogni settimana da GitHub Actions (`tools/aggiorna_openaip.py`) |
| Livello colorato degli spazi aerei sulla mappa (facoltativo) | openAIP | con la chiave dell'utente |
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
