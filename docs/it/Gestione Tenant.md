# Tenants

La SCMP è stata sviluppata come soluzione Multi-Tenant, ciò offre maggiore sicurezza, personalizzazione, flessibilità e scalabilità, con un'amministrazione più efficiente e costi ridotti.

Per permettere all’utente di gestire i tenant presenti nell’infrastruttura è stata resa disponibile la funzionalità “Tenant”, funzionalità disponibile non a tutti ma solo per gli utenti abilitati alla Gestione del servizio

Per accedere alla funzionalità, in alto a sinistra cliccare sul pulsante bento. Dopodiché, cliccare su “Tenant”.

![Accesso alla gestione Tenant](images/extract/media/image31.png)

### Creazione di un nuovo tenant

A questo punto, l’utente si ritrova all’interno della pagina del tab “Tenant” che contiene la lista dei tenant configurati sul sistema, per aggiungere un nuovo tenant cliccare il “menu” disponibile in alto a destra e selezionare la voce “+ Add”,.

![Aggiungi nuovo tenant](images/extract/media/image32.png)

Una volta premuto viene visualizzata la pagina di configurazione nuovo tenant  divisa in tre sezioni:

![Form di creazione nuovo tenant](images/extract/media/image33.png)

1. Parametri generali:

| **Nome** | **Descrizione** | **Obbligatorio** |
|----|----|----|
| Tenant ID | ID univoco del nuovo tenant | x |
| Tenant Name | Nome del tenant che verrà visualizzato all’ utente | x |
| Description | Una descrizione del tenant | x |
| MarketPlace Subscription ID | l’id ricevuto dal marketplace Azure alla sottoscrizione del servizio |  |

2. Data persistence:

| **Nome** | **Descrizione** | **Obbligatorio** |
|----|----|----|
| Inventory | Indica il numero di giorni per cui i dati relativi all ‘inventario saranno conservati nelle collections presenti su DB | x |
| Cost | Indica il numero di giorni per cui i dati relativi ai costi saranno conservati nelle collections presenti su DB | x |
| Monitoring | Indica il numero di giorni per cui i dati relativi al monitoraggio saranno conservati nelle collections presenti su DB | x |
| Security | Indica il numero di giorni per cui i dati relativi alla security saranno conservati nelle collections presenti su DB | x |

3. Init Catalog

In questa sezione è possibile selezionare gli elementi di catalogo che
verranno copiati automaticamente sul nuovo tenant.

La sezione iniziale (1) permette di scegliere una sola opzione tra:

- Empty Catalog: lasciare il catalogo vuoto senza eseguire nessuna copia di informazioni.
- Copy Catalog from Default Tenant: indica che il tenant dal quale recuperare le informazioni da copiare sia il tenant di Default.
- Copy Catalog from other Tenant: se viene selezionato nella sezione in basso verrà visualizzato un nuovo campo contenente la lista dei tenant disponibili così da permette la selezione del tenant dal quale recuperare le informazioni da copiare.

Successivamente è possibile compilare la sezione successiva (2) inserendo i campi non obbligatori:

- **Providers**: lista dei provider configurati nel tenant di partenza, selezionando uno o più provider ne verranno copiati gli elementi di catalogo nel nuovo tenant.
- **Copy SCMP Catalog**: se attivato tutti gli elementi presenti nel catalogo SCMP verranno aggiunti al nuovo tenant.
- **Copy Services**: se attivato tutti gli elementi presenti nel catalogo SCMP verranno aggiunti al nuovo tenant.
- **Copy Custom Services**: se attivato i servizi custom disponibili sul tenant verranno aggiunti al nuovo tenant.
- **Copy Blueprints**: se attivato tutte le Blueprint disponibili verranno aggiunte al nuovo tenant.

4. Association Catalog

In questa sezione è possibile selezionare il flag per abilitare il tenant all' utilizzo dei listini "Common" analizzati in seguito.
Selezionando questo campo non sarà piu necessario definire un catalogo specifico per il tenant, esso erediterà i listini comuni.

![Sezione di inizializzazione catalogo](images/extract/media/image34.png)

Per confermare l’inserimento del nuovo tenant cliccare il pulsante “Save” presente in basso a destra, dopo aver aspettato il caricamento verrà visualizzato un messaggio di conferma creazione e l’utente verrà riportato nella lista dei tenant dove sarà presente il nuovo tenant appena creato.

#### Visualizzazione, Modifica ed Eliminazione di un tenant

Nella lista dei tenant, in corrispondenza di ogni risultato è presente un “menù” con tre pulsanti:

- “Show”: permette la visualizzazione delle info sul tenant (indicato con una freccia rossa nell’ immagine).
- “Edit”: permette la modifica delle informazioni base del tenant (indicato con una freccia gialla nell’ immagine).
- “Delete”: permette l’eliminazione dell’utente dopo aver cliccato
  “conferma” nella modale visualizzata (indicato con una freccia viola nell’immagine).

![Pulsanti di controllo](images/extract/media/image35.png)

### Creazione tenant e sottosistemi automatizzata

Viene data la possibilità all' utente di automatizzare l'import di tenant e sottosistemi per velocizzare le operazioni di "onboarding".
Per accedere alla funzionalità è necessario cliccare il tab "import" disponibile in alto nella funzionalità "Tenants"

![Funzionalità di import tenant](images/extract/media/082425001.png)

Al centro della pagina troviamo un menu contestuale che permette la selezione della tipologia di import (Tenant o sottosistemi)

Analizziamo nel dettaglio le 2 pagine.

#### Import di Tenants

La funzionalità è composta da 2 sezioni:

1. La sezione "upload file" dove è possibile inserire un file in formato .xlsx (del quale possiamo scaricare un esempio utilizzando il tasto dedicato) {in rosso nella figura}
2. La sezione "configurazione" dove è possibile selezionare i parametri condivisi tra i tenant (in giallo nella figura), come descritto nella sezione ([Creazione di un nuovo tenant](#creazione-di-un-nuovo-tenant)).

Una volta inserite tutte le informazioni è possibile cliccare il pulsante "import"  (in verde nella figura) per validare il file inserito e iniziare il processo di import.

![Parametri di configurazione dei tenant](images/extract/media/082425002.png)

Dopo alcuni minuti è possibile utilizzare il pulsante "Results" (in rosa nell' immagine) per visualizzare il dettaglio delle operazioni eseguite dalla SCMP.

![Risultati degli import effettuati](images/extract/media/090425001.png)

#### Import di Sottosistemi

Per accedere alla funzionalità di import sottosistemi bisogna cliccare sul tab "subsystems" disponibile nella pagina di "import"

![Funzionalità di import sottosistemi](images/extract/media/082425003.png)

La funzionalità è composta da 2 sezioni:

1. La sezione "upload file" dove è possibile inserire un file in formato .xlsx (del quale possiamo scaricare un esempio utilizzando il tasto dedicato).
2. La selezione della tipologia di provider da importare

Una volta inseriti file e verificato che il provider sia compatibile è possibile cliccare il pulsante "import"  (in verde nella figura) per validare il file inserito e iniziare il processo di import.

![Funzionalità di import tenant e sottosistemi](images/extract/media/082425004.png)

Dopo alcuni minuti è possibile utilizzare il pulsante "Results" (in rosa nell' immagine) per visualizzare il dettaglio delle operazioni eseguite dalla SCMP.

![Risultati degli import effettuati](images/extract/media/090425001.png)

### Cataloghi "Common"

Viene data la possibilità all' utente di importare una serie di cataloghi per gli SKU o le risorse, che verranno poi utilizzati da tutti i tenant che hanno il [flag abilitato](#creazione-di-un-nuovo-tenant).

Per procedere con l'inserimento dei listini è possibile accedere alla pagina "Price list" disponibile sul modulo di amministrazione tenant

![Accesso a importazione cataloghi](images/extract/media/250530001.png)

Una volta all' interno della pagina. per visualizzare i dati, possiamo utilizzare il filtro "Provider" per selezionare la tipologia di provider del quale verificare lo stato dei listini.

![Filtro per provider](images/extract/media/250530002.png)

Possiamo utilizzare gli altri filtri presenti in pagina per:

- Visualizzare i dati di un anno specifico (filtro "Data")
- Visualizzare i cataloghi specifici per tenant selezionato (Filtro "tenant")

Per visualizzare i dati è necessario selezionare una sola tipologia di provider, cosi da visualizzare il calendario e la lista di listini applicati per un dato anno al tenant specificato e/o common.

All' interno della pagina troviamo la lista dei listini importati con il loro periodo di validità, per ogni riga viene indicato inoltre un colore, questo colore permette di identificare il listino nella sezione grafica sulla sinistra, questo calendario facilità l'individuazione dei periodi non coperti dal listino.

Viene visualizzata inoltre la lista dei listini "inattivi" che sono stati sostituiti in precedenza.

![Listini inattivi](images/extract/media/300625001.png)

#### Inserimento nuovo listino

Per inserire un nuovo listino è necessario cliccare l’ “hamburger menu” disponibile in alto a destra nella pagina delle risorse di catalogo e selezionare la voce “Import Catalogue”

![Accesso all "Importazione pianificata del catalogo"](images/extract/media/300625002.png)

Nella modale sono presenti tre parametri:

- Tenant: selezionare il tenant sul quale effettuare l'upload.
- Provider: Selezionare il provider relativo al listino che verrà inserito.
- Valid From: è possibile indicare una data di inizio validità del listino, nel giorno indicato in questa variabile il sistema aggiornerà automaticamente le risorse di catalogo per adeguarle al nuovo listino.

Se necessario l'utente può inserire un listino "common to all tenants" che verrà utilizzato da tutti i tenant configurati che contengano sistemi del provider di riferimento.

![Campi obbligatori per l'importazione](images/extract/media/300625003.png)

Inoltre sotto i parametri sono presenti due sezioni per l’upload del file, cliccando sul primo quadrato a sinistra sarà possibile selezionare un file di tipo “XLS” che contiene tutte le risorse da mappare.  
Cliccando sul secondo quadrato sarà possibile inserire un file di mappatura, seguendo le informazioni mostrate nella sezione “Aiuto” indicata con una icona “Punto di domanda”, cliccando su di essa verrà aperto un box, sotto le sezioni per l’upload che contiene tutte le informazioni relative al file di mapping da inserire .

![Messaggio di aiuto per il file di Mapping](images/extract/media/image190.png)

Dopo aver inserito tutti i parametri sarà possibile cliccare il tasto salva in basso, e verremo riportati nella pagina precedente che, dopo l'importazione visualizzerà il nuovo listino inserito.

#### Modifica validità e eliminazione dei listini

Per modificare un listino è necessario cliccare il menu in corrispondenza della riga della tabella contenente il listino, come indicato in figura, successivamente selezionare la voce edit per visualizzare la maschera di modifica

![Edit di un listino](images/extract/media/300625005.png)

All'interno della finestra è possibile modificare la data di validità del listino, sia per ridurne sia per estenderne la durata.
Se si seleziona l'opzione "Indefinite time", il listino resterà valido fino all'inserimento di un nuovo listino. A quel punto, il listino con validità indefinita verrà automaticamente disattivato e considerato valido fino al giorno di attivazione del nuovo listino.

Dopo l’aggiornamento, è necessario eseguire un refresh dei costi sui tenant coinvolti, in modo da calcolare correttamente il prezzo cliente in base ai listini aggiornati.

![Edit della validità di un listino](images/extract/media/300625006.png)

All’utente è inoltre data la possibilità di eliminare un listino. In questo caso, il periodo precedentemente coperto da quel listino rimarrà scoperto, ovvero senza una tariffa associata.

![Eliminazione listino](images/extract/media/300625007.png)

### Changelog delle modifiche ai listini

Utilizzando il tab "Price list changelog" disponibile in alto nella sezione "tenant administration" è possibile visualizzare una lista di operazioni effettuate sui listini  con indicazione delle date utilizzate per l'importazione e l'utenza di riferimento che ha effettuato le modifiche.

![Dettaglio dell' errore](images/extract/media/300625004.png)

Utilizzando il filtro disponibile in pagina possiamo visualizzare i dati di un solo tenant selezionato.
### Strumenti di reportistica

La funzionalità di reportistica, specifica per funzionalità, permette di generare dei report globali delle informazioni disponibili per i vari
provider, all’ interno delle pagine verrà data anche la possibilità di creare dei file per facilitare la condivisione delle informazioni.

Per accedere alla funzionalità, sopra il path del breadcrumb, cliccare sul tab “Reports”

![Accesso al report di Catalogo](images/extract/media/image141.png)

#### Tipologie di report disponibili

- **SKU non a Listino** – Elenco delle SKU , che hanno generato costi (recuperate tramite la funzionalità costi per ogni provider) che non sono presenti  nel listino prezzi inserito nella sezione "listini".

#### Creazione di un report

In alto sulla destra della pagina possiamo cliccare sul pulsante “New Report” per avviare la creazione di un report, nello specifico viene visualizzata una modale che contiene la lista delle tipologie di report disponibili.

![Creazione nuovo report](images/extract/media/image142.png)

Una volta selezionata la tipologia di report cliccare sul pulsante “Configure” per selezionare i provider da includere nel report, nella finestra appena aperta troviamo il campo “Provider” che permette di selezionare uno o più provider preesistenti nel sistema, successivamente è possibile selezionare uno o più sottosistemi da includere nel report, se non vengono selezionati dei provider non sarà possibile selezione nessun sottosistema. Infine è presente una sezione “tag” per includere le sole risorse che presentano il tag inserito

![Configurazione del report](images/extract/media/image143.png)


Per confermare la creazione di un report statico verificare che per il campo “Report type” sia stato selezionato “One-Shot” e cliccare il pulsante “Submit” presente in basso.

Dopo un periodo di caricamento sarà possibile visualizzare nella lista il report appena generato .

![Lista dei report effettuati](images/extract/media/image144.png)

<div class="no-print">

Rimosso nella release 8.0.0

### Sincronizzazione dei cataloghi tra tenant differenti

Viene implementata, all’interno della SCMP una funzionalità che permette all’utente di copiare un listino caricato precedentemente utilizzando un file XML nella funzionalità di catalogo, per farlo è necessario cliccare in corrispondenza del tenant di destinazione e cliccare la voce “Associate tenant”.

![Funzionalità di associazione cataloghi](images/extract/media/image36.png)

Verrà visualizzata una finestra che mostra la lista dei listini precedentemente associati. In basso, cliccando sul pulsante “Associate Catalog”, inizieremo la procedura di associazione.

![Avvio del processo di Associazione](images/extract/media/image37.png)

Il primo step necessario per l’associazione dei listini è la selezione della fonte, in questo caso del tenant che contiene il listino da associare

![Scelta del tenant "Fonte"](images/extract/media/image38.png)

Selezionando il tenant “Fonte” verrà visualizzata a schermo la lista dei listini presenti all’interno del tenant da cui è possibile selezionare uno o più elementi che verranno importati e associati automaticamente cliccando il pulsante “Associate Catalog”.

![Selezione del listino](images/extract/media/image39.png)

Verrà visualizzata una modale di conferma che ci informa di attendere qualche minuto per permettere al sistema di completare le operazioni e verremo riportati alla pagina “tenant”.

![Conferma di avvio del processo di importazione](images/extract/media/image40.png)

Nella lista dei tenant è possibile cliccare sulla riga corrispondente per visualizzare, oltre ai dettagli del tenant, anche la lista con all’interno il nuovo listino che abbiamo importato, sempre in questa pagina è possibile cliccare il tasto “Associate Catalog” per ripetere le operazioni appena descritte.

![Listino importato correttamente](images/extract/media/image41.png)

</div>
