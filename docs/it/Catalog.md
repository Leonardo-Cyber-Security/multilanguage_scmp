# Catalog

La sezione Catalog ha tre importanti funzionalità:

- Mostrare l’elenco degli asset installabili recuperati dai provider con i relativi prezzi e regioni associabili.
- Dare la possibilità all’amministratore del tenant di definire gli item utilizzabili successivamente per il provisioning.
- Dare la possibilità all’amministratore del tenant di definire gli item utilizzabili successivamente all’ interno delle simulazioni del modulo What If.

I prezzi recuperati, oltre a essere visibili all’interno del dettaglio dell’asset, vengono utilizzati per gli scenari What If e il calcolo dei
costi.

Per accedere alla funzionalità di Catalog, in alto a sinistra cliccare sul pulsante bento.

Dopodiché, cliccare su “Catalog” .

![Accesso a Catalog](images/extract/media/image149.png)

A questo punto, l’utente si ritrova all’interno della pagina del tab “Resources” .

Possiamo suddividere la funzionalità in 3 sezioni per specificarne il comportamento:

- Elementi di catalogo SCMP (riquadro giallo nell’ immagine).
- Elementi di catalogo dei Providers (riquadro verde nell’ immagine).
- Servizi e blueprint di catalogo SCMP (riquadro rosso nell’ immagine).

Di seguito analizzeremo ogni gruppo di funzionalità separatamente.

![Catalogo della SCMP](images/extract/media/image150.png)

### Gestione Elementi di catalogo SCMP

All’interno della pagina sono presenti una serie di filtri che una volta selezionati e cliccando sul pulsante che raffigura una lente d’ingrandimento verranno utilizzati per filtrare la lista dei risultati

![ Catalogo SCMP filtrato](images/extract/media/image151.png)

!!! warning "Associazione tra risorsa/SKU di catalogo SCMP e risorsa/SKU di catalogo Provider"

    Per permettere al sistema il corretto calcolo dei costi è necessario che la risorsa o lo SKU di catalogo SCMP contenga al suo interno un riferimento all' effettivo id che viene recuperato dal provider (come spiegato in questa sezione) in modo da sovrascrivere correttamente il costo della risorsa / SKU 

Accanto al pulsante che raffigura una lente d’ingrandimento, è presente il pulsante che raffigura una “X” per effettuare il reset dei filtri e della tabella delle risorse.

Sotto il filtro di ricerca, è presente il filtro di ricerca per tag.

Cliccare su di esso e selezionare un tag, a questo punto la tabella restituisce le risorse associate con il tag selezionato dall'utente.

#### Risorse e relazioni tra risorse

All’ interno della SCMP è possibile configurare una risorsa di tipo “Relazione”, questa relazione consente di mappare le macchine dei vari provider per modificarne i costi e permetterne l’utilizzo nelle altre funzionalità(ad esempio per il calcolo dei costi)

!!! warning "Relazioni automatiche"

    Se all' interno del catalogo SCMP è presente una risorsa di listino con l'indicazione dell UUID del provider ma senza relazione, la stessa verrà creata automaticamente e i costi verranno aggiornati di conseguenza.
    Dopo alcuni minuti la relazione sarà visibile anche all' interno del catalogo

Per accedere alla pagina delle relazioni cliccare il tab “SCMP Resources” in alto nella funzionalità di Catalogo

![Accesso a "SCMP resources"](images/extract/media/image152.png)

In alto è presente una sezione filtri che permette la ricerca per:

- “Search”: permette di inserire un testo libero per la ricerca.
- “Search By tags”: permette di cercare tramite i tag associati alle risorse.
- “Search by Service name”: permette la ricerca tramite nome del servizio.

##### Export delle risorse

Per esportare l’elenco delle risorse del Catalogo presenti all’interno della lista, all’interno della pagina in alto a destra cliccare sull'hamburger menu, e poi cliccare su “Export”

L’operatore avrà la possibilità di esportare la lista dei risultati in formato .csv e/o .json.

![Scaricare la lista di risultati](images/extract/media/image153.png)

##### Funzionalità Aggiornamento Forzato del Catalogo

Attraverso la funzionalità di Force Sync, è possibile richiedere un aggiornamento del catalogo cliccando sull'hamburger menù e successivamente cliccando su “Force Sync”

![Funzionalità Force Sync](images/extract/media/image154.png)

##### Creazione relazione di Catalogo

Per creare una risorsa sul Catalogo, sempre all’interno della pagina in alto a destra cliccare sull'hamburger menu, e poi cliccare su “Add Catalog Resource” .

![Opzione per aggiungere una risorsa](images/extract/media/image155.png)

A questo punto, l’utente si ritrova all’interno della pagina in cui è possibile selezionare il tipo di risorsa da creare

![Selezione del tipo di risorsa da creare](images/extract/media/image156.png)

Dal menu a tendina, selezionare il tipo di risorsa da creare. Dopodiché, cliccare sul pulsante “Next”. Ci si ritrova all’interno della pagina di compilazione della risorsa .

![Esempio di form per la creazione di una relazione](images/extract/media/image157.png)

I singoli parametri da inserire nella sezione “Properties” vengono specificati nella tabella:

Vengono indicati con \* i parametri obbligatori

| **Nome** | **Tipo** | **Descrizione** | **Esempio** |
|----|----|----|----|
| category | string | Inserire la categoria di appartenenza della risorsa | CAT0004BT |
| Price list code | string | Inserire il codice identificativo del listino prezzi dal quale vengono ricavate le associazioni | PRC005DE |
| confidential | boolean | Se abilitato indica che la risorsa è di tipo confidenziale | false |
| description | string | Inserire una descrizione libera della risorsa | Low end machine |
| Name\* | string | Inserire il nome della risorsa | 8Core16GB- small |
| RAM(GIB)\* | integer | Inserisci qui il la quantità in GiB utilizzate dalle macchine inserite nella relazione | 16 |
| VCPU\* | integer | Inserisci qui il numero di vCPU utilizzate dalle macchine inserite nella relazione | 8 |

All’interno della pagina di creazione della risorsa , compilare tutti i campi della sezione “Properties”. Dopo aver fatto ciò, selezionare uno o più tag per il campo “Add SCMP tag…” e compilare delle note all’interno della sezione “Tags & Note”

![Sezione tag e note](images/extract/media/image158.png)

All’interno della sezione “Relations”, aprire la sezione a sinistra, successivamente è possibile utilizzare i filtri “search” con testo libero o selezionare un “System Type” tra quelli disponibili per filtrare la tabella delle risorse

Una volta individuata la risorsa da associare portare , utilizzando il drag and drop, la risorsa dalla parte destra della pagina alla parte sinistra.

È possibile aggiungere una sola risorsa per tipologia di provider, se l’utente prova a inserire un'altra risorsa dello stesso provider apparirà un pop up che invita l’utente ad aggiungere una sola risorsa per provider.

![Selezione del provider per associare le risorse](images/extract/media/image159.png)

Possiamo effettuare una associazione “singola” inserendo in questa sezione una sola macchina, in questo modo il sistema ci permette di selezionare manualmente, nella sezione “Cost” in basso , un prezzo personalizzato da associare alla risorsa. Per farlo bisogna selezionare l’intervallo di fatturazione (orario, giornaliero, settimanale, mensile) e inserire a destra il costo relativo al periodo selezionato.

![Sezione costi delle relazioni](images/extract/media/image160.png)

Selezionando più di una macchina per provider, la sezione costi viene nascosta automaticamente, i costi applicati saranno definiti dalle percentuali configurate nei sottosistemi .

![Risorse associate alla risorsa SCMP](images/extract/media/image161.png)

Una volta inserite le risorse in relazione, nella sezione ‘Relations Chart’ si creerà automaticamente un diagramma illustrativo.

![Creazione automatica del Relation Chart](images/extract/media/image162.png)

Infine, in basso a destra, cliccare sul pulsante “Save” per salvare le modifiche. Apparirà un banner in basso che avvisa l’utente dell’avvenuta creazione della risorsa, e viene reindirizzato nella pagina contenente la lista di risorse.

##### Utilizzo della tabella di Catalogo

###### Visualizzazione riepilogo Risorsa

Per visualizzare i dati di una risorsa di SCMP, nella pagina “Resources” di Catalog, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul record di interesse, apparirà una finestra che riporta piccole informazioni della risorsa individuata: Sistema, Nome, Taglia, Data aggiornamento, RAM e CPU come presente nell’immagine seguente.

![Dettaglio rapido delle risorse di catalogo](images/extract/media/image163.png)

###### Visualizzazione delle relazioni di Catalogo

Per visualizzare i dati di una risorsa di SCMP, nella pagina “Resources” di Catalog, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Show” .

![Accesso alla risorsa in modalità view](images/extract/media/image164.png)

Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina della risorsa in modalità view, nel quale potrà visualizzare i dati ma non potrà modificarli .

![Dettaglio completo delle risorse di catalogo](images/extract/media/image165.png)

Il dettaglio di una risorsa è suddiviso in varie sezioni:

- Details.
- Properties.
- Tags & Notes.
- Relations.
- Cost, se presente
- Relations Chart.

![Sezione proprietà degli elementi del catalogo](images/extract/media/image166.png)

![Sezione Tags & Note degli elementi del catalogo](images/extract/media/image167.png)

![Sezione delle relazioni del catalogo SCMP](images/extract/media/image168.png)

![Sezione Relations Chart delle risorse](images/extract/media/image169.png)

In basso a destra, cliccare sul pulsante “Close”. L’utente verrà reindirizzato nella pagina “Resources” di Catalog.

###### Modifica delle relazioni di Catalogo

Per modificare una risorsa di SCMP, nella pagina “Resources” di Catalog, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Edit”.

![Accesso alla risorsa in modalità edit](images/extract/media/image170.png)

Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina della risorsa in modalità edit, a differenza della modalità ‘Show’ in quella ‘Edit’ è possibile modificare la sezione Properties e la sezione Cost.

In basso a destra, cliccare sul pulsante “Save”. A questo punto, in basso apparirà un banner che avvisa l’utente dell’avvenuto aggiornamento della risorsa.

Inoltre, l’utente verrà reindirizzato nella pagina “Resources” di Catalog.

![Modifica della relazione](images/extract/media/image171.png)

###### Eliminazione delle relazioni di Catalogo

Per eliminare una risorsa di SCMP, nella pagina “Resources” di Catalog, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Delete”.

![Eliminazione di una risorsa](images/extract/media/image172.png)

Fatto ciò, appare una modale in cui è necessario cliccare sul pulsante “Remove” per confermare l’eliminazione della risorsa

![Conferma eliminazione della risorsa](images/extract/media/image173.png)

#### Risorse e relazioni tra SKU

All’ interno della SCMP è possibile configurare una risorsa di tipo “SKU SCMP”, questa relazione consente di mappare gli SKU ricevuti dai provider per poterne definire i costi e l’unità di misura visualizzata nel sistema.

Per accedere alla pagina degli SKU cliccare il tab “SCMP SKU” in alto nella funzionalità di Catalog

![Accesso a "SCMP SKU"](images/extract/media/image174.png)

In alto è presente una sezione filtri che permette la ricerca per:

- “Search” : permette di inserire un testo libero per la ricerca
- “Search By tags” : permette di cercare tramite i tag associati alle risorse
- “Search by Service name”: permette la ricerca tramite nome del servizio.

##### Export delle risorse di catalogo

Per esportare l’elenco delle risorse del Catalogo presenti all’interno della lista, sempre all’interno della pagina del tab “SCMP” in alto a destra cliccare sull'hamburger menu, e poi cliccare su “Export” .

L’operatore avrà la possibilità di esportare la lista dei risultati in formato .csv e/o .json.

![Scaricare la lista di risultati](images/extract/media/image153.png)

##### Creazione relazione di Catalogo SKU

Per creare una risorsa sul Catalogo, sempre all’interno della pagina del tab “SCMP”, in alto a destra cliccare sull'hamburger menu, e poi cliccare su “Add Catalog Resource”.

![Opzione per aggiungere una risorsa “SKU”](images/extract/media/image175.png)

A questo punto, l’utente si ritrova all’interno della pagina di creazione di una risorsa ”SKU”, cliccare sugli accordion presenti in pagina per visualizzarne i dettagli.

![IPagina di creazione “SKU”](images/extract/media/image176.png)

Nella sezione “Properties”  compilare tutti i campi definiti nella tabella.

Vengono indicati con \* i parametri obbligatori

|**Nome**      | **Tipo** | **Descrizione** | **Esempio** |
|----|----|----|----|
| Price list code | string |Inserire il codice identificativo del  listino prezzi dal quale vengono ricavate le associazioni | PRI002FG |
| description | string  | Inserire una descrizione libera dello sku | This sku is the basic vm on this provider |
| name * |string |Inserire il nome dello SKU  |Simple vm sku |
| Service name  | string  | Inserire il nome del servizio correlato allo SKU  | inserire il nome del servizio |
| unit  | string  | Inserire un testo che verrà utilizzato come “unità di misura” visualizzata su tutte le funzionalità | MB/hour |
| Unit conversion Expression * | string  |Inserire la formula di conversione tra il valore ricevuto dal provider e il valore che verrà utilizzato nella SCMP (conversione tra unità di misura del provider e unità di misura indicata nella relazione SKU) “$var” indica il valore ricevuto dal provider | $var * 24 / 100 |

![Compilazione dei campi, selezione Properties](images/extract/media/image177.png)

Dopo aver inserito la formula di conversione è necessario cliccare sul pulsante “Test expression” per verificarne la correttezza.

Se è stata inserita correttamente il pulsante diventerà di colore “Verde” con scritto “TEST OK”, in caso contrario diventerà di colore “Rosso” “KO”, in questo caso la possibilità di salvare la relazione viene inibita.

![Conferma della formula di conversione](images/extract/media/image178.png)

Successivamente, selezionare uno o più tag per il campo “Add SCMP tag…” e compilare delle note all’interno della sezione “Tags & Note”.

Nella sezione “Relation” è possibile selezionare uno o più SKU provenienti dai vari cataloghi dei provider, per relazionarli tra loro e unificarne i costi, per farlo cliccare nella sezione “Composition” sulla sinistra, verrà aperta una sezione scura dove , tramite la tecnica del drag and drop possiamo spostare gli SKU disponibili nella sezione destra .

Nella sezione destra è possibile utilizzare i filtri per visualizzare solo i risultati pertinenti. I filtri disponibili sono: il provider d’origine , il nome del servizio e un campo di testo libero (in giallo nell’ immagine).

![Drag and drop Relazioni SKU](images/extract/media/image179.png)

Una volta inserite le risorse in relazione, nella sezione ‘Relations Chart’ si creerà automaticamente un diagramma illustrativo .

![Creazione automatica del Relation Chart](images/extract/media/image180.png)

Infine, cliccare il pulsante salva per confermare la creazione della relazione SKU, al termine si torna nella pagina contenente la lista di relazioni SKU dove potremo trovare all’ interno della lista la nuova
relazione.

##### Utilizzo della tabella del Catalogo

###### Visualizzazione riepilogo Risorsa di catalogo

Per visualizzare i dati di una risorsa SKU, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul record di interesse, apparirà una checkbox che riporta piccole informazioni della risorsa individuata: Sistema, Nome, Taglia, Data aggiornamento, nome e servizio come presente nell’immagine seguente .

![Dettaglio rapido delle risorse SKU](images/extract/media/image181.png)

###### Visualizzazione delle relazioni nel Catalogo

Per visualizzare i dati di una risorsa SKU, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Show” .

![Accesso alla risorsa in modalità view](images/extract/media/image182.png)

Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina della risorsa in modalità view, nel quale potrà visualizzare i dati ma non potrà modificarli .

![Dettaglio completo delle risorse di catalogo](images/extract/media/image183.png)

Il dettaglio di una risorsa è suddiviso in varie sezioni:

- Details.
- Properties.
- Tags & Notes : ove nel campo “Provider Tags…” non è possibile selezionare un tag, in quanto si ottiene automaticamente dal sottosistema a cui appartiene; il campo “Add SCMP Tag…” permette di selezionare dei tag da un elenco o inserirne uno manualmente; nel campo Notes è possibile inserire una nota testuale .
- Relations: ove presenti gli sku di provider in relazione .
- Cost.
- Relations Chart .

![Sezione proprietà degli elementi SKU di catalogo](images/extract/media/image184.png)

![Sezione Tags & Note degli elementi SKU di catalogo](images/extract/media/image185.png)

![Sezione delle relazioni degli SKU di catalogo](images/extract/media/image186.png)

![Sezione Relations Chart delle risorse](images/extract/media/image169.png)

In basso a destra, cliccare sul pulsante “Close”. L’utente verrà reindirizzato nella pagina contenente la lista delle risorse

###### Modifica delle relazioni del Catalogo

Per modificare una risorsa di SCMP, nella pagina “Resources” di Catalog, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Edit”.

![Accesso alla risorsa in modalità edit](images/extract/media/image170.png)

Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina della risorsa in modalità edit, a differenza della modalità ‘Show’ in quella ‘Edit’ è possibile modificare i parametri delle risorse

###### Eliminazione delle relazioni SKU di Catalogo

Per eliminare una risorsa SKU di catalogo, nella lista delle risorse, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Delete” .
![Eliminazione di una risorsa SKU](images/extract/media/image172.png)

Fatto ciò, appare una modale in cui è necessario cliccare sul pulsante “Remove” per confermare l’eliminazione della risorsa .

![Conferma eliminazione della risorsa](images/extract/media/image173.png)

#### Importazione pianificata di elementi di catalogo

L’inserimento manuale delle risorse di catalogo è un’operazione molto lunga e onerosa, per semplificare viene data la possibilità all’ utente di inserire un file “Excel” contenente i dati che verranno poi importati automaticamente nel giorno indicato come “Inizio validità”

##### Nuova importazione

Per inserire un nuovo listino è necessario cliccare l’ “hamburger menu” disponibile in alto a destra nella pagina delle risorse di catalogo e selezionare la voce “Import Catalogue”

![Accesso all "Importazione pianificata del catalogo"](images/extract/media/image187.png)

Dopo aver cliccato il pulsante, verrà aperta una modale, contenente due pulsanti:

- “Resources”: cliccando il pulsante indichiamo al sistema che il listino inserito conterrà delle risorse.
- “SKUs” cliccando il pulsante indichiamo al sistema che il listino inserito conterrà elementi SKU.

Una volta selezionata la tipologia di risorsa da creare la pagina si aggiorna per mostrare tutti i parametri obbligatori

![Scelta della tipologia di catalogo](images/extract/media/image188.png)

Nella modale sono presenti due parametri:

- Provider: Selezionare il provider relativo al listino che verrà inserito.
- Valid From: è possibile indicare una data di inizio validità del listino, nel giorno indicato in questa variabile il sistema aggiornerà automaticamente le risorse di catalogo per adeguarle al nuovo listino.

![Campi obbligatori per l'importazione](images/extract/media/image189.png)

Inoltre sotto i parametri sono presenti due sezioni per l’upload del file, cliccando sul primo quadrato a sinistra sarà possibile selezionare un file di tipo “XLS” che contiene tutte le risorse da mappare.  
Cliccando sul secondo quadrato sarà possibile inserire un file di mappatura, seguendo le informazioni mostrate nella sezione “Aiuto” indicata con una icona “Punto di domanda”, cliccando su di essa verrà aperto un box, sotto le sezioni per l’upload che contiene tutte le informazioni relative al file di mapping da inserire .

![Messaggio di aiuto per il file di Mapping](images/extract/media/image190.png)

Dopo aver inserito tutti i parametri sarà possibile cliccare il tasto salva in basso, e verremo riportati nella pagina di gestione dei cataloghi importati, dove sarà possibile monitorarne l’inserimento.

##### Gestione delle importazioni

Per inserire un nuovo listino è necessario cliccare l’ “hamburger menu” disponibile in alto a destra nella pagina delle risorse di catalogo e selezionare la voce “Imported Catalogues”

![Accesso ai cataloghi importati](images/extract/media/image191.png)

L’utente verrà quindi reindirizzato nella pagina contenente tutti i cataloghi importati precedentemente  all interno di questa pagina su ogni riga, che corrisponde ad un Upload , è possibile eliminare il file cliccando il pulsante “Tre punti” in corrispondenza della riga e cliccare la voce “Delete” per eliminarlo.

I cataloghi possono avere 3 stati differenti:

- Deleted: indica che il file è stato sostituito con una versione successiva.
- Success: indicato con un icona di colore verde, indica che il catalogo è pronto e verrà utilizzato partendo dal giorno indicato.
- In progress: indicato con un icona di colore giallo, indica che il sistema sta effettuando i controlli sulla validità delle informazioni inserite.

All’interno di questa pagina possiamo notare inoltre che gli upload effettuati con lo stesso file, vengono salvati utilizzando le versioni-, quindi all’ inserimento di un catalogo già esistente esso verrà sovrascritto con una versione superiore e le versioni precedenti verranno disattivate.

![Lista dei cataloghi importati](images/extract/media/image192.png)

Cliccando su una riga in stato “Success” della tabella verrà aperta una modale, all’ interno possiamo visualizzare uno specchietto riassuntivo che contiene, oltre alle informazioni di base, anche il numero di elementi , denominate “rows”, che sono state trovate nel file Excel.

Le righe disponibili nel file possono avere 3 stati differenti:

- Associated Rows: indica che il sistema riesce sia a creare la risorsa che ad associarla ad una size di catalogo del provider, per permetterne poi l’utilizzo durante il provisioning.
- Success Rows: indica che il sistema riesce a creare la risorsa ma non riesce ad effettuare la relazione con una risorsa del provider.
- Failed Rows: indica che il sistema non può inserire la risorsa.

![Dettagli dell' importazione](images/extract/media/image193.png)

In basso possiamo cliccare il pulsante “More Details” per visualizzare il dettaglio delle righe del file Excel che sono state scartate dal sistema , cliccando su una di esse possiamo visualizzare il numero della riga, il nome indicato nel file e l’errore che non ne ha permesso l’inserimento.

![Dettagli delle righe dell' importazione](images/extract/media/image194.png)

![Dettaglio dell' errore](images/extract/media/image195.png)

### Gestione elementi di catalogo dei Provider

All’interno del Modulo Catalog è possibile visualizzare la lista ed i dettagli delle “size” disponibili sui vari provider configurati sulla SCMP sia per le singole risorse (VM,STORAGE,NETWORK,SECURITY) che per i gruppi di risorse “SKU”.

#### Risorse

Per visualizzare la lista di risorse disponibili per un provider, selezionare in alto il menu “Cloud resources”(in rosso nell’ immagine) e selezionare uno dei provider disponibili (in giallo nell’ immagine), le funzionalità disponibili nelle pagine dei diversi provider sono identiche .

![Risorse del catalogo dei providers](images/extract/media/image196.png)

##### Export dei tagli del Provider

Per esportare l’elenco delle risorse del Catalogo visualizzate in pagina, in alto a destra cliccare sull'hamburger menu, e poi cliccare su “Export” .

L’operatore avrà la possibilità di esportare la lista dei risultati in formato .csv e/o .json.

![Esportazione dei risultati](images/extract/media/image197.png)

##### Funzionalità Aggiornamento Forzato del Catalogo e costi

È possibile forzare il sistema affinché dopo qualche minuto, vengano aggiornate automaticamente tutte le “size” e i relativi costi associati, per farlo, cliccare in alto a destra sull'hamburger menu, e poi cliccare su “Force Sync” .

![Funzionalità Force Sync](images/extract/media/image198.png)

##### Filtri delle risorse

Viene data la possibilità all’ utente di filtrare le liste di risorse visualizzate, in alto nella pagina è presente una sezione filtri  , i filtri disponibili sono:

- “search”: permette di cercare le risorse con un testo libero.
- “search by type”: permette di cercare le risorse di una sola tipologia specifica.
- “search by tags” permette di cercare tutte le risorse che contengono un tag specifico.

Dopo aver inserito uno o più filtri cliccare il pulsante “lente di ingrandimento” per effettuare la ricerca.

![Filtri del Catalogo](images/extract/media/image199.png)

##### Visualizzazione Riepilogo Risorsa

Per visualizzare l’anteprima di una risorsa in corrispondenza di una risorsa cliccare sul record di interesse, apparirà una modale che riporta le informazioni generali della risorsa individuata, tra cui: Sistema, Nome, Taglia , Data aggiornamento , RAM e CPU come presente nell’immagine seguente .

![Dettaglio rapido delle risorse di catalogo](images/extract/media/image200.png)

##### Visualizzazione dei dettagli delle Risorse

Per visualizzare i dati di una risorsa, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Show” . Dopo aver

![Accesso alla risorsa in modalità view](images/extract/media/image201.png)

fatto ciò, l’utente si ritrova all’interno della pagina della risorsa in modalità view, nel quale potrà visualizzare i dati ma non potrà modificarli
![Dettaglio Risorsa dal Modulo Catalog](images/extract/media/image202.png)

Il dettaglio di una risorsa è suddiviso in varie sezioni:

- Details
- Properties
- Tags & Notes
- Cost

Nella sezione Cost è possibile selezionare in successione la Regione, la Zona e la tipologia di Costo per ottenere una preview dei costi relativi alla risorsa selezionata .

![Sezione costi della risorsa](images/extract/media/image203.png)

In basso a destra, cliccare sul pulsante “Close” per tornare alla lista.

#### Risorse “On-Premise”

La gestione del catalogo risorse nei sistemi on-premise varia significativamente, risultando specifica per ogni sistema. In alcuni casi, la funzionalità di catalogo è assente, mentre in altri è disponibile ma non consente il recupero automatico delle risorse.

Viene data la possibilità all’ utente di definire un catalogo “Cloud” personalizzato direttamente nella SCMP, in questo modo successivamente sarà possibile aggiungere nelle relazioni delle risorse di “Catalogo SCMP” le risorse create.

Per farlo è necessario prima accedere al tab delle risorse di catalogo di un provider on-premise, nello specifico prendiamo come esempio “VMWare” selezionando la voce “VMWare” nel menù “Cloud resources" del modulo di catalogo

![Accesso al catalogo On-premise](images/extract/media/image204.png)

All’ interno della pagina, in alto sulla destra sopra la barra dei filtri, troviamo un menu contestuale, cliccare sull'icona “Tre linee” e selezionare “Add catalog resource” in questo modo verremo reindirizzati alla pagina, specifica per provider, di creazione della risorsa di catalogo.

![Creazione nuova risorsa](images/extract/media/image205.png)

A questo punto, l’utente si ritrova all’interno della pagina in cui è possibile selezionare il tipo di risorsa da creare .

![Selezione del tipo di risorsa da creare](images/extract/media/image156.png)

Dal menu a tendina, selezionare il tipo di risorsa da creare. Dopodiché, cliccare sul pulsante “Next”. Ci si ritrova all’interno della pagina di compilazione della risorsa.

![Esempio di form per la creazione di una risorsa](images/extract/media/image157.png)

All’ interno di questa pagina , dopo aver aperto le sezioni disponibili, inserire tutti i parametri necessari, nella sezione “Cost” in basso, sarà possibile aggiungere un prezzo personalizzato da associare alla risorsa. Per farlo bisogna selezionare l’intervallo di fatturazione (orario, giornaliero, settimanale, mensile) e inserire a destra il costo relativo al periodo selezionato.

![Sezione costi delle risorse](images/extract/media/image160.png)

#### Cloud SKU

Per visualizzare la lista degli sku disponibili per un provider, selezionare in alto il menu “Cloud SKU”(in rosso nell’ immagine) e selezionare uno dei provider disponibili (in giallo nell’ immagine), le funzionalità disponibili nelle pagine dei diversi provider sono identiche.

![Risorse del catalogo dei providers](images/extract/media/image206.png)

##### Export dei tagli del Provider disponibili

Per esportare l’elenco delle risorse del Catalogo visualizzate in pagina, in alto a destra cliccare sull'hamburger menu, e poi cliccare su “Export”.

L’operatore avrà la possibilità di esportare la lista dei risultati in formato .csv e/o .json.

![Esportazione dei risultati](images/extract/media/image197.png)

##### Funzionalità Aggiornamento Forzato del Catalog

È possibile forzare il sistema affinché dopo qualche minuto, vengano aggiornate automaticamente tutte le “size” e i relativi costi associati, per farlo, cliccare in alto a destra sull'hamburger menu, e poi cliccare su “Force Sync”.

![Funzionalità Force Sync](images/extract/media/image198.png)

##### Filtri delle risorse visualizzate

Viene data la possibilità all’ utente di filtrare le liste di risorse visualizzate, in alto nella pagina è presente una sezione filtri, i filtri disponibili sono:

- “search”: permette di cercare le risorse con un testo libero.
- “search by Service name”: permette di cercare le risorse relative ad una sola tipologia di servizio.
- “search by tags” permette di cercare tutte le risorse che contengono un tag specifico. Dopo aver inserito uno o più filtri cliccare il pulsante “lente di ingrandimento” per effettuare la ricerca.

![Filtri del Catalogo](images/extract/media/image207.png)

##### Visualizzazione Riepilogo Risorsa di catalogo

Per visualizzare l’anteprima di una risorsa in corrispondenza di una risorsa cliccare sul record di interesse, apparirà una modale che riporta le informazioni generali della risorsa individuata, tra cui: Sistema, Nome, Taglia , Data aggiornamento , nome del servizio

![Dettaglio rapido delle risorse di catalogo](images/extract/media/image208.png)

##### Visualizzazione dei dettagli delle Risorse nel catalogo

Per visualizzare i dati di una risorsa, in corrispondenza di una risorsa cliccare sul kebab menu e poi cliccare su “Show” . Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina della risorsa in modalità view, nel quale potrà visualizzare i dati ma non potrà modificarli

![Accesso alla risorsa in modalità view](images/extract/media/image201.png)

![Dettaglio Risorsa dal Modulo Catalog](images/extract/media/image209.png).

Il dettaglio di una risorsa è suddiviso in varie sezioni:

- Details
- Properties
- Tags & Notes
- Cost

Nella sezione Cost è possibile selezionare in successione la Regione, la Zona e la tipologia di Costo per ottenere una preview dei costi relativi alla risorsa selezionata.

![Sezione costi della risorsa](images/extract/media/image203.png)

In basso a destra, cliccare sul pulsante “Close” per tornare alla lista.

### Gestione elementi “Servizi e Blueprint”

#### Servizi

Per accedere alla funzionalità dei “Services”, in alto a sinistra cliccare sul pulsante bento e poi cliccare su “Catalog” .

![Accesso ai "Services"](images/extract/media/image210.png)

Dalla pagina “SCMP”, cliccare sul tab che raffigura tre quadrati uniti ‘Services’, posizionato sopra il path del breadcrumb. Fatto ciò, ci si ritrova all’ interno della pagina ‘Services’, viene visualizzata una lista di componenti denominati “Card” .

Ogni card fa riferimento ad un tipo di servizio specifico, essendo molti i servizi presenti il sistema ne esegue una paginazione, in basso possiamo utilizzare il campo “Item for page” per visualizzare più risultati oppure utilizzare le frecce per navigare tra le liste di servizi.

![Pagina dei servizi](images/extract/media/image211.png)

##### Filtri della pagina “Services”

Per facilitare l’utente nella ricerca di un servizio specifico è stata inserita nella pagina una sezione filtri laterale , all’ interno possiamo trovare tre filtri combinabili:

- “Filter by Text”: inserendo un testo in questo campo la lista di servizi verrà aggiornata per mostrare i servizi che riportano nel titolo o nella descrizione il testo inserito.(di colore arancione nell’ immagine).
- “Categories”: è possibile filtrare la lista per una o più categorie di servizi, la categoria viene inserita manualmente in fase di creazione del servizio (in verde nell’ immagine).
- “Tags”: è possibile selezionare uno o più tag per visualizzare solo i servizi che sono stati configurati con il tag (in rosso nell’ immagine).

Utilizzando i filtri in combinazione tra loro, sarà possibile visualizzare i soli servizi che soddisfano tutte le condizioni specificate. In altre parole, la query restituirà solo i servizi che coincidono con tutti i criteri impostati.

![Filtri disponibili](images/extract/media/image212.png)

##### Creazione Services

Dalla pagina “Services”, è possibile per l’utente poter creare un Service, accedendo nell’apposita sezione come mostrato in figura .

![Accesso al form di creazione del Service](images/extract/media/image213.png)

All’interno della pagina di creazione è necessario selezionare una tipologia di servizio utilizzando il campo "Service Type” per visualizzarne i parametri obbligatori

![Selezione della tipologia di servizio](images/extract/media/image214.png)

Nei prossimi paragrafi analizzeremo nel dettaglio le singole tipologie di servizi.

###### Servizi “Standard”

La prima tipologia di servizi disponibile per la SCMP sono i servizi “Standard”, questi servizi sono nativamente integrati nel sistema e il loro funzionamento non può essere modificato dall'utente.

Lista dei servizi offerti:

- CosmosDb Cassandra SQL
- CosmosDb Core SQL
- CosmosDb Mongo
- Kafka 3.2.1 on Ubuntu 20.04 LTS
- Kafka 3.2.1 on Ubuntu 22.04 LTS
- Mongo DB 5.0 on Ubuntu 20.04 LTS
- Mongo DB 6.0 on Ubuntu 20.04 LTS
- Mongo DB 6.0 on Ubuntu 22.04 LTS
- MySQL DB 8.0 on Ubuntu 20.04 LTS
- MySQL DB 8.0 on Ubuntu 22.04 LTS
- PostgreSQL 14 on Ubuntu 20.04 LTS
- PostgreSQL 14 on Ubuntu 22.04 LTS
- Redis DB 7.0 on Ubuntu 20.04 LTS
- Redis DB 7.0 on Ubuntu 22.04 LTS

Per inserire un nuovo servizio è necessario compilare tutti i campi della sezione properties, nello specifico:

- “Categories”: inserire un testo libero nel campo e selezionare dalla dropdown una categoria già configurata oppure è possibile aggiungere una nuova categoria cliccando il pulsante “+” nella dropdown (in arancione nella pagina).
- “Name”: il nome del servizio che sarà visualizzato nella card corrispondente.
- “Description”: la descrizione del servizio che verrà mostrata nella card relativa.
- “Upload File”: cliccando questo controllo sarà possibile selezionare dal proprio PC un file di tipo “immagine” che verrà visualizzato nella card del servizio.
- “Related Software”: in questa sezione è possibile selezionare uno o più software “Standard” che verranno poi utilizzati in fase di provisioning.

![Aggiunta nuova categoria](images/extract/media/image215.png)

Una volta inseriti tutti i dati è possibile salvare il servizio utilizzando il pulsante “save” in basso a destra, verrà visualizzata una modale di conferma e l’utente viene reindirizzato nella lista dei servizi disponibili.

###### Servizi “Custom”

Viene data la possibilità all’ utente di definire dei servizi “Custom” tramite inserimento di un file zip con all’ interno tutti file necessari per l’esecuzione.

In questo caso specifico il sistema SCMP viene utilizzato solo per salvare il servizio e lanciarne l’esecuzione, non è quindi possibile effettuare un controllo sulla correttezza del processo, che dovrà essere gestito dall'utente.

sono tutti orchestratori, ma con funzionalità e scopi differenti:

**1. Ansible:**

- **Orchestrazione di server e applicazioni:** Ansible automatizza la configurazione e la gestione di server e applicazioni su diverse piattaforme.

- **Esegue playbook YAML:** Ansible utilizza playbook YAML per definire le istruzioni da eseguire sui server.

- **Non richiede agent:** Ansible è agentLess, non richiede l'installazione di software sui server da gestire.

**2. Bicep:**

- **Linguaggio DSL per Azure:** Bicep è un DSL specifico per Azure che facilita la definizione di infrastruttura come codice.

- **Crea modelli ARM:** Bicep traduce i file in modelli ARM (Azure Resource Manager) che Azure utilizza per creare le risorse.

- **Si integra con Azure DevOps:** Bicep si integra con Azure DevOps per la gestione del ciclo di vita.

**3. Kubernetes:**

- **Orchestrazione di container:** Kubernetes è la piattaforma leader per l'orchestrazione di container su larga scala.

- **Automatizza la distribuzione e la gestione:** Kubernetes automatizza la distribuzione, il ridimensionamento e la gestione di container in cluster.

- **Offre un ecosistema di strumenti:** Kubernetes offre un ricco ecosistema di strumenti e librerie per la gestione dei container.

**4. Terraform:**

- **Infrastructure as Code:** Terraform è un tool open source per la gestione dell'infrastruttura come codice.

- **Definisce l'infrastruttura in file HCL:** Terraform utilizza file di configurazione HCL per definire l'infrastruttura desiderata.

- **Supporta diversi provider:** Terraform supporta un'ampia gamma di provider cloud e on-premise.

**In sintesi:**

- **Ansible:** Ideale per automatizzare la configurazione di server e applicazioni.

- **Bicep:** Ottimo per definire l'infrastruttura su Azure in modo leggibile.

- **Kubernetes:** Potente strumento per l'orchestrazione di container su larga scala.

- **Terraform:** Flessibile per gestire l'infrastruttura su più cloud provider o on-premise

Nella configurazione dei servizi “Custom” possiamo individuare una sezione comune composta dai parametri iniziali:

- “Categories”: inserire un testo libero nel campo e selezionare dalla dropdown una categoria già configurata oppure è possibile aggiungere una nuova categoria cliccando il pulsante “+” nella dropdown.
- “Name”: il nome del servizio che sarà visualizzato nella card corrispondente.
- “Description”: la descrizione del servizio che verrà mostrata nella card relativa.

![Parametri generali dei "Custom Services"](images/extract/media/image216.png)

Successivamente è necessario scegliere la tipologia di “orchestratore” da utilizzare  e inserire il file “.zip” corrispondente nella sezione “Upload File”, di seguito vengono indicate le specifiche per ogni tipologia:

| **Tipologia script** | **Contenuto obbligatorio del file .zip** |
|----|----|
| Ansible              | Instance.yaml - Vars.yaml                |
| Bicep                | Main.bicep - Main.parameters.json        |
| Kubernetes           | Solo files di tipo .YAML                 |
| Terraform            | Main.tf - Variable.tf - Provider.tf      |

Oltre ai files descritti nella tabella è possibile aggiungere nello zip un file di tipo “.png / .jpg / .img” che verrà poi utilizzato come immagine della Card corrispondente

![Selezione della tipologia di Orchestratore](images/extract/media/image217.png)

Una volta inseriti tutti i dati è possibile salvare il servizio utilizzando il pulsante “save” in basso a destra, verrà visualizzata una modale di conferma e l’utente viene reindirizzato nella lista dei servizi disponibili

###### Servizi “azure pipeline”

Viene data la possibilità all’ utente di definire dei servizi “Azure Pipeline” Questa tipologia di servizio permette alla SCMP di invocare l’esecuzione di una pipeline remota DEVOPS utilizzabile tramite la funzionalità di provisioning

Nella configurazione dei servizi “Azure Pipeline” possiamo individuare una sezione generale composta dai parametri:

- “Categories”: inserire un testo libero nel campo e selezionare dalla dropdown una categoria già configurata oppure è possibile aggiungere
  una nuova categoria cliccando il pulsante “+” nella dropdown “Name”: il nome del servizio che sarà visualizzato nella card corrispondente
- “Description”: la descrizione del servizio che verrà mostrata nella card relativa

![Parametri generali "Azure pipeline service"](images/extract/media/image218.png)

Anche per questo servizio sarà possibile, tramite il campo “upload File” , inserire un file di tipo “.zip” che contenga nello zip un file di tipo “.png / .jpg / .img” che verrà poi utilizzato come immagine della Card corrispondente.

Successivamente sarà necessario compilare i parametri specifici del servizio, in particolare bisognerà inserire:

- “Organizzazione” : il nome dell’ organizzazione DevOps dove risiede la pipeline.
- “Project”: il nome del progetto DevOps dove risiede la pipeline.
- “PAT”: il personal access token privato generato dal portale “Azure DevOps” Una volta compilati questi campi è possibile cliccare il pulsante “Test” per verificare i parametri inseriti.

Se i dati inseriti non sono validi verranno visualizzati diversi messaggi di errore che indicano quale parametro è errato (ad esempio: “Specified Organization is not valid.”) e il pulsante diventa rosso con scritto “KO”, quando tutti i parametri sono corretti il pulsante diventa di colore Verde con scritto “OK”.

![Parametri specifici delle Pipeline](images/extract/media/image219.png)

Dopo aver effettuato il test correttamente sarà possibile selezionare la pipeline da eseguire utilizzando il campo “Select Pipeline” e cliccando su una opzione disponibile .

![Selezione della pipeline](images/extract/media/image220.png)

Una volta inseriti tutti i dati è possibile salvare il servizio utilizzando il pulsante “save” in basso a destra, verrà visualizzata una modale di conferma e l’utente viene reindirizzato nella lista dei servizi disponibili

###### Servizi “HELM”

Possiamo configurare all’ interno della SCMP anche dei servizi di tipo “HELM”, per la configurazione di questi servizi è necessario inserire questi parametri  :

- “Categories”: inserire un testo libero nel campo e selezionare dalla dropdown una categoria già configurata oppure è possibile aggiungere una nuova categoria cliccando il pulsante “+” nella dropdown.
- “Chart name”: il nome effettivo del HELM CHART che verrà utilizzato.
- “Chart repository”: l’URL relativo alla repository contenente l’ HELM CHART da utilizzare.
- “Repository username”: se il repository indicata sopra è privata sarà necessario indicare un username per effettuare l’accesso al repository.
- “Repository password”: se il repository indicata sopra è privata sarà necessario indicare la password per l’utenza indicata in alto.
- “Chart version”: indica quale versione della chart utilizzare.
- “Cluster”: indicare quale è il cluster dove installare l'applicativo.
- “Description”: la descrizione del servizio che verrà mostrata nella card relativa.
- “Image”: in questa sezione è possibile inserire un file di tipo .png che verrà utilizzato come immagine del servizio su interfaccia.
- “Immutable”: Selezionando questo flag durante il provisioning non sarà possibile modificare le impostazioni e il servizio viene configurato automaticamente in base
- “Namespace”: inserire il nome per il namespace dove effettuare il deploy
- “Name”: il nome del servizio che sarà visualizzato nella card corrispondente.
- “Configurations”: in questa sezione è possibile caricare il file values.yaml che verrà utilizzato per il provisioning

![Parametri generali dei "HELM Services"](images/extract/media/image221.png)

Per questi servizi viene data inoltre la possibilità di impedire qualunque tipo di modifica del servizio, selezionando quindi la voce "immutable" e inserendo un namespace ed un cluster nel quale effettuare i deploy degli applicativi

![Parametro "immutabile"](images/extract/media/20250605003.png)

Una volta inseriti tutti i dati è possibile salvare il servizio utilizzando il pulsante “save” in basso a destra, verrà visualizzata una modale di conferma e l’utente viene reindirizzato nella lista dei servizi disponibili

##### Modifica ed Eliminazione Services

Oltre alla creazione di un Service, è possibile effettuare la visualizzazione, modifica ed eliminazione del suddetto

![Operazioni disponibili per i Services](images/extract/media/image222.png)

- Per modificare le informazioni di un “Service”, cliccare sul pulsante “Edit” all’interno della card. Dopodiché, all’interno del form, l’utente può modificare i dati necessari. Dopo aver effettuato le operazioni di edit, in basso a destra, cliccare sul pulsante “Submit”. Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina “Service” .

![Pagina di edit per un servizio](images/extract/media/image223.png)

- Per eliminare un “Service”, cliccare sul kebab menu di un suddetto e poi cliccare su “Delete”. Fatto ciò, appare una modale di conferma di eliminazione del Service. A questo punto, è necessario cliccare sul pulsante “Remove”.

![ Eliminazione di un servizio](images/extract/media/image224.png)

#### Gestione Blueprints

Per accedere alla funzionalità dei “Services”, in alto a sinistra cliccare sul pulsante bento e poi cliccare su “Catalog” .

![Accesso alle "Blueprint"](images/extract/media/image210.png)

Dalla pagina “SCMP”, cliccare sul tab che raffigura tre quadrati uniti ‘Blueprint’, posizionato sopra il path del breadcrumb. Fatto ciò, ci si ritrova all’ interno della pagina ‘Blueprint’, viene visualizzata la lista delle blueprint configurate nel sistema .

![Pagina delle Blueprint](images/extract/media/image225.png)

##### Aggiunta nuova blueprint

Dalla pagina “Blueprint”, è possibile per l’utente poter creare una nuova blueprint, accedendo nell’apposita sezione come mostrato in figura, cliccando l’“hamburger menu” presente in alto a destra e selezionando come opzione “Add Blueprint”.

![Aggiunta nuova Blueprint](images/extract/media/image226.png)

L’utente viene reindirizzato nello step 1 della creazione di una “Blueprint” dove è possibile inserire tutte le informazioni generali della blueprint. Dopo aver inserito i dati cliccare il pulsante “Save blueprint” per salvare la bozza della blueprint, per i dettagli sullo status è possibile consultare il paragrafo successivo.

![Blueprint step 1](images/extract/media/image227.png)

Viene aperta una modale di conferma inserimento, una volta cliccato “yes” per continuare l’utente visualizzerà lo stato 2 della creazione di una blueprint.

Cliccando “No” verrà annullato l’inserimento della bozza.

![Blueprint conferma della bozza](images/extract/media/image228.png)

Nello step 2 della creazione di una Blueprint è necessario cliccare all’ interno del campo “Upload File” e utilizzando la finestra di upload windows selezionare il file “.CSAR” che contiene la Blueprint .

Dopo aver selezionato un file cliccare sul pulsante “Upload” in basso a destra per lanciare il processo di validazione del file, seguendo la lista di stati presente nel paragrafo

![Inserimento file](images/extract/media/image229.png)

##### Status delle Blueprint

Essendo le “Blueprint” degli oggetti complessi, che devono essere opportunamente configurati, è stato inserito un sistema di validazione dei files inviati per permettere l’utilizzo dei soli servizi “Blueprint” configurati correttamente.

Nello specifico esistono 4 possibili “STATUS”:

1. READY TO USE (spunta di colore verde): indica che la blueprint è configurata correttamente e sarà possibile utilizzarla durante il “Provisioning”.
2. VERIFY (cerchio di colore giallo) indica che la SCMP sta validando il contenuto della Blueprint
3. FAILED (“X” di colore rosso): indica che il file inviato non è valido e dovrà essere reinserito dall'utente dopo averlo corretto.
4. DRAFT (di colore arancione): indica che la “blueprint” è stata creata come bozza ma non contiene all’ interno il file CSAR necessario, una volta inserito il file la blueprint passerà allo status VERIFY.

![Status delle Blueprint](images/extract/media/image230.png)

##### Visualizzazione, Modifica ed Eliminazione delle Blueprint

Nella tabella delle blueprint disponibili in corrispondenza di ogni riga, sulla destra è presente un menu contestuale, una volta aperto all’ interno troviamo tre funzionalità:

la funzionalità “View”: permette di visualizzare i dettagli della blueprint, una volta cliccato l’utente verrà reindirizzato nella pagina di visualizzazione della blueprint .

- Properties: in questa sezione è possibile modificare le informazioni base della blueprint (Figura 241).
- Provisioning plan: in questa sezione è presente il grafico bpmn che ci fornisce una rappresentazione grafica degli “step” previsti dalla “Blueprint” (Figura 242). In questa sezione sono presenti tre pulsanti per modificare il plan, il primo a forma di “cartella” permette l’upload sulla pagina di edit di un nuovo file BPMN , il secondo “download” permette di scaricare l’attuale file bpmn visualizzato , il terzo sulla destra “Upload” effettua la sovrascrittura dell’attuale file bpmn disponibile per la blueprint.
- Topology: La topologia di una blueprint è la disposizione dei componenti in un cluster Kubernetes. In questa sezione possiamo visualizzare graficamente la struttura del sistema tra i diversi pod, servizi e componenti (Figura 243).
- Update Model: in questa sezione è possibile eseguire l’upload del file CSAR, effettuando questa modifica la Blueprint tornerà nello stato di “VERIFY” per validarne il contenuto (Figura 244).

![Sezioni della pagina Blueprint "view"](images/extract/media/image231.png)

La funzionalità “Edit” permette di visualizzare e modificare tutti i parametri della blueprint, compreso il file CSAR relativo , contiene le seguenti sezioni:

- Properties: in questa sezione è possibile modificare le informazioni base della blueprint
- Provisioning plan: in questa sezione è presente il grafico bpmn che ci fornisce una rappresentazione grafica degli “step” previsti dalla “Blueprint”. In questa sezione sono presenti tre pulsanti per modificare il plan, il primo a forma di “cartella” permette l’upload sulla pagina di edit di un nuovo file BPMN , il secondo “download” permette di scaricare l’attuale file bpmn visualizzato , il terzo sulla destra “Upload” effettua la sovrascrittura dell’attuale file bpmn disponibile per la blueprint.
- Topology: La topologia di una blueprint è la disposizione dei componenti in un cluster Kubernetes. In questa sezione possiamo visualizzare graficamente la struttura del sistema tra i diversi pod, servizi e componenti .
- Update Model: in questa sezione è possibile eseguire l’upload del file CSAR, effettuando questa modifica la Blueprint tornerà nello stato di “VERIFY” per validarne il contenuto.

![Sezioni della pagina Blueprint "edit"](images/extract/media/image234.png)

![Sezione Plan di una Blueprint](images/extract/media/image235.png)

![Sezione Topology di una Blueprint](images/extract/media/image233.png)

![Sezione Model di una Blueprint](images/extract/media/image236.png)

La funzionalità “Delete”: permette di eliminare definitivamente la blueprint dal sistema. Per farlo basta confermare l’eliminazione cliccando il tasto “Yes” visualizzato nella modale di conferma eliminazione.

![Eliminazione di una Blueprint](images/extract/media/image237.png)

### Strumenti di reportistica

La funzionalità di reportistica, specifica per funzionalità, permette di generare dei report globali delle informazioni disponibili per i vari
provider, all’ interno delle pagine verrà data anche la possibilità di creare dei file per facilitare la condivisione delle informazioni.

Per accedere alla funzionalità, sopra il path del breadcrumb, cliccare sul tab “Reports”

![Accesso al report di Catalogo](images/extract/media/image141.png)

#### Tipologie di report disponibili

**CATALOG Missing SKU** – Elenco degli SKU di provider non presenti nel listino del catalogo SCMP, se presente. Di conseguenza, il prezzo cliente per gli SKU mancanti sarà dato dall'applicazione della percentuale di sconto/ricarico configurata nella sezione Administration

#### Creazione di un report

In alto sulla destra della pagina possiamo cliccare sul pulsante “New Report” per avviare la creazione di un report, nello specifico viene visualizzata una modale che contiene la lista delle tipologie di report disponibili.

![Creazione nuovo report](images/extract/media/image142.png)

Una volta selezionata la tipologia di report cliccare sul pulsante “Configure” per selezionare i provider da includere nel report, nella finestra appena aperta troviamo il campo “Provider” che permette di selezionare uno o più provider preesistenti nel sistema, successivamente è possibile selezionare uno o più sottosistemi da includere nel report, se non vengono selezionati dei provider non sarà possibile selezione nessun sottosistema. Infine è presente una sezione “tag” per includere le sole risorse che presentano il tag inserito

![Configurazione del report](images/extract/media/image143.png)

A questo punto l'utente può scegliere tra due diverse azioni:

- Creare un report statico che verrà salvato nel sistema.
- Programmare una schedula che generi il report periodicamente.

Per confermare la creazione di un report statico verificare che per il campo “Report type” sia stato selezionato “One-Shot” e cliccare il pulsante “Submit” presente in basso.

Dopo un periodo di caricamento sarà possibile visualizzare nella lista il report appena generato .

![Lista dei report effettuati](images/extract/media/image144.png)

##### Schedulazione del report

Se invece si vuole programmare l’esecuzione dei report automatica sarà necessario selezionare “Recurring” per il campo “Report Type”, in questo caso la finestra si aggiorna per mostrare i parametri aggiuntivi per la configurazione del report periodico .

I parametri da inserire sono:

- Period: permette di selezionare la frequenza di invio del report (oraria, giornaliera, ...).
- "Recive only if not empty" se selezionato il file non verrà inviato quando all interno non sono presenti informazioni
- Report Language: permette di selezionare la lingua utilizzata nel  report.
- File format: permette di selezionare una o più tipologie di file da includere nella mail.
- User E-mails: permette di inserire una mail alla quale inviare i report, dopo aver inserito una mail è necessario premere “Invio” sulla tastiera per confermarne l’inserimento, una volta premuto la mail appena inserita passerà nel box in fondo e il campo verrà svuotato per permettere l’inserimento, se necessario, di una nuova mail.

![Parametri dei report schedulati](images/extract/media/image145.png)

Avendo configurato tutti i parametri il pulsante “Submit” diventerà cliccabile, cliccarlo per confermare l’inserimento e dopo un periodo di caricamento sarà possibile visualizzare nella lista il report appena generato .

![Lista dei report effettuati](images/extract/media/image144.png)

##### Lista dei report schedulati

Per visualizzare la lista dei report schedulati, selezionare il tab “Scheduled” presente in alto sulla sinistra nella pagina dei report
.

![Lista dei report schedulati](images/extract/media/image146.png)

In questa pagina troviamo la lista e le relative informazioni dei report schedulati presenti nel sistema, per ogni risultato è possibile, cliccando il pulsante “Tre punti” sulla destra sarà possibile effettuare tre operazioni:

- Visualizzare l’ ultimo report generato .
- Editare le impostazioni della schedula, non sarà possibile modificare i provider o sottosistemi selezionati.
- Eliminare la schedula per interrompere l’invio delle e-mail.

![Modifica di una schedule](images/extract/media/image147.png)

##### Utilizzo dei report

Cliccando sulla riga di un report statico, o utilizzando il pulsante “Show report” disponibile per i report schedulati sarà possibile visualizzare la pagina di dettaglio del report selezionato .

All’interno del sommario del report dell’Inventory è presente la sezione “Stats” in cui sono presenti il numero dei dischi, delle interfacce, delle reti e delle virtual machines appartenenti al provider selezionato.

Sotto la sezione “Stats”, sono presenti i filtri usati dall'utente per generare il report.

Sotto i filtri, è presente la tabella riassuntiva delle risorse appartenenti ai provider. A destra sono presenti due pulsanti: “PRINT” ed “EXPORT”.

Cliccando sul pulsante “PRINT”, appare una modale di anteprima della stampa. Per stampare il report, cliccare sul pulsante in basso a destra “Stampa”, a questo punto si avvierà la stampa del suddetto.

Cliccando sul pulsante “EXPORT”, è possibile esportare il report in formato “.csv”, “. json” o “.pdf”.

Per tornare al tab “Results”, in basso a destra, cliccare sul pulsante “CLOSE” oppure in alto a sinistra cliccare sulla freccia che punta verso la sinistra, accanto al titolo del report.

![Dettagli dei report](images/extract/media/image148.png)
