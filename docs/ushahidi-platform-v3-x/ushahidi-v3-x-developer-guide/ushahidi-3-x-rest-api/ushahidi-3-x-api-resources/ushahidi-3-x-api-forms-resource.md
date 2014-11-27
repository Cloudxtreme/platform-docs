# Ushahidi 3.x API Forms Resource



FEATURE: COMPLETEDOCS: NEED UPDATE

  * POST forms
  * GET forms
  * GET forms/:id
  * PUT forms/:id
  * DELETE forms/:id

# POST forms

Create a Form

**METHOD**: POST  
**ENDPOINT**: /api/v2/forms/  
**AUTHENTICATED**: No

The request body is a JSON representation of the Form being created.Group and
attribute resources can be created at the same time as the form, however these
can only be updated/deleted through their own API endpoints.

##### Example request

POST https://ushv3.dev/api/v2/forms

**Post Data**

**Response**

# GET forms

Listing all Forms

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/  
**AUTHENTICATED**: No

Form attributes and groups are returned along with the form.

##### Query Parameters (no yet implemented)

Name

|

Type

|

Description  
  
---|---|---  
  
q

|

Optional

|

Only forms containing this search string will be returned, matched against
'tag' property  
  
order

|

Optional

|

Returned forms will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned forms will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

Forms returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/forms

**Response**

  

# GET forms/:id

Get a single form

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/:id  
**AUTHENTICATED**: Yes

Form attributes and groups are returned along with the form.

##### Query Parameters

Name

|

Type

|

Description  
  
---|---|---  
  
id

|

Required

|

The numerical id of the form being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/forms/1

**Response**

# PUT forms/:id

Update a form

**METHOD**: PUT  
**ENDPOINT**: /api/v2/forms/:id  
**AUTHENTICATED**: Yes

Only the form resource itself can be updated. Group and attribute resources
have to be updated through their respective endpoints.

##### Query Parameters

Name

|

Type

|

Description  
  
---|---|---  
  
id

|

Required

|

The numerical id of the form being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/forms/1

**Post Data**

**Response**

# DELETE forms/:id

Deleting a form

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/forms/:id  
**AUTHENTICATED**: YES

Form groups will be deleted along with the form itself. Attributes can belong
to many forms so will not be deleted.

##### Query Parameters

Name

|

Type

|

Description  
  
---|---|---  
  
id

|

Required

|

The numerical id of the form being deleted.  
  
##### Example request

DELETE /api/v2/forms/2

**Response**

