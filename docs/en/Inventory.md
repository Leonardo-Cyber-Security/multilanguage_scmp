# Inventory

The inventory functionality collects metadata of installed assets across all providers present on the SCMP.

The assets currently present are:

- Virtual Machine
- Data Stores
- Networks
- Clusters
- Edge
- Security
- Others

Heterogeneous metadata, coming from different sources, is then normalized by the SCMP to allow for standard visualization.

Inventory is accessible from the “Inventory” menu item.

![Accesso a Inventory](assets/images/extract/media/image104.png)

### Inventory Dashboard

The Dashboard page provides a global and aggregated view of all resources, while the menus above the breadcrumb path allow filtering by resource type. The functionalities available on the various pages are identical.

![dashboard di inventario](assets/images/extract/media/image105.png)

Within the “Resources” tab page, there are filters; in the first filter at the top, it is possible to search for resources by name, resource group, Provider, etc. It is also possible to filter resources by “Provider” and “Subsystem”.

The last filter allows searching by tag. Click on it and select a tag, then by clicking the button depicting a magnifying glass, the page will refresh and display the list of filtered resources.

![Ricerca generica, per tag, per Provider e Subsystem](assets/images/extract/media/image106.png)

It is also possible to click on the graphs to automatically apply the relevant filters.

#### Resource detail view

To view the details of a resource, you can click as shown in the figure:

![Accesso alla risorsa in modalità lettura](assets/images/extract/media/image107.png)

The detail of an inventory asset shows the main characteristics at the top, such as monthly cost, machine size, and an external link to the resource pointing to the reference provider.

Below is the detailed view of a VM:

![Dettaglio risorsa](assets/images/extract/media/image108.png)

And at the bottom, the asset's relationships with other SCMP elements, as shown in the figure:

![Grafico delle relazioni](assets/images/extract/media/image109.png)

The relationship graph allows navigating between resources by directly clicking on the circle of the linked resource, in order to land on its details.

Furthermore, it is possible to edit some attributes, such as tags, as shown in the figure:

![Selezione del tag](assets/images/extract/media/image110.png)

For the “Provider Tags…” field, it is not possible to select a tag, as tags in this section are retrieved directly from the subsystem.

The “Add SCMP Tag…” field allows selecting from a list or manually entering one. Inside the tag, there is an “X” symbol to delete it.

It is possible to add multiple tags to the resource.

Subsequently, in the bottom right of the “Tags & Note” section, click on the “Save” button to save the change, and a banner will appear at the bottom indicating the tag has been saved.

Scroll the page to the bottom, and click on the “Close” button located on the right to return to the “Dashboard” tab page.

#### Actions on inventory machines

For inventory machines from supported providers, a new button available in the table context menu called “Manage” can be used to perform basic operations on the machines.

![Accesso alla funzionalità di "management"](assets/images/extract/media/image111.png)

From this resource detail page, the following operations can be performed using the menu at the top of the page; the operations available on the machines may vary depending on the provider:

Azure Stack HCI

- Start machine
- Stop machine
- Resize machine
- Add storage disks
- Add network interface
- Delete resource
- Remove disk from resource
- Remove network interface

Red Hat Edge

- Update an EDGE device image

Operations are indicated in white when they can be executed and in gray when they are not supported or unavailable for the resource.

![Operazioni sulle macchine di inventario](assets/images/extract/media/image112.png)

#### “Cluster Explorer” functionality

Cluster Explorer is a powerful feature that allows users to view namespaces within a cluster in detail. This function provides a comprehensive overview of data and resource organization within the cluster, facilitating navigation and management of complex environments.

With Cluster Explorer, users can:

- View the complete list of namespaces in a cluster: Get a quick overview of all available namespaces in the cluster.
- Examine the details of each namespace: Access complete information about each namespace, including name, description, labels, and resource quotas.
- Filter and search namespaces: Quickly find specific namespaces using advanced filtering and search criteria.

To access the functionality, select the “Clusters” item from the horizontal menu of the Inventory module.

![Accesso alla funzionalità di cluster explorer](assets/images/extract/media/image113.png)

Inside the page, a list of clusters present within the subsystems configured in the system will be displayed. Clicking on one of them will open a modal with the general details of the cluster.

![Finestra di dettaglio del cluster](assets/images/extract/media/image114.png)

We can notice that at the bottom right there is a “cluster explorer” button; pressing it will redirect us to the cluster Dashboard. This page can also be accessed using the “cluster explorer” button available in the “three dots” context menu present for each cluster in the list of results.

Within this page, we can view a graph representing the distribution of namespaces within the cluster; on the right, the legend of namespaces with the number of active pods is displayed.

![Dashboard del “cluster explorer”](assets/images/extract/media/image115.png)

We can drill down into the details of namespaces using different components on the page:

it is possible to click on the “Explore namespaces” button at the top right or click on the number of namespaces displayed at the top left to view the namespace exploration page without filters. If we want to directly view the details of a namespace present in the graph, it is possible to click on the corresponding slice, and the detail page will be automatically filtered for the selected namespace.

![Pagina "Namespace explorer"](assets/images/extract/media/image116.png)

The namespaces field at the top allows searching among available clusters by entering free text. If a match is found, you can select the namespace from the list to view its details.

![Dettaglio dei namespace](assets/images/extract/media/image117.png)

Using the “Down Arrow” commands, it will be possible to navigate between available categories and sub-categories of elements. Finally, by selecting a result, its details will be displayed in the right section of the page, which will be automatically populated with the selected result from the left.

![Dettagli del contenuto del namespace](assets/images/extract/media/image118.png)

### “WHAT IF” Functionality

This functionality allows performing simulations for asset migration from one provider to another, or within the same provider, in order to compare management and maintenance costs.

To run a simulation, click on the tab above the breadcrumb path that depicts a relationship connecting two entities, named ‘What If’.

![Accesso a “What If”](assets/images/extract/media/image119.png)

After doing so, you will find yourself on the “What If” tab page.

Above the list of simulations, on the right, we can notice two tabs that allow filtering the list by simulation type, specifically:

upon opening the page, all “Change Provider” type simulations will be displayed, while clicking on the “Capacity” tab will allow viewing the list of “Change size” type simulations.

![](assets/images/extract/media/image120.png)
![Pagina di “What If”](assets/images/extract/media/image121.png)

#### Scenario “What If”: Provider Migration

To perform a “What If: Migrate Provider” simulation, click on the box on the left titled “Migrate to another provider”.

![Accesso alla funzionalità "What If: Migrate Provider"](assets/images/extract/media/image122.png)

After doing so, the user will find themselves on the “Start” page of step 1 for simulating resource migration from one cloud provider to another.

On the left, in the “Select Resources to migrate” box, the user can search for resources using three types of filters, including:

- “Search” which allows searching for a resource by name;
- “Search by Type” to obtain resources by selecting the resource type;
- “Search by tags” which allows searching for resources using one or more tags.

Within the resource table, only resources that have a relationship in the catalog will be displayed.

Within the resource table, click on one of them and, using the “drag and drop” technique, drag it to the right, into the box titled “Currently selected”.

A maximum of three resources can be included per simulation.

Subsequently, in the bottom right, click on the “Next” button.

![Scelta delle risorse in cui effettuare la migrazione del provider](assets/images/extract/media/image123.png)

After doing so, the user will find themselves on the “Destination Providers” page of step 2, where it is possible to click on the checkbox corresponding to one or more providers. Based on the selected provider type, the value in the ‘Option selected’ field at the bottom left will be automatically populated with the names of the selected providers.

Subsequently, in the bottom right, click on the “Next” button, while to return to the “Start” page of step 1, click on the “Back” button.

![Scelta del Cloud Provider in cui migrare le risorse](assets/images/extract/media/image124.png)

After clicking the “Next” button, the user will find themselves on the page of step 3 titled “Details”.

On this page, cards will be displayed, one for each subsystem selected in step 2.

In each card, on the left, there is a list of regions available for the cloud provider, and on the right, an empty section is displayed.

Selecting one or more regions in the right section (in red in the figure) will display a menu in the right section that allows selecting the type of cost to apply (in yellow in the figure). Selecting the “Consumption” type requires no further parameters, while selecting the “Reservation” type, to the left of the field, it will be possible to choose the Reservation period (in yellow in the figure).

![Selezione della "Regione" e del "Cost Model"](assets/images/extract/media/image125.png)

After clicking the “Next” button, the user will find themselves in step 4 titled “Duration”.

From the “Duration” page of step 4, select an interval for the simulation among:

- “One Month”
- “Six Months”
- “One Year”

To return to the “Details” page, in the bottom right, click on the “Back” button. Instead, to proceed with the simulation, click on the “Launch Simulation” button.

![Selezione dell'intervallo di tempo](assets/images/extract/media/image126.png)

After clicking the “Launch Simulation” button, the user will find themselves on the “Results” page of step 5.

Within the “Results” page, at the top, the “Simulation parameters” box can be viewed, which contains a summary of the parameters used. (in yellow in the figure)

Below the “Summary” box, there are different sections, one for each destination provider (in red in the figure), and inside, we can view the list of resources that can be migrated to the provider (in green in the figure). Clicking on one of them will display a histogram graph. In this graph we can note:

- A line parallel to the X-axis indicating the current cost of the resource.
- A series of bars (one for each region and selected cost type) that will be red when the destination price is higher than the starting price or green when the price is lower than the current cost of the resource; hovering over one of them will display its reference.
- A summary table of the selected cost types, which is used to generate the bar chart.

It is possible to view details for other simulations (in purple in the figure) using the procedure just described.

To exit the simulation without saving, in the bottom right, click on the “Close” button.

To save the simulation, click on the “Save” button next to the “Close” button, and then click on “Confirm”.

After clicking a button, the user is redirected to the “What If” tab page.

![Pagina dei risultati della simulazione WHAT IF](assets/images/extract/media/image127.png)

![Tabella riassuntiva della/e risorse](assets/images/extract/media/image128.png)

It is possible to update and re-run a simulation without re-entering all data.

To do this, click on the row to be modified. At this point, the user will be redirected to step 1 of the simulation, where all steps have been pre-filled using the saved parameters.

![Avvio per l'aggiornamento della simulazione di tipo "Migrate to another provider"](assets/images/extract/media/image129.png)

#### Scenario “What If”: Change Resource Capacity

This functionality allows comparing the costs of a resource in case of modification of its technical characteristics.

Still from the “What If” tab page, in the top right, click on the “Change resources capacity” box.

![Accesso alla funzionalità "What If: Change resources capacity"](assets/images/extract/media/image130.png)

After doing so, the user will find themselves on the “Start” page of step 1.

On the left, in the “Select Resources to change” box, the user can search for resources using three types of filters, including:

- “Search” which allows searching for a resource by name;
- “Search by Type” which allows obtaining resources by selecting the resource type;
- “Search by tags” which allows searching for resources using one or more tags associated with them.

The resource table will only show resources that, within the SCMP catalog, have more than one “Relationship” with different sizes but belong to the same region, price type, and operating system.

In the bottom left, there is the resource table, which can be filtered based on the parameters entered in the filter(s). Within the resource table, click on one of them and, using the “drag and drop” technique, drag it to the right, into the box titled “Currently selected:”.

A maximum of three resources can be included per simulation.

Subsequently, in the bottom right, click on the “Next” button.

![Selezione delle risorse da cui modificare le capacità](assets/images/extract/media/image131.png)

After doing so, the user will find themselves on the “Resource Provider” page of step 2, where it is possible to modify the size of one or more resources.

Within the “Resource Provider” page of step 2, for a resource, click on the dropdown menu in the “Size” column and select a different size from the initial one.

After that, in the bottom right, click on the “Next” button to continue the simulation.

To return to the “Start” page of step 1, click on the “Back” button.

![Modifica della size di una risorsa](assets/images/extract/media/image132.png)

After clicking the “Next” button, the user will find themselves on the “Duration” page of step 3.

Within the aforementioned page, it is necessary to select an interval for the simulation.

After that, in the bottom right, click on the “Launch Simulation” button.

To go back, click on the “Back” button; in this way, the user will find themselves on the “Resource Provider” page of step 2.

![Selezione dell'intervallo per la simulazione](assets/images/extract/media/image133.png)

After clicking the “Launch Simulation” button, the user will find themselves on the “Results” page of step 4.

Within the “Results” page, at the top, there is a “Summary” box that advises whether to modify the size of the resources. Below, there is an histogram graph, where the purple bar represents current costs, while the green bar represents target costs.

To save the simulation, click on the “Save” button next to the “Close” button, and then click on “Confirm”. After doing so, the user is redirected to the “What If” page.

To exit the simulation without saving it, in the bottom right, click on the “Close” button. After doing so, the user will find themselves on the “What If” page.

![](assets/images/extract/media/image134.png)
![](assets/images/extract/media/image135.png)
![Parametri di configurazione e consiglio sulla simulazione](assets/images/extract/media/image136.png)

#### What If scenario Export

For a simulation of a resource size modification, it is possible to export it in PDF, CSV, and JSON format.

Within the “What If” page, at the bottom, there is a table of simulations; click on the “Capacity” button located in the top right corner of the aforementioned table.

After doing so, the table shows simulations regarding resource size modification.

For a simulation, click on the button depicting an arrow.

At this point, a sub-menu will open where it is possible to export in the three previously described formats.

![Export della simulazione](assets/images/extract/media/image137.png)

Also for a simulation, it is possible to print it.

For a simulation, click on the kebab menu, and then click on the “Print” option.

At this point, a modal of the print preview will appear. Finally, click on the “Print” button to start printing the document.

![Stampa della simulazione](assets/images/extract/media/image138.png)

For a simulation, click on the kebab menu.

From the list of options, click on “Delete”.

![Opzione per eliminare una simulazione](assets/images/extract/media/image139.png)

After clicking the “Delete” option, a modal will appear where it is necessary to confirm the deletion of the simulation by clicking on the “Confirm” button.

After doing so, the simulation is no longer present in the table.

If, however, you do not want to confirm the deletion of the simulation, click on the “Cancel” button.

![Conferma dell'eliminazione della simulazione](assets/images/extract/media/image140.png)

### Reporting Tools

The reporting functionality, specific to features, allows generating global reports of the information available for the various providers. Within the pages, there will also be the possibility to create files to facilitate information sharing.

To access the functionality, above the breadcrumb path, click on the “Reports” tab.

![Accesso al report di Catalogo](assets/images/extract/media/image141.png)

#### Available report types

- **INVENTORY Summary** – Summary on the quantity of main inventory resources based on the selected provider/subsystem combination.

#### Report Creation

At the top right of the page, we can click on the “New Report” button to start creating a report. Specifically, a modal is displayed containing the list of available report types.

![Creazione nuovo report](assets/images/extract/media/image142.png)

Once the report type is selected, click on the “Configure” button to select the providers to include in the report. In the newly opened window, we find the “Provider” field which allows selecting one or more pre-existing providers in the system. Subsequently, it is possible to select one or more subsystems to include in the report; if no providers are selected, no subsystem can be selected. Finally, there is a “tag” section to include only resources that have the entered tag.

![Configurazione del report](assets/images/extract/media/image143.png)

At this point, the user can choose between two different actions:

- Create a static report that will be saved in the system.
- Schedule a task that generates the report periodically.

To confirm the creation of a static report, verify that “One-Shot” has been selected for the “Report type” field and click the “Submit” button at the bottom.

After a loading period, the newly generated report will be visible in the list.

![Lista dei report effettuati](assets/images/extract/media/image144.png)

##### Report Scheduling

If, instead, you want to schedule automatic report execution, it will be necessary to select “Recurring” for the “Report Type” field. In this case, the window refreshes to show additional parameters for configuring the periodic report.

The parameters to enter are:

- Period: allows selecting the report sending frequency (hourly, daily, ...).
- "Receive only if not empty" if selected, the file will not be sent when it contains no information.
- Report Language: allows selecting the language used in the report.
- File format: allows selecting one or more file types to include in the email.
- User E-mails: allows entering an email address to send reports to. After entering an an email, it is necessary to press “Enter” on the keyboard to confirm its insertion. Once pressed, the newly entered email will move to the box at the bottom, and the field will be cleared to allow the insertion of a new email, if necessary.

![Parametri dei report schedulati](assets/images/extract/media/image145.png)

Having configured all parameters, the “Submit” button will become clickable. Click it to confirm the insertion, and after a loading period, the newly generated report will be visible in the list.

![Lista dei report effettuati](assets/images/extract/media/image144.png)

##### List of scheduled reports

To view the list of scheduled reports, select the “Scheduled” tab at the top left of the reports page.

![Lista dei report schedulati](assets/images/extract/media/image146.png)

On this page, you will find the list and related information of scheduled reports present in the system. For each result, by clicking the “Three dots” button on the right, three operations can be performed:

- View the last generated report.
- Edit the schedule settings; it will not be possible to modify the selected providers or subsystems.
- Delete the schedule to stop sending emails.

![Modifica di una schedule](assets/images/extract/media/image147.png)

##### Using reports

By clicking on a static report row, or using the “Show report” button available for scheduled reports, it will be possible to view the detail page of the selected report.

Within the Inventory report summary, there is a “Stats” section showing the number of disks, interfaces, networks, and virtual machines belonging to the selected provider.

Below the “Stats” section, the filters used by the user to generate the report are present.

Below the filters, there is a summary table of resources belonging to the providers. On the right, there are two buttons: “PRINT” and “EXPORT”.

Clicking on the “PRINT” button, a print preview modal appears. To print the report, click on the “Print” button in the bottom right; at this point, the printing of the report will start.

Clicking on the “EXPORT” button, it is possible to export the report in “.csv”, “.json”, or “.pdf” format.

To return to the “Results” tab, in the bottom right, click on the “CLOSE” button or in the top left, click on the left-pointing arrow, next to the report title.

![Dettagli dei report](assets/images/extract/media/image148.png)
