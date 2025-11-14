# Inventory

La funzionalità di inventario raccoglie i metadati degli asset installati all’interno di tutti i provider presenti sulla SCMP.

Gli asset attualmente presenti sono:

- Virtual Machine
- Data Stores
- Networks
- Clusters
- Edge
- Security
- Others

I metadati eterogenei, provenienti da diverse fonti vengono poi normalizzati dalla SCMP per permettere una visualizzazione standard.

L’inventario è accessibile dalla voce di menu “Inventory”.

![Accesso a Inventory](assets/images/extract/media/image104.png)

### Dashboard di inventario

La pagina Dashboard permette di avere una visione globale e aggregata di tutte le risorse, mentre i menu sopra il path del breadcrumb danno la possibilità di filtrare per tipologia di risorsa. Le funzionalità disponibili nelle varie pagine sono identiche tra loro.

![dashboard di inventario](assets/images/extract/media/image105.png)

All’interno della pagina del tab “Resources”, sono presenti dei filtri, nel primo filtro in alto è possibile inserire la ricerca delle risorse in base al nome, al gruppo di risorse, provider, ecc., È inoltre possibile filtrare le risorse per “Provider” e “Subsystem”.

L’ultimo filtro permette la ricerca tramite tag. Cliccare su di esso e selezionare un tag, infine cliccando sul pulsante che raffigura una lente d’ingrandimento la pagina si aggiorna e si ottiene la lista delle risorse filtrate.

![Ricerca generica, per tag, per Provider e Subsystem](assets/images/extract/media/image106.png)

È possibile, inoltre, cliccare sui grafici per applicare automaticamente i relativi filtri.

#### Visualizzazione dettaglio risorsa

Per visualizzare il dettaglio di una risorsa, si può cliccare come in figura:

![Accesso alla risorsa in modalità lettura](assets/images/extract/media/image107.png)

Il dettaglio di un asset di inventario mostra in alto le caratteristiche principali come costo mensile, size della macchina e link esterno alla risorsa che punta al provider di riferimento.

Di seguito la visualizzazione dei dettagli di una VM:

![Dettaglio risorsa](assets/images/extract/media/image108.png)

E in calce le relazioni dell’asset con altri elementi di SCMP, come mostrato in figura:

![Grafico delle relazioni](assets/images/extract/media/image109.png)

Il grafico delle relazioni permette di navigare tra le risorse cliccando direttamente sul tondino della risorsa concatenata in relazione, al fine di atterrare sul dettaglio di quest’ultima.

Inoltre, è possibile editare alcuni attributi, come ad esempio i tags, come da figura:

![Selezione del tag](assets/images/extract/media/image110.png)

Per il campo “Provider Tags…” non è possibile selezionare un tag, in quanto i tag in questa sezione vengono recuperati direttamente dal sottosistema

Il campo “Add SCMP Tag…” permette di selezionare da un elenco o inserirne uno manualmente. All’interno del tag è presente il simbolo “X” per eliminare il suddetto.

È possibile inserire più tag per la risorsa.

Successivamente, in basso a destra della sezione “Tags & Note”, cliccare sul pulsante “Save” per salvare la modifica ed apparirà un banner in basso di avvenuto salvataggio del tag.

Scorrere la pagina verso il fondo, e cliccare sul pulsante “Close” posizionato a destra per tornare nella pagina del tab “Dashboard”.

#### Azioni sulle macchine di inventario

Per le macchine di inventario dei provider supportati è possibile utilizzare un nuovo pulsante disponibile nel menu contestuale delle tabelle chiamato “Manage” per effettuare delle operazioni di base sulle macchine.

![Accesso alla funzionalità di "management"](assets/images/extract/media/image111.png)

Da questa pagina di dettaglio della risorsa è possibile effettuare le seguenti operazioni utilizzando il menu in alto nella pagina, le operazioni disponibili sulle macchine possono variano a seconda del provider:

Azure Stack HCI

- Avvio della macchina
- Stop della macchina
- Ridimensionamento della macchina
- Aggiunta di dischi di memoria
- Aggiunta di una interfaccia di rete
- Eliminazione della risorsa
- Rimozione del disco nella risorsa
- Rimozione di un interfaccia di rete

Red Hat Edge

- Aggiornamento dell’immagine di un dispositivo EDGE

Le operazioni vengono indicate in bianco quando possono essere eseguite e in grigio quando non sono supportate o non disponibili per la risorsa.

![Operazioni sulle macchine di inventario](assets/images/extract/media/image112.png)

#### Funzionalità di “Cluster explorer”

Il Cluster Explorer è una funzionalità potente che consente agli utenti di visualizzare in modo dettagliato i namespace all'interno di un cluster. Questa funzione offre una panoramica completa dell'organizzazione dei dati e delle risorse all'interno del cluster, facilitando la navigazione e la gestione di ambienti complessi.

Con Cluster Explorer, gli utenti possono:

- Visualizzare l'elenco completo dei namespace in un cluster: Ottenere una rapida panoramica di tutti i namespace disponibili nel   cluster.
- Esaminare i dettagli di ogni namespace: Accedere a informazioni complete su ciascun namespace, tra cui nome, descrizione, etichette e quote di risorse.
- Filtrare e cercare i namespace: Trovare rapidamente i namespace specifici utilizzando criteri di filtro e ricerca avanzati.

Per accedere alla funzionalità bisogna selezionare dal menù orizzontale del modulo di Inventario, la voce “Clusters” .

![Accesso alla funzionalità di cluster explorer](assets/images/extract/media/image113.png)

All’ interno della pagina verrà visualizzata la lista dei cluster presenti all’ interno dei sottosistemi configurati nel sistema, cliccando su uno di essi si aprirà una modale con i dettagli generali del cluster .

![Finestra di dettaglio del cluster](assets/images/extract/media/image114.png)

Possiamo notare che in basso a destra è presente un pulsante “cluster explorer”, premendolo verremo reindirizzati alla dashboard del cluster. È possibile accedere a questa pagina anche utilizzando il pulsante “cluster explorer” disponibile nel menu contestuale “tre punti” presente per ogni cluster nella lista di risultati.

All’interno di questa pagina possiamo visualizzare un grafico che rappresenta la distribuzione dei namespace all’interno del cluster, sulla destra viene visualizzata la legenda dei namespace con il numero di pod attivi.

![Dashboard del “cluster explorer”](assets/images/extract/media/image115.png)

Possiamo scendere nel dettaglio dei namespace utilizzando diversi componenti nella pagina:

è possibile cliccare sul pulsante in alto a destra “Explore namespaces” o cliccare sul numero di namespace visualizzato in alto a sinistra per visualizzare la pagina di esplorazione dei namespace senza filtri , se vogliamo visualizzare direttamente il dettaglio di un namespace presente nel grafico è possibile cliccare sulla relativa fetta e la pagina di dettaglio verrà filtrata automaticamente per namespace selezionato

![Pagina "Namespace explorer"](assets/images/extract/media/image116.png)

Il campo namespaces presente in alto permette di effettuare una ricerca tra i cluster disponibili inserendo un testo libero. Se viene trovata una corrispondenza, è possibile selezionare il namespace dalla lista così da visualizzarne il dettaglio.

![Dettaglio dei namespace](assets/images/extract/media/image117.png)

Utilizzando i comandi “Freccia in basso” sarà possibile navigare tra le categorie e sotto-categorie di elementi disponibili, infine selezionando un risultato sarà possibile visualizzarne i dettagli nella sezione destra della pagina, che verrà popolata automaticamente con il risultato selezionato sulla sinistra .

![Dettagli del contenuto del namespace](assets/images/extract/media/image118.png)

### Funzionalità “WHAT IF”

Questa funzionalità permette di eseguire delle simulazioni per la migrazione degli asset da un provider a un altro, o all’ interno dello stesso provider in modo da poter confrontare i costi di gestione e mantenimento.

Per eseguire una simulazione, cliccare sopra il path del breadcrumb il tab che raffigura una relazione che collega due entità denominato ‘What If’ .

![Accesso a “What If”](assets/images/extract/media/image119.png)

Dopo aver fatto ciò, ci si ritrova all’interno della pagina del tab “What If” .

Possiamo notare sopra la lista delle simulazioni, sulla destra, due tab che permettono di filtrare la lista per tipologia di simulazione, nello specifico:

all’apertura della pagina verranno visualizzate tutte le simulazioni di tipo “Change Provider” mentre cliccando sul tab “Capacity” sarà possibile visualizzare la lista delle simulazioni di tipo “Change size”.

![](assets/images/extract/media/image120.png)
![Pagina di “What If”](assets/images/extract/media/image121.png)

#### Scenario “What If”: Provider Migration

Per effettuare una simulazione del “What If: Migrate Provider”, cliccare nel riquadro a sinistra intitolato “Migrate to another provider”

![Accesso alla funzionalità "What If: Migrate Provider"](assets/images/extract/media/image122.png)

Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina “Start” dello step 1 per la simulazione della migrazione delle risorse da un cloud provider ad un altro.

A sinistra nel riquadro “Select Resources to migrate”, l’utente può ricercare le risorse tramite tre tipi di filtri tra cui:

- “Search” che consente di cercare una risorsa per nome;
- “Search by Type” di ottenere le risorse tramite la selezione del tipo di risorsa;
- “Search by tags” che consente di ricercare le risorse tramite uno o più tag

All’interno della tabella delle risorse verranno visualizzate solo risorse che abbiano una relazione nel catalogo

All’interno della tabella delle risorse, cliccare su una di essa e tramite la tecnica del “drag and drop”, trascinarla a destra, all’interno nel riquadro intitolato “Currently selected”.

È possibile inserire un numero massimo di tre risorse per simulazione.

Successivamente, in basso a destra, cliccare sul pulsante “Next”.

![Scelta delle risorse in cui effettuare la migrazione del provider](assets/images/extract/media/image123.png)

Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina “Destination Providers” dello step 2 in cui è possibile cliccare sul checkbox in corrispondenza di uno o più provider ove, in base al tipo di provider selezionato, verrà automaticamente compilato in basso a sinistra il valore nel campo ‘Option selected” con i nomi dei providers selezionati

Successivamente, in basso a destra, cliccare sul pulsante “Next”, mentre per tornare alla pagina “Start” dello step 1, cliccare sul pulsante “Back”.

![Scelta del Cloud Provider in cui migrare le risorse](assets/images/extract/media/image124.png)

Dopo aver cliccato sul pulsante “Next”, l’utente si ritroverà all’interno della pagina dello step 3 intitolato “Details” .

In questa pagina verranno visualizzate delle card, rispettivamente una per sottosistema selezionato nello step 2.

In ogni card sono presenti, sulla sinistra, una lista di regioni disponibili per il cloud provider e sulla destra viene visualizzata una sezione vuota.

Selezionando una o più regioni nella sezione di destra (in rosso nella figura) verranno mostrati nella sezione di destra un menù che permette di selezionare la tipologia di costo da applicare ( in giallo nella figura). Selezionando la tipologia “Consumption” non sono richiesti ulteriori parametri , mentre selezionando la tipologia “Reservation” sulla sinistra del campo sarà possibile scegliere il periodo della Prenotazione (in giallo nella figura).

![Selezione della "Regione" e del "Cost Model"](assets/images/extract/media/image125.png)

Dopo aver cliccato sul pulsante “Next”, l’utente si ritroverà all’interno dello step 4 intitolato “Duration” .

Dalla pagina “Duration” dello step 4, selezionare un intervallo per la simulazione tra:

- “One Month”
- “Six Months”
- “One Year”

Per tornare indietro alla pagina “Details”, in basso a destra, cliccare sul pulsante “Back”. Invece, per andare avanti con la simulazione, cliccare sul pulsante “Launch Simulation”.

![Selezione dell'intervallo di tempo](assets/images/extract/media/image126.png)

Dopo aver cliccato sul pulsante “Launch Simulation”, l’utente si ritroverà all’interno della pagina “Results” dello step 5 .

All’interno della pagina “Results”, in alto, è possibile visualizzare il riquadro “Simulation parameters” che contiene un riepilogo dei parametri utilizzati. (in giallo nella figura)

Sotto il riquadro “Summary”,sono presenti diverse sezioni, una per provider di destinazione (in rosso nella figura) e all’ interno potremo visualizzare la lista delle risorse che possono essere migrate sul provider (in verde nella figura), cliccando su una di essere verrà visualizzato un grafico ad istogrammi  in questo grafico possiamo
notare:

- Una linea parallela all’asse X che indica il costo attuale della risorsa.
- Una serie di barre (una per ogni regione e tipologia di costo selezionata) che avranno colore rosso quando il prezzo di destinazione è superiore a quello di partenza o verde quando il prezzo è inferiore al costo attuale della risorsa, passando il mouse su una di esse verrà visualizzato il suo riferimento.
- Una tabella riassuntiva delle tipologie di costo selezionate, che viene utilizzata per generare il grafico a barre.

È possibile visualizzare i dettagli per le altre simulazioni (in viola nella figura) utilizzando la procedura appena descritta.

Per uscire dalla simulazione senza salvare, in basso a destra, cliccare sul pulsante “Close”.

Per salvare la simulazione, cliccare sul pulsante “Save” accanto al pulsante “Close”, e poi cliccare su “Confirm”.

Dopo aver cliccato un pulsante, l’utente viene reindirizzato nella pagina del tab “What If”.

![Pagina dei risultati della simulazione WHAT IF](assets/images/extract/media/image127.png)

![Tabella riassuntiva della/e risorse](assets/images/extract/media/image128.png)

È possibile aggiornare e eseguire nuovamente una simulazione senza dover reinserire tutti i dati.

Per farlo cliccare in corrispondenza della riga da modificare, a questo punto l’utente verrà reindirizzato allo step 1 della simulazione, dove tutti gli step sono stati precompilati utilizzando i parametri salvati

![Avvio per l'aggiornamento della simulazione di tipo "Migrate to another provider"](assets/images/extract/media/image129.png)

#### Scenario “What If”: Change Resource Capacity

Questa funzionalità permette di confrontare i costi di una risorsa in caso di modifica delle caratteristiche tecniche.

Sempre dalla pagina del tab “What If”, in alto a destra, cliccare sul riquadro “Change resources capacity “.

![Accesso alla funzionalità "What If: Change resources capacity"](assets/images/extract/media/image130.png)

Dopo aver fatto ciò, l’utente si ritroverà all’interno della pagina “Start” dello step 1

A sinistra nel riquadro “Select Resources to change”, l’utente può ricercare le risorse tramite tre tipi di filtri tra cui:

- “Search” che consente di cercare una risorsa per nome;
- “Search by Type” che consente di ottenere le risorse tramite la selezione del tipo di risorsa;
- “Search by tags” che consente di ricercare le risorse tramite uno o più tag associato alle suddette.

Nella tabella delle risorse verranno riportate solo risorse che, all’interno del catalogo SCMP, abbiamo più di una “Relazione” con size differenti ma appartenenti alla stessa regione, stesso tipo di prezzo e sistema operativo.

In basso a sinistra, è presente la tabella delle risorse, che può essere filtrata in base ai parametri inseriti nel o nei filtri. All’interno della tabella delle risorse, cliccare su una di essa e tramite la tecnica del “drag and drop”, trascinarla a destra, all’interno nel riquadro intitolato “Currently selected:”.

È possibile inserire un numero massimo di tre risorse per simulazione.

Successivamente, in basso a destra, cliccare sul pulsante “Next”.

![Selezione delle risorse da cui modificare le capacità](assets/images/extract/media/image131.png)

Dopo aver fatto ciò, l’utente si ritrova all’interno della pagina “Resource Provider” dello step 2 in cui è possibile modificare la size di una o più risorse .

All’interno della pagina “Resource Provider” dello step 2, in corrispondenza di una risorsa, cliccare sul menu a tendina della colonna “Size” e selezionare una size diversa da quella iniziale.

Dopodiché, in basso a destra, cliccare sul pulsante “Next” per proseguire la simulazione.

Per tornare alla pagina “Start” dello step 1, cliccare sul pulsante “Back”.

![Modifica della size di una risorsa](assets/images/extract/media/image132.png)

Dopo aver cliccato sul pulsante “Next”, l’utente si ritroverà all’interno della pagina “Duration” dello step 3 .

All’interno della suddetta pagina, è necessario selezionare un intervallo per la simulazione.

Dopodiché, in basso a destra, cliccare sul pulsante “Launch Simulation”.

Per tornare indietro, cliccare sul pulsante “Back”, in questo modo l’utente si ritrova all’interno della pagina “Resource Provider” dello step 2.

![Selezione dell'intervallo per la simulazione](assets/images/extract/media/image133.png)

Dopo aver cliccato sul pulsante “Launch Simulation”, l’utente si ritrova all’interno della pagina “Results dello step 4

All’interno della pagina “Results”, in alto è presente il riquadro “Summary” che consiglia se modificare la size delle risorse. Sotto, è presente un grafico di istogrammi, in cui la barra viola rappresenta i costi attuali, mentre la barra verde rappresenta i costi target.

Per salvare la simulazione, cliccare sul pulsante “Save” accanto al pulsante “Close”, e poi cliccare su “Confirm”. Fatto ciò, l’utente viene reindirizzato nella pagina di “What If”.

Per uscire dalla simulazione senza salvare la suddetta, in basso a destra, cliccare sul pulsante “Close”. Fatto ciò, l’utente si ritrova all’interno della pagina “What If”.

![](assets/images/extract/media/image134.png)
![](assets/images/extract/media/image135.png)
![Parametri di configurazione e consiglio sulla simulazione](assets/images/extract/media/image136.png)

#### Esportazione scenario What If

Per una simulazione della modifica di una size di una risorsa, è possibile esportare la suddetta in formato pdf, csv e json.

All’interno della pagina di “What If”, in basso è presente una tabella delle simulazioni, cliccare sul pulsante “Capacity” posizionato nell’angolo superiore destro della suddetta tabella.

Dopo aver fatto ciò, la tabella mostra le simulazioni sulla modifica della size delle risorse.

In corrispondenza di una simulazione, cliccare sul pulsante che raffigura una freccia.

A questo punto si aprirà un sotto-menu in cui è possibile effettuare l’export nei tre formati precedentemente descritti .

![Export della simulazione](assets/images/extract/media/image137.png)

Sempre per una simulazione è possibile effettuare la stampa della suddetta.

In corrispondenza di una simulazione, cliccare sul kebab menu, e a quel punto cliccare sull'opzione “Print” .

A questo punto, apparirà una modale dell’anteprima del documento da stampare. Infine, cliccare sul pulsante “Stampa” per avviare la stampa del documento.

![Stampa della simulazione](assets/images/extract/media/image138.png)

In corrispondenza di una simulazione, cliccare sul kebab menu.

Dalla lista delle opzioni, cliccare su “Delete” .

![Opzione per eliminare una simulazione](assets/images/extract/media/image139.png)

Dopo aver cliccare sull'opzione “Delete”, apparirà una modale in cui è necessario confermare l’eliminazione della simulazione cliccando sul pulsante “Confirm”

Fatto ciò, la simulazione non è più presene all’interno della tabella.

Se invece non si vuole dare la conferma per l’eliminazione della simulazione, cliccare sul pulsante “Cancel”.

![Conferma dell'eliminazione della simulazione](assets/images/extract/media/image140.png)


### Strumenti di reportistica

La funzionalità di reportistica, specifica per funzionalità, permette di generare dei report globali delle informazioni disponibili per i vari
provider, all’ interno delle pagine verrà data anche la possibilità di creare dei file per facilitare la condivisione delle informazioni.

Per accedere alla funzionalità, sopra il path del breadcrumb, cliccare sul tab “Reports”

![Accesso al report di Catalogo](assets/images/extract/media/image141.png)

#### Tipologie di report disponibili

- **INVENTORY Summary** – Sommario sulla quantità delle principali risorse d'inventario in base alla combinazione provider/sottosistema selezionata.

#### Creazione di un report

In alto sulla destra della pagina possiamo cliccare sul pulsante “New Report” per avviare la creazione di un report, nello specifico viene visualizzata una modale che contiene la lista delle tipologie di report disponibili.

![Creazione nuovo report](assets/images/extract/media/image142.png)

Una volta selezionata la tipologia di report cliccare sul pulsante “Configure” per selezionare i provider da includere nel report, nella finestra appena aperta troviamo il campo “Provider” che permette di selezionare uno o più provider preesistenti nel sistema, successivamente è possibile selezionare uno o più sottosistemi da includere nel report, se non vengono selezionati dei provider non sarà possibile selezione nessun sottosistema. Infine è presente una sezione “tag” per includere le sole risorse che presentano il tag inserito

![Configurazione del report](assets/images/extract/media/image143.png)

A questo punto l'utente può scegliere tra due diverse azioni:

- Creare un report statico che verrà salvato nel sistema.
- Programmare una schedula che generi il report periodicamente.

Per confermare la creazione di un report statico verificare che per il campo “Report type” sia stato selezionato “One-Shot” e cliccare il pulsante “Submit” presente in basso.

Dopo un periodo di caricamento sarà possibile visualizzare nella lista il report appena generato .

![Lista dei report effettuati](assets/images/extract/media/image144.png)

##### Schedulazione del report

Se invece si vuole programmare l’esecuzione dei report automatica sarà necessario selezionare “Recurring” per il campo “Report Type”, in questo caso la finestra si aggiorna per mostrare i parametri aggiuntivi per la configurazione del report periodico .

I parametri da inserire sono:

- Period: permette di selezionare la frequenza di invio del report (oraria, giornaliera, ...).
- "Recive only if not empty" se selezionato il file non verrà inviato quando all interno non sono presenti informazioni
- Report Language: permette di selezionare la lingua utilizzata nel  report.
- File format: permette di selezionare una o più tipologie di file da includere nella mail.
- User E-mails: permette di inserire una mail alla quale inviare i report, dopo aver inserito una mail è necessario premere “Invio” sulla tastiera per confermarne l’inserimento, una volta premuto la mail appena inserita passerà nel box in fondo e il campo verrà svuotato per permettere l’inserimento, se necessario, di una nuova mail.

![Parametri dei report schedulati](assets/images/extract/media/image145.png)

Avendo configurato tutti i parametri il pulsante “Submit” diventerà cliccabile, cliccarlo per confermare l’inserimento e dopo un periodo di caricamento sarà possibile visualizzare nella lista il report appena generato .

![Lista dei report effettuati](assets/images/extract/media/image144.png)

##### Lista dei report schedulati

Per visualizzare la lista dei report schedulati, selezionare il tab “Scheduled” presente in alto sulla sinistra nella pagina dei report
.

![Lista dei report schedulati](assets/images/extract/media/image146.png)

In questa pagina troviamo la lista e le relative informazioni dei report schedulati presenti nel sistema, per ogni risultato è possibile, cliccando il pulsante “Tre punti” sulla destra sarà possibile effettuare tre operazioni:

- Visualizzare l’ ultimo report generato .
- Editare le impostazioni della schedula, non sarà possibile modificare i provider o sottosistemi selezionati.
- Eliminare la schedula per interrompere l’invio delle e-mail.

![Modifica di una schedule](assets/images/extract/media/image147.png)

##### Utilizzo dei report

Cliccando sulla riga di un report statico, o utilizzando il pulsante “Show report” disponibile per i report schedulati sarà possibile visualizzare la pagina di dettaglio del report selezionato .

All’interno del sommario del report dell’Inventory è presente la sezione “Stats” in cui sono presenti il numero dei dischi, delle interfacce, delle reti e delle virtual machines appartenenti al provider selezionato.

Sotto la sezione “Stats”, sono presenti i filtri usati dall'utente per generare il report.

Sotto i filtri, è presente la tabella riassuntiva delle risorse appartenenti ai provider. A destra sono presenti due pulsanti: “PRINT” ed “EXPORT”.

Cliccando sul pulsante “PRINT”, appare una modale di anteprima della stampa. Per stampare il report, cliccare sul pulsante in basso a destra “Stampa”, a questo punto si avvierà la stampa del suddetto.

Cliccando sul pulsante “EXPORT”, è possibile esportare il report in formato “.csv”, “. json” o “.pdf”.

Per tornare al tab “Results”, in basso a destra, cliccare sul pulsante “CLOSE” oppure in alto a sinistra cliccare sulla freccia che punta verso la sinistra, accanto al titolo del report.

![Dettagli dei report](assets/images/extract/media/image148.png)
