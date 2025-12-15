### Getting Started

The Secure Cloud Management Platform solution, in line with Gartner's definition indicated in the Reference Documents, is an operational platform that enables the governance, lifecycle management, brokering, and automation of resources managed in a cloud environment.

#### Requirements

The SCMP solution is designed to run exclusively in Kubernetes environments compliant with the supported versions indicated in the section [Supported Kubernetes Versions](#supported-kubernetes-versions).  
Installation requires the availability of an existing Kubernetes cluster (upstream or managed service) or OpenShift Container Platform, equipped with the necessary resources to host the platform's core components.

In OpenShift environments, it is possible to leverage the benefits of Red Hat certified operators. Alternatively, it is possible to use upstream or managed Kubernetes clusters (EKS, AKS, GKE) with Helm v3.

#### Recommended Sizing

To ensure optimal performance, it is recommended that the Kubernetes cluster has nodes with the following minimum characteristics:

| Type | Role | #qty | vCPU | Memory (GB) | Disk (GB) | Notes |
|-----------|------|------|------|------|------|------|
| Node | Control Plane | 3 | 8 | 16 | 128 | Respect native Kubernetes HA |
| Node | Infra | 3 | 12 | 24 | 628 | For ingress, logging, monitoring services |
| Node | Worker | 4 | 8 | 32 | 128 | For SCMP modules and user workloads |

> ⚠ **Note:** Node quantities and sizes may vary based on environment size, number of SCMP modules installed, and workloads to be managed.

#### Other Requirements

- **Helm v3** installed and configured.
- Access to Helm repositories and container registries indicated in the next section.
- Outbound network connectivity (port 443) to the Internet and APIs/consoles of supported cloud providers.
- Persistent Storage available via `StorageClass` compatible with Kubernetes PersistentVolumeClaim (NFS, Ceph, Portworx, EBS, Azure Disk, etc.).

The SCMP platform is supported on Kubernetes and OpenShift in the following versions:

| Platform | Supported Version(s) | Notes |
| ----------------------------------- | ----------------------------------- | ---------------------------------------------------------------- |
| **OpenShift Container Platform (OCP)** | >= 4.14 | Recommended to use versions >= 4.14 to ensure compatibility with certified operators |
| **Kubernetes Upstream** | >= 1.25 | Supported with Helm v3; recommended to use versions >= 1.26 |
| **Amazon EKS (Elastic Kubernetes Service)** | >= 1.25 | Validated support for managed EKS environments |
| **Azure AKS (Azure Kubernetes Service)** | >= 1.25 | Validated for managed AKS environments |
| **Google GKE (Google Kubernetes Engine)** | >= 1.25 | Validated for managed GKE environments |

To perform the installation correctly, access to the following repositories is required:

- [Repository Leonardo](https://dev.azure.com/Leonardo-Cybersecurity/ETD-CMP-HELM/_git/charts)
- [repository charts k8s](https://artifacthub.io/)

Furthermore, it is necessary to verify that the environment can make requests to the consoles and APIs provided by the providers that will be used.

#### Storage Considerations

[comment]: # (mandatory paths?)

[comment]: # (are there any special configurations to make for storage?)

[comment]: # (there is also info on where and how files and data are saved)

#### Network Connectivity

[comment]: # (network considerations (e.g. create an OUTBOUND SSL on port 443))

#### Components

In this section, we define all the components necessary for the SCMP to function.
The "required" elements must be installed before the various SCMP modules as explained in the "Installation" section.

##### Prerequisites

- [Nginx Ingress Controller](https://artifacthub.io/packages/helm/nginx/nginx-ingress)
- [Cert Manager](https://cert-manager.io/docs/installation/kubernetes/)
- [Minio Operator](../minio-operator/README.md)
- [Strimzi Operator](../strimzi-operator/README.md)
- [MongoDB Operator](https://github.com/mongodb/mongodb-kubernetes-operator?tab=readme-ov-file#documentation)
- [Vault AutoUnseal](../vault-autounseal/README.md)

##### Modules

[comment]: # (insert the list of scmp modules?)

#### Common Ports & Requirements

[comment]: # (ports used and related requirement)

#### Communication Data

To update data, the SCMP uses a series of cron-jobs, divided by reference provider and relevant module.
Specifically, we can identify:

| Type | Launched every | Activity performed |
|-----------|--------------|------|
| Inventory | 1 hour | Retrieves all inventory resources available on the provider |
| Costs | 24 hours | Retrieves costs for the last 2 days for resources available on the provider (multiple days are retrieved to validate data) |
| Monitoring | 24 hours | Retrieves monitoring information for the provider's resources |
| Catalog | 24 hours | Retrieves catalog resources/SKUs from the provider, allowing their use in the SCMP |
| Security | 24 hours | Retrieves compliance and security information for available providers |

#### Supported Locales

Currently, the languages supported by SCMP are:

- Italian
- English

It is possible to change the language used by following [these steps](Funzionalita condivise.md#supporto-multilingua)

### Installation

In this section, you can find the order and the necessary steps to perform a complete and functional installation.

#### Installation Overview

1. Log in to the necessary Helm registries using this code:
`helm registry login leonardocharts.azurecr.io --username leonardocharts --password $PASSWORD`
2. Install the [prerequisites](#prerequisites)
3. Install a MongoDB instance (if not available, "MongoDB Operator" can be used)
4. Configure the necessary parameters for the Leonardo `vault-autounseal` chart as indicated in the code section.
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
5. Install the newly configured Leonardo `vault-Autounseal` chart using the code.
`helm install vault-autounseal vault-autounseal`
6. **After the completion of the `vault-autounseal` installation (i.e., when `vault-prod` pods are already available in the cluster), configure the SCMP installation parameters as in the code.
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
7. Launch the SCMP installation using the newly modified chart; to launch it, we can use:
`helm install scmp scmp/`

!!! warning "Perform Configurations"

    After the installation, configuration steps are required, as described in the [Appliance Setup](#appliance_setup) section.

### Upgrades & Maintenance

[comment]: # (upgrade guide (readme.md))

### Additional Configuration Options

#### Load Balancer Configuration

[comment]: # (load balancer configuration?)

#### Proxies

[comment]: # (proxy configuration?)

#### SSL Certificates

[comment]: # (necessary certificates?)

#### Data Encryption

[comment]: # (how do we ensure encryption?)

### Initial Appliance Setup

#### Appliance Setup

#### Network Configuration

- Enable the ingress controller to expose services on the network.
- (optional) Create a DNS name to facilitate connection to the system.

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

- Configure IAM users and roles, as indicated in the [IAM User Creation](Authentication#utenti) section.

