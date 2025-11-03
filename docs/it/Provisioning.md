# Provisioning

Provisioning is one of the most important functionalities of SCMP. Through these modules, it is possible to allocate runtime assets within the providers managed by SCMP.

To use this functionality, relations must be defined within the SCMP.

This constraint was made available to bind certain characteristics to provisioning; for example, the VM size is not selectable during provisioning but is among the predefined characteristics by administrators within the catalog.

![Access to "Provisioning"](images/extract/media/image6.png)

### Dashboard

Accessing the functionality, the first available page is the Dashboard of provisionings carried out within the system.

The page presents a series of graphs, filters, and the list of provisionings performed.

The graphs allow visualizing the information present in the table, grouped by:

- The total of all provisionings carried out, divided by type.
- The status of provisionings carried out, divided by outcome and category of the provisioned asset.

![Provisioning page graphs](images/extract/media/image282.png)

At the bottom of the page, we can use the filters section to modify the results present in the table. The "Provisioning Type" filter is the main filter that allows selecting the type of asset to display, specifically:

- Selecting "Resources" adds a filter that allows selecting the type of resource for which you want to display the provisioning status. By default, the system shows the list of provisioned VMs.
- Selecting "Services" and "Custom services" has no additional filters, and the list is updated with only provisionings related to Services.
- Selecting "Blueprint" adds a filter that allows changing the flow (i.e., the type of blueprint to display), and the table is modified to show only flows not yet completed. Above the table, there is a control that allows changing tabs, to switch from "in progress" flows to "Completed" flows.

![Filter by asset type](images/extract/media/image283.png)

### Provisioning Table Specifications

#### "Resources", "Services", "Custom Services"

The list has the following attributes when "Resources", "Services", "Custom Services" is selected as a filter:

- Uuid, Provisioning identifier;
- Provisioning completion date;
- Provisioning request date;
- User who created the instance;
- Status;
- Output of provisioning systems;
- Detailed provisioning Json;
- Status information;
- Resource type.

![“Resources” Table](images/extract/media/image284.png)

When in this view, the following operations can be performed:

- By clicking on the row of a failed provisioning, it is possible to modify and re-execute it.
- By clicking on the "Output Message" icon corresponding to a provisioning, it is possible to view the response received from the "Terraform" module.
- By clicking the "Download" button, it is possible to download the files returned by the functionality.
- By clicking the "State" button, it is possible to view the graph and the list of provisioned resources.

![Terraform message visualization](images/extract/media/image285.png)

![Resource graph visualization](images/extract/media/image286.png)

#### Auto uninstall of HELM services

When we select "Custom services" as a filter type, we can notice a new "Uninstall" button displayed with a "Stop" icon.

![Uninstall HELM service](images/extract/media/20250605001.png)

Clicking the button will ask for confirmation of deletion. Upon confirmation, SCMP will delete all HELM resources deployed in the indicated namespace.

![Uninstall confirmation](images/extract/media/20250605002.png)

#### Blueprint

The list has the following attributes when "Blueprint" is selected as a filter:

- Blueprint Name
- Creation Date
- User who provisioned the blueprint

Above the table, we can notice two tabs. By clicking on them, the table is filtered respectively for Blueprints to be completed and Completed Blueprints (in red in the image).

![“Provisioning blueprint” table tabs](images/extract/media/image287.png)

In this view, it is possible to click on a table row to view the blueprint details.

When the selected blueprint is "to be completed," we will be redirected to the blueprint provisioning page where we can perform the necessary operations for completion.

![“To be completed” flow visualization](images/extract/media/image288.png)

If a completed blueprint is selected instead, we will be redirected to the blueprint provisioning details page where the prediction "flow" will not be displayed because it has already been completed.

![“Completed” flow visualization](images/extract/media/image289.png)

### Creation of Provisionings

#### Provisioning of "Physical Resources"

Using the tabs in the provisioning functionality, it is possible to view the lists of provisionable resources within the SCMP, such as Virtual Machines, Storage, and Kubernetes.

To view elements within the result lists, it is necessary that a relation exists in the SCMP catalog with the catalog resource of the provider to be provisioned.

The functionalities available for these elements are identical; only the parameters to be entered in the creation steps change.

![Tabs for resource creation](images/extract/media/image290.png)

##### Virtual Machines

To start provisioning a resource, click on the corresponding row to view the page containing step 1 of provisioning creation. In this step, it is necessary to select, using the dropdown on the left, the "target" subsystem where the resources are to be provisioned. Once selected, an information mirror will be displayed on the right indicating the characteristics of the resource that will be provisioned. To continue, click the "Next" button at the bottom right to go to step 2 "Config" page.

![Selection of the “target” subsystem, provisioning step 1](images/extract/media/image291.png)

On the "Config" page of step 2, fill in all mandatory fields in all sections of the form. At the bottom left, click the "Reset" button to reset all fields on the page.

Instead, on the right, click the "Submit" button to go to step 3 "Plan".

![](images/extract/media/image292.png)
![Filling in the resource prediction form fields](images/extract/media/image293.png)

After clicking the "Submit" button, the user is redirected to the "Plan" page of step 3 where we can view the provisioning plan sent by Terraform, which indicates all the parameters of the resources that will be configured, and at the bottom, there is a list with a cost perspective.

![Forecast screen](images/extract/media/image294.png)

Still from the "Plan" page of step 3, at the bottom right, there are three buttons: "Back", "Reset", and "Apply". If you click the "Back" button, the user returns to the "Config" page of step 2 where parameters can be modified.

If you click the "Reset" button, the user is redirected to the "Subscription" page of step 1 where it is necessary to select a subsystem, and then enter the parameters on the "Config" page of step 2.

Finally, if you click the "Apply" button, the forecast is saved, and the user is redirected to the "Dashboard" tab page where the user verifies the presence of the newly created forecast.

![List of provisionings performed](images/extract/media/image295.png)

#### Provisioning of "Services"

To access the services page, click on the tab that depicts a shelf located in the top menu. After doing this, you will find yourself on the "Service" page.

![List of cards](images/extract/media/image296.png)

On the page, a list of components called "Card" is displayed. Each card refers to a specific type of service; in particular, the following information is displayed:

- Service name;
- Service icon;
- Type of script used for service provisioning;
- Service description;
- "Subscribe" button to proceed with service creation.

Depending on the type of service selected, the steps for provisioning change; these will be analyzed in detail below.

##### "Standard" Services

Click the "Subscribe" button corresponding to a "standard" service. The user will be redirected to step 1 of the service creation page, and all instantiable versions of the service by SCMP will be displayed. In particular, various blocks will be shown, each with a list of configurations:

- Name and version of the service that will be instantiated.
- Name and version of the operating system that will be installed on the machine.
- Belonging provider on which the service will be provisioned.

![Provisioning of a "standard" service](images/extract/media/image297.png)

Select a software version and press the "Continue" button; the user is redirected to step 2 of service provisioning.

In step 2, it will be necessary to select a subsystem and fill out the form with the details of the chosen subsystem.

![Configuration of a "standard" service](images/extract/media/image298.png)

After completing all the form fields, click "Submit".

A request will be sent to the Terraform service, which will validate the activation configuration of the indicated flow and return the result.

![Service configuration summary](images/extract/media/image299.png)

Click "Apply" to validate the flow and activate the service subscription.

The dashboard page will open with the list of all subscribed services and their relative statuses. Specifically, the newly provisioned service will have a "Running" status in yellow, and subsequently, depending on the result, the status will also be updated to "Completed" in green or "Error" in red.

![Dashboard with the list of all subscribed services and their relative statuses](images/extract/media/image300.png)

##### "Custom" Services

Click the "Subscribe" button corresponding to a "custom" service. The user will be redirected to step 1 of the service creation page where the subsystem can be selected, in which to perform the provisioning, from the dropdown in the center of the page.

![Provisioning of a “Custom” service](images/extract/media/image301.png)

By selecting the subsystem, the page updates to proceed to step 2 of service provisioning.

In this step 2, it will be necessary to fill out the form with the specific configuration parameters of the selected service.

![Configuration of a "custom" service](images/extract/media/image298.png)

After completing all the form fields, click "Launch".

A request will be sent to the Terraform service, which will validate the activation configuration of the indicated flow and return the result.

![Service configuration summary](images/extract/media/image299.png)

Click "Apply" to validate the flow and start the automatic configuration operations.

The dashboard page will open with the list of all subscribed services and their relative statuses.

Specifically, the newly provisioned service will have a "Running" status in yellow, and subsequently, depending on the result, the status will also be updated to "Completed" in green or "Error" in red.

![Dashboard with the list of all subscribed services and their relative statuses](images/extract/media/image300.png)

##### "Azure Pipeline" Services

Click the "Subscribe" button corresponding to an "Azure Pipeline" service. The user will be redirected to step 1 of the service creation page. From the dropdown in the center of the page, select the "Branch" of the pipeline to execute.

![Provisioning of an "Azure pipeline" service](images/extract/media/image302.png)

By selecting the branch, the page updates to proceed to step 2 of service creation.

In this step 2, it will be necessary to fill out the form with the configuration parameters retrieved directly from the Pipeline that will be executed.

![Configuration of an "Azure pipeline" service](images/extract/media/image303.png)

After completing all the form fields, click "Launch" to send the pipeline start request. The dashboard page will open with the list of all subscribed services and their relative statuses.

Specifically, the newly provisioned service will have a "Running" status in yellow, and subsequently, depending on the result, the status will also be updated to "Completed" in green or "Error" in red.

![Dashboard with the list of all subscribed services and their relative statuses](images/extract/media/image300.png)

##### "PaaS" and "AI Services"

Click the "Subscribe" button corresponding to a "PaaS" service. The user will be redirected to step 1 of the service creation page where it will be necessary to fill out the form with the specific configuration parameters of the selected service.

![Configuration of a "PaaS" service](images/extract/media/image304.png)

After completing all the form fields, click "Launch".

The dashboard page will open with the list of all subscribed services and their relative statuses.

Specifically, the newly provisioned service will have a "Running" status in yellow, and subsequently, depending on the result, the status will also be updated to "Completed" in green or "Error" in red.

![Dashboard with the list of all subscribed services and their relative statuses](images/extract/media/image300.png)

##### "HELM" Services

Click the "Subscribe" button corresponding to a "HELM" service. The user will be redirected to step 1 of the service creation page where it will be necessary to select the cluster on which to perform the provisioning.

![Cluster selection](images/extract/media/image305.png)

Fill out the form with the specific configuration parameters of the selected service. Also, add the "values.yaml" file at the bottom, which contains all the configuration parameters necessary for the service.

![Configuration of "HELM" parameters](images/extract/media/image306.png)

After completing all the form fields, click "Launch".

The dashboard page will open with the list of all subscribed services and their relative statuses.

Specifically, the newly provisioned service will have a "Running" status in yellow, and subsequently, depending on the result, the status will also be updated to "Completed" in green or "Error" in red.

![Dashboard with the list of all subscribed services and their relative statuses](images/extract/media/image300.png)

##### "Immutable" HELM Services

If the "immutable" flag was selected for the HELM service during creation, the user is not given the option to view and modify the service information, thus allowing for a "one-Click" installation.
Once "subscribe" is selected, the system automatically begins provisioning and returns the user to the dashboard page to monitor the results.

![Dashboard with the list of all subscribed services and their relative statuses](images/extract/media/image300.png)

#### Provisioning of "Edge" device images

To access the "Edge" provisioning page, click on the tab of the same name in the top menu.

After doing this, we will be taken to the "Edge" page of the provisioning module.

![Access to Edge provisioning](images/extract/media/image307.png)

At first glance, the page may appear empty, but by selecting a configured EDGE subsystem from the "Subsystem" filter, all available images in the subsystem will be displayed below.

![Images available in the system](images/extract/media/image308.png)

By selecting one of the available images, a section will open on the right that allows selecting a compatible inventory machine from the list.

After selecting a machine, we can confirm the operation using the "Apply" button.

We will be returned to the "dashboard" section of the "Provisioning" module where we can view the outcome of the operations.

![Confirmation of "Edge" provisioning](images/extract/media/image309.png)

#### Creation of a "Blueprint" provisioning request

To access the services page, click on the "blueprint" tab in the top menu. After doing this, you will find yourself on the "Blueprints" page.

On the page, a list of components called "Card" is displayed. Each card refers to a specific type of service; in particular, the following information is displayed:

- Service name.
- Service icon.
- Type of script used for service provisioning.
- Service description.
- "Subscribe" button to proceed with service creation.

Depending on the blueprint selected, the parameters for provisioning change, while the functionalities remain unchanged.

![List of blueprints](images/extract/media/image296.png)

##### "Blueprint" execution request

Click the "Subscribe" button corresponding to a "Blueprint". The user will be redirected to step 1 of the creation page. In this step, it is necessary to select the subsystem in which provisioning is to be performed from the dropdown.

![Step 1 of Blueprint creation](images/extract/media/image310.png)

By selecting a subsystem, the page will move to step 2 of creation where it will be necessary to fill out the form with the specific configuration parameters of the selected blueprint.

![Step 2 of "Blueprint" creation](images/extract/media/image311.png)

Once the parameters have been entered, you can click the "Start" button at the bottom right to initiate provisioning. After a few seconds, you will be redirected to the "Dashboard" page, filtered for "Blueprints to be completed".

![Blueprint Request sent successfully](images/extract/media/image312.png)

##### "To be completed" blueprint management page

To work on the blueprint, it is necessary to select a "to be completed" blueprint from the dashboard. Clicking on the corresponding row will display its management page.

This page is divided into sections, specifically:

- "Process Diagram": This section displays an image that graphically represents all the steps to be executed in the blueprint. Additionally, the step currently in execution is indicated in red.
- "Variables": In this section, we can view all parameters entered manually or automatically during the blueprint execution.
- "Task": In this section, it is possible to manage the blueprint steps that require manual intervention using the available controls.
- "Subprocess": In this section, we can view the status of all automatic operations performed during the blueprint execution.

![Provisioning plan flow](images/extract/media/image313.png)

The execution, and therefore the corresponding change, between the Blueprint steps can be carried out in two ways: automatically or manually, exactly as described within the Blueprint itself.

###### Automatic steps

The system automatically manages the creation, configuration of resources, and deployment of applications. The status and result of these steps are visible in the "Subprocess" section below.

For each row in the table, by clicking the buttons on the right, it is possible to verify the generated output message and download its content.

![Blueprint subprocesses section](images/extract/media/image314.png)

###### Manual steps

Manual tasks, when present and required in the blueprint, will appear in the relevant section. To work on it, it is first necessary to click the "Assign" button (red in the figure) to take charge of the task.

![Task assignment to the user](images/extract/media/image315.png)

A confirmation modal for assignment will be displayed. By clicking "Yes", the task will be taken over by the user and cannot be worked on by a different user.

![Assignment confirmation](images/extract/media/image316.png)

A confirmation message will appear at the bottom, and we can note that the "Task" section has been updated. On the left, below the task name, the relevant assignee is indicated, and on the right, there are 2 buttons:

- "Remove assignment" (red in the figure).
- "Complete manual task" (yellow in the figure).

![Task management buttons](images/extract/media/image317.png)

Clicking "Remove assignment" will open a confirmation modal. Clicking "Yes" will make the task available to other users who can take charge of it.

![Task release](images/extract/media/image318.png)

Clicking the "Complete task" button will open a modal containing one or more customizable fields. The fields can be of different types.

We can enter numeric, boolean, and text fields. Once entered, it is possible to confirm by clicking the "Continue" button at the bottom right.

![Numeric fields of blueprints](images/extract/media/image319.png)

![Text fields in Blueprints](images/extract/media/image320.png)

Once pressed, we can see that the BPMN graph on the page has been updated and that the next step of the blueprint is active and has a red outline.

![Next step](images/extract/media/image321.png)

All manual tasks present in the blueprint will follow the procedure described previously; therefore, regardless of the type of data to be entered, it is always necessary to assign the task to oneself.

It is possible to insert a temporal field within the manual steps of blueprints, using a calendar it will be possible to manually select the correct day and time.

![Date field in tasks](images/extract/media/image322.png)

The last type of step that we can find within the blueprints is the "Multi-choice" field. This field allows managing the blueprint's flow.

![Multi-choice field](images/extract/media/image323.png)

This field is of "Selection" type, so it will not be possible to enter a custom value, but selectable options will be proposed. Specifically, we can find three choices:

- "Repeat": allows re-executing the previous steps as described in the blueprint (path in pink in the figure).
- "End": allows concluding the blueprint execution without performing further operations (path in yellow in the figure).
- "Insert date": allows moving to a subsequent step of the blueprint (path in green in the figure).

![Multi-choice field values](images/extract/media/image324.png)

![Possible state changes for Multi-choice](images/extract/media/image325.png)

Once all blueprint steps are completed, the graph will be automatically removed from the page, and in the step section, it will no longer be possible to take charge of an operation. Furthermore, in the "sub-processes" section, we will be able to view the result of all automated steps in the blueprint.

![Blueprint completion](images/extract/media/image326.png)

#### Modification of a performed provisioning

For a provisioning that has been carried out and has failed, it is possible to modify it.

Provisioning modification is only available for resource types.

To start modifying a provisioning, click on a failed forecast.

![Start modification of a Provisioning](images/extract/media/image327.png)

After doing so, you will find yourself on the "Config" page of step 2 where you can modify the previously entered parameters.

![Configuration parameters](images/extract/media/image328.png)

![Modification of parameters](images/extract/media/image329.png)

After modifying the necessary parameters, at the bottom right, click the "Submit" button.

By doing so, you will find yourself on the "Plan" page of step 3, where the forecast is present, and below, the quote table.

At the bottom right, click the "Apply" button. After clicking the "Apply" button, you will find yourself on the "Dashboard" tab page.

Subsequently, from the "Dashboard" page, the user notes that the modification was successful.

It is also possible to modify a failed provisioning for other elements managed by SCMP.

![Provisioning summary and quote table](images/extract/media/image330.png)
