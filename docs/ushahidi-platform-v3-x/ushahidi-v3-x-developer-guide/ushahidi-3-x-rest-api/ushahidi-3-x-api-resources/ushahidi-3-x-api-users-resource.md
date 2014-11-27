# Ushahidi 3.x API Users Resource



  * POST users
  * GET users
    * Search Example
  * GET users/:id
  * PUT users/:id
  * DELETE users/:id

# POST users

Create a user

**METHOD**: POST  
**ENDPOINT**: /api/v2/users/  
**AUTHENTICATED**: No

The request body is a JSON representation of the user being created.

##### Example request

POST https://ushv3.dev/api/v2/users

**Post Data**

**Response**

# GET users

Listing all users

**METHOD**: GET  
**ENDPOINT**: /api/v2/users/  
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

Only users containing this search string will be returned, matched against
'email', 'first_name', 'last_name' and 'username' properties  
  
email| Optional| Filter results by email address  
first_name| Optional| Filter results by first name  
last_name| Optional| Filter results by last name  
username| Optional| Filter results by username  
  
order

|

Optional

|

Returned users will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned users will be sorted by this field. Allowed: id, created, email,
username Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

Users returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/users

**Response**

## Search Example

GET  https://ushv3.dev/api/v2/users?q=rob

**Response**

# GET users/:id

Get a single user

**METHOD**: GET  
**ENDPOINT**: /api/v2/users/:id  
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

The numerical id of the user being updated

In a special case this can also be 'me' to get the current user  
  
##### Example Request

GET http://ushv3.dev/api/v2/users/1

**Response**

# PUT users/:id

Update a user

**METHOD**: PUT  
**ENDPOINT**: /api/v2/users/:id  
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

The numerical id of the user being updated.

In a special case this can also be 'me' to get the current user  
  
##### Example Request

PUT http://ushv3.dev/api/v2/users/1

**Post Data**

**Response**

# DELETE users/:id

Deleting a user

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/users/:id  
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

The numerical id of the user being deleted.  
  
##### Example request

DELETE /api/v2/users/1

**Response**

