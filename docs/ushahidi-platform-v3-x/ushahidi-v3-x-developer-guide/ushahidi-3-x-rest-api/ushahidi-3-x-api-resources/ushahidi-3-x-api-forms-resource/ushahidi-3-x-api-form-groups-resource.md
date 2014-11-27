# Ushahidi 3.x API Form Groups Resource



FEATURE: COMPLETEDOCS: UP TO DATE

  * POST forms/:form_id/groups
  * GETforms/:form_id/groups
  * GETforms/:form_id/groups/:id
  * PUTforms/:form_id/groups/:id
  * DELETEforms/:form_id/ groups/:id
  * POST forms/:form_id/groups/:group_id/attributes
    * Add an existing attribute to the group
  * GET forms/:form_id/groups/:group_id/attributes
  * GET forms/:form_id/groups/:group_id/attributes
  * DELETE forms/:form_id/groups/:group_id/attributes/:id

# POST forms/:form_id/groups

Create a group

**METHOD**: POST  
**ENDPOINT**: /api/v2/forms/:form_id/groups/  
**AUTHENTICATED**: No

The request body is a JSON representation of the group being created.

##### Example request

POST https://ushv3.dev/api/v2/forms/1/groups

**Post Data**

**Response**

# GETforms/:form_id/groups

Listing all groups

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/:form_id/groups/  
**AUTHENTICATED**: No

##### Query Parameters (Not implemented yet)

Name

|

Type

|

Description  
  
---|---|---  
  
order

|

Optional

|

Returned groups will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned groups will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

groups returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/forms/1/groups

**Response**

  

# GETforms/:form_id/groups/:id

Get a singlegroup

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/:form_id/groups/:id  
**AUTHENTICATED**: Yes

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

The numerical id of the group being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/forms/1/groups/1

**Response**

# PUTforms/:form_id/groups/:id

Update agroup

**METHOD**: PUT  
**ENDPOINT**: /api/v2/forms/:form_id/groups/:id  
**AUTHENTICATED**: Yes

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

The numerical id of the group being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/forms/1/groups/1

**Post Data**

**Response**

# DELETEforms/:form_id/ groups/:id

Deleting agroup

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/forms/:form_id/groups/:id  
**AUTHENTICATED**: YES

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

The numerical id of the group being deleted.  
  
##### Example request

DELETE /api/v2/forms/1/groups/2

**Response**

# POST forms/:form_id/groups/:group_id/attributes

Add a new or existing attribute to a group

**METHOD**: POST  
**ENDPOINT**: /api/v2/forms/:form_id/groups/:id/attributes  
**AUTHENTICATED**: Yes

The request data should be JSON object, containing either the full
representation of a new attribute, or the id of an existing attribute.

##### Create a new attribute and add to the group

##### Example Request

POST http://ushv3.dev/api/v2/forms/1/groups/1/attributes

**Post Data**

**Response**

## Add an existing attribute to the group

##### Example Request

POST  http://ushv3.dev/api/v2/forms/1/groups/1/attributes

**Post Data**

**Response**

# GET forms/:form_id/groups/:group_id/attributes

List all attributes from a group.

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/:form_id/groups/:group_id/attributes  
**AUTHENTICATED**: Yes

##### Query Parameters (Not implemented)

Name

|

Type

|

Description  
  
---|---|---  
  
order

|

Optional

|

Returned groups will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned groups will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

groups returned will be offset by this number of results  
  
##### Example Request

GET http://ushv3.dev/api/v2/forms/1/groups/1/attributes

**Response**

# GET forms/:form_id/groups/:group_id/attributes

Find a single attribute in a group.

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/:form_id/groups/:group_id/attributes/:id  
**AUTHENTICATED**: Yes

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

The numerical id of the group being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/forms/1/groups/1/attributes/1

**Response**

# DELETE forms/:form_id/groups/:group_id/attributes/:id

Remove an attribute from a group.

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/forms/:form_id/groups/:group_id/attributes/:id  
**AUTHENTICATED**: Yes

Note: This just removes the attribute from the group, it doesn't delete the
attribute entirely.

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

The numerical id of the group being updated.  
  
##### Example Request

DELETE http://ushv3.dev/api/v2/forms/1/groups/1/attributes/1

**Response**

