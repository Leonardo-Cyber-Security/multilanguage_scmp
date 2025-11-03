# Administration

The Administration functionality is the starting point for using the SCMP.

The providers configured within this functionality will be used by the system to retrieve all necessary information.

Within this functionality, it will be possible to:

- Configure cloud providers that can be used in the reference Tenant.
- Configure folders for various providers.
- Configure cloud SIEMs for various providers.
- Configure KeyVaults for various providers.
- Configure CommVaults for Backup and Disaster & Recovery for various providers.
- Configure Confidential Computing for various providers.

### providers/subsystems

#### List of subsystems

To access the Administration functionality, click the bento button in the top left corner. Then, click "Administration".

![Access to Administration functionality](images/extract/media/image42.png)

At this point, the user is on the "Cloud Systems" tab page, where general information about the subsystems can be viewed, such as the reference provider and the subsystem's creation date. It also indicates with a red checkmark if the system is On-Premise.

We can notice that the list contains "folders," which are containers for subsystems. Clicking on the "arrow" corresponding to the folder row displays the subsystems within it and their information.

![List of subsystems and folders](images/extract/media/270125001.png)

Additionally, each subsystem has a status, represented by a colored "LED":

- Green: the subsystem functions correctly in the SCMP "status: ok".
- Red: the subsystem is no longer usable by the SCMP "status: failed".

The SCMP periodically performs connection tests on all configured subsystems. When a subsystem fails this check, its status is updated, and all information retrieval processes (costs, inventory, monitoring, security) are disabled.

This might happen, for example, when the secret or passwords used for connection expire and need to be renewed.
By modifying the subsystem, it is possible to insert new connection parameters to re-establish its correct functioning, which will be confirmed by an "OK" status.

##### **Information on subsystem cron-jobs**

Each tenant performs various information retrieval operations for all configured subsystems throughout the day, allowing the user to view all necessary data using only the SCMP.

To view the outcome of these operations, click on the subsystem row and, within the modal, select the "Show discovery info" button.

In addition to the number of operations and their outcome, scrolling down reveals the list and relevant details by clicking the "arrow" next to the operation of interest.

![Information on cron-jobs](images/extract/media/image55.png)

##### Viewing, modifying, and deleting a subsystem

To view the data of a Cloud Provider, within the list, click on the kebab menu corresponding to the Cloud Provider of interest and click "Show".

![Access to Cloud Provider in view mode](images/extract/media/image43.png)

On this page, you can view the Provider's configuration.

![Subsystem in view mode](images/extract/media/image44.png)

If the provider is "ON-PREMISE", a table showing the usable capacities on the system and the list of resources already present in the subsystem will be visible below the configuration.

![List of On-Premise machines](images/extract/media/image45.png)

To return to the Cloud Provider page, click the "Close" button in the bottom left.

To modify the data of a Cloud Provider, within the list, click on the kebab menu corresponding to a Cloud Provider, and click "Edit".

![Access to Cloud Provider in edit mode](images/extract/media/image46.png)

After doing so, the user will be on the Cloud Provider page in "edit" mode, which allows data modification.

To return to the Cloud Provider page, click the "Save" button in the bottom left.
At this point, the user will be on the Cloud Provider page.

![Initiating the deletion of a Cloud Provider](images/extract/media/image47.png)

To delete a Cloud Provider, within the list, click on the kebab menu corresponding to a Cloud Provider, and click "Delete".

![Confirm Cloud Provider deletion](images/extract/media/image48.png)

After doing so, a modal will appear where you need to click the "Remove" button.

At this point, the Cloud Provider will no longer be present in the list, and the asset removal flow will be launched on the resource-manager.

##### **Cost model for "On-Premise" providers**

To manage resource usage costs for "On-Premise" providers, the ability to define a specific cost model per subsystem is provided.

The cost model allows configuring both "provider" costs (i.e., those actually incurred) and subsequently applying a discount or markup percentage to be applied to the customer.

Providers that use this functionality are:

- VMWare
- VCloud Director
- RedHat Edge
- OpenShift

To modify the model, click the "three dots" button next to a subsystem and select "Cost model".

![Access to subsystem cost model](images/extract/media/image49.png)

On the model page, we find a first generic section where it will be possible to configure the following fields:

- Currency: the reference currency to be used for the subsystem.
- Discount/Surcharge: a discount or markup percentage to be applied to customer costs.

![Cost model](images/extract/media/270125002.png)

Subsequently, clicking the "Add rate" button will open a modal where, after choosing a metric (specific to the provider) and its relative unit of measurement, the price to be applied to all elements of the subsystem will be entered. Finally, click the "Save" button to confirm the entry.

![Selection of metric to price](images/extract/media/image51.png)

To confirm the changes to the model after entering all costs for each available component type, click the "Apply" button at the bottom.

![Complete cost model](images/extract/media/image52.png)

##### **Manual cost update**

The user is given the possibility to perform a manual cost update if needed. This asynchronous operation can be requested individually per subsystem or globally for the entire tenant, which is automatically propagated to all available subsystems.

To request an update for a single subsystem, click the "three dots" button on the subsystem row and select "Refresh Cost".

![Manual cost update](images/extract/media/image53.png)

Within the modal, we can specify for how many days, starting from today's date, the costs of the selected subsystem should be re-downloaded and re-confirmed. After confirmation, we can go to the "cron-job Info" section to confirm the operations.

Additionally, it is possible to request a cost update for the entire tenant: by first clicking the "hamburger menu" button available in the top left and selecting "refresh cost", the activity will be distributed across all available subsystems on the page.

![Cost update for the entire tenant](images/extract/media/image54.png)

Once a cost recovery is selected, it is possible to indicate the number of days to recover, and by selecting the "Reset the cost" box, the SCMP will first perform a data cleanup (for the selected range) and then perform the refresh.

![Cost refresh configuration](images/extract/media/20250604001.png)

##### Cost recovery and calculation process

###### Cost recovery structure

The cost recovery process is performed by the "Abstraction Layer" module, which consists of:

- A sub-module of ABS called "layer" for each provider type (e.g., "CMP-ABS-VMWare-layer").
- ABS Gateway: this sub-module manages the communication and standardization of information retrieved from the various Layers of different providers and makes it available to other modules of the SCMP system.

The cost recovery process is performed by a cron-job, which is launched once per provider, automatically during nighttime hours.

For ON-Premise providers, usage values are automatically generated by the SCMP based on the quantity of resources available in inventory, using the same "ABS" modules. Subsequently, as with other providers, the usage values will be used to calculate costs via the cost model described in the Administration section.

In case of failure, the process is automatically scheduled up to 3 attempts. If the system fails to resolve automatically, manual intervention is required. Additionally, a manual cost update can be requested using the buttons available in the Administration section.

Below are the specific details by subsystem type.

###### Customer cost recovery and calculation for the *Azure* provider

**Recovery methods:**

- **"Standard" model**: The ABS module requests costs for the last 2 days via Azure's REST APIs, which are then saved in the SCMP database.
- **"Storage Account" model**: The ABS module retrieves a file containing cost extractions, divided by subsystem, which are then saved in the SCMP database.
- **"Billing storage" model**: The ABS module retrieves a file containing extractions of all subscriptions available in the "billing account"; the results are divided by subsystem and saved in the database.

**Cost calculation per single resource:**

1.  The ABS module sends cost information and information about the resource that generated them to the cost module.
2.  The cost module verifies the subsystem configuration to identify the "aggregation type". This parameter indicates which catalog to use ([RESOURCES](Catalog.md#risorse-e-relazioni-tra-risorse) or [SKUs](Catalog.md#risorse-e-relazioni-tra-sku)) to correctly calculate the price.
3.  The cost module checks if the resource identifier (UUID) is present in the [SCMP catalog](Catalog.md#gestione-elementi-di-catalogo-scmp). If present, the system multiplies the usage by the catalog cost.
4.  If the resource is not present in the catalog (and therefore does not fall into the previous step), the SCMP will apply the discount/markup percentage configured [in the subsystem](Administration.md#parametri-azure).

###### Customer cost recovery and calculation for the *AWS* provider

- **"Standard" model**: The ABS module queries AWS Cost Explorer APIs to get costs for the last 2 days, saving the data into the SCMP database.
- **"ARN ROLE" model**: The ABS module assumes a specific IAM role ([ARN ROLE](Administration.md#parametri-amazon-web-services)) to access AWS billing data. Costs are extracted and divided by subsystem, then saved into the SCMP database.

**Cost calculation per single resource:**

1.  The ABS module sends cost information and information about the resource that generated them to the cost module.
2.  The cost module verifies the subsystem configuration to identify the "aggregation type". This parameter indicates which catalog to use ([RESOURCES](Catalog.md#risorse-e-relazioni-tra-risorse) or [SKUs](Catalog.md#risorse-e-relazioni-tra-sku)) to correctly calculate the price.
3.  The cost module checks if the resource identifier (UUID) is present in the [SCMP catalog](Catalog.md#gestione-elementi-di-catalogo-scmp). If present, the system multiplies the usage by the catalog cost.
4.  If the resource is not present in the catalog (and therefore does not fall into the previous step), the SCMP will apply the discount/markup percentage configured [in the subsystem](Administration.md#parametri-amazon-web-services).

###### Customer cost recovery and calculation for the *Google* provider

- **"Standard" model**: The ABS module queries Google Cloud Billing APIs to get costs for the last 2 days, saving the data into the SCMP database.
- **"Dataset Export" model**: The ABS module accesses billing data exported from **BigQuery**. Costs are extracted, divided by subsystem, and saved into the SCMP database.

**Cost calculation per single resource:**

1.  The ABS module sends cost information and information about the resource that generated them to the cost module.
2.  The cost module verifies the subsystem configuration to identify the "aggregation type". This parameter indicates which catalog to use ([RESOURCES](Catalog.md#risorse-e-relazioni-tra-risorse) or [SKUs](Catalog.md#risorse-e-relazioni-tra-sku)) to correctly calculate the price.
3.  If the "Cost from USD" field has been selected, the system will use the price in USD (returned by the provider) for the calculation, to which a discount/markup percentage defined in the administration section is applied. Otherwise, the price already converted to EUR is used.
4.  The cost module checks if the resource identifier (UUID) is present in the [SCMP catalog](Catalog.md#gestione-elementi-di-catalogo-scmp). If present, the system multiplies the usage by the catalog cost.
5.  If the resource is not present in the catalog (and therefore does not fall into the previous step), the SCMP will apply the discount/markup percentage configured [in the subsystem](Administration.md#parametri-google-cloud).

###### Customer cost recovery and calculation for *Oracle, OracleEXAcc* providers

- **"Standard" model**: The ABS module queries ORACLE APIs to get costs for the last 2 days, saving the data into the SCMP database.

**Cost calculation per single resource:**

1.  The ABS module sends cost information and information about the resource that generated them to the cost module.
2.  The cost module verifies the subsystem configuration to identify the "aggregation type". This parameter indicates which catalog to use ([RESOURCES](Catalog.md#risorse-e-relazioni-tra-risorse) or [SKUs](Catalog.md#risorse-e-relazioni-tra-sku)) to correctly calculate the price.
3.  If the "Cost from USD" field has been selected, the system will use the price in USD (returned by the provider) for the calculation, to which a discount/markup percentage defined in the administration section is applied. Otherwise, the price already converted to EUR is used.
4.  The cost module checks if the resource identifier (UUID) is present in the [SCMP catalog](Catalog.md#gestione-elementi-di-catalogo-scmp). If present, the system multiplies the usage by the catalog cost.
5.  If the resource is not present in the catalog (and therefore does not fall into the previous step), the SCMP will apply the discount/markup percentage configured [in the subsystem](Administration.md#parametri-oracle).

###### Customer cost recovery and calculation for *Kubernetes, OpenShift, vcloudDirector, VMWare, Red Hat Edge* providers

- *Standard model*: The ABS module generates Usage data on a 24-hour basis for all resources available in the inventory, as the providers are On-premise and all resources are allocated to the customer.

**Cost calculation per single resource:**

1.  The ABS module sends cost information and information about the resource that generated them to the cost module.
2.  The SCMP will apply the discount/markup percentage configured [in the cost model](Administration.md#modello-di-costo-per-i-provider-on-premise).

#### New subsystem creation

To add a new subsystem to the portal, click on the "menu" available in the top right and select "+ Add new cloud provider".

![Adding a new Cloud Provider](images/extract/media/image56.png)

The user views the basic data of the subsystem to be entered, explained below.

##### **Parameters shared among providers**

On the creation page, we can note 3 fields:

- Name: indicates the name that will be displayed to identify the subsystem.
- Type: indicates the type of cloud provider to which the subsystem belongs.
- Version: the version relative to the provider of the subsystem to be installed.

![General parameters of a subsystem](images/extract/media/image57.png)

After selecting the type and version of the system, the form updates to display specific parameters based on the selected provider, as each of them manages authentication and resources differently.

All providers require authentication, which may vary by system, for asset retrieval.

This sensitive information, such as passwords or certificates, is securely saved on an infrastructural element that handles data security <https://www.vaultproject.io/>.

##### Connection verification and saving, shared among providers

For all subsystems, 3 buttons are available at the bottom of the page:

The "Close" button allows cancelling the addition of a new subsystem.

The "Test Connection" button is used to perform a connection test using the entered parameters. In case of errors, the system returns an error message indicating "Error: Unauthorized system" and the button turns red. Otherwise, the button will turn green, and it will be possible to save the subsystem using the "Save" button.

![Connection buttons](images/extract/media/image58.png)

Upon saving, the SCMP will communicate to the module managing that provider type to load all inventory items, metrics, costs, and security elements into our bus (Kafka).

The same module will subsequently schedule jobs for the periodic update of all existing assets.

After saving, a modal will appear informing the user that a cloud provider cannot be deleted before 24 hours. From the modal, click "OK". After doing so, the user is redirected to the Cloud Provider page.

##### **Amazon Web Services Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the Amazon Web Services subsystem to be entered are shown in the table:

![Amazon Web Services configuration mask](images/extract/media/image59.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| AccessKey \* | string | The AWS access key is an alphanumeric string that identifies the AWS user. | ZYKZGVAKIS4YK5IXCAXB |
| SecretKey \* | password | The AWS secret access key is an alphanumeric string used to authenticate the AWS user. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| use A role | Boolean | Specifies the use of one or more administration roles for authentication on one or more specific accounts within the provider's organization. | true |
| Arn Role (only if useArole is active) | string | Enter here the Arn ID of the role associated with a specific account for performing the monitoring discovery phase and for provisioning. | arn:aws:iam:{accountID}:role/{roleName} |
| Audit Arn Role (only if useArole is active) | string | Enter here the Audit Arn ID of the role associated with a specific account for performing the inventory discovery phase. | arn:aws:iam:{accountID}:role/{roleName} |
| Aggregator Name | string | Enter here the name of the aggregator on resources for using the AWS Config service to support the inventory discovery phase. | aws-{aggregatorName} |
| Cost Bucket Path | string | Enter here the path of the storage bucket for cost queries. | s3://{bucketPath} |
| Cost Export Dataset ID | string | Enter here the ID of the cost dataset on which to execute queries. | {databaseName}.{tableName} |
| usageAggregation | Boolean | Indicates the type of aggregation used for cost calculation (true for resources, false for SKUs). | True |
| Rate Code Aggregation (only if useAggregation is false) | Boolean | Indicates whether SKU aggregation occurs by SKU ID or by rate code. | true |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

!!! info "Provider Configurations"
    1.  S3 Configuration
        - Access **Amazon S3**.
        - Create or use a bucket for CUR data.
        - Enable **Bucket Versioning**.
    2.  CUR Definition
        - Access **Billing and cost management**.
        - Go to the Data Exports section.
        - Configure a new CUR report as follows:
            - Export details:
                - **Standard data export**: standard export format
                - **Export name**: name of the report
            - Data table content settings:
                - Select **CUR 2.0**.
                - Select **Hourly** as granularity.
            - Data export delivery options:
                - file format: **Parquet**.
                - file versioning: **Overwrite existing data export file**.
            - Data export storage settings:
                - Configure the S3 bucket pointer with the one initially created.
                - Configure the bucket path prefix with **data**.
    3.  IAM Role Creation for Glue
        - Access **IAM**.
        - Create a custom role for Amazon Glue management.
        - Assign the following policies:
            - `AWSGlueServiceRole` (standard AWS policy)
            - Custom policy for S3 bucket access:
    ```json
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "s3:PutObject"
        ],
        "Resource": [
                "arn:aws:s3:::{bucketPath}/*"
        ]
        }
    ]
    }
    ```
    4.  Glue Database Creation
        - Access **AWS Glue**.
        - Create the database.
    5.  Crawler Configuration
        - Create a **crawler** in Glue:
            - Select the custom role previously created.
            - Define the S3 path as `s3://{bucketPath}/data/`.
            - Set a **scheduling** (e.g., hourly: `0 * * * * *`).
    6.  Usage in Athena
        - After the first execution of the crawler, data will be available in **Athena** for queries.
        - ⚠️ *For past historical data, contact AWS support.*
    ---
    1.  AWS Configuration and Aggregators
        1.  Initial Configuration
            - Access **AWS Config** and click **Get started**.
            - Create an S3 bucket for aggregated data.
            - Enable override for **IAM** resource types and leave the remaining default options; AWS will automatically create the necessary role.
        2.  Config Aggregator
            - Create a **resource aggregator** in the **Aggregators** section.
            - Include all regions.
    ---
    1.  IAM User Creation
        - Access **IAM** and go to the **Users** section.
        - Create a new user or select an existing one.
        - Optional: enable console access for the created user.

    2.  Policies to Assign to the User
        - `AmazonAthenaFullAccess`
        - `AmazonS3FullAccess`
        - `AWS_ConfigRole`
        - `AWSConfigUserAccess`
        - `AmazonEC2ReadOnlyAccess`
        - `CloudWatchReadOnlyAccess`
        - Add the following custom policy for managing the CUR bucket:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "VisualEditor0",
          "Effect": "Allow",
          "Action": [ "s3:*" ],
          "Resource": [
            "arn:aws:s3:::{bucketPath}/",
            "arn:aws:s3:::{bucketPath}/*"
          ]
        }
      ]
    }
    ```
    3.  Access Key
        - Generate **Secret Credential**.
        - Save the **Access Key** and **Secret Key** (cannot be retrieved later).
        To enable **role assumption** via STS for cross-account services (e.g., AWS Config), associate the following policy with the created user:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": [
            "arn:aws:iam::{accountIamID}:role/{roleName}"
          ]
        }
      ]
    }
    ```

##### **Azure Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the Azure subsystem to be entered are shown in the table:

![Azure configuration mask](images/extract/media/image60.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId **\*** | string | The unique ID of the client connecting to the Azure Cloud subsystem. This ID is used to identify the client and authorize access to the subsystem's resources. | 5a85c16c6ad-49db-a58e-e209-ee11f53d6c6b |
| clientSecret \* | password | The client's secret key, used to authenticate the client with the Azure Cloud subsystem. The secret key must be kept confidential and not shared with anyone. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| tenantId \* | string | The ID of the Azure tenant to which the Azure Cloud subsystem belongs. A tenant is an organizational entity in Azure representing a company or organization. | 884147733-ff13-4783-a765-834183773083 |
| subscriptionId \* | string | The ID of the Azure subscription used to access the Azure Cloud subsystem. A subscription is a contract for using Azure services. | 884147733-ff13-4783-a765-834183773083 |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| Storage account ID\*\* | String | Enter the path where cost exports are performed. | /subscriptions/{{subscription}}/resourceGroups/{{resourcegroup}}/providers/Microsoft.Storage/storageAccounts/{{storage account}} |
| Cost from Billing storage\*\* | boolean | Select this checkbox to retrieve costs in "billing Account" format. | true |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

!!! warning "Variables for cost calculation"

    Variables indicated with \*\* are exclusive, so only one can be selected at a time. Each variable activates a different system for cost calculation, and if more than one is set, subsystem saving will be prevented.
    Specifically, we can:

    - Use the "Storage account ID" field to retrieve costs via automatic extractions performed individually per subsystem (only if the storage belongs to the same tenant).
    - Use the "Cost from Billing storage" field to retrieve costs at the billing account level, thus using a single file for all available subscriptions (Contributor and Blob Contributor permissions are required).
    - By leaving "Cost from Billing storage" and "Cost from billing storage" empty, the SCMP will retrieve costs using the Azure APIs prepared for daily costs.

    This distinction is necessary to prevent Azure APIs from responding with a 429 error due to a large number of requests. Additionally, to use the methods described previously, the Azure system must be correctly configured and the entered credentials must have all necessary permissions.

##### **AzureStack Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the AzureStack subsystem to be entered are shown in the table:

![AzureStack configuration mask](images/extract/media/image61.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId **\*** | string | The unique ID of the client connecting to the Azure Cloud subsystem. This ID is used to identify the client and authorize access to the subsystem's resources. | 5a85c16c6ad-49db-a58e-e209-ee11f53d6c6b |
| clientSecret \* | password | The client's secret key, used to authenticate the client with the Azure Cloud subsystem. The secret key must be kept confidential and not shared with anyone. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| tenantId \* | string | The ID of the Azure tenant to which the Azure Cloud subsystem belongs. A tenant is an organizational entity in Azure representing a company or organization. | 884147733-ff13-4783-a765-834183773083 |
| subscriptionId \* | string | The ID of the Azure subscription used to access the Azure Cloud subsystem. A subscription is a contract for using Azure services. | 884147733-ff13-4783-a765-834183773083 |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

For On-Premise providers, in particular, data on infrastructure capacity is requested so that the SCMP can perform preliminary calculations in multiple scenarios.

For example, during provisioning, to ensure that the maximum allowed capacity of the provider is not exceeded.

##### **AzureStack HCI Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the AzureStack HCI subsystem to be entered are shown in the table:

![AzureStack HCI configuration mask](images/extract/media/image62.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId **\*** | string | The unique ID of the client connecting to the Azure Cloud subsystem. This ID is used to identify the client and authorize access to the subsystem's resources. | 5a85c16c6ad-49db-a58e-e209-ee11f53d6c6b |
| clientSecret \* | password | The client's secret key, used to authenticate the client with the Azure Cloud subsystem. The secret key must be kept confidential and not shared with anyone. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| tenantId \* | string | The ID of the Azure tenant to which the Azure Cloud subsystem belongs. A tenant is an organizational entity in Azure representing a company or organization. | 884147733-ff13-4783-a765-834183773083 |
| subscriptionId \* | string | The ID of the Azure subscription used to access the Azure Cloud subsystem. A subscription is a contract for using Azure services. | 884147733-ff13-4783-a765-834183773083 |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

For On-Premise providers, in particular, data on infrastructure capacity is requested so that the SCMP can perform preliminary calculations in multiple scenarios.

For example, during provisioning, to ensure that the maximum allowed capacity of the provider is not exceeded.

##### **AzureStack Hybrid Cloud Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the AzureStack Hybrid cloud subsystem to be entered are shown in the table:

![AzureStack Hybrid cloud configuration mask](images/extract/media/image63.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId **\*** | string | The unique ID of the client connecting to the Azure Cloud subsystem. This ID is used to identify the client and authorize access to the subsystem's resources. | 5a85c16c6ad-49db-a58e-e209-ee11f53d6c6b |
| clientSecret \* | password | The client's secret key, used to authenticate the client with the Azure Cloud subsystem. The secret key must be kept confidential and not shared with anyone. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| tenantId \* | string | The ID of the Azure tenant to which the Azure Cloud subsystem belongs. A tenant is an organizational entity in Azure representing a company or organization. | 884147733-ff13-4783-a765-834183773083 |
| subscriptionId \* | string | The ID of the Azure subscription used to access the Azure Cloud subsystem. A subscription is a contract for using Azure services. | 884147733-ff13-4783-a765-834183773083 |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

For On-Premise providers, in particular, data on infrastructure capacity is requested so that the SCMP can perform preliminary calculations in multiple scenarios.

For example, during provisioning, to ensure that the maximum allowed capacity of the provider is not exceeded.

##### RedHat Edge device Parameters

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the Google Cloud subsystem to be entered are shown in the table.

![Edge configuration mask](images/extract/media/image64.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| client_id \* | string | | 104822473261100667392 |
| clientSecret \* | string | Client secret used for connection | 82hg7ds1h0sds7392 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 10 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

!!! info "PROVIDER side configuration"

    To be able to add the system to the SCMP, some configurations need to be performed on the provider's portal.

    Specifically:

    - Create a service account
        1. Access https://console.redhat.com
        2. In the top right, click on the ⚙ Settings icon → Service Accounts → Create service account.
        3. Enter Name and Description ➜ Create.
        4. Immediately copy the Client ID and Client Secret (the secret will not be shown again).

    - Assign permissions
        1. Go to Settings → User Access → Groups
        2. Create a group that contains the following permissions/roles:

    | Service             | Recommended role                      |
    |---------------------|---------------------------------------|
    | Edge Management (fleet, update) | **Edge Management Administrator** or **User** |
    | Image Builder       | **Image Builder Administrator** or **User** |
    | Insights Inventory (host read) | **Insights Inventory Viewer**         |

    - In the Service accounts tab of the group ➜ Add service account ➜ select the newly created account.
    - Rotate and revoke permissions
        1. Portal ➜ Service Accounts → menu (⋮)
        2. Select **Reset credentials** to regenerate only the Client Secret.
        3. Select **Delete service account** to permanently decommission the automation.

    With this configuration, you can securely orchestrate the entire edge lifecycle – from image generation to update rollout – without ever using personal credentials.

##### Google Cloud Parameters

Enabled functionalities:

Catalog item retrieval

- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the Google Cloud subsystem to be entered are shown in the table. The “Service account” field can be entered either automatically or manually as described in the paragraph.

![Google configuration mask](images/extract/media/image65.png)

Parameters indicated with * are mandatory (available below the service account section).

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| serviceAccount \* | object | Connection file generated from the Google console | service_account.json |
| discoveryProjectId \* | string | Identifier of the project for which discovery will be performed | Theproject-547280 |
| costExportProjectId | string | Dataset ID of the cost export service account if the dataset is different from the ProjectID | test-customer.test_customer.gcp_billing_export_resource_v1_01527DF_51B683_EB2A9 |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| Cost from USD Currency | boolean | Indicates whether the final cost is calculated from the price in USD or EUR. | true |
| providerPriceDiscount \*\* (only if costFromUSDCurrency is true) | integer | Enter here a discount/markup to apply to provider prices in USD for all resources. | 30 |
| catalogPriceDiscount \*\* | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | -5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

!!! warning "Variables for cost calculation"

    The variables indicated with \*\* are used differently for "customer" cost calculation depending on the presence of the "Cost from USD Currency" field.
    Specifically:

    - If the field is deactivated, the value entered in "catalogPriceDiscount" is used as a percentage added to the price retrieved from the provider (or discounted if the value is negative), as for other providers.
    - If the field is activated, the value entered in "catalogPriceDiscount" and the "providerPriceDiscount" value are used as a coefficient multiplied by the cost in USD retrieved from the provider.


    This distinction is necessary to prevent Azure APIs from responding with a 429 error due to a large number of requests. Additionally, to use the methods described previously, the Azure system must be correctly configured and the entered credentials must have all necessary permissions.

![Loading the configuration file](images/extract/media/image66.png)

By uploading the file, the form is automatically completed with the necessary parameters, but it is also possible to enter them manually (yellow box in the image), following the table. All fields are mandatory:

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| Type | string | Enter the name of the configured authentication type. | service_account |
| project_id \* | string | Enter here the unique ID of the project associated with the service account. | Theproject-367810 |
| private_key_id \* | string | Enter here the unique ID of the service account's private key. | 55cb5cf903ee93ea1e9c294a07e46e0af0633e6 |
| private_key \* | password | Contains the service account's private key in PEM format. It is essential for authenticating the service account to Google Cloud APIs. | -----BEGIN PRIVATE KEY-----MIIJQgIBADANB… |
| client_e-mail \* | string | The unique email address of the service account. It is used to identify the service account when authenticating to Google Cloud APIs. | <user@dominio.com> |
| client_id \* | string | The client ID of the service account. It is a unique identifier used to identify the service account in Google Cloud. | 104822473261100667392 |
| auth_uri \* | string | The URI used for authenticating the service account to Google Cloud APIs. | <https://accounts.google.com/o/oauth2/auth> |
| token_uri \* | string | The URI used to obtain an access token for the service account. | <https://oauth2.googleapis.com/token> |
| auth_provider_x509_cert_url\* | string | The URL of the X.509 certificate used for authenticating the service account. | <https://www.googleapis.com/oauth2/v1/certs> |
| client_x509_cert_url \* | string | The URL of the X.509 certificate in the client. | <https://www.googleapis.com/robot/v1/metadata/f543/myserviceaccount%40projectName.gserviceaccount.com> |

!!! info "Provider Configuration"

    1. Access GCP Console
        - Go to https://console.cloud.google.com/
        - Log in with your Google Cloud account.
    2. Create or Identify the Service Account (SA)
    From the console, select the project at the top where you want to add (or where it is already present) the service account.
    From the console, to create the service account, go to IAM and admin > Service accounts.
        Click on Create service account.
        Assign an ID (e.g., my-service-account), name, and description, then Create.
        On the service account page, go to the Keys section.
        Click on Add key and select Create new key.
        Choose JSON format and click Create.
        Download and keep the JSON file in a safe place.
    3. Associate Permissions with the Service Account

        On the same service accounts page, find the newly created account and click on its name.
        Go to the Permissions section and in the table below, next to the service account, in the Inheritance column, click on Edit principal.
        In the pop-up menu, select the appropriate roles for the service account. Below is the minimal list of roles for the SCMP:
            - App Engine Admin
            - BigQuery Data Transfer Service Agent
            - Cloud OS Config Service Agent
            - Compute Admin
            - Kubernetes Engine Service Agent
            - OS Inventory Viewer
            - Security Center Service Agent
        Click Save and add the permissions to the service account.

    4. Enable Service APIs

        Go back to the console home.
        Select the project at the top where the service account is present.
        Go to APIs and services.
        At the top, click on + Enable APIs and services.
        Search for the API services to enable in the search bar and click on their name.
        Once inside the API service, select Enable to activate it; below are the API services for the SCMP:
            - Cloud Monitoring API
            - Compute Engine API
            - Cloud Asset API
            - BigQuery API
            - Cloud Resource Manager API
            - OS Config API
            - Security Command Center API
            - Cloud Billing API
            - Service Usage API
            - Cloud Dataplex API

    5. Cost Dataset

        If the cost dataset is located in a different service account than the one you want to integrate, specify the complete connection string to the relevant dataset in the Cost Export Dataset ID text box (in the subsystem creation module present in SCMP administration) (e.g., projectId.datasetName.tableName).

##### Kubernetes Parameters

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the Kubernetes subsystem to be entered are shown in the table.

![Kubernetes configuration mask](images/extract/media/image67.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| Certificate authority data \* | string | Enter the data related to the certificate used by the user for connection. | Sgeijesf90434n7u3h97ef |
| Kubernetes API server URI \* | string | Enter the URL of the server to connect to. | <https://www.google.com/infos> |
| User certificate Data \* | String | Enter the certificate related to the user used for connection. | ---begin private key--- fnbsujffsfoije … |
| User key Data \* | String | Enter the key related to the user used for connection. | Sf8j9jts4ewht7h3wfwj908w |
| User token \* | String | Secret token related to the user used for connection to the provider. | Sf8eufce9sfber4543jh8ddsfh89r43 |
| User name \* | String | Enter the username used for authentication. | administrator |
| Label selector | string | Enter here a selector to filter resources retrieved by the SCMP. | Name=rossi |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | -10 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |

!!! info "Provider Configuration"

    The standard authentication method is via the parameters contained in the kubeconfig file.
    The kubeconfig defines:
        API server endpoint (server)
        Authentication method (client certificates, tokens, oidc, etc.)
        Default namespace
        Context
    Authentication:
        Via client certificates (client-certificate-data and client-key-data)

        Or via token (token in the user context)

    Minimal kubeconfig example:

    apiVersion: v1
    kind: Config
    clusters:
    - cluster:
        certificate-authority-data: <ca-data>
        server: https://<api-server>
    name: my-cluster
    contexts:
    - context:
        cluster: my-cluster
        user: my-user
    name: my-context
    current-context: my-context
    users:
    - name: my-user
    user:
        token: <token>

##### **OpenShift Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the OpenShift subsystem to be entered are shown in the table:

![OpenShift configuration mask](images/extract/media/image68.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| Username **\*** | string | The username of the OpenShift user that will be used for connection to the provider. | name.surname@mail.com |
| Password \* | password | The client's password, used to authenticate the client with the subsystem. The secret key must be kept confidential and not shared with anyone. | np6KcXmbqfMGQLOEzfMt |
| API server port \* | integer | The port on which the OpenShift APIs are listening. | 8090 |
| API url \* | string | The OpenShift URL on which to make requests. | www.google.com |
| discover all Namespaces | boolean | If the user has administrator permissions on all OpenShift "projects," all namespaces will be retrieved. | false |
| Namespace selector (only visible if "discover all namespaces" is active) | selection | If the user has visibility of a limited number of namespaces, it is necessary to enter the list of enabled namespaces here. | demo,infos,production |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

!!! warning "User authorizations"

    If the "Discover all namespaces" field is selected, it is necessary that the user has administration permissions on **ALL** namespaces, otherwise, the system cannot be added.

    This distinction is necessary because the OpenShift system automatically blocks incorrectly authorized requests.

!!! info "Provider Configuration"

    To connect an OpenShift cluster system, it is sufficient to have a named or impersonal user with adequate privileges (e.g., cluster-admin or otherwise sufficient for the intended use) on the cluster.

    Authentication:

        Username and Password

    Notes:

        In OpenShift, it is very common to use specially created ServiceAccounts, with corresponding RoleBindings or ClusterRoleBindings.

        Users can be both human (named) and technical (impersonal).

##### **Oracle Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Resource cost retrieval
- Security information retrieval

The specific parameters of the Oracle subsystem to be entered are shown in the table:

![Oracle configuration mask](images/extract/media/image69.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| username \* | string | The username used for authentication with OCI. | ocid5.user.oc77.aaabnbthaj6pnvsb2gqnaaaaait3mqzekefmlhwkige2wxna6hfaj3f6njma |
| fingerprint \* | string | Is a unique value that identifies the device, used for authentication with OCI. | 6a:f4:6e:9a:73:95:27:d5:64:8d11:a3:f5:0e:fb:f4: |
| tenantId \* | string | The ID of the OCI tenant to connect to. | ocid5.tenancy.oc77...aaabnbthaj6pnvsb2gqnaaaaait3mqzekefmlhwkige2wxna6hfaj3f6njma |
| region \* | string | The region is the specific geographic location where OCI resources are located. | eu-dcc-rome-1 |
| Realm | string | The name of the logical container that groups OCI resources and their associated costs. | personal-realm.it |
| keyFile \* | password | A PEM file containing the public and private key used for authentication. | " -----BEGIN PRIVATE KEY-----MIIJQgIBADANB…" |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | -10 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

!!! info "Provider Configuration"

    Procedure for creating parameters for external integration in Oracle Cloud Infrastructure (OCI):
    1. Access OCI Console

        Go to https://cloud.oracle.com/
        Log in with your Oracle Cloud account.

    2. Create or Identify the IAM User

        In the main console menu, go to Identity & Security > Users.
        Select an existing user or create a new user for the integration:
            Click on Create User if you need to create one.
            Assign a name and an email.
            Save.

    3. Associate the user with a group with adequate permissions

        After creating the user, you must associate it with a group that has permissions for the resources you want to manage via API.
        Go to Identity > Groups.
        Select a group (e.g., Administrators or create a custom group).
        Click on Add User to Group and add the newly created user.

    4. Generate the API key (Key File)

        Go back to the user page (Identity > Users > select user).
        Go to the API Keys tab.
        Click on Add API Key.
        You have two options:
            Upload an existing public key (RSA public).
            Or generate a new public and private key from the console (download the private key).
        Select “Generate API Key Pair” to locally generate the key:
            Download the private key (.pem) and save it securely (it is your Key File).
            The public key will be automatically associated with the user.

    5. Obtain the required parameters

        User OCID (User OCID):
            Go to Identity > Users > select user.
            You will find the user OCID on the user page (format ocid1.user.oc1..aaaaaaa...).
        Fingerprint:
            It is the fingerprint of the public API key you added (displayed in the API Keys section).
        Tenant OCID (Tenant OCID / Main Compartment OCID):
            Go to Identity > Tenancy (click on the tenancy name in the top left).
            You will find the tenancy OCID (it is the main tenant, e.g., ocid1.tenancy.oc1..aaaaaaa...).
        Region:
            Choose your OCI region (e.g., eu-frankfurt-1, us-ashburn-1, etc.).
            You can find it in the top right of the console or in Governance & Administration > Regions.
        Realm:
            It is usually oc1 for most public OCI tenants. You can verify this in the documentation or via CLI if necessary.

    Summary of parameters and where to find them

    
    Parameter	Where to find it / how to obtain it
    User OCID	Identity > Users > select user > OCID
    Fingerprint	Identity > Users > API Keys > fingerprint
    Tenant OCID	Identity > Tenancy > OCID
    Region	Top right of the console (e.g., eu-frankfurt-1)
    Realm	Generally oc1 (standard OCI realm)
    Key File	Private .pem key generated at the time of API Key creation

##### OracleExAcc Parameters

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Resource cost retrieval
- Security information retrieval

The specific parameters of the OracleExAcc subsystem to be entered are shown in the table:

![OracleExAcc configuration mask](images/extract/media/image70.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| username \* | string | The username used for authentication with OCI. | ocid5.user.oc77.aaabnbthaj6pnvsb2gqnaaaaait3mqzekefmlhwkige2wxna6hfaj3f6njma |
| fingerprint \* | string | Is a unique value that identifies the device, used for authentication with OCI. | 6a:f4:6e:9a:73:95:27:d5:64:8d11:a3:f5:0e:fb:f4: |
| tenantId \* | string | The ID of the OCI tenant to connect to. | ocid5.tenancy.oc77...aaabnbthaj6pnvsb2gqnaaaaait3mqzekefmlhwkige2wxna6hfaj3f6njma |
| region \* | string | The region is the specific geographic location where OCI resources are located. | eu-dcc-rome-1 |
| Private key \* | password | A PEM file containing the public and private key used for authentication. | " -----BEGIN PRIVATE KEY-----MIIJQgIBADANB…" |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | -10 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| dataFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

##### **VCloud Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval

The specific parameters of the VCloudDirector subsystem to be entered are shown in the table.

![VCloudDirector configuration mask](images/extract/media/image71.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| url \* | string | The address of the VCloudDirector server to connect to. | <https://url.westeurope.com/tenant/org-zzg-435832> |
| tenantId \* | string | The VCloudDirector tenant ID is the unique identifier of the tenant to connect to. | org-zzg-435832 |
| Use providerPermission | boolean | To be activated if the user has all provider-level authorizations; if not activated, not all information is retrieved, only that of the enabled organizations. | true |
| token \* | password | The authentication token for the VCloudDirector is a secret string used to authenticate the user with the VCloudDirector. | aesZo6LextKTQx92VoRpyzaesZo6LextKT |
| Location | String | Enter the region to which the VCloudDirector resources belong. | Eu west |
| Location | string | Enter the geographical location of the system. | OnPremise |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |

##### **VMWare Parameters**

Enabled functionalities:

- Catalog item retrieval
- Inventory item retrieval
- Usage metrics retrieval
- Resource cost retrieval
- Security information retrieval
- Resource provisioning
- Service provisioning
- Complex blueprint provisioning

The specific parameters of the VMWare subsystem to be entered are shown in the table:

![VMWare configuration mask](images/extract/media/image72.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId **\*** | string | The unique ID of the client connecting to the Azure Cloud subsystem. This ID is used to identify the client and authorize access to the subsystem's resources. | 5a85c16c6ad-49db-a58e-e209-ee11f53d6c6b |
| clientSecret \* | password | The client's secret key, used to authenticate the client with the Azure Cloud subsystem. The secret key must be kept confidential and not shared with anyone. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| tenantId \* | string | The ID of the Azure tenant to which the Azure Cloud subsystem belongs. A tenant is an organizational entity in Azure representing a company or organization. | 884147733-ff13-4783-a765-834183773083 |
| subscriptionId \* | string | The ID of the Azure subscription used to access the Azure Cloud subsystem. A subscription is a contract for using Azure services. | 884147733-ff13-4783-a765-834183773083 |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| datsFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

For On-Premise providers, in particular, data on infrastructure capacity is requested so that the SCMP can perform preliminary calculations in multiple scenarios.

For example, during provisioning, to ensure that the maximum allowed capacity of the provider is not exceeded.

#### Folders

##### Azure Folder

To allow the SCMP to leverage all the potential offered by the "Azure" provider, the ability to configure "Folders" has been introduced.

During the creation of a provider, by selecting the "Azure" type, we can observe the presence of an exclusive field for the provider:

- A confirmation box to indicate to the SCMP if the provider being added is a "Folder".

![Azure folder option](images/extract/media/image73.png)

The specific parameters of the Azure subsystem to be entered are shown in the following table:

![Azure Folder configuration mask](images/extract/media/image74.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId **\*** | string | The unique ID of the client connecting to the Azure Cloud subsystem. This ID is used to identify the client and authorize access to the subsystem's resources. | 5a85c16c6ad-49db-a58e-e209-ee11f53d6c6b |
| clientSecret \* | password | The client's secret key, used to authenticate the client with the Azure Cloud subsystem. The secret key must be kept confidential and not shared with anyone. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| tenantId \* | string | The ID of the Azure tenant to which the Azure Cloud subsystem belongs. A tenant is an organizational entity in Azure representing a company or organization. | 884147733-ff13-4783-a765-834183773083 |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | 5 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| datsFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

##### Google Cloud Folders

To allow the SCMP to leverage all the potential offered by the "Google Cloud" provider, the ability to configure "Folders" has been introduced, along with the option to import the file generated from the provider's console to simplify its insertion.

During the creation of a provider, by selecting the "Google Cloud" type, we can observe the presence of 2 exclusive fields for the provider:

1.  A confirmation box to indicate to the SCMP if the provider being added is a "Folder".
2.  A box where, by clicking inside, it will be possible, through the Windows file selection window, to insert the "JSON" file exported directly from the Google console.

![Google Cloud specific parameters](images/extract/media/image75.png)

The specific parameters for the Google Folder to be entered are shown in the table:

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| serviceAccount | object | Connection file generated from the Google console | service_account.json |
| costExportDatasetID | string | Enter the ID of the dataset to be used for information retrieval. | Projectid.dataset.table |
| usageAggregation | boolean | Indicates whether "usage" aggregation is enabled for the subscription. When this option is enabled, subsystem costs will be grouped by Resource Type. | false |
| Cost from USD Currency | Boolean | Indicates whether the final cost is calculated from the price in USD or EUR. | true |
| providerPriceDiscount (only if costFromUSDCurrency is true) | integer | Enter here a discount/markup to apply to provider prices in USD for all resources. | 30 |
| Cost cross project | Boolean | Indicates whether to retrieve costs for all projects in the billing account or only for the current project. | true |
| catalogPriceDiscount | integer | Enter here a discount/markup to apply to catalog prices for all resources that do not have an SCMP relationship. | -20 |
| odlID | string | Enter here the ID of the work order that will be associated with the subsystem and will be inserted as a tag on all subsystem resources. | ODL001 |
| datsFirstCostRecover | int | Enter the number of days prior to the creation date for which costs should be recovered at the first startup of the subsystem. | 15 |

!!! warning "Mandatory Enabled Services"

    The following services must be enabled on the service account used:

    - bigquery.googleapis.com
    - cloudresourcemanager.googleapis.com
    - cloudasset.googleapis.com
    - cloudbilling.googleapis.com
    - compute.googleapis.com
    - container.googleapis.com
    - monitoring.googleapis.com

The "ServiceAccount" field can be automatically entered by uploading the file or manually by entering the fields available in the form.

After configuring a "Folder" type system, it will be displayed in both the cloud provider list and the folders page.

![Folder display](images/extract/media/image76.png)

From the "Cloud System" page of the "Administration" module, click the "Folders" tab in the top right, which will display the list of folders configured in the tenant.

Within the page, the same view, modify, and delete operations can be performed on folders as those performed on the "Cloud Provider" page.

![Access to Folders](images/extract/media/image77.png)

When accessing a "Folder" in "View" mode, scrolling down the page reveals a list of subsystems present in the provider and their status information:

- In green, we can see a subsystem correctly configured in the provider that the SCMP automatically adds to the system and will be visible in the "Cloud Providers" section and in all SCMP functionalities.
- In red, we can see an incorrectly configured subsystem which, after appropriate modifications from the "Google Cloud" console, can be accepted by the SCMP.

![Viewing subsystems of the Folder](images/extract/media/image78.png)

### SIEM

The user can create a SIEM provider by clicking on the tab depicting a shield, located in the top bar, after accessing the "Cloud SIEMs" page, in the top right, click on the hamburger menu and then click on "Attach a SIEM".

![Creating a cloud SIEM provider](images/extract/media/image79.png)

On the "Add SIEM" page, fill in all fields in the "General properties" section. After doing this, fill in all fields in the "SIEM's properties" section according to the table:

![Filling out the form for creating a SIEM provider](images/extract/media/image80.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId \* | string | Unique ID of the SIEM to connect to, provided by the SIEM during application registration. | 1b16698f-2df5-ed44-86b9ed-4b42c 1fe7ad9 |
| clientSecret \* | password | The secret to use for the connection, provided by the SIEM during application registration. | 1b16698f-2df5-ed44-86b9ed-4b42c 1fe7ad9 |
| resourceGroup \* | string | The Azure resource group where the SIEM is hosted. | myGroup |
| subscriptionId \* | string | The Azure subscription ID associated with the SIEM. | 1b16698f-2df5-ed44-86b9ed-4b42c 1fe7ad9 |
| tenantId \* | string | The Azure tenant ID associated with the SIEM. | 1b16698f-2df5-ed44-86b9ed-4b42c 1fe7ad9 |
| workspaceID\* | string | The Log Analytics workspace ID associated with the SIEM. | 1b16698f-2df5-ed44-86b9ed-4b42c 1fe7ad9 |
| workspaceName\* | string | The name of the Log Analytics workspace associated with the SIEM. | theWorkspaceName |

Finally, in the bottom right, click the "Save" button. Afterward, a popup will appear confirming the SIEM's creation, and the user will be redirected to the list of SIEMs.

#### Viewing, modifying, and deleting

To view a SIEM, next to it, click on the kebab menu and then click "Show". At this point, the user is on the "Show SIEM" page where data can be viewed but not modified. After viewing the data, in the bottom right, click the "Close" button.
After this, the user is back on the list of SIEMs.

![Access to SIEM in view mode](images/extract/media/image81.png)

![SIEM in view mode](images/extract/media/image82.png)

To modify a SIEM, next to it, click on the kebab menu and then click "Edit". At this point, you are on the "Edit SIEM" page where fields can be modified.

After modifying the fields of interest, in the bottom right, click the "Update" button. After this, a popup will appear confirming the SIEM's modification, and the user will be back on the list of SIEMs.

![Access to SIEM in edit mode](images/extract/media/image83.png)

![](images/extract/media/image84.png)
![SIEM in edit mode](images/extract/media/image85.png)

To delete a SIEM, next to it, click on the kebab menu and then click "Delete". At this point, a modal will appear where you need to click the "Remove" button. After this, the SIEM is no longer present in the list.

![Option to delete a SIEM "Delete"](images/extract/media/image86.png)

![Confirmation to delete a SIEM](images/extract/media/image87.png)

### Secrets Managers

The user can create a secret manager by clicking on the tab depicting a padlock, located in the top bar, as shown in the figure.

After accessing the "Secret manager" page, in the top right, click on the hamburger menu and then click on "Add a secret manager".
![Adding a new Secret Manager](images/extract/media/image88.png)

Here is an example form for adding a Secret manager from an Azure type provider (selectable from the "Type" dropdown at the top of the page).

After entering all the required parameters, click the "Save" button at the bottom to complete the entry, and the user will be redirected to the "Secret manager" list where the newly created component can be viewed.

#### Azure Key Vault

The specific parameters for an Azure Key Vault to be entered are shown in the table:

![Azure Key Vault configuration mask](images/extract/media/image89.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| clientId \* | string | Unique identifier of the key vault. | 09f8985-9f89d0-4623-98982-5a510fd3d2 |
| clientSecret \* | password | A secret key used to authenticate the application with the Key Vault. | np6Kc\_.xwsvhR8Q~rP05fCqYNXmbqfMGQLOEzfMt |
| resourceGroup \* | string | The Azure resource group where the Key Vault is hosted. | resourceGroupName |
| subscriptionId \* | string | The Azure subscription ID associated with the Key Vault. | 09f8985-9f89d0-4623-98982-5a510fd3d2 |
| tenantId | string | The Azure tenant ID associated with the Key Vault. | 09f8985-9f89d0-4623-98982-5a510fd3d2 |
| privateUrl | string | Private access URL to the Key Vault. | <https://vault.azure.net/vault> |

Table 25 – Azure Key Vault specific fields

#### Google Secret Manager

The specific parameters for the Google Secret Manager to be entered are shown in the following table:

![Google Secret Manager configuration mask](images/extract/media/image90.png)

Parameters indicated with * are mandatory.

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| kmsProjectId **\*** | string | The Google Cloud Platform (GCP) project ID associated with the Google Cloud Key Management Service (KMS). | 5a85c16c6ad-49db-a58e-e209-ee11f53d6c6b |
| serviceAccount \* | object | Connection file generated from the Google console. | service_account.json |

It is possible to manually enter the parameters present in the “service_account.json” file into the displayed form if you do not want to upload it. All parameters are mandatory:

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| Type | string | Enter the name of the configured authentication type. | service_account |
| project_id \* | string | Enter here the unique ID of the project associated with the service account. | Theproject-367810 |
| private_key_id \* | string | Enter here the unique ID of the service account's private key. | 55cb5cf903ee93ea1e9c294a07e46e0af0633e6 |
| private_key \* | password | Contains the service account's private key in PEM format. It is essential for authenticating the service account to Google Cloud APIs. | -----BEGIN PRIVATE KEY-----MIIJQgIBADANB… |
| client_e-mail \* | string | The unique email address of the service account. It is used to identify the service account when authenticating to Google Cloud APIs. | <user@dominio.com> |
| client_id \* | string | The client ID of the service account. It is a unique identifier used to identify the service account in Google Cloud. | 104822473261100667392 |
| auth_uri \* | string | The URI used for authenticating the service account to Google Cloud APIs. | <https://accounts.google.com/o/oauth2/auth> |
| token_uri \* | string | The URI used to obtain an access token for the service account. | <https://oauth2.googleapis.com/token> |
| auth_provider_x509_cert_url\* | string | The URL of the X.509 certificate used for authenticating the service account. | <https://www.googleapis.com/oauth2/v1/certs> |
| client_x509_cert_url \* | string | The URL of the X.509 certificate in the client. | <https://www.googleapis.com/robot/v1/metadata/f543/myserviceaccount%40projectName.gserviceaccount.com> |

#### Viewing, modifying, and deleting a system

It is possible to view the data of a Secret Manager, within the list, by clicking on the kebab menu corresponding to a manager, and then on "Show".

![Access to manager in view mode](images/extract/media/image91.png)

On this page, you can view the Provider's configuration.

![manager in view mode](images/extract/media/image92.png)

To return to the Secret manager page, click the "Close" button in the bottom left.

At this point, the user will be on the Secret manager page.

To modify the data of a Secret manager within the list, click on the kebab menu corresponding to a Cloud Provider, and click on "Edit".

![Access to manager in edit mode](images/extract/media/image93.png)

After doing so, the user will be on the Cloud Provider page in edit mode where data can be modified. To return to the Cloud Provider page, click the "Save" button in the bottom left. At this point, the user will be on the Cloud Provider page.

To delete a "Secret manager", within the list, click on the kebab menu corresponding to a Secret manager, and click on "Delete".
![Initiating the deletion of a Secret manager](images/extract/media/image94.png)

After doing so, a modal will appear where you need to click the "Remove" button.
![Confirm Secret manager deletion](images/extract/media/image95.png)

At this point, the Secret manager will no longer be present in the list, and the asset removal flow will be launched on the resource-manager.

### Backup

The user is given the ability to connect the SCMP to a CommVault to subsequently retrieve and display information related to backups and operations performed by the Vault.

To access this functionality, you need to select the "CommVault" tab available at the top of the "Administration" functionality.

We will be directed to the page containing the list of all configured "CommVaults", and by clicking on the menu on the right, it will be possible to add a new CommVault.

![Access to CommVault](images/extract/media/image96.png)

On this page, after entering the access credentials (IP address, username, and password), we can click the "Test connection" button to confirm the correct data entry and then confirm the entry via the "Save" button.

![Creating the connection to a CommVault](images/extract/media/image97.png)

### Confidential computing

In the Confidential Computing section, the user is given the ability to add a connection to a "Remote Attestation" service within the SCMP to control and view information regarding the confidentiality status of machines managed by the service.

To access this functionality, you need to select the "Confidential computing" tab available at the top in the "Administration" functionality.

We will be directed to the page containing the list of all configured "Remote attestation" services, and by clicking on the menu on the right, it will be possible to add a new connection.

![Access to Confidential Computing](images/extract/media/image98.png)

On this page, after entering the access credentials (IP address, username, and password), we can click the "Test connection" button to confirm the correct data entry and then confirm the entry via the "Save" button.

![Creating the connection to a "Remote Attestation" service](images/extract/media/image99.png)
