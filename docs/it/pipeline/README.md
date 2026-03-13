Triggerare Azure Pipelines dal frontend (esempio con Personal Access Token)

Questo esempio mostra come elencare pipeline e avviarne una su Azure DevOps usando un Personal Access Token (PAT).

ATTENZIONE SULLA SICUREZZA
- Esporre un PAT nel frontend è intrinsecamente insicuro: chiunque con accesso al browser/pagina può copiarlo e usarlo.
- Raccomandazione: conservare il PAT in un componente server-side o usare Azure AD/OAuth per flussi più sicuri.

Quando usare questo esempio
- Debug rapido o ambiente di test controllato.
- Se non è possibile avere un componente server-side e il PAT viene usato solo in ambienti molto controllati.

Endpoint principali (YAML pipelines)
- Elencare pipeline: `GET https://dev.azure.com/{organization}/{project}/_apis/pipelines?api-version=7.1-preview.1`
- Avviare pipeline: `POST https://dev.azure.com/{organization}/{project}/_apis/pipelines/{pipelineId}/runs?api-version=7.1-preview.1`

Autenticazione via PAT
- Usare header `Authorization: Basic BASE64(:{PAT})` (ossia base64 di ":{PAT}").

Contenuto della cartella
- `trigger.html`: esempio UI per inserire organization, project, PAT, selezionare pipeline e avviare con parametri.
- `trigger.js`: helper JS per mettere il PAT in `sessionStorage`, chiamare gli endpoint e mostrare risultati.

Note CORS
- Azure DevOps REST API può richiedere CORS abilitato per chiamate da browser; verifica se la tua organizzazione lo permette. Se CORS è bloccato, dovrai usare un proxy sicuro.
