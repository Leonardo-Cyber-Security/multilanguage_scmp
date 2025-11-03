# Cost and Usages

La SCMP raccoglie, attraverso le API messe a disposizione dai provider, i dettagli dei costi degli asset di inventario.

Nella eventualità che i provider non espongano dati riguardo i costi, questi potranno essere inseriti editorialmente nel catalogo in modo che possano essere poi conteggiati all’interno di questa funzionalità.

I costi vengono raccolti con la suddivisione per costo giornaliero e per risorsa. Successivamente, come avviene per la parte delle metriche, i dati vengono normalizzati e aggregati per permettere una visualizzazione uniforme della dashboard.

!!! danger "Attenzione"
    Come indicato anche sulle dashboard dei costi i dati relativi alle ultime 48 ore non sono ancora stati confermati dai relativi provider, possiamo prendere come riferimento questa tabella, ma per i dettagli è necessario verificare sulla documentazione del provider specifico.

Ad esempio:

| **Cloud Provider** | **Strumento/Metodo** | **Tempistiche di aggiornamento** | **Note** |
|----|----|----|----|
| Azure | Cost using export file | 6/7 giorni | nei primi 6 giorni del mese successivo vengono consolidati i costi del mese precedente |
| Azure | Cost Management | 8-24 ore | Dati consolidati aggiornati entro 24/48 ore; ritardo maggiore rispetto ad altri. |
| Google Cloud | Billing Dashboard | Alcune ore, massimo 24 ore | Aggiornamenti quasi in tempo reale; consolidamento fino a 24 ore. |
| Google Cloud | BigQuery Export | Ogni ora | Ritardo minimo per analisi avanzate tramite BigQuery. |
| Oracle Cloud | Cost Analysis | 4-6 ore, massimo 24 ore | alcuni servizi possono avere ritardi maggiori. |
| AWS | Cost Explorer | 8-24 ore | Dati aggregati aggiornati entro 12-24 ore. |
| AWS | Cost and Usage Reports (CUR) | 8-24 ore | Report dettagliati con ritardo simile. |
| AWS | CloudWatch Metrics (Billing) | Ogni 6 ore | Monitoraggio quasi in tempo reale. |
| AWS | Budget Alerts | 3-5 ore | Notifiche rapide al superamento delle soglie di budget. |

### Dashboard dei costi

Per accedere alla sezione costi, è necessario utilizzare il menu come da figura .

![Accesso a Costs](images/extract/media/image238.png)

A questo punto, l’utente si ritroverà all’interno della pagina del tab “Dashboard” dei costi.
In questa schermata possiamo notare nell’ ordine:

- Il valore di “Cost trend” che indica il totale dei costi per il periodo selezionato.
- Il valore di “Cost difference” che indica il ricarico effettuato nel periodo selezionato.
- Un grafico a barre “Cloud provider Spend” che indica il costo fatturato al cliente per ogni provider nel periodo selezionato.
- Un grafico a barre “Effective Spend” che indica il costo effettivo delle risorse sul provider.

 In basso saranno presenti diversi grafici di aggregazione delle  risorse, ad esempio, per Regione o Tipologia di Servizio, come  indicato nei rispettivi cloud providers e come analizzeremo in seguito  sarà possibile personalizzare i grafici e le sezioni disponibili.

![Dashboard dei costi](images/extract/media/image239.png)

Nella funzionalità dei costi viene data la possibilità di filtrare per tipologia di risorsa utilizzando la barra dei tab in alto, mentre per avere una visualizzazione generale è possibile utilizzare la dashboard.

![Filtrare per tipologia di risorsa](images/extract/media/image240.png)

#### Filtri della sezione Costi

All’interno della pagina sono disponibili una serie di filtri che possono essere selezionati anche contemporaneamente per filtrare i risultati della dashboard.

Il filtro principale è il periodo di visualizzazione, lo possiamo trovare in alto a destra, cliccandoci verrà aperta una finestra di scelta (in giallo nella figura) dove sarà possibile sia inserire un intervallo di tempo personalizzato, utilizzando i campi “From” e “To” presenti sulla sinistra, o selezionare un intervallo di tempo “smart” cliccando direttamente sulla scelta desiderata nella sezione scrollable a destra.

![Filtro temporale dei costi](images/extract/media/image241.png)

Vengono messi a disposizione, in alto a sinistra della pagina, una serie di filtri che permettono di filtrare le risorse recuperate, nello specifico è possibile filtrare per:

- Tag
- Tipologia di provider
- Nome del sottosistema.

 Questi filtri permettono di selezionare dei valori multipli e possono  essere combinati tra loro per raggiungere la granularità desiderata

![Filtri della funzionalità costi](images/extract/media/image242.png)

#### Panoramica dei dati mostrati

##### Sezione “General”

Nella prima sezione vengono mostrati all’utente dei grafici riassuntivi rappresentanti i costi di provider e della SCMP sulla base dei filtri applicati.

Nel dettaglio:

- **Provider Cost Difference:** grafico contenente la differenza di costo tra la somma dei costi originali dei provider e la somma dei costi concordati con il provider.  
  *Utile per identificare il risparmio ottenuto tramite la negoziazione o rivendita rispetto ai prezzi di listino.*

- **Customer Cost Difference:** grafico contenente la differenza di costo tra la somma dei costi SCMP addebitati al cliente e la somma dei costi originali dei provider.  
  *Serve a monitorare i margini di guadagno e la competitività dei prezzi offerti al cliente.*

- **Customer Cost Trend:** grafico contenente il totale dei costi SCMP addebitati al cliente, con rispettiva percentuale di guadagno/perdita.  
  *Permette di osservare l’andamento economico nel tempo e rilevare picchi o anomalie nei costi.*

- **Provider Spend:** grafico contenente la somma dei costi originali per ciascun provider.  
  *Consente di identificare su quali provider si concentra la spesa e il livello di dipendenza.*

- **Provider Agreement Spend:** grafico contenente la somma dei costi concordati per ciascun provider.  
  *Utile per confrontare la bontà degli accordi commerciali con ciascun provider.*

- **Effective Spend:** grafico contenente la somma dei costi SCMP addebitati al cliente per ciascun provider.  
  *Aiuta a valutare la redditività ottenuta su ogni provider.*

![General](images/extract/media/image243.png)

##### **Sezione “Accounts”**

Nella seconda sezione vengono mostrati all’utente dei grafici focalizzati sui costi generati da ciascun account subordinato di ogni provider.

Nel dettaglio:

- **Sub-Account Provider Cost %:** Percentuale del costo totale dei provider, per ogni account.  
  *Serve per identificare gli account più costosi e analizzare il carico economico distribuito.*

- **Sub-Account Provider Agreement Cost %:** Percentuale del costo totale concordato dei provider, per ogni account subordinato.  
  *Utile per verificare quali account beneficiano di sconti più significativi.*

- **Sub-Account Effective Cost %:** Percentuale del costo totale SCMP addebitato al cliente, per ogni account subordinato.  
  *Consente di vedere quali account generano più fatturato.*

![Accounts](images/extract/media/image244.png)

##### **Sezione “Services”**

Nella terza sezione vengono mostrati all’utente dei grafici focalizzati sui costi generati da ciascun servizio cloud di ogni provider.

Nel dettaglio:

- **Service Provider Cost %:** Percentuale del costo totale dei provider, per ogni servizio.  
  *Permette di capire quali servizi (es. compute, storage, network) pesano di più sui costi.*

- **Service Provider Agreement Cost %:** Percentuale del costo totale concordato dei provider, per ogni servizio.  
  *Utile per analizzare l’efficacia delle negoziazioni sui vari servizi.*

- **Service Effective Cost %:** Percentuale del costo totale SCMP addebitato al cliente, per ogni servizio.  
  *Fornisce una visione chiara delle fonti principali di ricavo per servizio.*

![Services](images/extract/media/image245.png)

##### **Sezione “SKUs”**

Nella quarta sezione vengono mostrati all’utente dei grafici focalizzati sui costi generati da ciascuno SKU di ogni provider.

Nel dettaglio:

- **Sku Provider Cost %:** Percentuale del costo totale dei provider, per ogni SKU.  
  *Consente l’analisi dettagliata dei costi a livello di unità di fatturazione.*

- **Sku Provider Agreement Cost %:** Percentuale del costo totale concordato dei provider, per ogni SKU.  
  *Utile per valutare se anche i singoli SKU beneficiano di sconti e ottimizzazioni.*

- **Sku Effective Cost %:** Percentuale del costo totale SCMP addebitato al cliente, per ogni SKU.  
  *Aiuta a evidenziare eventuali squilibri nei margini a livello di SKU.*

![Skus](images/extract/media/image246.png)

##### **Sezione “Resources”**

Nella quinta sezione vengono mostrati all’utente dei grafici focalizzati sui costi generati da ciascuna risorsa di ogni provider.

Nel dettaglio:

- **Resource Provider Cost %:** Percentuale del costo totale dei provider, per ogni risorsa.  
  *Permette l’individuazione di risorse particolarmente costose o sottoutilizzate.*

- **Resource Provider Agreement Cost %:** Percentuale del costo totale concordato dei provider, per ogni risorsa.  
  *Consente di vedere se gli sconti sono distribuiti equamente tra le risorse.*

- **Resource Effective Cost %:** Percentuale del costo totale SCMP addebitato al cliente, per ogni risorsa.  
  *Fornisce visibilità sulla redditività delle singole risorse.*

![Resources](images/extract/media/image247.png)

##### **Sezione “Types”**

Nella sesta sezione vengono mostrati all’utente dei grafici focalizzati sui costi generati da ciascuna tipologia di risorsa d’inventario, di ogni provider.

Nel dettaglio:

- **Resource Type Provider Cost %:** Percentuale del costo totale dei provider, per ogni tipo di risorsa.  
  *Offre una visione aggregata utile per la pianificazione dei costi.*

- **Resource Type Provider Agreement Cost %:** Percentuale del costo totale concordato dei provider, per ogni tipo di risorsa.  
  *Aiuta a capire quali tipologie sono più ottimizzate tramite accordi.*

- **Resource Type Effective Cost %:** Percentuale del costo totale SCMP addebitato al cliente, per ogni tipo di risorsa.  
  *Consente di misurare il peso commerciale di ogni categoria.*

![Types](images/extract/media/image248.png)

##### **Sezione “Regions”**

Nella settima sezione vengono mostrati all’utente dei grafici focalizzati sui costi generati in ciascuna regione, di ogni provider.

Nel dettaglio:

- **Regional Provider Cost %:** Percentuale del costo totale dei provider, per ogni regione.  
  *Indica dove sono geograficamente localizzate le risorse e le relative spese.*

- **Regional Provider Agreement Cost %:** Percentuale del costo totale concordato dei provider, per ogni regione.  
  *Permette di valutare la convenienza delle regioni scelte in base agli sconti.*

- **Regional Effective Cost %:** Percentuale del costo totale SCMP addebitato al cliente, per ogni regione.  
  *Utile per analizzare la distribuzione del fatturato per area geografica.*

![Regions](images/extract/media/image249.png)

##### **Sezione “History”**

Infine, nell’ottava sezione, vengono mostrati all’utente dei grafici focalizzati sui costi storici di ogni account di fatturazione (Billing Account), generati da ogni sottosistema integrato nella SCMP.

Nel dettaglio:

- **System Costs Details:** Confronto tra il costo totale del provider, il costo totale concordato del provider ed il costo totale del cliente, per tutti i sottosistemi integrati nella SCMP.  
  *Fondamentale per analisi retrospettive e per valutare la sostenibilità economica del sistema.*

- **Historical Provider Billing Costs:** Storico dell’andamento dei costi totali di ogni account cloud di fatturazione.  
  *Aiuta a prevedere trend futuri e ad anticipare problemi di spesa o budget.*

![History](images/extract/media/image250.png)

#### Visualizzazione limitata per il cliente

Se viene utilizzata, per l’accesso alla dashboard dei costi, una utenza configurata con il parametro “LIMITED” i grafici disponibili sulla dashboard saranno relativi ai soli costi ricalcolati della SCMP, mentre i costi effettivi ricevuti dai provider non saranno visibili perché superflui come si può vedere nell’ immagine.

![Dashboard dei costi limitata](images/extract/media/image251.png)

### Dashboard dello “Usage”

Oltre alla dashboard principale dei costi e le relative dashboard di dettaglio per tipologia di risorsa, nel modulo Costs della SCMP l’utente potrà visualizzare un’ulteriore dashboard, focalizzata sui consumi delle risorse d’inventario integrate nella piattaforma.

Navigando dunque alla sezione Usages del modulo, verranno mostrate informazioni generiche e di dettaglio sul consumo dei singoli servizi/sku integrati e sulle rispettive risorse.

Per accedere alla funzionalità, sopra il path del breadcrumb, cliccare sul tab “Usages” .

![Accesso a "Usages"](images/extract/media/image252.png)

#### Filtri della sezione Usage

All’interno della pagina sono disponibili una serie di filtri, che possono essere selezionati anche contemporaneamente per filtrare i risultati della dashboard.

Il filtro principale è il periodo di visualizzazione, lo possiamo trovare in alto a destra, cliccandoci verrà aperta una finestra di scelta (in giallo nella figura) dove sarà possibile sia inserire un intervallo di tempo personalizzato, utilizzando i campi “From” e “To” presenti sulla sinistra, o selezionare un intervallo di tempo “smart” cliccando direttamente sulla scelta desiderata nella sezione scrollable a destra.

![Filtro temporale dello usage](images/extract/media/image241.png)

Vengono messi a disposizione, in alto a sinistra della pagina, una serie di filtri che permettono di filtrare le risorse recuperate, nello specifico è possibile filtrare per:

- Tag
- Tipologia di provider
- Nome del sottosistema.
- Tipo di risorsa
- Nome del servizio cloud
- Nome dello sku cloud

Questi filtri permettono di selezionare dei valori multipli e possono essere combinati tra loro per raggiungere la granularità desiderata.

![Filtri della funzionalità costi](images/extract/media/image242.png)

#### Panoramica dei dati mostrati sezione costi

##### Sezione “Skus Usage Average”

Il primo grafico rappresenta la media giornaliera consumata da ogni SKU.
È un grafico riassuntivo che mostra all’utente l’andamento generale del consumo.

Per ogni SKU, infatti, viene indicata la media di consumo e l’unità di misura, nel range temporale specificato, per fornire sommariamente quali di essi sono mediamente più utilizzati e di conseguenza quali di essi potrebbero generare maggiore costo per l’utente.

![Sezione "Skus Usage"](images/extract/media/image253.png)

##### Sezione “SKU Resource Average”

Il secondo grafico invece, è focalizzato sullo SKU selezionato come filtro dall'utente e mostra la media giornaliera consumata da ogni risorsa, correlata allo specifico SKU.

anch'esso, può essere classificato come un grafico riassuntivo che fornisce all’utente quali risorse per un determinato SKU, sono mediamente più utilizzate e di conseguenza quali tra esse potrebbero generare maggiore costo per l’utente.

![Sezione "SKU resource"](images/extract/media/image253.png)

##### Sezione “Historical SKU Usage”

Il primo grafico temporale mostra l’andamento giornaliero del consumo dello specifico SKU, selezionato come filtro nella dashboard.

Nel caso in figura, si evidenzia un consumo (in ore) costante nel tempo, utile all’utente per fasi successive d’analisi.

![Sezione "Historical SKU"](images/extract/media/image254.png)

##### Sezione “SKU Resources Usage”

Il secondo grafico temporale mostra invece l’andamento giornaliero del consumo dello specifico sku, per ogni risorsa correlata ad esso.

Questo grafico, dunque mostra all’utente il dettaglio storico del grafico precedente, evidenziando quali risorse sono coinvolte nel consumo dello specifico sku e in che misura lo sono.


Quest’ultimo grafico è particolarmente utile all’utente perché evidenzia quali risorse vengono effettivamente utilizzate nell’ambito di uno sku specifico e, di conseguenza, quali tra esse potrebbero portare maggiori costi all’utente o essere pagate senza nemmeno essere utilizzate.

![Sezione "Sku Resources"](images/extract/media/image255.png)

### Personalizzazione dashboard dei costi e Usage

Per la personalizzazione delle dashboard è possibile consultare la [guida ufficiale](https://grafana.com/docs/grafana/latest/)

### Strumenti di reportistica

La funzionalità di reportistica, specifica per funzionalità, permette di generare dei report globali delle informazioni disponibili per i vari
provider, all’ interno delle pagine verrà data anche la possibilità di creare dei file per facilitare la condivisione delle informazioni.

Per accedere alla funzionalità, sopra il path del breadcrumb, cliccare sul tab “Reports”

![Accesso al report di Catalogo](images/extract/media/image141.png)

#### Tipologie di report disponibili

- **Cost Summary** – Sommario del costo totale per servizio, in base alla combinazione di filtri selezionata.
- **Cost Summary – Group by Resource Type** – Sommario del costo totale per servizio, con indicazione sul numero di risorse coinvolte, in base alla combinazione di filtri selezionata.
- Cost Details – Dettaglio del costo giornaliero regionale per risorsa, in base alla combinazione di filtri selezionata.
- **Cost Details – Group by Resource Type** – Dettaglio del costo giornaliero totale per servizio, con indicazione sul numero di risorse coinvolte, in base alla combinazione di filtri selezionata..
- **FinOps Report** – Sommario sui costi totali e su l'utilizzo totale delle risorse secondo lo standard FinOps FOCUS, per l’ottimizzazione finanziaria dei servizi cloud, in base alla combinazione di filtri selezionata.

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
