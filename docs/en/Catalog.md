# Catalog

The Catalog section has three important features:

- Displaying the list of installable assets retrieved from providers, along with their associated prices and regions.
- Enabling the tenant administrator to define items that can be subsequently used for provisioning.
- Enabling the tenant administrator to define items that can be subsequently used within What If module simulations.

The retrieved prices, in addition to being visible within the asset's details, are used for What If scenarios and cost calculation.

To access the Catalog functionality, click on the bento button in the upper left corner.

Then, click on "Catalog".

![Accesso a Catalog](images/extract/media/image149.png)

At this point, the user is on the "Resources" tab page.

We can divide the functionality into 3 sections to specify its behavior:

- SCMP catalog items (yellow box in the image).
- Provider catalog items (green box in the image).
- SCMP catalog services and blueprints (red box in the image).

Below, we will analyze each group of functionalities separately.

![Catalogo della SCMP](images/extract/media/image150.png)

### SCMP Catalog Item Management

On the page, there is a series of filters that, once selected and by clicking on the magnifying glass button, will be used to filter the list of results.

![ Catalogo SCMP filtrato](images/extract/media/image151.png)

!!! warning "Association between SCMP catalog resource/SKU and Provider catalog resource/SKU"

    To allow the system to correctly calculate costs, it is necessary that the SCMP catalog resource or SKU contains a reference to the actual ID retrieved from the provider (as explained in this section) in order to correctly overwrite the cost of the resource / SKU.

Next to the magnifying glass button, there is an "X" button to reset the filters and the resource table.

Below the search filter, there is a search filter for tags.

Click on it and select a tag; at this point, the table returns the resources associated with the tag selected by the user.

#### Resources and relationships between resources

Within the SCMP, it is possible to configure a "Relationship" type resource. This relationship allows mapping machines from various providers to modify their costs and enable their use in other functionalities (e.g., for cost calculation).

!!! warning "Automatic Relationships"

    If a price list resource with the provider's UUID but no relationship is present in the SCMP catalog, the relationship will be created automatically, and costs will be updated accordingly.
    After a few minutes, the relationship will also be visible within the catalog.

To access the relationships page, click the "SCMP Resources" tab at the top of the Catalog functionality.

![Accesso a "SCMP resources"](images/extract/media/image152.png)

At the top, there is a filter section that allows searching by:

- "Search": allows entering free text for searching.
- "Search By tags": allows searching using tags associated with resources.
- "Search by Service name": allows searching by service name.

##### Resource Export

To export the list of Catalog resources present in the list, on the page, in the upper right corner, click on the hamburger menu, and then click on "Export".

The operator will have the option to export the list of results in .csv and/or .json format.

![Scaricare la lista di risultati](images/extract/media/image153.png)

##### Forced Catalog Update Functionality

Through the Force Sync functionality, it is possible to request a catalog update by clicking on the hamburger menu and then clicking on "Force Sync".

![Funzionalità Force Sync](images/extract/media/image154.png)

##### Catalog Relationship Creation

To create a resource in the Catalog, always on the page, in the upper right corner, click on the hamburger menu, and then click on "Add Catalog Resource".

![Opzione per aggiungere una risorsa](images/extract/media/image155.png)

At this point, the user is on the page where they can select the type of resource to create.

![Selezione del tipo di risorsa da creare](images/extract/media/image156.png)

From the dropdown menu, select the type of resource to create. Then, click the "Next" button. You will be on the resource compilation page.

![Esempio di form per la creazione di una relazione](images/extract/media/image157.png)

The individual parameters to be entered in the "Properties" section are specified in the table:

Mandatory parameters are indicated with \*

| **Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| category | string | Enter the resource's category | CAT0004BT |
| Price list code | string | Enter the price list identifier code from which associations are derived | PRC005DE |
| confidential | boolean | If enabled, indicates that the resource is confidential | false |
| description | string | Enter a free description of the resource | Low end machine |
| Name\* | string | Enter the resource name | 8Core16GB- small |
| RAM(GIB)\* | integer | Enter here the quantity in GiB used by the machines included in the relationship | 16 |
| VCPU\* | integer | Enter here the number of vCPUs used by the machines included in the relationship | 8 |

On the resource creation page, fill in all fields in the "Properties" section. After doing this, select one or more tags for the "Add SCMP tag…" field and fill in notes in the "Tags & Note" section.

![Sezione tag e note](images/extract/media/image158.png)

In the "Relations" section, open the left section. Subsequently, it is possible to use the "search" filters with free text or select a "System Type" from those available to filter the resource table.

Once the resource to be associated is identified, drag and drop it from the right side of the page to the left side.

It is possible to add only one resource per provider type. If the user tries to insert another resource from the same provider, a pop-up will appear inviting the user to add only one resource per provider.

![Selezione del provider per associare le risorse](images/extract/media/image159.png)

We can make a "single" association by entering only one machine in this section. In this way, the system allows us to manually select a customized price to associate with the resource in the "Cost" section below. To do this, select the billing interval (hourly, daily, weekly, monthly) and enter the cost relative to the selected period on the right.

![Sezione costi delle relazioni](images/extract/media/image160.png)

By selecting more than one machine per provider, the cost section is automatically hidden; the applied costs will be defined by the percentages configured in the subsystems.

![Risorse associate alla risorsa SCMP](images/extract/media/image161.png)

Once the resources are related, an illustrative diagram will automatically be created in the 'Relations Chart' section.

![Creazione automatica del Relation Chart](images/extract/media/image162.png)

Finally, in the bottom right, click the "Save" button to save the changes. A banner will appear at the bottom, notifying the user of the successful resource creation, and the user will be redirected to the page containing the list of resources.

##### Using the Catalog Table

###### Resource Summary View

To view the data of an SCMP resource, on the "Resources" page of Catalog, in the list of resources, click on the record of interest for a resource. A window will appear showing brief information about the identified resource: System, Name, Size, Update Date, RAM, and CPU as shown in the following image.

![Dettaglio rapido delle risorse di catalogo](images/extract/media/image163.png)

###### Viewing Catalog Relationships

To view the data of an SCMP resource, on the "Resources" page of Catalog, in the list of resources, click on the kebab menu for a resource and then click on "Show".

![Accesso alla risorsa in modalità view](images/extract/media/image164.png)

After doing this, the user is on the resource page in view mode, where they can see the data but cannot modify it.

![Dettaglio completo delle risorse di catalogo](images/extract/media/image165.png)

The detail of a resource is divided into various sections:

- Details.
- Properties.
- Tags & Notes.
- Relations.
- Cost, if present.
- Relations Chart.

![Sezione proprietà degli elementi del catalogo](images/extract/media/image166.png)

![Sezione Tags & Note degli elementi del catalogo](images/extract/media/image167.png)

![Sezione delle relazioni del catalogo SCMP](images/extract/media/image168.png)

![Sezione Relations Chart delle risorse](images/extract/media/image169.png)

In the bottom right, click the "Close" button. The user will be redirected to the "Resources" page of Catalog.

###### Editing Catalog Relationships

To modify an SCMP resource, on the "Resources" page of Catalog, in the list of resources, click on the kebab menu for a resource and then click on "Edit".

![Accesso alla risorsa in modalità edit](images/extract/media/image170.png)

After doing this, the user is on the resource page in edit mode. Unlike 'Show' mode, in 'Edit' mode, it is possible to modify the Properties section and the Cost section.

In the bottom right, click the "Save" button. At this point, a banner will appear at the bottom, notifying the user of the successful resource update.

In addition, the user will be redirected to the "Resources" page of Catalog.

![Modifica della relazione](images/extract/media/image171.png)

###### Deleting Catalog Relationships

To delete an SCMP resource, on the "Resources" page of Catalog, in the list of resources, click on the kebab menu for a resource and then click on "Delete".

![Eliminazione di una risorsa](images/extract/media/image172.png)

Once done, a modal appears where it is necessary to click the "Remove" button to confirm the resource deletion.

![Conferma eliminazione della risorsa](images/extract/media/image173.png)

#### Resources and relationships between SKUs

Within the SCMP, it is possible to configure an "SCMP SKU" type resource. This relationship allows mapping SKUs received from providers to define their costs and the unit of measure displayed in the system.

To access the SKUs page, click the "SCMP SKU" tab at the top of the Catalog functionality.

![Accesso a "SCMP SKU"](images/extract/media/image174.png)

At the top, there is a filter section that allows searching by:

- "Search": allows entering free text for searching.
- "Search By tags": allows searching using tags associated with resources.
- "Search by Service name": allows searching by service name.

##### Export of Catalog Resources

To export the list of Catalog resources present in the list, always on the "SCMP" tab page, in the upper right corner, click on the hamburger menu, and then click on "Export".

The operator will have the option to export the list of results in .csv and/or .json format.

![Scaricare la lista di risultati](images/extract/media/image153.png)

##### Creating a Catalog SKU Relationship

To create a resource in the Catalog, always on the "SCMP" tab page, in the upper right corner, click on the hamburger menu, and then click on "Add Catalog Resource".

![Opzione per aggiungere una risorsa “SKU”](images/extract/media/image175.png)

At this point, the user is on the "SKU" resource creation page. Click on the accordions on the page to view their details.

![IPagina di creazione “SKU”](images/extract/media/image176.png)

In the "Properties" section, fill in all fields defined in the table.

Mandatory parameters are indicated with \*

|**Name** | **Type** | **Description** | **Example** |
|----|----|----|----|
| Price list code | string | Enter the price list identifier code from which associations are derived | PRI002FG |
| description | string | Enter a free description of the SKU | This sku is the basic vm on this provider |
| name * |string | Enter the SKU name | Simple vm sku |
| Service name | string | Enter the name of the service related to the SKU | enter the service name |
| unit | string | Enter text that will be used as the "unit of measure" displayed across all functionalities | MB/hour |
| Unit conversion Expression * | string | Enter the conversion formula between the value received from the provider and the value that will be used in the SCMP (conversion between the provider's unit of measure and the unit of measure indicated in the SKU relationship) "$var" indicates the value received from the provider | $var * 24 / 100 |

![Compilazione dei campi, selezione Properties](images/extract/media/image177.png)

After entering the conversion formula, it is necessary to click the "Test expression" button to verify its correctness.

If it has been entered correctly, the button will turn "Green" with "TEST OK" written on it; otherwise, it will turn "Red" with "KO". In this case, the possibility of saving the relationship is inhibited.

![Conferma della formula di conversione](images/extract/media/image178.png)

Subsequently, select one or more tags for the "Add SCMP tag…" field and fill in notes in the "Tags & Note" section.

In the "Relation" section, it is possible to select one or more SKUs from the various provider catalogs to relate them and unify their costs. To do this, click on the "Composition" section on the left; a dark section will open where, using drag and drop, we can move the available SKUs to the right section.

In the right section, filters can be used to display only relevant results. The available filters are: the origin provider, the service name, and a free text field (in yellow in the image).

![Drag and drop Relazioni SKU](images/extract/media/image179.png)

Once the resources are related, an illustrative diagram will automatically be created in the 'Relations Chart' section.

![Creazione automatica del Relation Chart](images/extract/media/image180.png)

Finally, click the save button to confirm the creation of the SKU relationship. Upon completion, you will return to the page containing the list of SKU relationships, where you can find the new relationship in the list.

##### Using the Catalog Table

###### Catalog Resource Summary View

To view the data of an SKU resource, in the list of resources, click on the record of interest for a resource. A checkbox will appear showing brief information about the identified resource: System, Name, Size, Update Date, name, and service as shown in the following image.

![Dettaglio rapido delle risorse SKU](images/extract/media/image181.png)

###### Viewing Relationships in the Catalog

To view the data of an SKU resource, in the list of resources, click on the kebab menu for a resource and then click on "Show".

![Accesso alla risorsa in modalità view](images/extract/media/image182.png)

After doing this, the user is on the resource page in view mode, where they can see the data but cannot modify it.

![Dettaglio completo delle risorse di catalogo](images/extract/media/image183.png)

The detail of a resource is divided into various sections:

- Details.
- Properties.
- Tags & Notes: where in the "Provider Tags…" field it is not possible to select a tag, as it is automatically obtained from the subsystem it belongs to; the "Add SCMP Tag…" field allows selecting tags from a list or entering one manually; in the Notes field, it is possible to enter a text note.
- Relations: where provider SKUs are present in relation.
- Cost.
- Relations Chart.

![Sezione proprietà degli elementi SKU di catalogo](images/extract/media/image184.png)

![Sezione Tags & Note degli elementi SKU di catalogo](images/extract/media/image185.png)

![Sezione delle relazioni degli SKU di catalogo](images/extract/media/image186.png)

![Sezione Relations Chart delle risorse](images/extract/media/image169.png)

In the bottom right, click the "Close" button. The user will be redirected to the page containing the list of resources.

###### Editing Catalog Relationships

To modify an SCMP resource, on the "Resources" page of Catalog, in the list of resources, click on the kebab menu for a resource and then click on "Edit".

![Accesso alla risorsa in modalità edit](images/extract/media/image170.png)

After doing this, the user is on the resource page in edit mode. Unlike 'Show' mode, in 'Edit' mode, it is possible to modify the resource parameters.

###### Deleting Catalog SKU Relationships

To delete a catalog SKU resource, in the list of resources, click on the kebab menu for a resource and then click on "Delete".
![Eliminazione di una risorsa SKU](images/extract/media/image172.png)

Once done, a modal appears where it is necessary to click the "Remove" button to confirm the resource deletion.

![Conferma eliminazione della risorsa](images/extract/media/image173.png)

#### Scheduled Import of Catalog Items

Manually entering catalog resources is a very long and costly operation. To simplify this, the user is given the possibility to insert an "Excel" file containing data that will then be automatically imported on the day indicated as "Start validity".

##### New Import

To insert a new price list, it is necessary to click the "hamburger menu" available in the upper right corner of the catalog resources page and select "Import Catalogue".

![Accesso all "Importazione pianificata del catalogo"](images/extract/media/image187.png)

After clicking the button, a modal will open, containing two buttons:

- "Resources": clicking this button indicates to the system that the inserted price list will contain resources.
- "SKUs": clicking this button indicates to the system that the inserted price list will contain SKU items.

Once the resource type to be created is selected, the page updates to show all mandatory parameters.

![Scelta della tipologia di catalogo](images/extract/media/image188.png)

Two parameters are present in the modal:

- Provider: Select the provider related to the price list that will be inserted.
- Valid From: It is possible to indicate a start validity date for the price list. On the day indicated in this variable, the system will automatically update the catalog resources to conform to the new price list.

![Campi obbligatori per l'importazione](images/extract/media/image189.png)

Furthermore, below the parameters, there are two sections for file upload. Clicking on the first square on the left will allow selecting an "XLS" file containing all the resources to be mapped.
Clicking on the second square will allow inserting a mapping file, following the information shown in the "Help" section indicated with a "Question Mark" icon. Clicking on it will open a box, below the upload sections, containing all the information related to the mapping file to be inserted.

![Messaggio di aiuto per il file di Mapping](images/extract/media/image190.png)

After entering all parameters, it will be possible to click the save button at the bottom, and we will be redirected to the imported catalogs management page, where it will be possible to monitor their insertion.

##### Import Management

To insert a new price list, it is necessary to click the "hamburger menu" available in the upper right corner of the catalog resources page and select "Imported Catalogues".

![Accesso ai cataloghi importati](images/extract/media/image191.png)

The user will then be redirected to the page containing all previously imported catalogs. On this page, for each row, which corresponds to an Upload, it is possible to delete the file by clicking the "Three dots" button corresponding to the row and clicking "Delete" to remove it.

Catalogs can have 3 different states:

- Deleted: indicates that the file has been replaced with a subsequent version.
- Success: indicated with a green icon, indicates that the catalog is ready and will be used starting from the indicated day.
- In progress: indicated with a yellow icon, indicates that the system is checking the validity of the entered information.

On this page, we can also note that uploads made with the same file are saved using versions, so when an already existing catalog is inserted, it will be overwritten with a higher version, and previous versions will be deactivated.

![Lista dei cataloghi importati](images/extract/media/image192.png)

Clicking on a "Success" row in the table will open a modal. Inside, we can view a summary that contains, in addition to basic information, the number of elements, called "rows", that were found in the Excel file.

The rows available in the file can have 3 different states:

- Associated Rows: indicates that the system is able to both create the resource and associate it with a provider catalog size, allowing its use during provisioning.
- Success Rows: indicates that the system is able to create the resource but cannot establish a relationship with a provider resource.
- Failed Rows: indicates that the system cannot insert the resource.

![Dettagli dell' importazione](images/extract/media/image193.png)

At the bottom, we can click the "More Details" button to view the details of the Excel file rows that were discarded by the system. Clicking on one of them allows us to view the row number, the name indicated in the file, and the error that prevented its insertion.

![Dettagli delle righe dell' importazione](images/extract/media/image194.png)

![Dettaglio dell' errore](images/extract/media/image195.png)

### Provider Catalog Item Management

Within the Catalog Module, it is possible to view the list and details of the "sizes" available on the various providers configured on the SCMP for both individual resources (VM, STORAGE, NETWORK, SECURITY) and resource groups "SKU".

#### Resources

To view the list of resources available for a provider, select the "Cloud resources" menu (in red in the image) at the top and select one of the available providers (in yellow in the image). The functionalities available on the pages of the different providers are identical.

![Risorse del catalogo dei providers](images/extract/media/image196.png)

##### Export of Provider Sizes

To export the list of Catalog resources displayed on the page, in the upper right corner, click on the hamburger menu, and then click on "Export".

The operator will have the option to export the list of results in .csv and/or .json format.

![Esportazione dei risultati](images/extract/media/image197.png)

##### Forced Catalog and Cost Update Functionality

It is possible to force the system so that, after a few minutes, all "sizes" and their associated costs are automatically updated. To do this, click on the hamburger menu in the upper right corner, and then click on "Force Sync".

![Funzionalità Force Sync](images/extract/media/image198.png)

##### Resource Filters

The user is given the possibility to filter the displayed resource lists. At the top of the page, there is a filter section. The available filters are:

- "search": allows searching for resources with free text.
- "search by type": allows searching for resources of a specific type only.
- "search by tags" allows searching for all resources containing a specific tag.

After entering one or more filters, click the "magnifying glass" button to perform the search.

![Filtri del Catalogo](images/extract/media/image199.png)

##### Resource Summary View

To view a preview of a resource, click on the record of interest for a resource. A modal will appear showing the general information of the identified resource, including: System, Name, Size, Update Date, RAM, and CPU as shown in the following image.

![Dettaglio rapido delle risorse di catalogo](images/extract/media/image200.png)

##### Viewing Resource Details

To view the data of a resource, click on the kebab menu for a resource and then click on "Show". After

![Accesso alla risorsa in modalità view](images/extract/media/image201.png)

doing this, the user is on the resource page in view mode, where they can see the data but cannot modify it.
![Dettaglio Risorsa dal Modulo Catalog](images/extract/media/image202.png)

The detail of a resource is divided into various sections:

- Details
- Properties
- Tags & Notes
- Cost

In the Cost section, it is possible to sequentially select the Region, Zone, and Cost type to obtain a preview of the costs related to the selected resource.

![Sezione costi della risorsa](images/extract/media/image203.png)

In the bottom right, click the "Close" button to return to the list.

#### “On-Premise” Resources

The management of resource catalogs in on-premise systems varies significantly, being specific to each system. In some cases, the catalog functionality is absent, while in others, it is available but does not allow automatic retrieval of resources.

The user is given the possibility to define a personalized "Cloud" catalog directly in the SCMP. In this way, it will then be possible to add the created resources to the relationships of "SCMP Catalog" resources.

To do this, it is first necessary to access the catalog resources tab of an on-premise provider. Specifically, we take "VMWare" as an example by selecting "VMWare" in the "Cloud resources" menu of the catalog module.

![Accesso al catalogo On-premise](images/extract/media/image204.png)

On the page, in the upper right, above the filter bar, we find a contextual menu. Click on the "Three lines" icon and select "Add catalog resource". In this way, we will be redirected to the provider-specific page for creating the catalog resource.

![Creazione nuova risorsa](images/extract/media/image205.png)

At this point, the user is on the page where they can select the type of resource to create.

![Selezione del tipo di risorsa da creare](images/extract/media/image156.png)

From the dropdown menu, select the type of resource to create. Then, click the "Next" button. You will be on the resource compilation page.

![Esempio di form per la creazione di una risorsa](images/extract/media/image157.png)

On this page, after opening the available sections, enter all necessary parameters. In the "Cost" section at the bottom, it will be possible to add a customized price to associate with the resource. To do this, you need to select the billing interval (hourly, daily, weekly, monthly) and enter the cost related to the selected period on the right.

![Sezione costi delle risorse](images/extract/media/image160.png)

#### Cloud SKU

To view the list of SKUs available for a provider, select the "Cloud SKU" menu (in red in the image) at the top and select one of the available providers (in yellow in the image). The functionalities available on the pages of the different providers are identical.

![Risorse del catalogo dei providers](images/extract/media/image206.png)

##### Export of Available Provider Sizes

To export the list of Catalog resources displayed on the page, in the upper right corner, click on the hamburger menu, and then click on "Export".

The operator will have the option to export the list of results in .csv and/or .json format.

![Esportazione dei risultati](images/extract/media/image197.png)

##### Forced Catalog Update Functionality

It is possible to force the system so that, after a few minutes, all "sizes" and their associated costs are automatically updated. To do this, click on the hamburger menu in the upper right corner, and then click on "Force Sync".

![Funzionalità Force Sync](images/extract/media/image198.png)

##### Filters for Displayed Resources

The user is given the possibility to filter the displayed resource lists. At the top of the page, there is a filter section. The available filters are:

- "search": allows searching for resources with free text.
- "search by Service name": allows searching for resources related to a specific service type only.
- "search by tags" allows searching for all resources containing a specific tag. After entering one or more filters, click the "magnifying glass" button to perform the search.

![Filtri del Catalogo](images/extract/media/image207.png)

##### Catalog Resource Summary View

To view a preview of a resource, click on the record of interest for a resource. A modal will appear showing the general information of the identified resource, including: System, Name, Size, Update Date, service name.

![Dettaglio rapido delle risorse di catalogo](images/extract/media/image208.png)

##### Viewing Resource Details in the Catalog

To view the data of a resource, click on the kebab menu for a resource and then click on "Show". After doing this, the user is on the resource page in view mode, where they can see the data but cannot modify it.

![Accesso alla risorsa in modalità view](images/extract/media/image201.png)

![Dettaglio Risorsa dal Modulo Catalog](images/extract/media/image209.png).

The detail of a resource is divided into various sections:

- Details
- Properties
- Tags & Notes
- Cost

In the Cost section, it is possible to sequentially select the Region, Zone, and Cost type to obtain a preview of the costs related to the selected resource.

![Sezione costi della risorsa](images/extract/media/image203.png)

In the bottom right, click the "Close" button to return to the list.

### “Services and Blueprints” Item Management

#### Services

To access the "Services" functionality, click on the bento button in the upper left corner and then click on "Catalog".

![Accesso ai "Services"](images/extract/media/image210.png)

From the "SCMP" page, click on the tab that depicts three joined squares, 'Services', located above the breadcrumb path. After doing this, you will be on the 'Services' page, where a list of components called "Card" is displayed.

Each card refers to a specific type of service. Since there are many services, the system paginates them. At the bottom, we can use the "Item for page" field to display more results or use the arrows to navigate through the lists of services.

![Pagina dei servizi](images/extract/media/image211.png)

##### “Services” Page Filters

To facilitate the user in searching for a specific service, a side filter section has been added to the page. Inside, we can find three combinable filters:

- "Filter by Text": by entering text in this field, the list of services will be updated to show services that include the entered text in their title or description (orange in the image).
- "Categories": it is possible to filter the list by one or more service categories. The category is manually entered during the service creation phase (green in the image).
- "Tags": it is possible to select one or more tags to display only services that have been configured with that tag (red in the image).

By using the filters in combination, it will be possible to display only the services that satisfy all specified conditions. In other words, the query will return only the services that match all set criteria.

![Filtri disponibili](images/extract/media/image212.png)

##### Creating Services

From the "Services" page, the user can create a Service by accessing the appropriate section as shown in the figure.

![Accesso al form di creazione del Service](images/extract/media/image213.png)

On the creation page, it is necessary to select a service type using the "Service Type" field to display its mandatory parameters.

![Selezione della tipologia di servizio](images/extract/media/image214.png)

In the following paragraphs, we will analyze the individual service types in detail.

###### “Standard” Services

The first type of services available for the SCMP are "Standard" services. These services are natively integrated into the system, and their operation cannot be modified by the user.

List of services offered:

- CosmosDb Cassandra SQL
- CosmosDb Core SQL
- CosmosDb Mongo
- Kafka 3.2.1 on Ubuntu 20.04 LTS
- Kafka 3.2.1 on Ubuntu 22.04 LTS
- Mongo DB 5.0 on Ubuntu 20.04 LTS
- Mongo DB 6.0 on Ubuntu 20.04 LTS
- Mongo DB 6.0 on Ubuntu 22.04 LTS
- MySQL DB 8.0 on Ubuntu 20.04 LTS
- MySQL DB 8.0 on Ubuntu 22.04 LTS
- PostgreSQL 14 on Ubuntu 20.04 LTS
- PostgreSQL 14 on Ubuntu 22.04 LTS
- Redis DB 7.0 on Ubuntu 20.04 LTS
- Redis DB 7.0 on Ubuntu 22.04 LTS

To insert a new service, it is necessary to fill in all fields in the properties section, specifically:

- "Categories": enter free text in the field and select an already configured category from the dropdown, or it is possible to add a new category by clicking the "+" button in the dropdown (orange in the page).
- "Name": the name of the service that will be displayed on the corresponding card.
- "Description": the description of the service that will be shown on the relative card.
- "Upload File": by clicking this control, it will be possible to select an "image" type file from your PC that will be displayed on the service card.
- "Related Software": in this section, you can select one or more "Standard" software that will then be used during provisioning.

![Aggiunta nuova categoria](images/extract/media/image215.png)

Once all data has been entered, the service can be saved using the "save" button in the bottom right. A confirmation modal will be displayed, and the user will be redirected to the list of available services.

###### “Custom” Services

The user is given the possibility to define "Custom" services by uploading a zip file containing all the necessary files for execution.

In this specific case, the SCMP system is only used to save the service and launch its execution, so it is not possible to check the correctness of the process, which will have to be managed by the user.

all are orchestrators, but with different functionalities and purposes:

**1. Ansible:**

- **Server and application orchestration:** Ansible automates the configuration and management of servers and applications across different platforms.

- **Executes YAML playbooks:** Ansible uses YAML playbooks to define instructions to be executed on servers.

- **Does not require an agent:** Ansible is agentless; it does not require software installation on the servers to be managed.

**2. Bicep:**

- **DSL language for Azure:** Bicep is an Azure-specific DSL that facilitates defining infrastructure as code.

- **Creates ARM templates:** Bicep translates files into ARM (Azure Resource Manager) templates that Azure uses to create resources.

- **Integrates with Azure DevOps:** Bicep integrates with Azure DevOps for lifecycle management.

**3. Kubernetes:**

- **Container orchestration:** Kubernetes is the leading platform for large-scale container orchestration.

- **Automates deployment and management:** Kubernetes automates the deployment, scaling, and management of containers in clusters.

- **Offers an ecosystem of tools:** Kubernetes offers a rich ecosystem of tools and libraries for container management.

**4. Terraform:**

- **Infrastructure as Code:** Terraform is an open-source tool for managing infrastructure as code.

- **Defines infrastructure in HCL files:** Terraform uses HCL configuration files to define the desired infrastructure.

- **Supports different providers:** Terraform supports a wide range of cloud and on-premise providers.

**In summary:**

- **Ansible:** Ideal for automating server and application configuration.

- **Bicep:** Great for defining infrastructure on Azure in a readable way.

- **Kubernetes:** Powerful tool for large-scale container orchestration.

- **Terraform:** Flexible for managing infrastructure across multiple cloud providers or on-premise.

In the configuration of "Custom" services, we can identify a common section composed of the initial parameters:

- "Categories": enter free text in the field and select an already configured category from the dropdown, or it is possible to add a new category by clicking the "+" button in the dropdown.
- "Name": the name of the service that will be displayed on the corresponding card.
- "Description": the description of the service that will be shown on the relative card.

![Parametri generali dei "Custom Services"](images/extract/media/image216.png)

Subsequently, it is necessary to choose the type of "orchestrator" to use and insert the corresponding ".zip" file in the "Upload File" section. The specifications for each type are indicated below:

| **Script type** | **Mandatory .zip file content** |
|----|----|
| Ansible | Instance.yaml - Vars.yaml |
| Bicep | Main.bicep - Main.parameters.json |
| Kubernetes | Only .YAML files |
| Terraform | Main.tf - Variable.tf - Provider.tf |

In addition to the files described in the table, it is possible to add a ".png / .jpg / .img" file to the zip that will then be used as the image for the corresponding Card.

![Selezione della tipologia di Orchestratore](images/extract/media/image217.png)

Once all data has been entered, the service can be saved using the "save" button in the bottom right. A confirmation modal will be displayed, and the user will be redirected to the list of available services.

###### “Azure Pipeline” Services

The user is given the possibility to define "Azure Pipeline" services. This type of service allows the SCMP to invoke the execution of a remote DEVOPS pipeline usable through the provisioning functionality.

In the configuration of "Azure Pipeline" services, we can identify a general section composed of the parameters:

- "Categories": enter free text in the field and select an already configured category from the dropdown, or it is possible to add
  a new category by clicking the "+" button in the dropdown. "Name": the name of the service that will be displayed on the corresponding card.
- "Description": the description of the service that will be shown on the relative card.

![Parametri generali "Azure pipeline service"](images/extract/media/image218.png)

Also for this service, it will be possible, through the "Upload File" field, to insert a ".zip" file that contains a ".png / .jpg / .img" file within the zip, which will then be used as the image for the corresponding Card.

Subsequently, it will be necessary to fill in the specific parameters of the service, in particular, it will be necessary to insert:

- "Organization": the name of the DevOps organization where the pipeline resides.
- "Project": the name of the DevOps project where the pipeline resides.
- "PAT": the private personal access token generated from the "Azure DevOps" portal. Once these fields are filled, it is possible to click the "Test" button to verify the entered parameters.

If the entered data is not valid, various error messages will be displayed indicating which parameter is incorrect (e.g., "Specified Organization is not valid.") and the button will turn red with "KO" written. When all parameters are correct, the button will turn green with "OK" written.

![Parametri specifici delle Pipeline](images/extract/media/image219.png)

After successfully performing the test, it will be possible to select the pipeline to execute using the "Select Pipeline" field and clicking on an available option.

![Selezione della pipeline](images/extract/media/image220.png)

Once all data has been entered, the service can be saved using the "save" button in the bottom right. A confirmation modal will be displayed, and the user will be redirected to the list of available services.

###### “HELM” Services

We can also configure "HELM" type services within the SCMP. For the configuration of these services, it is necessary to enter these parameters:

- "Categories": enter free text in the field and select an already configured category from the dropdown, or it is possible to add a new category by clicking the "+" button in the dropdown.
- "Chart name": the actual name of the HELM CHART that will be used.
- "Chart repository": the URL relative to the repository containing the HELM CHART to be used.
- "Repository username": if the repository indicated above is private, it will be necessary to provide a username to access the repository.
- "Repository password": if the repository indicated above is private, it will be necessary to provide the password for the user indicated above.
- "Chart version": indicates which version of the chart to use.
- "Cluster": indicates which cluster to install the application on.
- "Description": the description of the service that will be shown on the corresponding card.
- "Image": in this section, it is possible to insert a .png file that will be used as the service image on the interface.
- "Immutable": Selecting this flag during provisioning will prevent modification of settings, and the service will be automatically configured based on.
- "Namespace": enter the name for the namespace where the deployment should occur.
- "Name": the name of the service that will be displayed on the corresponding card.
- "Configurations": in this section, it is possible to upload the values.yaml file that will be used for provisioning.

![Parametri generali dei "HELM Services"](images/extract/media/image221.png)

For these services, it is also possible to prevent any kind of service modification by selecting the "immutable" option and entering a namespace and a cluster in which to deploy the applications.

![Parametro "immutabile"](images/extract/media/20250605003.png)

Once all data has been entered, the service can be saved using the "save" button in the bottom right. A confirmation modal will be displayed, and the user will be redirected to the list of available services.

##### Editing and Deleting Services

In addition to creating a Service, it is possible to view, modify, and delete it.

![Operazioni disponibili per i Services](images/extract/media/image222.png)

- To modify the information of a "Service", click the "Edit" button within the card. Afterward, within the form, the user can modify the necessary data. After performing the edit operations, in the bottom right, click the "Submit" button. After doing this, the user is on the "Service" page.

![Pagina di edit per un servizio](images/extract/media/image223.png)

- To delete a "Service", click on the kebab menu of said service and then click on "Delete". After doing this, a confirmation modal for service deletion appears. At this point, it is necessary to click the "Remove" button.

![ Eliminazione di un servizio](images/extract/media/image224.png)

#### Blueprint Management

To access the "Services" functionality, click on the bento button in the upper left corner and then click on "Catalog".

![Accesso alle "Blueprint"](images/extract/media/image210.png)

From the "SCMP" page, click on the tab that depicts three joined squares, 'Blueprint', located above the breadcrumb path. After doing this, you will be on the 'Blueprint' page, where the list of blueprints configured in the system is displayed.

![Pagina delle Blueprint](images/extract/media/image225.png)

##### Adding a new blueprint

From the "Blueprint" page, the user can create a new blueprint by accessing the appropriate section as shown in the figure, by clicking the "hamburger menu" in the upper right corner and selecting "Add Blueprint".

![Aggiunta nuova Blueprint](images/extract/media/image226.png)

The user is redirected to step 1 of the "Blueprint" creation where all general information about the blueprint can be entered. After entering the data, click the "Save blueprint" button to save the blueprint draft. For details on the status, please refer to the next paragraph.

![Blueprint step 1](images/extract/media/image227.png)

A confirmation modal for insertion will open. Once "yes" is clicked to continue, the user will see step 2 of blueprint creation.

Clicking "No" will cancel the draft insertion.

![Blueprint conferma della bozza](images/extract/media/image228.png)

In step 2 of creating a Blueprint, it is necessary to click within the "Upload File" field and, using the Windows upload window, select the ".CSAR" file that contains the Blueprint.

After selecting a file, click the "Upload" button in the bottom right to start the file validation process, following the list of statuses in the paragraph below.

![Inserimento file](images/extract/media/image229.png)

##### Blueprint Status

Since "Blueprints" are complex objects that must be properly configured, a file validation system has been implemented to allow the use of only "Blueprint" services that are correctly configured.

Specifically, there are 4 possible "STATUSES":

1. READY TO USE (green checkmark): indicates that the blueprint is configured correctly and can be used during "Provisioning".
2. VERIFY (yellow circle): indicates that the SCMP is validating the content of the Blueprint.
3. FAILED (red "X"): indicates that the uploaded file is not valid and must be re-entered by the user after correction.
4. DRAFT (orange): indicates that the "blueprint" has been created as a draft but does not contain the necessary CSAR file. Once the file is inserted, the blueprint will change to VERIFY status.

![Status delle Blueprint](images/extract/media/image230.png)

##### Viewing, Editing, and Deleting Blueprints

In the table of available blueprints, for each row, on the right, there is a contextual menu. Once opened, it contains three functionalities:

The "View" functionality: allows viewing the details of the blueprint. Once clicked, the user will be redirected to the blueprint viewing page.

- Properties: in this section, it is possible to modify the basic information of the blueprint (Figure 241).
- Provisioning plan: in this section, there is the bpmn graph which provides a graphical representation of the "steps" foreseen by the "Blueprint" (Figure 242). This section contains three buttons to modify the plan: the first, shaped like a "folder", allows uploading a new BPMN file to the edit page; the second, "download", allows downloading the currently displayed bpmn file; the third, on the right, "Upload", overwrites the current bpmn file available for the blueprint.
- Topology: The topology of a blueprint is the arrangement of components in a Kubernetes cluster. In this section, we can graphically visualize the system structure among different pods, services, and components (Figure 243).
- Update Model: in this section, it is possible to upload the CSAR file. By making this modification, the Blueprint will return to the "VERIFY" state to validate its content (Figure 244).

![Sezioni della pagina Blueprint "view"](images/extract/media/image231.png)

The "Edit" functionality allows viewing and modifying all blueprint parameters, including the related CSAR file. It contains the following sections:

- Properties: in this section, it is possible to modify the basic information of the blueprint.
- Provisioning plan: in this section, there is the bpmn graph which provides a graphical representation of the "steps" foreseen by the "Blueprint". This section contains three buttons to modify the plan: the first, shaped like a "folder", allows uploading a new BPMN file to the edit page; the second, "download", allows downloading the currently displayed bpmn file; the third, on the right, "Upload", overwrites the current bpmn file available for the blueprint.
- Topology: The topology of a blueprint is the arrangement of components in a Kubernetes cluster. In this section, we can graphically visualize the system structure among different pods, services, and components.
- Update Model: in this section, it is possible to upload the CSAR file. By making this modification, the Blueprint will return to the "VERIFY" state to validate its content.

![Sezioni della pagina Blueprint "edit"](images/extract/media/image234.png)

![Sezione Plan di una Blueprint](images/extract/media/image235.png)

![Sezione Topology di una Blueprint](images/extract/media/image233.png)

![Sezione Model di una Blueprint](images/extract/media/image236.png)

The "Delete" functionality: allows permanently deleting the blueprint from the system. To do this, simply confirm the deletion by clicking the "Yes" button displayed in the deletion confirmation modal.

![Eliminazione di una Blueprint](images/extract/media/image237.png)

### Reporting Tools

The reporting functionality, specific to each feature, allows generating global reports of the information available for the various
providers. Within the pages, the possibility will also be given to create files to facilitate information sharing.

To access the functionality, above the breadcrumb path, click on the "Reports" tab.

![Accesso al report di Catalogo](images/extract/media/image141.png)

#### Available Report Types

**CATALOG Missing SKU** – List of provider SKUs not present in the SCMP catalog price list, if applicable. Consequently, the customer price for missing SKUs will be given by applying the discount/markup percentage configured in the Administration section.

#### Creating a Report

In the upper right of the page, we can click on the "New Report" button to start creating a report. Specifically, a modal will be displayed containing the list of available report types.

![Creazione nuovo report](images/extract/media/image142.png)

Once the report type is selected, click the "Configure" button to select the providers to include in the report. In the newly opened window, we find the "Provider" field which allows selecting one or more existing providers in the system. Subsequently, it is possible to select one or more subsystems to include in the report. If no providers are selected, no subsystem can be selected. Finally, there is a "tag" section to include only resources that have the entered tag.

![Configurazione del report](images/extract/media/image143.png)

At this point, the user can choose between two different actions:

- Create a static report that will be saved in the system.
- Schedule a recurring report generation.

To confirm the creation of a static report, verify that "One-Shot" has been selected for the "Report type" field and click the "Submit" button at the bottom.

After a loading period, the newly generated report will be visible in the list.

![Lista dei report effettuati](images/extract/media/image144.png)

##### Report Scheduling

If, on the other hand, you want to schedule automatic report execution, you will need to select "Recurring" for the "Report Type" field. In this case, the window will update to show additional parameters for configuring the periodic report.

The parameters to be entered are:

- Period: allows selecting the frequency of report delivery (hourly, daily, ...).
- "Receive only if not empty" if selected, the file will not be sent if it contains no information.
- Report Language: allows selecting the language used in the report.
- File format: allows selecting one or more file types to include in the email.
- User E-mails: allows entering an email to which reports will be sent. After entering an email, it is necessary to press "Enter" on the keyboard to confirm its entry. Once pressed, the newly entered email will move to the bottom box, and the field will be cleared to allow the entry of a new email, if necessary.

![Parametri dei report schedulati](images/extract/media/image145.png)

Having configured all parameters, the "Submit" button will become clickable. Click it to confirm the entry, and after a loading period, the newly generated report will be visible in the list.

![Lista dei report effettuati](images/extract/media/image144.png)

##### List of Scheduled Reports

To view the list of scheduled reports, select the "Scheduled" tab in the upper left of the reports page.

![Lista dei report schedulati](images/extract/media/image146.png)

On this page, you will find the list and related information of the scheduled reports present in the system. For each result, it is possible, by clicking the "Three dots" button on the right, to perform three operations:

- View the last generated report.
- Edit the schedule settings; it will not be possible to modify the selected providers or subsystems.
- Delete the schedule to stop sending emails.

![Modifica di una schedule](images/extract/media/image147.png)

##### Using Reports

Clicking on a row of a static report, or using the "Show report" button available for scheduled reports, will display the detail page of the selected report.

In the summary of the Inventory report, there is a "Stats" section which contains the number of disks, interfaces, networks, and virtual machines belonging to the selected provider.

Below the "Stats" section, there are the filters used by the user to generate the report.

Below the filters, there is a summary table of resources belonging to the providers. On the right, there are two buttons: "PRINT" and "EXPORT".

Clicking the "PRINT" button, a print preview modal appears. To print the report, click the "Print" button in the bottom right, at which point the printing of said report will begin.

Clicking the "EXPORT" button, it is possible to export the report in ".csv", ".json", or ".pdf" format.

To return to the "Results" tab, in the bottom right, click the "CLOSE" button or in the upper left, click the left-pointing arrow, next to the report title.

![Dettagli dei report](images/extract/media/image148.png)
