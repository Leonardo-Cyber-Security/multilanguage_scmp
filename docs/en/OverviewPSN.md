# Leonardo Services

Leonardo provides several managed services which are represented in the following figure by type (called service families).

![Overview Leonardo Services](assets/images/extract/media/PSN1.png)

From a logical-functional point of view, the services can be divided into three macro-categories:

- Infrastructure as a Service (IaaS) Services
- Container as a Service (CaaS) Services
- Platform as a Service (PaaS) Services

The IaaS and CaaS categories include some services from the "Compute" family. The PaaS category includes services from all other families.

The aforementioned macro-categories will be described below.

## Infrastructure as a Service (IaaS) Services

In the following table, you can consult the services pertaining to the Infrastructure as a Service (IaaS) category.

| FAMILY | SUB-FAMILY | SERVICE NOMENCLATURE |
| -------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Compute | Confidential - IaaS - Private | - Pool Small (Confidential)<br> - Pool Medium (Confidential)<br> - Pool Large (Confidential)<br> - Pool X-Large (Confidential) |

### Compute
Below are the sub-families pertaining to the Compute family:
- Confidential - IaaS - Private

#### Confidential - IaaS - Private

Below is the list of services pertaining to the Confidential - IaaS - Private sub-family:

 - Pool Small (Confidential) 
 - Pool Medium (Confidential)
 - Pool Large (Confidential)
 - Pool X-Large (Confidential)

 "**Service Description**"

 The services allow for the provision of virtual computational environments (IaaS) of Private type, i.e., on a pool of physical resources, dedicated and isolated for each individual client, based on the use of “bare metal” compute instances. 
 The data of the physical resources are encrypted and kept protected in all phases of their use (At-Rest, In-transit & In-use), leveraging the Confidential Computing paradigm. 
 Depending on the pool of computational resources required for each individual Administration, it is possible to choose the most suitable service from the four available types.

 "**Service Features and Benefits**"

Private Cloud resources are exclusively dedicated to each client. The services use secure Enclaves based on Trusted Execution Environment (TEE) leveraging HW Confidential, which offer an advanced level of security for data in use, protecting them during processing. 
They support advanced data encryption at Rest, in Transit & in Use.
They use advanced Remote Attestation systems to verify the correctness of the TEE environment, isolating the memory of virtual machines from the host operating system and other malicious guests.

The advantages offered by the services are:

- Security and confidentiality of data in dedicated environments;
- Workload isolation through advanced virtualization;
- Dedicated firewalls and network micro-segmentation;
- Automated provisioning and rapid resource management;
- Total control and centralized governance: centralized monitoring and auditing for traceability.

## Container as a Service (CaaS) Services

In the following table, you can consult the services pertaining to the Container as a Service (CaaS) category.

| FAMILY | SUB-FAMILY | SERVICE NOMENCLATURE |
| -------- | ----------------------------------- | --------------------------------- |
| Compute | Confidential - Kubernetes - Private | Kubernetes Confidential Computing |

### Compute
Below are the sub-families pertaining to the Compute family:
- Confidential - Kubernetes - Private

#### Confidential - Kubernetes - Private
Below is the list of services pertaining to the Confidential - IaaS - Private sub-family:

- Kubernetes Confidential Computing

 "**Service Description**"
Service that allows the provision of a platform for the orchestration of private and secure containers, designed to manage containerized applications in highly regulated environments or with confidentiality requirements.
It offers a secure and controlled Kubernetes environment where the security component is one of the main aspects of the solution. The operating system on which the solution is based is hardened, to minimize the attack surface and potential vulnerabilities. 
Within the architectural components of the solution, mechanisms are used to ensure data security even during communication phases (through encryption mechanisms applied by default to communications between platform components) and for data stored within the platform itself.
The platform can be customized to adapt to the specific needs of each Organization, ensuring integration with existing corporate systems and applications.

 "**Service Features and Benefits**"
Its implementation requires a combination of hardware certified for Confidential Computing, a security-hardened private Kubernetes infrastructure, and a set of observability and governance tools to maintain total control over the container lifecycle.
Included functionalities:

- *Data protection* → the operating system is configured to ensure protection in all its phases: data in memory, through full disk encryption and key rotation; data in transit, using secure and encrypted communication protocols; data in use, adopting Confidential Computing practices and secure execution environments.

- *Secure Enclaves* → apply isolation and encryption, ensuring that only authorized parties can access the data.
- *Trusted Execution Environments (TEE)* → add a secure processing environment, protecting data from external threats.

Being a managed Kubernetes solution, the client will not have to deal with infrastructure management and its complexity, as the infrastructural layer is managed by Leonardo throughout the service lifecycle.

The advantages offered are:

- Security and confidentiality of containerized applications: end-to-end encryption, confidential computing for workloads, container isolation on dedicated nodes with hardware-based protection, integrated security policies, and advanced RBAC;
- Centralized control and governance of clusters;
- Scalability and flexibility;
- Integration with multicloud and legacy environments.

## Platform as a Service (PaaS) Services

In the following table, you can consult the services pertaining to the Platform as a Service (PaaS) category.

| FAMILY | SUB-FAMILY | SERVICE NOMENCLATURE |
| -------------------- | -------------------------- | ----------------------------------------------------------- |
| Compute | FAAS | Functions as a Service |
| Security | IAM | Identity & Access Management Service |
| Security | Key Management | Key Vault as a Service |
| Middleware | API Platform | PaaS API Management |
| Middleware | APP Runtime | Jboss as a Service |
| Middleware | APP Runtime | Spring boot as a Service |
| Middleware | BPM | PaaS Business Process as a Service |
| Middleware | CMS | PaaS CMS as a Service |
| Middleware | ETL | PaaS ETL - Batch / Real Time Processing - 1 worker |
| Infra & Ops Platform | Multicloud Management | Multicloud Management Platform-Leonardo SCMP |
| Infra & Ops Platform | Multicloud Management | Multicloud Management Platform-Morpheus |
| Infra & Ops Platform | Observability-Infra | Control Room as Service |
| Infra & Ops Platform | Observability-Infra | IT infrastructure Service Operations (Logging & Monitoring) |
| Infra & Ops Platform | TTM | PaaS Ticket Management Service |
| Infra & Ops Platform | TTM | PaaS Ticket Management Service (ITSM) |
| Infra & Ops Platform | TTM | PaaS Ticket Management Service (ADD-ON ITOM) |
| DevSecOps | CI | Configuration Manager |
| DevSecOps | CI | Test Automation |
| DevSecOps | CI | Quality Code Analysis |
| DevSecOps | CI/CD | DevSecOps As A Service By PSN |
| DevSecOps | CI/CD | Qualizer DevSecOps |
| Big Data | Data Lake | Data Lake - 1TB |
| Big Data | Data Lakehouse | Data Lakehouse |
| Big Data | Business Intelligence | Business Intelligence |
| Big Data | ETL | Batch/Real time Processing - 1 Worker |
| Big Data | Event Platform | Event Message |
| Big Data | Data Governance | Data Governance |
| AI | AI - Audio & Conversations | Speech to Text |
| AI | AI - Image | OCR |
| AI | AI - Text | AI Search - AI Search - RAG - 10 GB - 1 worker |
| AI | AI - Text | Text Analytics |
| AI | AI - Text | Translation |
| AI | AI - Generative | AI SLM/LLM |
| AI | AI - Tools | AI workflow |
| AI | AI - Tools | Vector DB |
| AI | AI - Tools | AI Platform |
| VDI | Virtual Desktop | VDI |
| VDI | Virtual Desktop | VDI with GPU Support |
| Collaboration | Communication | Instant Messaging |

### Compute
Below are the sub-families pertaining to the Compute family:
- FAAS       

#### FAAS
Below is the list of services pertaining to the FAAS sub-family:

- Functions as a Service

 "**Service Description**"         
 FaaS (Function as a Service) is a system design model, event-driven, executed on stateless containers, where developers create, deploy, and run small, independent functions to perform specific tasks without worrying about the underlying infrastructure.
 The adoption of FaaS allows for the standardization of application development and execution, centralizing cross-functional capabilities such as orchestration, automatic provisioning, monitoring, integrated service management, and event-driven flow control.
 It offers tools for: 

 - centrally manage serverless functions;
 - automate component lifecycle management;
 - enable multi-cloud and hybrid cloud portability;
 - support innovation with GPU runtimes and dedicated AI tools.
The FaaS platform provides and scales underlying resources based on demand. It is ideal for highly dynamic scenarios, with variable workloads, and integrates seamlessly with microservices and event-driven architectures.

 "**Service Features and Benefits**"
 The service is not limited to providing an execution engine, but offers a complete ecosystem, composed of: 

- *Serverless execution* → stateless functions and event-driven workflows, scalable and available in various programming languages.
- *Portability and independence* → executable on any Kubernetes cluster, multi-environment, without lock-in constraints.
- *Security and compliance* → data protection and centralized access management.
- The solution allows organizations to adopt a modern and flexible model, reducing operational complexity and benefiting from a standardized and easily accessible service.

The service is delivered via Apache OpenServerless, an open-source, cloud-agnostic serverless platform based on Apache OpenWhisk as a Function-as-a-Service (FaaS) engine.

The advantages offered are:

- *Reduction of operating costs* → you only pay for the actual use of the functions;
- *Flexibility and scalability* → resources adapt to demand;
- *Operational efficiency* → elimination of direct server management, patching, and updates;
- *High availability* → integrated redundancy and fault tolerance, ensuring high availability of functions even in the event of hardware failures or other interruptions;
- *Accelerated time-to-market* → rapid release of new functionalities without worrying about the infrastructure;
- *Development agility* → focus on code and business logic, not on server management;
- *Continuous innovation* → rapid experimentation with new low-cost services;
- *Competitive advantage* in cost and speed compared to traditional hosting models.
