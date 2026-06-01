# ERP_UI_STANDARDS.md

## Layout

### Page Layout

* Page Header at top
* Search and Filters below header
* Table below filters
* Pagination at bottom
* Add button aligned right

---

## Drawer

### Width

Desktop:

* 700px

Tablet:

* 600px

Mobile:

* 100%

### Tabs

Supported

Examples:

* Basic Information
* Academic Information
* Documents
* Guardian Information
* Medical Information

---

## Forms

### Responsive Grid

Desktop:

* 2 columns

Tablet:

* 2 columns

Mobile:

* 1 column

### Field Spacing

* Vertical gap: 16px
* Horizontal gap: 16px

---

## Buttons

### Primary

Used For:

* Save
* Add
* Submit

### Secondary

Used For:

* Cancel
* Close

### Danger

Used For:

* Delete

---

## Tables

### Features

* Search
* Sorting
* Pagination
* Multi Select
* Sticky Header
* Sticky Action Column
* Export Excel
* Export PDF
* Import
* Print

### Action Menu

Three Dot Menu

Actions:

* View
* Edit
* Delete
* Duplicate
* Activate
* Deactivate

---

## Dialogs

### Confirm Dialog

Used For:

* Delete
* Status Change
* Bulk Delete

### Delete Dialog

Message:

"Are you sure you want to delete this record?"

---

## Module Structure

modules/

module-name/

* components/
* pages/
* services/
* routes/
* config/

---

## Global Components

components/

ui/
crud/
forms/
dialogs/

---

## Service Rules

Pages never call axios directly.

Use:

service.js

Example:

buildingService.js
studentService.js
teacherService.js

---

## Naming Convention

List Page

* BuildingListPage.jsx

Form

* BuildingForm.jsx

Service

* buildingService.js

Routes

* buildingRoutes.jsx

Columns

* buildingColumns.js

Fields

* buildingFields.js
