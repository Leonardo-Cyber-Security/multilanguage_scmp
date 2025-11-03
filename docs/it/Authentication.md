# Authentication

La funzionalità di “Authentication” permette di interagire con lo IAM per modificare la profilatura utenti.

Per le configurazioni preliminari attenersi alle specifiche indicate nel documento DI-IPSC-81443 inserito nella tabella dei documenti di riferimento.

Il menu è accessibile dal tasto in alto a destra, come mostrato di seguito.

In particolare, per accedere alla profilatura utente il menu è “Authentication”.

![Accesso alla funzionalità Authentication](images/extract/media/image8.png)

Visualizzazione dashboard per la profilatura utente:

![Dashboard di IAM](images/extract/media/image10.png)

### Gruppi

Per semplificare l’assegnazione di menù attributi e autorizzazioni è possibile utilizzare dei gruppi di utenti, cliccare il menù “Groups” nella sezione “Entities” della dashboard IAM.

![Accesso alla gestione Gruppi](images/extract/media/image11.png)

Una volta cliccato il link verrà mostrata all’utente la lista di tutti i gruppi disponibili sul portale con i rispettivi pulsanti di configurazione

![Lista dei gruppi configurati](images/extract/media/image12.png)

#### Creazione Gruppi

Per creare un nuovo gruppo all’ interno del sistema, cliccare il pulsante “+” in alto a destra, verrà visualizzata una maschera di creazione del Gruppo.

![Aggiunta nuovo Gruppo](images/extract/media/image13.png)

Inserire il nome del gruppo e cliccare il tasto “Add Group” per aggiungerlo al sistema. Una volta premuto il sistema ci porta alla lista dei gruppi disponibili dove possiamo trovare il gruppo appena creato.

![Parametri di inserimento Gruppo](images/extract/media/image14.png)

#### Gestione utenti assegnati e attributi

Per poter assegnare degli utenti a un gruppo, dalla lista dei gruppi disponibili, cliccare sull'icona “persone” sulla riga corrispondente al gruppo interessato. L’utente verrà reindirizzato nella pagina “Members” dove è possibile visualizzare tutti gli utenti assegnati al gruppo e le loro informazioni di base.

![Accesso gestione assegnazione utenti](images/extract/media/image15.png)

Possiamo aggiungere un utente al gruppo cliccando il tasto “+” presente in alto a Destra (1), una volta premuto nella lista degli utenti assegnati verrà creata una nuova riga (2) dove all’ interno è possibile selezionare dalla lista degli utenti disponibili un utente (3).

![Assegnare un utente al gruppo](images/extract/media/image16.png)

Analogamente è possibile rimuovere gli utenti dal gruppo, cliccando il pulsante “Cestino” in corrispondenza dell’utente da rimuovere.

Dopo aver aggiunto tutti gli utenti al gruppo cliccare il tasto “Save” in basso a sinistra per salvare le modifiche. Verrà visualizzata una modale di conferma salvataggio.

Possiamo assegnare degli attributi al gruppo che verranno automaticamente utilizzati dagli utenti assegnati, per farlo selezionare il tab “Attributes” in alto nella pagina (1), poi utilizzando il tasto “+” in alto a destra (2) è possibile aggiungere un attributo, nella parte sinistra bisogna inserire la chiave (3) e nella parte bianca sulla destra bisogna inserirne il suo valore (4), durante l’inserimento vedremo sotto al campo una drop down dove cliccando sarà possibile salvare il valore inserito (5).

![Inserire Attributi](images/extract/media/image17.png)

Una volta inseriti tutti gli attributi necessari è possibile salvare le modifiche utilizzando il tasto “Save” in basso.

Per tornare alla lista dei Gruppi disponibili cliccare il tasto “Back” presente in ogni pagina.

#### Visualizzazione Modifica ed Eliminazione di un Gruppo

Sempre dalla lista dei Gruppi disponibili per ogni gruppo sono disponibili una serie di pulsanti:

- “Lente di ingrandimento”: permette la visualizzazione delle info sul Gruppo (indicato con una freccia rossa nell’ immagine);
- “Matita”: permette la modifica delle informazioni base del gruppo (indicato con una freccia gialla nell’ immagine);
- “Cestino”: permette l’eliminazione del gruppo dopo aver cliccato
  “conferma” nella modale visualizzata (indicato con una freccia viola nell’ immagine).

![Pulsanti di controllo](images/extract/media/image18.png)

### Utenti

Per poter accedere e utilizzare il sistema è necessario che l’utenza da utilizzare sia opportunamente configurata, di seguito vedremo il processo di creazione e gestione di un utente all’interno della SCMP utilizzando IAM come applicazione per il controllo degli accessi.

Per accedere alla gestione Utenti cliccare il menù “Users” nella sezione “Entities” della dashboard IAM.

![Accesso alla gestione Utenti](images/extract/media/image19.png)

Una volta cliccato il link verrà mostrata all’utente la lista di tutti i gruppi disponibili sul portale con i rispettivi pulsanti di configurazione.

![Lista degli utenti configurati](images/extract/media/image20.png)

#### Creazione nuovi utenti

Per creare un nuovo utente all’ interno del sistema, cliccare il pulsante “+” in alto a destra, verrà visualizzata una maschera di creazione dell’utente .

![Creazione nuovo utente](images/extract/media/image21.png)

Verrà visualizzato il form di creazione di un nuovo utente, compilare i campi obbligatori della lista:

- E-mail: l’indirizzo e-mail valido dell’ utente.
- Username: l’username da utilizzare come utenza di accesso al portale.
- First Name: Nome dell’utente.
- Last Name: Cognome dell’utente.
- Password: Password di almeno 8 caratteri da utilizzare per l’accesso.
- Max concurrent connections: Numero di connessioni massime in   contemporanea abilitate per l’utente.
- Default Language: la lingua di base da visualizzare nel sistema.

![Maschera di creazione utente](images/extract/media/image22.png)

Una volta inseriti tutti i campi obbligatori cliccare il pulsante “+ Add user” per completare l’inserimento.

Verrà visualizzato un messaggio di conferma e la pagina si resetta per permettere l’inserimento di un nuovo utente.

Per visualizzare l’utente appena creato tornare nella pagina contenente la lista degli utenti.

#### Assegnazione Ruoli e Attributi

Per gestire gli utenti è possibile cliccare il tasto “Gruppi” in corrispondenza della riga dell’utente da modificare

![Accesso alla gestione utente](images/extract/media/image23.png)

Una volta premuto il pulsante, la pagina si aggiorna per mostrare la pagina “Groups”  dove è possibile assegnare o rimuovere uno o più gruppi all’ utente.

Per aggiungere un nuovo gruppo all’utente bisogna selezionare, nella sezione di sinistra, il gruppo che si vuole assegnare all’utente (1) e, successivamente cliccando il pulsante “Associa” al centro della pagina (2) il gruppo passerà automaticamente nella sezione destra e le modifiche verranno salvate automaticamente.

![Associare un utente al gruppo](images/extract/media/image24.png)

Analogamente è possibile rimuovere l’utente dal gruppo cliccando prima il gruppo da rimuovere nella sezione di destra e successivamente il tasto “Dissocia” al centro della pagina , le modifiche verranno salvate automaticamente.

![Dissociare un utente dal gruppo](images/extract/media/image25.png)

È possibile, inoltre, tramite i tasti presenti nella sezione di destra, in corrispondenza di ogni gruppo, modificare la priorità dei vari gruppi.

Anche per gli utenti è possibile assegnare degli attributi personalizzati, per farlo selezionare il tab “Attributes”  in alto nella pagina (1), poi utilizzando il tasto “+” in alto a destra (2) è possibile aggiungere un attributo, nella parte sinistra bisogna inserire la chiave (3) e nella parte bianca sulla destra bisogna inserirne il suo valore (4), durante l’inserimento vedremo sotto al campo una drop down dove cliccando sarà possibile salvare il valore inserito (5).

La lista degli attributi disponibili si trova nel paragrafo.

![Inserire Attributi](images/extract/media/image17.png)

Una volta inseriti tutti gli attributi necessari è possibile salvare le modifiche utilizzando il tasto “Save” in basso.

#### Reset delle credenziali

Come amministratore degli utenti è possibile resettare le password, per farlo bisogna cliccare sul tab “Credentials” visualizzato in alto nella pagina,  in questo tab è possibile inserire una nuova password per l’utente e configurarla come “Temporanea”, la password temporanea dovrà essere modificata dall'utente dopo il primo accesso. Si può inoltre definire un periodo di validità della password espresso in giorni.

![Modifica della password per l'utente](images/extract/media/image26.png)

#### Visualizzazione modifica ed Eliminazione di un Utente

Sempre dalla lista degli utenti disponibili per ogni gruppo sono disponibili una serie di pulsanti:

- “Lente di ingrandimento”: permette la visualizzazione delle info utente(indicato con una freccia rossa nell’ immagine).
- “Matita”: permette la modifica delle informazioni base dell’ utente (indicato con una freccia gialla nell’ immagine).
- “Cestino”: permette l’eliminazione dell’utente dopo aver cliccato “conferma” nella modale visualizzata (indicato con una freccia viola nell’ immagine).

![Pulsanti di controllo](images/extract/media/image27.png)

### Gestione menù abilitati per utente/Gruppo

Il sistema IAM integrato nella SCMP permette anche la gestione degli elementi di menù disponibili per i vari utenti e gruppi, per accedere alla funzionalità basta cliccare il link “User management X Pages” disponibile nella sezione “Administration” della dashboard IAM.

![Accesso alla gestione dei menù](images/extract/media/image28.png)

All’interno della pagina in alto, sono presenti due menu a tendina, il menu a tendina a sinistra consente di selezionare un singolo utente, quello a destra consente di selezionare un gruppo.

![Selezione dell'utente/gruppo da modificare](images/extract/media/image29.png)

Dopo aver selezionato un’utenza, la pagina verrà aggiornata per mostrare tutti gli “STREAM” disponibili sull'applicazione, è possibile cliccare il tasto “+” in corrispondenza di ogni riga per visualizzarne i “MODULES” e i “COMPONENT” disponibili.

Le liste delle componenti visualizzate sono generate automaticamente dal sistema utilizzando le configurazioni eseguite durante l’installazione.

Per ogni component presente è possibile, cliccando il menù a tendina sulla riga corrispondente, indicarne la visibilità o meno all’utente/gruppo che abbiamo selezionato precedentemente.

I valori selezionabili sono:

- Enabled and default: può essere indicato solo un default per modulo, selezionando questa opzione rendiamo come principale la pagina selezionata; quindi, al click del menù l’utente verrà reindirizzato su questa pagina.
- Enabled: Indica che il menù è visibile e utilizzabile  dall'utente/gruppo.
- Disabled: Indica che il menù non verrà abilitato e non sarà  visibile all’ utente/gruppo.
- N.D: non definito (il menù è disabilitato e non sarà visibile).

![Gestione delle autorizzazioni del menù](images/extract/media/image30.png)

### Liste profili utente e Attributi

In questa sezione vengono evidenziate le diverse tipologie di utente che possono accedere e utilizzare il prodotto descritto.

Per ognuno di essi, viene riportato un elenco delle funzionalità alle quali l’utente è stato abilitato e con le quali può interagire.

Vengono indicati qui anche tutti gli attributi che possono essere assegnati a Utenti e Gruppi.

#### Attributi

| **Attributo**      | **Valori accettabili** | **Tipologia** | **Descrizione** |
|----|----|----|----|
| Monitoring            | Default, AS01, mase | String array   | Inserire la lista dei tenant abilitati per l’utente inserendo una virgola tra i nomi di ogni tenant  |
| Costs                 | true / false | Boolean | Abilitando l’attributo specifichiamo che l’utente può effettuare ricerche per TAG invece di utilizzare il tenant come discriminante   |
| Inventory             |ADMIN  /  LIMITED | Enumeration | Inserendo ADMIN come valore l’utente potrà visualizzare sia i costi ricevuti dal provider che i costi calcolati dalla SCMP Inserendo LIMITED sarà possibile visualizzare solo i costi calcolati dalla SCMP|
| Inventory             | Zona1   | String   | Parametro obbligatorio degli strumenti utilizzati da IAM|

#### Amministratore

| **Funzionalità**      | **Create** | **Read** | **Undo** | **Delete** |
|----|----|----|----|----|
| Monitoring            | x          | x        | x        | x          |
| Costs                 | x          | x        | x        | x          |
| Inventory             | x          | x        | x        | x          |
| Security              | x          | x        | x        | x          |
| Dashboard             | x          | x        | x        | x          |
| Catalog               | x          | x        | x        | x          |
| Authentication        | x          | x        | x        | x          |
| Administration        | x          | x        | x        | x          |
| Cloud Maturity model  | x          | x        | x        | x          |
| Provisioning          | x          | x        | x        | x          |
| Tenant Management     |            |          |          |            |
| Service Detail Design |            |          |          |            |

#### Gestore del servizio

| **Funzionalità**      | **Create** | **Read** | **Undo** | **Delete** |
|----|----|----|----|----|
| Monitoring            |            |          |          |            |
| Costs                 |            |          |          |            |
| Inventory             |            |          |          |            |
| Security              |            |          |          |            |
| Dashboard             |            |          |          |            |
| Catalog               |            |          |          |            |
| Authentication        | x          | x        | x        | x          |
| Administration        |            |          |          |            |
| Cloud Maturity model  |            |          |          |            |
| Provisioning          |            |          |          |            |
| Tenant Management     | x          | x        | x        | x          |
| Service Detail Design | x          | x        | x        | x          |

#### Visualizzatore

| **Funzionalità**      | **Create** | **Read** | **Undo** | **Delete** |
|----|----|----|----|----|
| Monitoring            | x          | x        |          |            |
| Costs                 | x          | x        |          |            |
| Inventory             | x          | x        |          |            |
| Security              |            | x        |          |            |
| Dashboard             |            | x        |          |            |
| Catalog               |            | x        |          |            |
| Authentication        |            |          |          |            |
| Administration        |            |          |          |            |
| Cloud Maturity model  |            | x        |          |            |
| Provisioning          |            |          |          |            |
| Tenant Management     |            |          |          |            |
| Service Detail Design |            |          |          |            |

#### Autorizzato

| **Funzionalità**      | **Create** | **Read** | **Undo** | **Delete** |
|----|----|----|----|----|
| Monitoring            | x          | x        | x        | x          |
| Costs                 | x          | x        | x        | x          |
| Inventory             | x          | x        | x        | x          |
| Security              |            |          |          |            |
| Dashboard             | x          | x        | x        | x          |
| Catalog               | x          | x        | x        | x          |
| Authentication        |            |          |          |            |
| Administration        | x          | x        | x        | x          |
| Cloud Maturity model  |            |          |          |            |
| Provisioning          | x          | x        | x        | x          |
| Tenant Management     |            |          |          |            |
| Service Detail Design |            |          |          |            |
