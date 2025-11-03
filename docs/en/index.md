# HOME

SCMP is the cloud management platform of Leonardo S.p.A. that allows the governance, lifecycle management, brokering, and automation of resources managed in a cloud environment.

## In brief

The Secure Cloud Management Platform solution, in line with Gartner's definition indicated in the Reference Documents, is an operational platform that allows the governance, lifecycle management, brokering, and automation of resources managed in a cloud environment and is divided into the following functional areas:

*   Inventory and classification
*   Monitoring and Analytics
*   Cost management and workload optimization
*   Security & compliance
*   Orchestration and Provisioning

The platform supports environments on Google Cloud, Microsoft Azure, VMWare, Azure Stack HUB & HCI, Red Hat OpenShift, Amazon Web Services (AWS), Oracle OCI, given their wide presence in the Enterprise sector.

## Architecture

The SCMP architecture is a modular architecture as described below:

*   SCMP Portal: A flexible web and mobile front-end solution, it allows composing the solution to different customer needs. It enables the management of users, resources such as Virtual Machines, storage, network, and allows monitoring and Provisioning of all resources from each configured cloud provider.

*   SCMP Components: This layer includes all platform components developed to provide the management functionalities of the cloud management platform.

*   SCMP Abstraction Layer: The Abstraction Layer allows providing a level of abstraction for resources delivered by cloud Providers by directly implementing specific communication protocols and standardizing access to resources of the same type.

*   SCMP Platform Components: This layer includes all platform components managed with third-party solutions. This layer contains identification systems, the API gateway solution, the cache system, and topic management.

*   Cloud Providers: This layer includes all cloud platforms that SCMP can support, such as Microsoft Azure, VMWare vSphere, Google Cloud Provider (GCP), Amazon Web Services (AWS), Red Hat OpenShift, Microsoft Azure Stack Hub and Microsoft Stack HCI, RedHat OpenShift, Vcloud Director, and Oracle.

The development of the Cloud Management Platform was created to satisfy the need to manage, orchestrate, protect, and govern hybrid, multi-cloud, and Edge computing environments.

SCMP plays an essential role for integrated management of complex environments where services provided by multiple Cloud Service Providers and services present on on-premise or Edge infrastructures can coexist and cooperate.

The integration between the various modules that compose it allows the management of all functionalities present on SCMP which can be grouped into the following categories:

## Software functionalities

| **Functionality** | **Description** |
|-------------------|---------------------------------------------------------------------------------------------------|
| **Monitoring** | Monitoring Inventory Instances |
| **Costs** | Cost Visualization and Reporting |
| **Inventory** | Inventory Visualization, Reporting, and "What if" Scenarios |
| **Security** | Visualization and management of security vulnerabilities on inventory assets |
| **Dashboard** | Synthetic visualization of the various modules |
| **Catalog** | Management and definition of Catalog elements |
| **Authentication** | User Profiling |
| **Administration** | Provider Administration |
| **Cloud Maturity Model** | Tool to support the cloud migration process (Ref. R2) |
| **Provisioning** | Provisioning of subsystem and software assets |
| **Tenant management** | Tenant Management and Creation |
| **Service Detail Design** | Receipt and management of work orders to be performed in SCMP |

[Download PDF documentation](SCMP_SUM.pdf)
