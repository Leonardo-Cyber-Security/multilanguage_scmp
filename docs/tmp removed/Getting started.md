### Getting Started

La soluzione di Secure Cloud Management Platform, in linea con la definizione di Gartner indicata nei Documenti di riferimento, è una piattaforma operativa che permette la governance, la gestione del ciclo di vita, il brokering e l’automazione delle risorse gestite in ambiente cloud.

#### Requirements

La soluzione SCMP è progettata per essere eseguita esclusivamente in ambienti Kubernetes conformi alle versioni supportate indicate nella sezione [Supported Kubernetes Versions](#supported-kubernetes-versions).  
L'installazione richiede la disponibilità di un cluster Kubernetes (upstream o managed service) o OpenShift Container Platform già esistente, dotato delle risorse necessarie per ospitare i componenti core della piattaforma.

In ambienti OpenShift è possibile sfruttare i vantaggi degli operatori certificati Red Hat. In alternativa, è possibile utilizzare cluster Kubernetes upstream o gestiti (EKS, AKS, GKE) con Helm v3.

#### Sizing Raccomandato

Per garantire prestazioni ottimali, si raccomanda che il cluster Kubernetes disponga di nodi con le seguenti caratteristiche minime:

| Tipologia | Ruolo | #qty | vCPU | Memoria (GB) | Disco (GB) | Note |
|-----------|------|------|------|------|------|------|
| Node | Control Plane | 3 | 8 | 16 | 128 | Rispettare l'HA nativa Kubernetes |
| Node | Infra | 3 | 12 | 24 | 628 | Per servizi ingress, logging, monitoring |
| Node | Worker | 4 | 8 | 32 | 128 | Per moduli SCMP e carichi utente |

> ⚠ **Nota:** Le quantità e le dimensioni dei nodi possono variare in base alla dimensione dell'ambiente, al numero di moduli SCMP installati e ai workload da gestire.

#### Altri Requisiti

- **Helm v3** installato e configurato.
- Accesso ai repository Helm e ai registries container indicati nella sezione successiva.
- Network connectivity outbound (porta 443) verso Internet e API/console dei cloud provider supportati.
- Persistent Storage disponibile tramite `StorageClass` compatibile con PersistentVolumeClaim Kubernetes (NFS, Ceph, Portworx, EBS, Azure Disk, ecc.).

La piattaforma SCMP è supportata su Kubernetes e OpenShift nelle seguenti versioni:

| Piattaforma | Versione(i) Supportata(e) | Note |
| ----------------------------------- | ----------------------------------- | ---------------------------------------------------------------- |
| **OpenShift Container Platform (OCP)** | >= 4.14 | Raccomandato l'utilizzo di versioni >= 4.14 per garantire compatibilità con gli operatori certificati |
| **Kubernetes Upstream** | >= 1.25 | Supportato con Helm v3; raccomandato utilizzare versioni >= 1.26 |
| **Amazon EKS (Elastic Kubernetes Service)** | >= 1.25 | Supporto validato per ambienti gestiti EKS |
| **Azure AKS (Azure Kubernetes Service)** | >= 1.25 | Validato per ambienti gestiti AKS |
| **Google GKE (Google Kubernetes Engine)** | >= 1.25 | Validato per ambienti gestiti GKE |

Per effettuare correttamente l' installazione è necessario avere accesso ai seguenti repository:

- [Repository Leonardo](https://dev.azure.com/Leonardo-Cybersecurity/ETD-CMP-HELM/_git/charts)
- [repository charts k8s](https://artifacthub.io/)

Inoltre è necessario verificare che l'ambiente possa effettuare richieste verso le console e le API messe a disposizione dei providers che verranno utilizzati

#### Storage Considerations

[comment]: # (path obbligatori?)

[comment]: # (ci sono configurazioni speciali da fare per gli storage?)

[comment]: # (ci sono anche info su dove e come vengono salvati file e dati)

#### Network Connectivity

[comment]: # (considerazioni di rete (esempio creare un OUTBOUND SSL sulla porta 443))

#### Components

In questa sezione andiamo a definire tutti i componenti necessari per il funzionamento della SCMP.
Gli elementi "required" devono essere installati prima dei vari moduli SCMP come spiegato nella sezione "Installation"

##### Prerequisites

- [Nginx Ingress Controller](https://artifacthub.io/packages/helm/nginx/nginx-ingress)
- [Cert Manager](https://cert-manager.io/docs/installation/kubernetes/)
- [Minio Operator](../minio-operator/README.md)
- [Strimzi Operator](../strimzi-operator/README.md)
- [MongoDB Operator](https://github.com/mongodb/mongodb-kubernetes-operator?tab=readme-ov-file#documentation)
- [Vault AutoUnseal](../vault-autounseal/README.md)

##### Modules

[comment]: # (inserire la lista dei moduli della scmp?)

#### Common Ports & Requirements

[comment]: # (porte utilizzate e relativo requirement)

#### Communication Data

Per aggiornare i dati la SCMP utilizza una serie di cron-job, suddivisi per provider di riferimento e modulo interessato.
Nello specifico possiamo individuare:

| Tipologia | Lanciato ogni | Attività svolta |
|-----------|--------------|------|
| Inventario | 1 ora | Recupera tutte le risorse di inventario disponibili sul provider |
| Costi | 24 ore | Recupera i costi degli ultimi 2 giorni per le risorse disponibili sul provider (vengono recuperati piu giorni per convalidare i dati) |
| Monitoraggio | 24 ore | Recupera le informazioni di monitoraggio delle risorse del provider |
| Catalogo | 24 ore | Recupera le risorse/SKU di catalogo del provider, cosi da permetterne l'utilizzo nella SCMP |
| Sicurezza | 24 ore | Recupera le informazioni di compliance e sicurezza per i provider disponibili |

#### Supported Locales

Al momento le lingue supportate dalla SCMP sono:

- italiano
- inglese

è possibile modificare la lingua utilizzata seguendo [questi passaggi](Funzionalita condivise.md#supporto-multilingua)

### Installation

In questa sezione possiamo trovare l'ordine e i passaggi necessari per effettuare una installazione completa e funzionante.

#### Installation Overview

1. Effettuare l'accesso ai registry helm necessari utilizzando questo codice:
`helm registry login leonardocharts.azurecr.io --username leonardocharts --password $PASSWORD`
2. installare i  [prerequisiti](#prerequisites)
3. Installare una istanza MongoDB (se non disponibile è possibile utilizzare "MongoDB Operator")
4. Configurare i parametri necessari alla chart Leonardo `vault-autounseal` come indicato nella sezione di codice.
```yaml
global:
  OpenShift: true
  imagePullSecrets:
    - name: acr-secret-cs
      credentials: # specify the credentials for the image registry if you want to create the pull secret automatically
      - registry: $DOCKER_REGISTRY
        username: $DOCKER_REGISTRY_USERNAME
        password: $DOCKER_REGISTRY_PASSWORD
        email: ignorethis@email.com
  # The `namespace` key is needed by the official Vault chart in order to load the resources in the appropriate namespace
  # and it has to adhere to our naming scheme '<tenant>-<suffix_namespace>'
  namespace: scmp-vault
  tenant: scmp
  suffix_namespace: vault
```
5. Installare il chart Leonardo `vault-Autounseal` appena configurato utilizzando il codice. 
`helm install vault-autounseal vault-autounseal`
6. **Dopo il completamento dell' installazione di `vault-autounseal` (cioè quando nel cluster sono gia disponibili i pod denominati `vault-prod`) configurare i parametri di installazione della SCMP come nel codice.
```yaml
global:
  tenant: scmp
  imagePullSecrets:
    - name: acr-secret-cs
      credentials: # specify the credentials for the image registry if you want to create the pull secret automatically
      - registry: $DOCKER_REGISTRY
          username: $DOCKER_REGISTRY_USERNAME
          password: $DOCKER_REGISTRY_PASSWORD
          email: ignorethis@email.com
  minio:
    accesskey: "minioadmin"
    password: "minioadmin123!"
```
7. Lanciare l'installazione della SCMP utilizzando la chart appena modificata, per lanciarlo possiamo utilizzare:
`helm install scmp scmp/`

!!! warning "Esegui le configurazioni"

    Dopo aver effettuato l'installazione sono necessari dei passaggi di configurazione, come descritto nella sezione [Appliance Setup](#appliance_setup)

### Upgrades & Maintenance

[comment]: # (guida all' aggiornamento (readme.md))

### Additional Configuration Options

#### Load Balancer Configuration

[comment]: # (configurazione load balancer?)

#### Proxies

[comment]: # (configurazione proxy?)

#### SSL Certificates

[comment]: # (certificati necessari?)

#### Data Encryption

[comment]: # (come garantiamo l' encryption?)

### Initial Appliance Setup

#### Appliance Setup

#### Network Configuration

- Abilitare l' ingress controller cosi da esporre in rete i servizi
- (opzionale) Creare un DNS name per facilitare la connessione al sistema

#### Keycloak Setup

- Configure Realm theme on Keycloak
- Create client 'microfe' on Keycloak Realm:
  - Enable 'Implicit Flow'
  - Set 'Valid Redirect URIs' to:
    - `http://localhost:3000/*`
    - SCMP host domain

#### Content Management

- Upload micro frontends in singlespa bucket
  - *Alternatively:* Use minio-uploader utility chart
- Upload micro frontends config in singlespa-config bucket
  - *Alternatively:* Use minio-uploader utility chart

#### Access Control

- Set anonymous read-only access on Minio buckets:
  - singlespa
  - singlespa-config
  - config

- Configurare utenze e ruoli di IAM , come indicato nella sezione [Creazione Utenti IAM](Authentication#utenti)
