# Tenants

SCMP has been developed as a Multi-Tenant solution, which offers greater security, customization, flexibility, and scalability, with more efficient administration and reduced costs.

To allow the user to manage the tenants present in the infrastructure, the "Tenant" functionality has been made available, a feature not available to everyone but only to users enabled for Service Management.

To access the functionality, click on the bento button in the top left. Afterwards, click on "Tenant".

![Access to Tenant management](images/extract/media/image31.png)

### Creation of a new tenant

At this point, the user is inside the "Tenant" tab page, which contains the list of tenants configured on the system. To add a new tenant, click the "menu" available in the top right and select the "+ Add" item.

![Add new tenant](images/extract/media/image32.png)

Once pressed, the new tenant configuration page is displayed, divided into three sections:

![New tenant creation form](images/extract/media/image33.png)

1. General parameters:

| **Name** | **Description** | **Required** |
|----|----|----|
| Tenant ID | Unique ID of the new tenant | x |
| Tenant Name | Name of the tenant that will be displayed to the user | x |
| Description | A description of the tenant | x |
| MarketPlace Subscription ID | the ID received from the Azure marketplace upon service subscription |  |

2. Data persistence:

| **Name** | **Description** | **Required** |
|----|----|----|
| Inventory | Indicates the number of days for which inventory data will be retained in the collections present in the DB | x |
| Cost | Indicates the number of days for which cost data will be retained in the collections present in the DB | x |
| Monitoring | Indicates the number of days for which monitoring data will be retained in the collections present in the DB | x |
| Security | Indicates the number of days for which security data will be retained in the collections present in the DB | x |

3. Init Catalog

In this section, you can select the catalog items that
will be automatically copied to the new tenant.

The initial section (1) allows choosing only one option from:

- Empty Catalog: leave the catalog empty without copying any information.
- Copy Catalog from Default Tenant: indicates that the tenant from which to retrieve information to copy is the Default tenant.
- Copy Catalog from other Tenant: if selected, a new field containing the list of available tenants will be displayed in the section below, allowing the selection of the tenant from which to retrieve information to copy.

Subsequently, you can fill in the next section (2) by entering the non-mandatory fields:

- **Providers**: list of providers configured in the source tenant; selecting one or more providers will copy their catalog items to the new tenant.
- **Copy SCMP Catalog**: if activated, all elements present in the SCMP catalog will be added to the new tenant.
- **Copy Services**: if activated, all elements present in the SCMP catalog will be added to the new tenant.
- **Copy Custom Services**: if activated, custom services available on the tenant will be added to the new tenant.
- **Copy Blueprints**: if activated, all available Blueprints will be added to the new tenant.

4. Association Catalog

In this section, you can select the flag to enable the tenant to use the "Common" price lists analyzed later.
By selecting this field, it will no longer be necessary to define a specific catalog for the tenant; it will inherit the common price lists.

![Catalog initialization section](images/extract/media/image34.png)

To confirm the creation of the new tenant, click the "Save" button in the bottom right. After waiting for loading, a creation confirmation message will be displayed, and the user will be returned to the tenant list where the newly created tenant will be present.

#### Viewing, Modifying, and Deleting a tenant

In the tenant list, next to each result, there is a "menu" with three buttons:

- "Show": allows viewing tenant information (indicated with a red arrow in the image).
- "Edit": allows modifying basic tenant information (indicated with a yellow arrow in the image).
- "Delete": allows deleting the user after clicking "confirm" in the displayed modal (indicated with a purple arrow in the image).

![Control buttons](images/extract/media/image35.png)

### Automated tenant and subsystem creation

The user is given the possibility to automate the import of tenants and subsystems to speed up "onboarding" operations. To access the functionality, click the "import" tab available at the top of the "Tenants" functionality.

![Tenant import functionality](images/extract/media/082425001.png)

In the center of the page, there is a contextual menu that allows selecting the import type (Tenant or subsystems).

Let's analyze the 2 pages in detail.

#### Tenant Import

The functionality consists of 2 sections:

1. The "upload file" section where you can insert a file in .xlsx format (of which an example can be downloaded using the dedicated button) {in red in the figure}
2. The "configuration" section where it is possible to select the parameters shared between tenants (in yellow in the figure), as described in the section ([Creation of a new tenant](#creazione-di-un-nuovo-tenant)).

Once all information has been entered, you can click the "import" button (in green in the figure) to validate the uploaded file and start the import process.

![Tenant configuration parameters](images/extract/media/082425002.png)

After a few minutes, you can use the "Results" button (in pink in the image) to view the details of the operations performed by the SCMP.

![Results of performed imports](images/extract/media/090425001.png)

#### Subsystem Import

To access the subsystem import functionality, you need to click on the "subsystems" tab available on the "import" page.

![Subsystem import functionality](images/extract/media/082425003.png)

The functionality consists of 2 sections:

1. The "upload file" section where you can insert a file in .xlsx format (of which an example can be downloaded using the dedicated button).
2. The selection of the provider type to import.

Once files are inserted and it's verified that the provider is compatible, you can click the "import" button (in green in the figure) to validate the uploaded file and start the import process.

![Tenant and subsystem import functionality](images/extract/media/082425004.png)

After a few minutes, you can use the "Results" button (in pink in the image) to view the details of the operations performed by the SCMP.

![Results of performed imports](images/extract/media/090425001.png)

### "Common" Catalogs

The user is given the possibility to import a series of catalogs for SKUs or resources, which will then be used by all tenants that have the [enabled flag](#creazione-di-un-nuovo-tenant).

To proceed with price list entry, you can access the "Price list" page available on the tenant administration module.

![Access to catalog import](images/extract/media/250530001.png)

Once inside the page, to view the data, we can use the "Provider" filter to select the type of provider for which to check the status of price lists.

![Filter by provider](images/extract/media/250530002.png)

We can use the other filters on the page to:

- View data for a specific year ("Date" filter)
- View specific catalogs for the selected tenant ("tenant" filter)

To view the data, it is necessary to select only one type of provider, in order to display the calendar and the list of price lists applied for a given year to the specified tenant and/or common.

Inside the page, you will find the list of imported price lists with their validity period. For each row, a color is also indicated; this color helps identify the price list in the graphic section on the left. This calendar facilitates the identification of periods not covered by the price list.

The list of "inactive" price lists that have been previously replaced is also displayed.

![Inactive price lists](images/extract/media/300625001.png)

#### New price list entry

To enter a new price list, you need to click the "hamburger menu" available in the top right of the catalog resources page and select "Import Catalogue".

![Access to "Scheduled Catalog Import"](images/extract/media/300625002.png)

Three parameters are present in the modal:

- Tenant: select the tenant on which to perform the upload.
- Provider: Select the provider related to the price list to be entered.
- Valid From: it is possible to indicate a start date for the price list's validity. On the day indicated in this variable, the system will automatically update the catalog resources to match the new price list.

If necessary, the user can enter a "common to all tenants" price list which will be used by all configured tenants containing systems from the reference provider.

![Required fields for import](images/extract/media/300625003.png)

Additionally, below the parameters, there are two sections for file upload. By clicking on the first square on the left, you can select an "XLS" file containing all resources to be mapped. By clicking on the second square, you can insert a mapping file, following the information shown in the "Help" section indicated by a "Question Mark" icon. Clicking on it will open a box below the upload sections that contains all information related to the mapping file to be inserted.

![Help message for Mapping file](images/extract/media/image190.png)

After entering all parameters, you can click the save button at the bottom, and you will be returned to the previous page which, after the import, will display the new price list.

#### Modifying validity and deleting price lists

To modify a price list, it is necessary to click the menu corresponding to the table row containing the price list, as indicated in the figure. Subsequently, select the edit item to display the modification mask.

![Edit a price list](images/extract/media/300625005.png)

Within the window, it is possible to modify the validity date of the price list, either to reduce or extend its duration. If the "Indefinite time" option is selected, the price list will remain valid until a new price list is entered. At that point, the price list with indefinite validity will be automatically deactivated and considered valid until the day the new price list is activated.

After the update, it is necessary to refresh the costs on the involved tenants, in order to correctly calculate the customer price based on the updated price lists.

![Edit the validity of a price list](images/extract/media/300625006.png)

The user is also given the option to delete a price list. In this case, the period previously covered by that price list will remain uncovered, i.e., without an associated rate.

![Price list deletion](images/extract/media/300625007.png)

### Price list changes changelog

Using the "Price list changelog" tab available at the top of the "tenant administration" section, it is possible to view a list of operations performed on the price lists, with an indication of the dates used for import and the reference user who made the changes.

![Error details](images/extract/media/300625004.png)

Using the filter available on the page, we can view data for only one selected tenant.
### Reporting tools

The reporting functionality, specific to features, allows generating global reports of the information available for the various providers. Within the pages, the possibility will also be given to create files to facilitate information sharing.

To access the functionality, above the breadcrumb path, click on the "Reports" tab.

![Access to Catalog report](images/extract/media/image141.png)

#### Available report types

- **SKUs not in Price List** – List of SKUs that have generated costs (retrieved through the cost functionality for each provider) that are not present in the price list entered in the "price lists" section.

#### Report creation

In the top right of the page, we can click on the "New Report" button to start creating a report. Specifically, a modal is displayed containing the list of available report types.

![New report creation](images/extract/media/image142.png)

Once the report type is selected, click on the "Configure" button to select the providers to include in the report. In the newly opened window, you will find the "Provider" field that allows selecting one or more pre-existing providers in the system. Subsequently, you can select one or more subsystems to include in the report; if no providers are selected, no subsystems can be selected. Finally, there is a "tag" section to include only resources that have the entered tag.

![Report configuration](images/extract/media/image143.png)

To confirm the creation of a static report, verify that "One-Shot" has been selected for the "Report type" field and click the "Submit" button at the bottom.

After a loading period, the newly generated report will be visible in the list.

![List of generated reports](images/extract/media/image144.png)

<div class="no-print">

Removed in release 8.0.0

### Catalog synchronization between different tenants

A functionality is implemented within SCMP that allows the user to copy a price list previously uploaded using an XML file in the catalog functionality. To do this, it is necessary to click on the destination tenant and then click on "Associate tenant".

![Catalog association functionality](images/extract/media/image36.png)

A window will be displayed showing the list of previously associated price lists. At the bottom, by clicking the "Associate Catalog" button, we will start the association procedure.

![Start of Association process](images/extract/media/image37.png)

The first necessary step for associating price lists is the selection of the source, in this case, the tenant containing the price list to be associated.

![Selection of "Source" tenant](images/extract/media/image38.png)

By selecting the "Source" tenant, the list of price lists present within the tenant will be displayed on screen, from which one or more items can be selected. These will be automatically imported and associated by clicking the "Associate Catalog" button.

![Price list selection](images/extract/media/image39.png)

A confirmation modal will be displayed informing us to wait a few minutes to allow the system to complete the operations, and we will be returned to the "tenant" page.

![Confirmation of import process start](images/extract/media/image40.png)

In the tenant list, you can click on the corresponding row to view, in addition to the tenant details, also the list containing the new price list that we have imported. On this same page, you can click the "Associate Catalog" button to repeat the operations just described.

![Price list successfully imported](images/extract/media/image41.png)

</div>
