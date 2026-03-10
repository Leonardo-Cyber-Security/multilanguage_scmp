# Service Detail Design

Il servizio Service Detail Design è la soluzione implementata per la gestione delle richieste, che devono poi essere lavorate all’interno del nostro ambiente da un utente autorizzato.

Per accedere a Service Detail Design, effettuare il login su SCMP con l’utente Service Manager.

Dopo aver effettuato l’accesso, cliccare sul modulo "Service Detail Design" dal pulsante bento.

![Accesso al modulo Service Detail Design](assets/images/extract/media/image339.png)

Verrà mostrata la pagina di ricerca dove è possibile filtrare i work order già creati in base a:

- Stato
- Cliente
- Tipologia servizio
- Fase
- Data creazione

La tabella mostrerà le informazioni generali del Work Order.

![Filtri funzionalità Service Detail Design](assets/images/extract/media/image340.png)

Cliccare al centro di una riga di work order per visualizzarne il contenuto; si aprirà una modale dove è possibile espandere le varie sezioni cliccandoci sopra.

Per uscire dalla visualizzazione di dettaglio, cliccare fuori dalla finestra grigia.

![Dettaglio Work Order](assets/images/extract/media/image341.png)

### Flusso Work Order

Per prendere in carico un work order, cliccare sul simbolo “Play” accanto a un ordine in stato “Nuovo”.

Verrà visualizzata una notifica di cambio stato a schermo e lo stato corrente dell’Ordine diventa “In lavorazione”; i pulsanti dell’ordine corrispondente vengono modificati:

- cliccando il pulsante “Pausa”, l’ordine passerà in stato “Idle”;
- cliccando il pulsante “Segna come completato”, è possibile chiudere il Work Order;
- cliccando il pulsante “Rifiutato”, è possibile segnalare l’annullamento dell’Ordine;

![Pagina gestione work order Service Detail Design](assets/images/extract/media/image342.png)

Quando viene cliccato il pulsante “Segna come completato”, viene visualizzata a schermo una finestra dove è possibile inserire le informazioni da allegare all’ordine, nello specifico:

- l’esito della lavorazione;
- una descrizione dell’esito scelto;
- una nota per l’operatore.

![Chiusura Work order](assets/images/extract/media/image343.png)

Scorrendo la pagina verso il basso, troviamo la sezione parametri dove è possibile inserire diverse combinazioni chiave/valore per i parametri utilizzati durante la lavorazione.

Dopo aver inserito chiave e valore, cliccare il pulsante “Plus” per confermare l’inserimento; vengono aggiunti nuovi campi vuoti dove è possibile inserire ulteriori parametri. Per eliminare una coppia chiave/valore, cliccare il pulsante “Minus”; una volta inseriti tutti i parametri, cliccare il pulsante “Finish”.

![Inserimento parametri](assets/images/extract/media/image344.png)

Dopo aver completato l’ordine, è possibile, aprendo i relativi menu, visualizzare tutte le informazioni inserite durante la lavorazione all’interno della sezione info.

![Informazioni aggiunte durante la lavorazione](assets/images/extract/media/image345.png)
