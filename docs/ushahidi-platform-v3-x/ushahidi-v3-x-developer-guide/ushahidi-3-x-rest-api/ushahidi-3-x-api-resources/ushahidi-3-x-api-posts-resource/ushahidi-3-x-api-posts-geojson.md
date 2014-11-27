# Ushahidi 3.x API Posts GeoJSON



Posts GeoJSON Api returns Posts in GeoJSON format. The API accepts the same
params as the standard Posts API, but is read-only and only accepts GET
requests.

  * GET posts
    * Bounding Box Search Example
    * Specific 'geometry_attribute' Example
  * GET posts/:id
  * GET posts/geojson/:z/:x/:y

  

# GET posts

Listing all posts

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/geojson  
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

Only Posts containing this search string will be returned, matched against
post title and content  
  
type

|

Optional

|

Only posts of this type will be returned: report, revision, comment or alert  
  
locale| Optional| Only posts with matching locale will be returned  
  
slug

|

Optional

|

Only posts with a matching slug will be returned  
  
form_id

|

Optional

|

Only posts with this form_id will be returned  
  
user_id

|

Optional

|

Only posts created by this user_id will be returned  
  
created_before

|

Optional

|

Returned posts will have a created date smaller than this date  
  
created_after

|

Optional

|

Returned posts will have a created date greater than this date  
  
updated_before

|

Optional

|

Returned posts will have an updated date smaller than this date  
  
updated_after

|

Optional

|

Returned posts will have an updated date greater than this date  
  
bbox| Optional| Returned posts will have a point attribute within the
specified bounding box. bbox expects lat lon values as follows:
west,north,east,south  
**geometry_attribute**| **Optional**| **Returned GeoJSON will only include geometries for the specified attribute**  
  
order

|

Optional

|

Returned posts will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned posts will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

Posts returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/posts/geojson

**Response**

## Bounding Box Search Example

GET  https://ushv3.dev/api/v2/posts/geojson?bbox=-2,-2,2,2

**Response**

## Specific 'geometry_attribute' Example

GET  https://ushv3.dev/api/v2/posts/geojson?geometry_attribute=second_point

**Response**

# GET posts/:id

Get a singlepost

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:id/geojson  
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

The numerical id of the post being retrieved.  
  
##### Example Request

GET http://ushv3.dev/api/v2/posts/1/geojson

**Response**

# GET posts/geojson/:z/:x/:y

Get tiled geojson response

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/geojson/:z/:x/:y  
**AUTHENTICATED**: No

##### Query Parameters

Name

|

Type

|

Description  
  
---|---|---  
**z**| **Required**| **Zoom level**  
**x**| **Required**| **Tile x offset**  
**y**| **Required**| **Tile y offset**  
  
q

|

Optional

|

Only Posts containing this search string will be returned, matched against
post title and content  
  
type

|

Optional

|

Only posts of this type will be returned: report, revision, comment or alert  
  
locale| Optional| Only posts with matching locale will be returned  
  
slug

|

Optional

|

Only posts with a matching slug will be returned  
  
form_id

|

Optional

|

Only posts with this form_id will be returned  
  
user_id

|

Optional

|

Only posts created by this user_id will be returned  
  
created_before

|

Optional

|

Returned posts will have a created date smaller than this date  
  
created_after

|

Optional

|

Returned posts will have a created date greater than this date  
  
updated_before

|

Optional

|

Returned posts will have an updated date smaller than this date  
  
updated_after

|

Optional

|

Returned posts will have an updated date greater than this date  
  
bbox| Optional| Returned posts will have a point attribute within the
specified bounding box. bbox expects lat lon values as follows:
west,north,east,south  
geometry_attribute| Optional| Returned GeoJSON will only include geometries
for the specified attribute  
  
order

|

Optional

|

Returned posts will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned posts will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

Posts returned will be offset by this number of results  
  
##### Example Request

GET  https://ushv3.dev/api/v2/posts/geojson/1/1/0

**Response**

