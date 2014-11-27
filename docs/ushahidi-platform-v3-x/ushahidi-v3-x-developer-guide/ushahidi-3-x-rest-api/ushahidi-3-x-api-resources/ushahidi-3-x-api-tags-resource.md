# Ushahidi 3.x API Tags Resource



FEATURE: COMPLETEDOCS: UP TO DATE

  * POST tags
  * GET tags
    * Search Example
  * GET tags/:id
  * PUT tags/:id
  * DELETE tags/:id

# POST tags

Create a Tag

**METHOD**: POST  
**ENDPOINT**: /api/v2/tags/  
**AUTHENTICATED**: No

The request body is a JSON representation of the [Ushahidi 3.x API Tags
Resource](/display/WIKI/Ushahidi+3.x+API+Tags+Resource) being created.

##### Example request

POST https://ushv3.dev/api/v2/tags

**Post Data**

**Response**

# GET tags

Listing all tags

**METHOD**: GET  
**ENDPOINT**: /api/v2/tags/  
**AUTHENTICATED**: No

##### Query Parameters

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

Only Tags containing this search string will be returned, matched against
'tag' property  
  
type

|

Optional

|

Only tags of this type will be returned: category, status  
  
parent| Optional| Only tags with a matching parent_id will be returned  
tag| Optional| Only tags with a matching tag will be returned  
  
order

|

Optional

|

Returned tags will be sorted in this order: ASC or DESC. Default: ASC  
  
order_by

|

Optional

|

Returned tags will be sorted by this field. Default: priority  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

Tags returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/tags

**Response**

## Search Example

GET  https://ushv3.dev/api/v2/tags?q=Explo

**Response**

# GET tags/:id

Get a single tag

**METHOD**: GET  
**ENDPOINT**: /api/v2/tags/:id  
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

The numerical id of the tag being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/tags/1

**Response**

# PUT tags/:id

Update a tag

**METHOD**: PUT  
**ENDPOINT**: /api/v2/tags/:id  
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

The numerical id of the tag being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/tags/1

**Post Data**

**Response**

# DELETE tags/:id

Deleting a tag

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/tags/:id  
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

The numerical id of the tag being deleted.  
  
##### Example request

DELETE /api/v2/tags/2

**Response**

