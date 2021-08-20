<h1 align="center">Tor</h1>

### To Check

- DarkWebNews
- [Psychonautwiki](https://psychonautwiki.org/wiki/Main_Page)
- [Grams](https://grams-search.com/)

### Onion services

TorProject.org riceve soldi dal dipartimento degli stati uniti d'America per sviluppo e ricerca.
- ```I server Tor agiscono da router per costruire una rete privata virtuale a strati```
  - LV1: Client
  - LV2: Middleman
    - Server di rimbalzo dei dati
  - LV3: Exit Router
    - Server finali della rete Tor
  - LV4: Bridge Router
    - simili agli exit router (LV3)
    - sono server con identificatore privato per bypassare il blocco della rete Tor se viene applicata dagli ISP, o dallo stato, o altro
  - LV5: Tor Relay
    - ogni utente puo' essere un relay, puoi decidere se essere un middleman o un exit node
    - i middleman e gli exit node (LV3), anche loro sono relay
  - LV6: Pluggable Transports (PT)
    - Hanno il compito di transformare il flusso del traffico tor in traffico pulito tra il client e il bridge che altrimenti potrebbe essere intercettato dall'ISP con una tecnica chiamata DPI (deep packet inspection)
    - Chiamati anche **Bridge offuscati**
    - Protocolli
      - obfs2 (**NO**)
      - obfs3 (WAT)
      - obfs4 (Simile a ScrambleSuite) [**Presente di default su Tor Browser**]

## Conf

Installato e avviato Tor esso funzionera' come un **proxy locale in ascolto sulla porta 9050 tramite socks4 (nel 2017)** e **porta 9150 per Tor Browser**.

### Settare il proxy per farlo lavorare sulla porta di tor

### Tor Bundle, Tor Expert Bundle

- Firefox ESR -> Tor Browser -> Proxyserver SOCKS (9150)
  - Plugin già inseriti
    - TorLauncher
    - TorButton
    - NoScript
    - HTTPS Everywhere
  - Da inserire
    - qualcosa per fare un fake FingerPrint
      - CanvasBlocker
- TorChat
  - decentralizzato
- bridges.torproject.org/bridges
  - possono essere blacklistati

### Surf 

- The Hidden Wiki
- Exit Node Compromessi? Cripta tutto il traffico (HTTPS)
- I2P
- Freenet
- PGP asimmetrica = Diffie–Hellman
- GPG (GNU Provacy Guard) suite di tools alternativa a PGP


