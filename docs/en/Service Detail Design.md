# Service Detail Design

The Service Detail Design service is the solution implemented for managing requests, which must then be processed within our environment by an authorized user.

To access Service Detail Design, log in to SCMP with the Service Manager user.

After logging in, click the "Service Detail Design" module from the bento button.

![Access to Service Detail Design module](images/extract/media/image339.png)

The search page will be shown where it is possible to filter already created work orders based on:

- Status
- Customer
- Service Type
- Phase
- Creation Date

The table will show the general information of the Work Order.

![Service Detail Design functionality filters](images/extract/media/image340.png)

Click the center of a work order row to view its content; a modal will open where we can expand the various sections by clicking on them.

To exit the detail view, click outside the gray window.

![Work Order Details](images/extract/media/image341.png)

### Work Order Flow

To take charge of a work order, click the "Play" symbol next to an order in "New" status.

A status change notification will be displayed on the screen, and the current status of the Order becomes "In progress"; the buttons of the corresponding order are modified:

- by clicking the “Pause” button, the order will transition to “Idle” status;
- by clicking the “Mark as completed” button, it is possible to close the Work Order;
- by clicking the “Rejected” button, it is possible to report the cancellation of the Order;

![Work order management page for Service Detail Design](images/extract/media/image342.png)

When the “Mark as completed” button is clicked, a window is displayed on the screen where information to be attached to the order can be entered, specifically:

- the result of the processing;
- a description of the chosen result;
- a note for the operator.

![Closing a Work order](images/extract/media/image343.png)

By scrolling down the page, we can find the parameters section where it is possible to enter different key/value combinations for the parameters used during processing.

After entering the key and value, click the “Plus” button to confirm the entry; new empty fields are added where additional parameters can be entered. To delete a key/value pair, click the “Minus” button; once all parameters have been entered, click the “Finish” button.

![Parameter entry](images/extract/media/image344.png)

After completing the order, it is possible, by opening the respective menus, to view all the information entered during processing within the info section.

![Information added during processing](images/extract/media/image345.png)
