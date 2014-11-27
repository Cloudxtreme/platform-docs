# Ushahidi 3.x Revisions Resource



FEATURE: COMPLETEDOCS: UP TO DATE

The Revisions endpoint is an extension of the Posts endpoint. However
Revisions are read only so the only allowed method is GET.

  * GET posts/:post_id/revisions
  * GETposts/:post_id/revisions/:id

# GET posts/:post_id/revisions

Listing all posts

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:post_id/revisions/  
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
  
Posts can also be filtered by form attributes by using the attribute as a
parameter. ie

##### Example Request

GET https://ushv3.dev/api/v2/posts/1/revisions

**Response**

# GETposts/:post_id/revisions/:id

Get a single post

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:post_id/revisions/:id  
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

The numerical id of the post being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/posts/1/revisions/5

**Response**

