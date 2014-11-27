# Ushahidi 3.x API Media Resource



FEATURE: IN PROGRESSDOCS: UP TO DATE

  * POST media
  * GET media
  * GET media/:id
  * DELETE media/:id

# POST media

Create a media

**METHOD**: POST  
**ENDPOINT**: /api/v2/media/  
**AUTHENTICATED**: YES

Make a **multipart/form-data****POST** request with the following parameters.

##### Form Parameters

Name| Type| Description  
---|---|---  
file| Required| The path to the image. Supported types are gif,jpg,jpeg,png  
caption| Optional| A short title or caption for the image to be uploaded  
  
POST https://ushv3.dev/api/v2/media

**Response**

##### Example request

# GET media

Listing all media

**METHOD**: GET  
**ENDPOINT**: /api/v2/media/  
**AUTHENTICATED**: No

##### Query Parameters

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

Returned media will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned media will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

Media returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/media

**Response**

# GET media/:id

Get a single media

**METHOD**: GET  
**ENDPOINT**: /api/v2/media/:id  
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

The numerical id of the media being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/media/1

**Response**

# DELETE media/:id

Deleting a media

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/media/:id  
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

The numerical id of the media being deleted.  
  
##### Example request

DELETE /api/v2/media/2

**Response**

