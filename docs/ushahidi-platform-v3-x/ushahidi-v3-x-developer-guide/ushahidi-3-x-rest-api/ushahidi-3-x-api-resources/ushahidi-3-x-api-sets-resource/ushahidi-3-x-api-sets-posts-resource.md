# Ushahidi 3.x API Sets Posts Resource



  * POST sets/:set_id/posts
  * GET sets/:set_id/posts
  * GET sets/:set_id/posts/:id
  * DELETE sets/:set_id/posts/

# POST sets/:set_id/posts

Add a Post to a Set

**METHOD**: POST  
**ENDPOINT**: /api/v2/sets/:set_id/posts  
**AUTHENTICATED**: No

The request body is a JSON representation of the Sets Posts being created.

##### Example request

POST https://ushv3.dev/api/v2/sets/1/posts/

**Post Data**

**Response**

# GET sets/:set_id/posts

Listing all Sets Posts

**METHOD**: GET  
**ENDPOINT**: /api/v2/sets/1/posts  
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
  
|

|  
  
order

|

Optional

|

Returned [resources] will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned [resources] will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

[Resources] returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/sets/1/posts/?limit=50

**Response**

# GET sets/:set_id/posts/:id

Get a single Set Post

**METHOD**: GET  
**ENDPOINT**: /api/v2/sets/:set_id/posts/:id  
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

The numerical id of the set post being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/sets/1/posts/1

**Response**

# DELETE sets/:set_id/posts/

Deleting a Set Post

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/sets/:set_id/posts/  
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

The numerical id of the set post being deleted.  
  
##### Example request

DELETE /api/v2/sets/1/posts

**Response**

