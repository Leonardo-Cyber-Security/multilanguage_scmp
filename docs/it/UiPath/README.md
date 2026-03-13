Integrazione front-end con UiPath Orchestrator (autenticazione utente)

Questo esempio mostra come far autenticare gli utenti (Authorization Code + PKCE) e, dal browser, avviare job su UiPath Orchestrator sia Cloud che On‑Prem.

Prerequisiti
- Registrare un'applicazione su Orchestrator (ottenere `client_id` e configurare `redirect_uri`).
- Assicurarsi che l'endpoint token e le API di Orchestrator accettino CORS per il dominio statico (MinIO).

Perché questa soluzione
- Non usiamo proxy serverless: l'utente si autentica direttamente e il frontend ottiene i token (flow Authorization Code + PKCE). Non vengono salvati secret nel repository.

Contenuto della cartella
- `login.html`: pagina di esempio con pulsanti di login e start job.
- `auth.js`: implementazione PKCE + exchange token + chiamata start job (template con segnaposti da sostituire).

Note Cloud vs On-Prem
- UiPath Cloud: registrare l'app su Automation Cloud e usare gli endpoint OAuth di UiPath (verificare CORS).
- On-Prem: la configurazione può variare; verificare che Orchestrator sia configurato per OAuth2 e che l'amministratore registri l'app.

Uso rapido
1. Modifica `login.html` inserendo `client_id`, `orchestratorUrl`, `tenant` e `redirect_uri`.
2. Pubblica i file statici su MinIO (o aprili in browser per test locale).
3. Clicca `Login` → autorizza → verrai reindirizzato indietro; quindi `Start Job` per inviare i parametri.

Limitazioni e check
- Verificare che l'endpoint token supporti chiamate CORS dal dominio dove pubblicate i file.
- Se l'endpoint token non supporta CORS, sarà necessario un piccolo componente server-side per scambiare il codice con il token (proxy) — questa soluzione evita secret ma richiede comunque che Orchestrator permetta richieste dal browser.

Se vuoi, provo a:
- Aggiungere una checklist passo-passo per registrare l'app su Automation Cloud.
- Creare la versione in inglese.
