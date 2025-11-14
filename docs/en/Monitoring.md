# Monitoring

The SCMP collects metrics from all cloud providers and aggregates them by macro categories.

This aggregation allows comparison between metrics from different providers.

By accessing the dashboard, we can see how this aggregation mechanism provides an overview of resource utilization, divided by provider and organized by associated resource type.

Within the functionality, it is possible to filter by resource type using the tab bar at the top, while for a general view, the dashboard can be used.

The monitoring module can be accessed via the dedicated menu. As shown in the figure:

![Access to the Monitoring Module](assets/images/extract/media/image259.png)

### Monitoring Dashboard

At this point, the user will be on the "Dashboard" monitoring tab page.

![Monitoring Dashboard](assets/images/extract/media/170325001.png)

#### Monitoring Section Filters

Within the page, a series of filters are available that can be selected simultaneously to filter the dashboard results.

The main filter is the display period, which can be found at the top right. Clicking on it will open a selection window (in yellow in the figure) where it will be possible to either enter a customized time range, using the "From" and "To" fields on the left, or select a "Smart" time range by directly clicking on the desired choice in the scrollable section on the right.

![Monitoring Time Filter](assets/images/extract/media/120325006.png)

Additionally, a series of filters are available at the top left of the page, allowing users to filter the retrieved resources. Specifically, it is possible to filter by:

- Provider type
- Subsystem name.
- Resource name (only in detailed dashboards)

 These filters allow for multiple values to be selected and can be combined to achieve the desired granularity.

![Monitoring Functionality Filters](assets/images/extract/media/170325002.png)

### Quotas Dashboard

The Quotas dashboard, available in the "Quotas" tab, allows viewing the details of consumption and related limits applied to Vcloud type subsystems.

To access it, you need to click the button at the top of the tab bar.

![Access to the Quotas section](assets/images/extract/media/170325003.png)

At this point, the user will be on the "Quotas" monitoring tab page.
At the top, we can see a filter bar, which allows filtering by provider or subsystem. Additionally, it is possible to view the filters for the chart using the "Show additional filters" button; these filters modify the chart's display.
Below the filters, there is a table indicating the subsystem name and
the quotas used, limits, and an average utilization divided by resource type.
Finally, at the bottom, a time-based chart on the selected metric in the filters can be displayed.

![Quotas Dashboard](assets/images/extract/media/170325004.png)

### Alarms on Quota Usage

To allow the user to receive notifications when quota usage thresholds are exceeded, an "Alerting" module has been included. To access it, you need to select the tab at the top of the Monitoring functionality.

![Access to the Alerting system](assets/images/extract/media/090425002.png)

Within the page, we find the list of "alerts" configured on the system, along with their respective configurations.

#### New Alert Creation

Using the menu available on the right, it is possible to add a new alert to the system.
To do this, we select the displayed "New alert" option, and a configuration page will open.

![New Alert Creation](assets/images/extract/media/090425004.png)

On the configuration page, all fields must be filled in, specifically:

- **"Alert type"**: Select the alert type
- **"Alert schedule"**: Indicates the frequency of checks to be performed
- **"Quota type"**: Select the quota type to monitor
- **"Threshold (%)"**: Enter the percentage beyond which the alert will be sent.
- **"Subsystems"**: Select one or more subsystems to monitor
- **"Alert send type"**: Select the type of alert to receive, via e-Mail or Rabbit queue (for automatic integration with other systems)
- **"Alert format"**: Select the format of the sent file that defines the alert details.
- **"Emails"**: By selecting E-mail as the notification type, we can enter an email address to send reports to. After entering an email, it is necessary to press "Enter" on the keyboard to confirm its entry. Once pressed, the newly entered email will move to the box at the bottom, and the field will be cleared to allow for the entry of a new email, if necessary.

![Configuration Page](assets/images/extract/media/090425005.png)

#### Viewing, Modifying, and Deleting an Alert

On this page, we find the list and related information of the alerts present in the system. For each result, by clicking the "Three dots" button on the right, it will be possible to perform three operations:

- View the "alert" configuration
- Edit the alert settings.
- Delete the schedule to stop sending emails.

![Alert Operations](assets/images/extract/media/090425003.png)

### Reporting Tools

The reporting functionality, specific to each feature, allows generating global reports of the information available for the various
providers. Within the pages, the possibility will also be given to create files to facilitate information sharing.
To access the functionality, above the breadcrumb path, click on the "Reports" tab.

![Access to Catalog Report](assets/images/extract/media/image141.png)

#### Available Report Types

- **Monitoring Threshold Quotas** – List of VCloud and/or Backup subsystems, integrated into the SCMP, with details of utilization quotas (CPU, Memory, Storage, Backup). Based on the selected filter combination, it is possible to filter subsystems that exceed a certain utilization threshold.

#### Report Creation

At the top right of the page, we can click the "New Report" button to start creating a report. Specifically, a modal is displayed containing the list of available report types.

![New Report Creation](assets/images/extract/media/image142.png)

Once the report type is selected, click the "Configure" button to select the providers to include in the report. In the newly opened window, we find the "Provider" field which allows selecting one or more pre-existing providers in the system. Subsequently, it is possible to select one or more subsystems to include in the report; if no providers are selected, no subsystems can be selected. Finally, there is a "tag" section to include only resources that have the entered tag.

![Report Configuration](assets/images/extract/media/image143.png)

At this point, the user can choose between two different actions:

- Create a static report that will be saved in the system.
- Schedule a job that generates the report periodically.

To confirm the creation of a static report, verify that "One-Shot" has been selected for the "Report type" field and click the "Submit" button at the bottom.
After a loading period, the newly generated report will be visible in the list.

![List of Generated Reports](assets/images/extract/media/image144.png)

##### Report Scheduling

If, on the other hand, automatic report execution is desired, it will be necessary to select "Recurring" for the "Report Type" field. In this case, the window updates to show additional parameters for configuring the periodic report.
The parameters to enter are:

- Period: allows selecting the report sending frequency (hourly, daily, ...).
- "Receive only if not empty": if selected, the file will not be sent when it contains no information.
- Report Language: allows selecting the language used in the report.
- File format: allows selecting one or more file types to include in the email.
- User E-mails: allows entering an email address to send reports to. After entering an email, it is necessary to press "Enter" on the keyboard to confirm its entry. Once pressed, the newly entered email will move to the box at the bottom, and the field will be cleared to allow for the entry of a new email, if necessary.

![Scheduled Report Parameters](assets/images/extract/media/image145.png)

Having configured all parameters, the "Submit" button will become clickable. Click it to confirm the entry, and after a loading period, the newly generated report will be visible in the list.

![List of Generated Reports](assets/images/extract/media/image144.png)

##### List of Scheduled Reports

To view the list of scheduled reports, select the "Scheduled" tab located at the top left of the reports page.

![List of Scheduled Reports](assets/images/extract/media/image146.png)

On this page, we find the list and related information of the scheduled reports present in the system. For each result, by clicking the "Three dots" button on the right, it will be possible to perform three operations:

- View the last generated report.
- Edit the schedule settings; it will not be possible to modify the selected providers or subsystems.
- Delete the schedule to stop sending emails.

![Modify a schedule](assets/images/extract/media/image147.png)

##### Report Usage

By clicking on a static report row, or by using the "Show report" button available for scheduled reports, it will be possible to view the detail page of the selected report.
Within the Inventory report summary, there is a "Stats" section which includes the number of disks, interfaces, networks, and virtual machines belonging to the selected provider.
Below the "Stats" section, there are the filters used by the user to generate the report.
Below the filters, there is a summary table of resources belonging to the providers. On the right, there are two buttons: "PRINT" and "EXPORT".
Clicking the "PRINT" button will display a print preview modal. To print the report, click the "Print" button at the bottom right; at this point, the printing of the report will start.
Clicking the "EXPORT" button allows exporting the report in ".csv", ".json", or ".pdf" format.
To return to the "Results" tab, click the "CLOSE" button at the bottom right, or click the left-pointing arrow at the top left, next to the report title.

![Report Details](assets/images/extract/media/image148.png)
