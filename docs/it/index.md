# HOME

SCMP è la piattaforma di cloud management di Leonardo S.p.A. che permette la governance, la gestione del ciclo di vita, il brokering e l’automazione delle risorse gestite in ambiente cloud.

## In breve

La soluzione di Secure Cloud Management Platform, in linea con la definizione di Gartner indicata nei Documenti di riferimento, è una piattaforma operativa che permette la governance, la gestione del ciclo di vita, il brokering e l’automazione delle risorse gestite in ambiente cloud e si divide nelle seguenti aree funzionali:

* Inventory and classification
* Monitoring and Analytics
* Cost management and workload optimization
* Security & compliance
* Orchestration and Provisioning

La piattaforma supporta gli ambienti su Google Cloud, Microsoft Azure, VMWare, Azure Stack HUB & HCI, Red Hat OpenShift, Amazon Web Services (AWS), Oracle OCI, data la loro ampia presenza nel settore Enterprise.

## Architettura

L’architettura di SCMP è un’architettura a moduli come descritto di seguito:

* SCMP Portal: Una soluzione di front end web e mobile flessibile, consente di comporre la soluzione verso diverse esigenze del cliente. Permette la gestione degli utenti, delle risorse come Virtual Machines, storage, network e consente di effettuare monitoring e Provisioning di tutte le risorse di ogni cloud provider configurato.

* SCMP Components: In questo layer vengono inserite tutte le componenti della piattaforma sviluppate per poter erogare le funzionalità di gestione della piattaforma cloud management.

* SCMP Abstraction Layer: L’Abstraction Layer consente di fornire un livello di astrazione delle risorse erogate dai cloud Providers implementando direttamente i protocolli di comunicazione specifici e uniformando l’accesso a risorse della stessa tipologia.

* SCMP Platform Components: In questo layer vengono inserite tutte le componenti della piattaforma gestite con soluzioni di terze parti. In questo layer sono presenti i sistemi di identificazione, la soluzione di Api gateway, il sistema di cache e la gestione dei topics.

* Cloud Providers: In questo layer vengono inseriti tutte le piattaforme cloud che la SCMP riesce a supportare, come Microsoft Azure, VMWare vSphere, Google Cloud Provider (GCP), Amazon Web Services (AWS), Red Hat OpenShift, Microsoft Azure Stack Hub and Microsoft Stack HCI, RedHat OpenShift e Vcloud Director e Oracle.

Lo sviluppo della Cloud Management Platform nasce per soddisfare il
bisogno di gestire, orchestrare, proteggere e governare ambienti Cloud
ibridi, multi-cloud ed Edge computing.

La SCMP svolge un ruolo essenziale per una gestione integrata di
ambienti complessi dove possono coesistere e cooperare servizi erogati
da molteplici Cloud Service Provider e servizi presenti su
infrastrutture on premise o in infrastrutture Edge.

L’integrazione tra i vari moduli che la compongono permette la gestione
di tutte le funzionalità presenti su SCMP che possono essere raggruppate
per le seguenti categorie:

## Funzionalità software

| **Funzionalità** | **Descrizione** |
|----|----|
| **Monitoring** | Monitoraggio Istanze Inventario |
| **Costs** | Visualizzazione e Reportistica Costi |
| **Inventory** | Visualizzazione, Reportistica e Scenari “what if” Inventario |
| **Security** | Visualizzazione e gestione falle di sicurezza sugli asset di inventario |
| **Dashboard** | Visualizzazione sintetica dei vari moduli |
| **Catalog** | Gestione e definizione elementi a Catalogo |
| **Authentication** | Profilatura Utenti |
| **Administration** | Amministrazione Provider |
| **Cloud Maturity Model** | Strumento a supporto del processo di migrazione al cloud (Rif. R2) |
| **Provisioning** | Provisioning asset sottosistemi e software |
| **Tenant management** | Gestione e creazione di Tenant |
| **Service Detail Design** | Ricezione e gestione di ordini di lavoro da svolgere nella SCMP |

[Scarica la documentazione PDF](SCMP_SUM.pdf)
