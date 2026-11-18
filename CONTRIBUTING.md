# Come contribuire

Grazie! Il progetto migliora soprattutto grazie a chi vola e conosce i propri campi.

## Correggere i dati di un campo

1. Apri una **issue** con il titolo `Correzione <CODICE> – <nome campo>`.
2. Scrivi il dato sbagliato, quello corretto e **la fonte** (sito del gestore, AIP, WebAAI, carta del campo).
3. Le correzioni verificate vengono aggiunte in `correzioni.json` con la loro fonte, e poi si esegue `python3 tools/aggiorna_campi.py`.

Senza una fonte verificabile la correzione non viene inserita: in aviazione un dato sbagliato è peggio di un dato mancante.

Ricorda di non copiare contenuti protetti (per esempio le schede di Avioportolano): servono dati di fonti pubbliche o del gestore.

## Proporre funzioni o segnalare errori

Apri una issue descrivendo cosa ti aspettavi e cosa succede, con uno screenshot se puoi.

## Codice

L'app è un unico file `index.html` (HTML, CSS e JavaScript senza framework), così si può aprire anche in locale. Le pull request sono benvenute: mantieni lo stesso stile, testi in italiano e nessun servizio che richieda dati personali.
