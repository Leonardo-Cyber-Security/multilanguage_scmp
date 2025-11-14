# Cost and Usages

SCMP collects, through the APIs made available by the providers, the cost details of inventory assets.

In the event that providers do not expose cost data, this data can be editorially entered into the catalog so that it can then be counted within this functionality.

Costs are collected with a breakdown by daily cost and by resource. Subsequently, as with the metrics section, the data is normalized and aggregated to allow for a uniform dashboard visualization.

!!! danger "Attention"
    As also indicated on the cost dashboards, data related to the last 48 hours has not yet been confirmed by the respective providers. We can use this table as a reference, but for details, it is necessary to check the specific provider's documentation.

For example:

| **Cloud Provider** | **Tool/Method** | **Update Times** | **Notes** |
|----|----|----|----|
| Azure | Cost using export file | 6/7 days | in the first 6 days of the following month, the costs of the previous month are consolidated |
| Azure | Cost Management | 8-24 hours | Consolidated data updated within 24/48 hours; greater delay compared to others. |
| Google Cloud | Billing Dashboard | A few hours, maximum 24 hours | Near real-time updates; consolidation up to 24 hours. |
| Google Cloud | BigQuery Export | Every hour | Minimum delay for advanced analysis via BigQuery. |
| Oracle Cloud | Cost Analysis | 4-6 hours, maximum 24 hours | some services may have greater delays. |
| AWS | Cost Explorer | 8-24 hours | Aggregated data updated within 12-24 hours. |
| AWS | Cost and Usage Reports (CUR) | 8-24 hours | Detailed reports with similar delay. |
| AWS | CloudWatch Metrics (Billing) | Every 6 hours | Near real-time monitoring. |
| AWS | Budget Alerts | 3-5 hours | Rapid notifications when budget thresholds are exceeded. |

### Cost Dashboard

To access the cost section, use the menu as shown in the figure.

![Access to Costs](assets/images/extract/media/image238.png)

At this point, the user will find themselves within the "Dashboard" tab page of costs.
On this screen, we can note in order:

- The "Cost trend" value, which indicates the total costs for the selected period.
- The "Cost difference" value, which indicates the markup applied in the selected period.
- A "Cloud provider Spend" bar chart, which indicates the cost billed to the client for each provider in the selected period.
- An "Effective Spend" bar chart, which indicates the effective cost of resources on the provider.

 At the bottom, there will be several resource aggregation charts, for example, by Region or Service Type, as indicated by the respective cloud providers, and as we will analyze later, it will be possible to customize the available charts and sections.

![Cost Dashboard](assets/images/extract/media/image239.png)

In the cost functionality, it is possible to filter by resource type using the tab bar at the top, while for a general view, the dashboard can be used.

![Filter by resource type](assets/images/extract/media/image240.png)

#### Cost Section Filters

Within the page, a series of filters are available that can be selected simultaneously to filter the dashboard results.

The main filter is the display period, which can be found in the upper right. Clicking on it will open a selection window (in yellow in the figure) where it will be possible to either enter a custom time range, using the "From" and "To" fields on the left, or select a "smart" time range by clicking directly on the desired choice in the scrollable section on the right.

![Cost time filter](assets/images/extract/media/image241.png)

A series of filters are available in the upper left of the page, allowing you to filter the retrieved resources. Specifically, you can filter by:

- Tag
- Provider type
- Subsystem name.

 These filters allow multiple values to be selected and can be combined to achieve the desired granularity

![Cost functionality filters](assets/images/extract/media/image242.png)

#### Overview of the data shown

##### "General" Section

In the first section, summary charts representing provider and SCMP costs are shown to the user based on the applied filters.

In detail:

- **Provider Cost Difference:** chart containing the cost difference between the sum of the original provider costs and the sum of the costs agreed upon with the provider.  
  *Useful for identifying savings obtained through negotiation or resale compared to list prices.*

- **Customer Cost Difference:** chart containing the cost difference between the sum of SCMP costs charged to the customer and the sum of the original provider costs.  
  *Used to monitor profit margins and the competitiveness of prices offered to the customer.*

- **Customer Cost Trend:** chart containing the total SCMP costs charged to the customer, with the respective profit/loss percentage.  
  *Allows observing economic trends over time and detecting cost peaks or anomalies.*

- **Provider Spend:** chart containing the sum of original costs for each provider.  
  *Allows identifying which providers the spending is concentrated on and the level of dependency.*

- **Provider Agreement Spend:** chart containing the sum of agreed costs for each provider.  
  *Useful for comparing the effectiveness of commercial agreements with each provider.*

- **Effective Spend:** chart containing the sum of SCMP costs charged to the customer for each provider.  
  *Helps evaluate the profitability obtained from each provider.*

![General](assets/images/extract/media/image243.png)

##### **"Accounts" Section**

In the second section, charts focused on the costs generated by each subordinate account of each provider are shown to the user.

In detail:

- **Sub-Account Provider Cost %:** Percentage of the total provider cost, for each account.  
  *Used to identify the most expensive accounts and analyze the distributed economic load.*

- **Sub-Account Provider Agreement Cost %:** Percentage of the total agreed provider cost, for each subordinate account.  
  *Useful for checking which accounts benefit from more significant discounts.*

- **Sub-Account Effective Cost %:** Percentage of the total SCMP cost charged to the customer, for each subordinate account.  
  *Allows seeing which accounts generate more revenue.*

![Accounts](assets/images/extract/media/image244.png)

##### **"Services" Section**

In the third section, charts focused on the costs generated by each cloud service of each provider are shown to the user.

In detail:

- **Service Provider Cost %:** Percentage of the total provider cost, for each service.  
  *Allows understanding which services (e.g., compute, storage, network) have the most impact on costs.*

- **Service Provider Agreement Cost %:** Percentage of the total agreed provider cost, for each service.  
  *Useful for analyzing the effectiveness of negotiations on various services.*

- **Service Effective Cost %:** Percentage of the total SCMP cost charged to the customer, for each service.  
  *Provides a clear view of the main revenue sources per service.*

![Services](assets/images/extract/media/image245.png)

##### **"SKUs" Section**

In the fourth section, charts focused on the costs generated by each SKU of each provider are shown to the user.

In detail:

- **Sku Provider Cost %:** Percentage of the total provider cost, for each SKU.  
  *Allows detailed cost analysis at the billing unit level.*

- **Sku Provider Agreement Cost %:** Percentage of the total agreed provider cost, for each SKU.  
  *Useful for evaluating whether individual SKUs also benefit from discounts and optimizations.*

- **Sku Effective Cost %:** Percentage of the total SCMP cost charged to the customer, for each SKU.  
  *Helps highlight any imbalances in margins at the SKU level.*

![Skus](assets/images/extract/media/image246.png)

##### **"Resources" Section**

In the fifth section, charts focused on the costs generated by each resource of each provider are shown to the user.

In detail:

- **Resource Provider Cost %:** Percentage of the total provider cost, for each resource.  
  *Allows the identification of particularly expensive or underutilized resources.*

- **Resource Provider Agreement Cost %:** Percentage of the total agreed provider cost, for each resource.  
  *Allows seeing if discounts are distributed equally among resources.*

- **Resource Effective Cost %:** Percentage of the total SCMP cost charged to the customer, for each resource.  
  *Provides visibility into the profitability of individual resources.*

![Resources](assets/images/extract/media/image247.png)

##### **"Types" Section**

In the sixth section, charts focused on the costs generated by each inventory resource type of each provider are shown to the user.

In detail:

- **Resource Type Provider Cost %:** Percentage of the total provider cost, for each resource type.  
  *Offers an aggregated view useful for cost planning.*

- **Resource Type Provider Agreement Cost %:** Percentage of the total agreed provider cost, for each resource type.  
  *Helps understand which types are most optimized through agreements.*

- **Resource Type Effective Cost %:** Percentage of the total SCMP cost charged to the customer, for each resource type.  
  *Allows measuring the commercial weight of each category.*

![Types](assets/images/extract/media/image248.png)

##### **"Regions" Section**

In the seventh section, charts focused on the costs generated in each region of each provider are shown to the user.

In detail:

- **Regional Provider Cost %:** Percentage of the total provider cost, for each region.  
  *Indicates where resources are geographically located and their associated expenses.*

- **Regional Provider Agreement Cost %:** Percentage of the total agreed provider cost, for each region.  
  *Allows evaluating the convenience of chosen regions based on discounts.*

- **Regional Effective Cost %:** Percentage of the total SCMP cost charged to the customer, for each region.  
  *Useful for analyzing the distribution of revenue by geographical area.*

![Regions](assets/images/extract/media/image249.png)

##### **"History" Section**

Finally, in the eighth section, charts focused on the historical costs of each billing account, generated by each subsystem integrated into the SCMP, are shown to the user.

In detail:

- **System Costs Details:** Comparison between the total provider cost, the total agreed provider cost, and the total customer cost, for all subsystems integrated into the SCMP.  
  *Fundamental for retrospective analysis and for evaluating the economic sustainability of the system.*

- **Historical Provider Billing Costs:** History of the trend of total costs for each cloud billing account.  
  *Helps predict future trends and anticipate spending or budget issues.*

![History](assets/images/extract/media/image250.png)

#### Limited view for the customer

If a user configured with the "LIMITED" parameter is used to access the cost dashboard, the charts available on the dashboard will only relate to the recalculated SCMP costs, while the actual costs received from the providers will not be visible as they are superfluous, as can be seen in the image.

![Limited cost dashboard](assets/images/extract/media/image251.png)

### "Usage" Dashboard

In addition to the main cost dashboard and its related detailed dashboards by resource type, in the SCMP Costs module, the user can view an additional dashboard, focused on the consumption of inventory resources integrated into the platform.

By navigating to the Usages section of the module, generic and detailed information on the consumption of individual integrated services/SKUs and their respective resources will be shown.

To access the functionality, above the breadcrumb path, click on the "Usages" tab.

![Access to "Usages"](assets/images/extract/media/image252.png)

#### Usage section filters

Within the page, a series of filters are available that can be selected simultaneously to filter the dashboard results.

The main filter is the display period, which can be found in the upper right. Clicking on it will open a selection window (in yellow in the figure) where it will be possible to either enter a custom time range, using the "From" and "To" fields on the left, or select a "smart" time range by clicking directly on the desired choice in the scrollable section on the right.

![Usage time filter](assets/images/extract/media/image241.png)

A series of filters are available in the upper left of the page, allowing you to filter the retrieved resources. Specifically, you can filter by:

- Tag
- Provider type
- Subsystem name.
- Resource type
- Cloud service name
- Cloud SKU name

These filters allow multiple values to be selected and can be combined to achieve the desired granularity.

![Cost functionality filters](assets/images/extract/media/image242.png)

#### Overview of the data shown in the costs section

##### "SKUs Usage Average" Section

The first chart represents the daily average consumed by each SKU.
It is a summary chart that shows the user the general trend of consumption.

For each SKU, in fact, the average consumption and the unit of measure are indicated, within the specified time range, to briefly show which of them are, on average, most used and consequently which of them could generate higher costs for the user.

![ "SKUs Usage" Section](assets/images/extract/media/image253.png)

##### "SKU Resource Average" Section

The second chart, on the other hand, is focused on the SKU selected as a filter by the user and shows the daily average consumed by each resource, correlated to the specific SKU.

It too can be classified as a summary chart that provides the user with which resources for a given SKU are, on average, most used and consequently which of them could generate higher costs for the user.

![ "SKU resource" Section](assets/images/extract/media/image253.png)

##### "Historical SKU Usage" Section

The first temporal chart shows the daily consumption trend of the specific SKU, selected as a filter in the dashboard.

In the case shown, a constant consumption (in hours) over time is highlighted, useful for the user for subsequent analysis phases.

![ "Historical SKU" Section](assets/images/extract/media/image254.png)

##### "SKU Resources Usage" Section

The second temporal chart, on the other hand, shows the daily consumption trend of the specific SKU, for each resource related to it.

This chart, therefore, shows the user the historical detail of the previous chart, highlighting which resources are involved in the consumption of the specific SKU and to what extent.

This last chart is particularly useful to the user because it highlights which resources are actually used within a specific SKU and, consequently, which of them could lead to higher costs for the user or be paid for without even being used.

![ "SKU Resources" Section](assets/images/extract/media/image255.png)

### Cost and Usage dashboard customization

For dashboard customization, please consult the [official guide](https://grafana.com/docs/grafana/latest/)

### Reporting Tools

The reporting functionality, specific per feature, allows generating global reports of the information available for the various
providers. Within the pages, the possibility to create files to facilitate information sharing will also be provided.

To access the functionality, above the breadcrumb path, click on the "Reports" tab

![Access to Catalog report](assets/images/extract/media/image141.png)

#### Available report types

- **Cost Summary** – Summary of total cost per service, based on the selected filter combination.
- **Cost Summary – Group by Resource Type** – Summary of total cost per service, with an indication of the number of resources involved, based on the selected filter combination.
- Cost Details – Detail of daily regional cost per resource, based on the selected filter combination.
- **Cost Details – Group by Resource Type** – Detail of total daily cost per service, with an indication of the number of resources involved, based on the selected filter combination.
- **FinOps Report** – Summary of total costs and total resource usage according to the FinOps FOCUS standard, for financial optimization of cloud services, based on the selected filter combination.

#### Creating a report

In the upper right of the page, we can click on the "New Report" button to start creating a report. Specifically, a modal window appears containing the list of available report types.

![New report creation](assets/images/extract/media/image142.png)

Once the report type is selected, click on the “Configure” button to select the providers to include in the report. In the newly opened window, you will find the “Provider” field, which allows you to select one or more pre-existing providers in the system. Subsequently, it is possible to select one or more subsystems to include in the report; if no providers are selected, no subsystem can be selected. Finally, there is a “tag” section to include only resources that have the entered tag.

![Report configuration](assets/images/extract/media/image143.png)

At this point, the user can choose between two different actions:

- Create a static report that will be saved in the system.
- Schedule a job that generates the report periodically.

To confirm the creation of a static report, verify that "One-Shot" has been selected for the "Report type" field and click the "Submit" button at the bottom.

After a loading period, the newly generated report will be visible in the list.

![List of generated reports](assets/images/extract/media/image144.png)

##### Report Scheduling

If, instead, you want to schedule automatic report execution, you will need to select “Recurring” for the “Report Type” field. In this case, the window updates to show additional parameters for configuring the periodic report.

The parameters to enter are:

- Period: allows selecting the report sending frequency (hourly, daily, ...).
- "Receive only if not empty" if selected, the file will not be sent when no information is present inside
- Report Language: allows selecting the language used in the report.
- File format: allows selecting one or more file types to include in the email.
- User E-mails: allows entering an email address to send reports to. After entering an email, it is necessary to press “Enter” on the keyboard to confirm its insertion. Once pressed, the newly entered email will move to the bottom box, and the field will be cleared to allow the insertion, if necessary, of a new email.

![Scheduled report parameters](assets/images/extract/media/image145.png)

Having configured all parameters, the “Submit” button will become clickable. Click it to confirm the insertion, and after a loading period, the newly generated report will be visible in the list.

![List of generated reports](assets/images/extract/media/image144.png)

##### List of Scheduled Reports

To view the list of scheduled reports, select the “Scheduled” tab located at the top left of the reports page.

![List of scheduled reports](assets/images/extract/media/image146.png)

On this page, you will find the list and related information of the scheduled reports present in the system. For each result, by clicking the “Three dots” button on the right, three operations can be performed:

- View the last generated report.
- Edit the schedule settings; it will not be possible to modify the selected providers or subsystems.
- Delete the schedule to stop sending emails.

![Editing a schedule](assets/images/extract/media/image147.png)

##### Report Usage

By clicking on the row of a static report, or using the “Show report” button available for scheduled reports, you will be able to view the detail page of the selected report.

Within the Inventory report summary, there is a "Stats" section which includes the number of disks, interfaces, networks, and virtual machines belonging to the selected provider.

Below the “Stats” section, there are the filters used by the user to generate the report.

Below the filters, there is a summary table of resources belonging to the providers. On the right, there are two buttons: “PRINT” and “EXPORT”.

Clicking the “PRINT” button brings up a print preview modal. To print the report, click the “Stampa” (Print) button in the lower right; at this point, the printing of the aforementioned will start.

Clicking the “EXPORT” button allows exporting the report in “.csv”, “.json” or “.pdf” format.

To return to the “Results” tab, click the “CLOSE” button in the lower right, or click the left-pointing arrow in the upper left, next to the report title.

![Report details](assets/images/extract/media/image148.png)
