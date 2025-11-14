# Authentication

The "Authentication" functionality allows interaction with the IAM to modify user profiling.

For preliminary configurations, refer to the specifications indicated in document DI-IPSC-81443, included in the reference documents table.

The menu is accessible from the button at the top right, as shown below.

Specifically, to access user profiling, the menu is "Authentication".

![Access to Authentication functionality](assets/images/extract/media/image8.png)

Dashboard view for user profiling:

![IAM Dashboard](assets/images/extract/media/image10.png)

### Groups

To simplify the assignment of menu attributes and authorizations, user groups can be used. Click the "Groups" menu in the "Entities" section of the IAM dashboard.

![Access to Group management](assets/images/extract/media/image11.png)

Once the link is clicked, the user will be shown the list of all available groups on the portal with their respective configuration buttons.

![List of configured groups](assets/images/extract/media/image12.png)

#### Group Creation

To create a new group within the system, click the "+" button in the top right. A group creation form will be displayed.

![Adding a new Group](assets/images/extract/media/image13.png)

Enter the group name and click the "Add Group" button to add it to the system. Once pressed, the system will take us to the list of available groups where we can find the newly created group.

![Group entry parameters](assets/images/extract/media/image14.png)

#### Management of Assigned Users and Attributes

To assign users to a group, from the list of available groups, click the "people" icon on the row corresponding to the group of interest. The user will be redirected to the "Members" page where it is possible to view all users assigned to the group and their basic information.

![Access to user assignment management](assets/images/extract/media/image15.png)

We can add a user to the group by clicking the "+" button at the top right (1). Once pressed, a new row (2) will be created in the list of assigned users where a user can be selected from the list of available users (3).

![Assign a user to the group](assets/images/extract/media/image16.png)

Similarly, it is possible to remove users from the group by clicking the "Trash" button corresponding to the user to be removed.

After adding all users to the group, click the "Save" button at the bottom left to save the changes. A save confirmation modal will be displayed.

We can assign attributes to the group that will be automatically used by the assigned users. To do this, select the "Attributes" tab at the top of the page (1), then using the "+" button at the top right (2), it is possible to add an attribute. In the left part, the key must be entered (3) and in the white part on the right, its value must be entered (4). During entry, we will see a dropdown below the field where clicking will allow saving the entered value (5).

![Enter Attributes](assets/images/extract/media/image17.png)

Once all necessary attributes have been entered, changes can be saved using the "Save" button at the bottom.

To return to the list of available Groups, click the "Back" button present on each page.

#### Viewing, Modifying, and Deleting a Group

From the list of available Groups, a series of buttons are available for each group:

- "Magnifying glass": allows viewing group information (indicated by a red arrow in the image);
- "Pencil": allows modifying the group's basic information (indicated by a yellow arrow in the image);
- "Trash": allows deleting the group after clicking
  "confirm" in the displayed modal (indicated by a purple arrow in the image).

![Control buttons](assets/images/extract/media/image18.png)

### Users

For an account to access and use the system, it must be appropriately configured. Below, we will see the process of creating and managing a user within the SCMP using IAM as an access control application.

To access User management, click the "Users" menu in the "Entities" section of the IAM dashboard.

![Access to User management](assets/images/extract/media/image19.png)

Once the link is clicked, the user will be shown the list of all available groups on the portal with their respective configuration buttons.

![List of configured users](assets/images/extract/media/image20.png)

#### New User Creation

To create a new user within the system, click the "+" button at the top right. A user creation form will be displayed.

![New user creation](assets/images/extract/media/image21.png)

The new user creation form will be displayed. Fill in the mandatory fields in the list:

- E-mail: the user's valid e-mail address.
- Username: the username to be used as the account for portal access.
- First Name: User's first name.
- Last Name: User's last name.
- Password: Password of at least 8 characters to be used for access.
- Max concurrent connections: Maximum number of simultaneous connections enabled for the user.
- Default Language: the basic language to be displayed in the system.

![User creation form](assets/images/extract/media/image22.png)

Once all mandatory fields are entered, click the "+ Add user" button to complete the entry.

A confirmation message will be displayed, and the page will reset to allow the entry of a new user.

To view the newly created user, return to the page containing the list of users.

#### Role and Attribute Assignment

To manage users, you can click the "Groups" button corresponding to the row of the user to be modified.

![Access to user management](assets/images/extract/media/image23.png)

Once the button is pressed, the page refreshes to show the "Groups" page where one or more groups can be assigned to or removed from the user.

To add a new group to the user, you must select the group to be assigned to the user in the left section (1) and then, by clicking the "Associate" button in the center of the page (2), the group will automatically move to the right section and the changes will be saved automatically.

![Associate a user to the group](assets/images/extract/media/image24.png)

Similarly, it is possible to remove the user from the group by first clicking the group to be removed in the right section and then the "Disassociate" button in the center of the page. The changes will be saved automatically.

![Disassociate a user from the group](assets/images/extract/media/image25.png)

Furthermore, using the buttons in the right section, corresponding to each group, it is possible to modify the priority of the various groups.

For users, it is also possible to assign custom attributes. To do this, select the "Attributes" tab at the top of the page (1), then using the "+" button at the top right (2), it is possible to add an attribute. In the left part, the key must be entered (3) and in the white part on the right, its value must be entered (4). During entry, we will see a dropdown below the field where clicking will allow saving the entered value (5).

The list of available attributes is in the paragraph.

![Enter Attributes](assets/images/extract/media/image17.png)

Once all necessary attributes have been entered, changes can be saved using the "Save" button at the bottom.

#### Credential Reset

As a user administrator, it is possible to reset passwords. To do this, click on the "Credentials" tab displayed at the top of the page. In this tab, you can enter a new password for the user and configure it as "Temporary". The temporary password must be changed by the user after the first login. A password validity period, expressed in days, can also be defined.

![Modifying the user's password](assets/images/extract/media/image26.png)

#### Viewing, Modifying, and Deleting a User

From the list of available users, a series of buttons are available for each group:

- "Magnifying glass": allows viewing user info (indicated by a red arrow in the image).
- "Pencil": allows modifying the user's basic information (indicated by a yellow arrow in the image).
- "Trash": allows deleting the user after clicking "confirm" in the displayed modal (indicated by a purple arrow in the image).

![Control buttons](assets/images/extract/media/image27.png)

### Management of Menus Enabled per User/Group

The IAM system integrated into the SCMP also allows the management of menu elements available to various users and groups. To access this functionality, simply click the "User management X Pages" link available in the "Administration" section of the IAM dashboard.

![Access to menu management](assets/images/extract/media/image28.png)

At the top of the page, there are two dropdown menus: the left dropdown allows selecting a single user, and the right one allows selecting a group.

![Selection of user/group to modify](assets/images/extract/media/image29.png)

After selecting an account, the page will update to show all "STREAM" available on the application. It is possible to click the "+" button corresponding to each row to view the available "MODULES" and "COMPONENT".

The displayed component lists are automatically generated by the system using the configurations performed during installation.

For each component present, by clicking the dropdown menu on the corresponding row, it is possible to indicate its visibility (or lack thereof) to the user/group we previously selected.

The selectable values are:

- Enabled and default: only one default can be indicated per module. Selecting this option makes the selected page the main one; thus, upon clicking the menu, the user will be redirected to this page.
- Enabled: Indicates that the menu is visible and usable by the user/group.
- Disabled: Indicates that the menu will not be enabled and will not be visible to the user/group.
- N.D: not defined (the menu is disabled and will not be visible).

![Menu authorization management](assets/images/extract/media/image30.png)

### User Profile Lists and Attributes

This section highlights the different types of users who can access and use the described product.

For each of them, a list of functionalities the user has been enabled for and can interact with is provided.

All attributes that can be assigned to Users and Groups are also indicated here.

#### Attributes

| **Attribute** | **Acceptable Values** | **Type**       | **Description**                                                                                                                                                                                                                                                            |
| :------------ | :-------------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monitoring    | Default, AS01, mase   | String array   | Enter the list of enabled tenants for the user, separated by commas between each tenant name.                                                                                                                                                                                |
| Costs         | true / false          | Boolean        | By enabling the attribute, we specify that the user can perform searches by TAG instead of using the tenant as a discriminant.                                                                                                                                              |
| Inventory     | ADMIN / LIMITED       | Enumeration    | By entering ADMIN as the value, the user will be able to view both costs received from the provider and costs calculated by the SCMP. By entering LIMITED, only costs calculated by the SCMP will be viewable.                                                                   |
| Inventory     | Zona1                 | String         | Mandatory parameter for tools used by IAM.                                                                                                                                                                                                                                 |

#### Administrator

| **Functionality**     | **Create** | **Read** | **Undo** | **Delete** |
| :-------------------- | :--------- | :------- | :------- | :--------- |
| Monitoring            | x          | x        | x        | x          |
| Costs                 | x          | x        | x        | x          |
| Inventory             | x          | x        | x        | x          |
| Security              | x          | x        | x        | x          |
| Dashboard             | x          | x        | x        | x          |
| Catalog               | x          | x        | x        | x          |
| Authentication        | x          | x        | x        | x          |
| Administration        | x          | x        | x        | x          |
| Cloud Maturity model  | x          | x        | x        | x          |
| Provisioning          | x          | x        | x        | x          |
| Tenant Management     |            |          |          |            |
| Service Detail Design |            |          |          |            |

#### Service Manager

| **Functionality**     | **Create** | **Read** | **Undo** | **Delete** |
| :-------------------- | :--------- | :------- | :------- | :--------- |
| Monitoring            |            |          |          |            |
| Costs                 |            |          |          |            |
| Inventory             |            |          |          |            |
| Security              |            |          |          |            |
| Dashboard             |            |          |          |            |
| Catalog               |            |          |          |            |
| Authentication        | x          | x        | x        | x          |
| Administration        |            |          |          |            |
| Cloud Maturity model  |            |          |          |            |
| Provisioning          |            |          |          |            |
| Tenant Management     | x          | x        | x        | x          |
| Service Detail Design | x          | x        | x        | x          |

#### Viewer

| **Functionality**     | **Create** | **Read** | **Undo** | **Delete** |
| :-------------------- | :--------- | :------- | :------- | :--------- |
| Monitoring            | x          | x        |          |            |
| Costs                 | x          | x        |          |            |
| Inventory             | x          | x        |          |            |
| Security              |            | x        |          |            |
| Dashboard             |            | x        |          |            |
| Catalog               |            | x        |          |            |
| Authentication        |            |          |          |            |
| Administration        |            |          |          |            |
| Cloud Maturity model  |            | x        |          |            |
| Provisioning          |            |          |          |            |
| Tenant Management     |            |          |          |            |
| Service Detail Design |            |          |          |            |

#### Authorized

| **Functionality**     | **Create** | **Read** | **Undo** | **Delete** |
| :-------------------- | :--------- | :------- | :------- | :--------- |
| Monitoring            | x          | x        | x        | x          |
| Costs                 | x          | x        | x        | x          |
| Inventory             | x          | x        | x        | x          |
| Security              |            |          |          |            |
| Dashboard             | x          | x        | x        | x          |
| Catalog               | x          | x        | x        | x          |
| Authentication        |            |          |          |            |
| Administration        | x          | x        | x        | x          |
| Cloud Maturity model  |            |          |          |            |
| Provisioning          | x          | x        | x        | x          |
| Tenant Management     |            |          |          |            |
| Service Detail Design |            |          |          |            |
