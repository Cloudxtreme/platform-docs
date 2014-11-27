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
    
    
    {
    	"email":"linda@ushahidi.com",
    	"first_name":"Linda",
    	"last_name":"Kamau",
    	"username":"kamaulynder",
    	"password":"testing"
    }
    

**Response**
    
    
    {
        "id": 4,
        "url": "http:\/\/ushv3.dev\/api\/v2\/users\/4",
        "email": "linda@ushahidi.com",
        "first_name": "Linda",
        "last_name": "Kamau",
        "username": "kamaulynder",
        "logins": null,
        "last_login": null,
        "failed_attempts": null,
        "last_attempt": null,
        "created": "2013-08-21T00:25:20+00:00",
        "updated": null
    }
    

# GET users

Listing all users

**METHOD**: GET  
**ENDPOINT**: /api/v2/users/  
**AUTHENTICATED**: No

##### Query Parameters

Name| Type| Description  
---|---|---  
q| Optional| Only users containing this search string will be returned,
matched against 'email', 'first_name', 'last_name' and 'username' properties  
email| Optional| Filter results by email address  
first_name| Optional| Filter results by first name  
last_name| Optional| Filter results by last name  
username| Optional| Filter results by username  
order| Optional| Returned users will be sorted in this order: ASC or DESC.
Default: DESC  
order_by| Optional| Returned users will be sorted by this field. Allowed: id,
created, email, username Default: created  
limit| Optional| Limit number of results returned. Default: 50. Max: 500  
offset| Optional| Users returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/users

**Response**
    
    
    {
        
        "count": 3,
        "results": [{
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1",
            "email": "robbie@ushahidi.com",
            "first_name": "Robbie",
            "last_name": "Mackay",
            "username": "robbie",
            "logins": "0",
            "last_login": null,
            "failed_attempts": "0",
            "last_attempt": null,
            "created": "1970-01-01T00:00:00+00:00",
            "updated": "1970-01-01T00:00:00+00:00"
        }, {
            "id": "2",
            "url": "http:\/\/ushv3.dev\/api\/v2\/users\/2",
            "email": null,
            "first_name": null,
            "last_name": null,
            "username": "admin",
            "logins": "0",
            "last_login": null,
            "failed_attempts": "0",
            "last_attempt": null,
            "created": "1970-01-01T00:00:00+00:00",
            "updated": "1970-01-01T00:00:00+00:00"
        }, {
            "id": "3",
            "url": "http:\/\/ushv3.dev\/api\/v2\/users\/3",
            "email": null,
            "first_name": null,
            "last_name": null,
            "username": "test",
            "logins": "0",
            "last_login": null,
            "failed_attempts": "0",
            "last_attempt": null,
            "created": "1970-01-01T00:00:00+00:00",
            "updated": "1970-01-01T00:00:00+00:00"
        }],
        "limit": 50,
        "offset": 0,
        "order": "DESC",
        "orderby": "created",
        "curr": "http:\/\/ushv3.dev\/api\/v2\/users?limit=50&offset=0",
        "next": "http:\/\/ushv3.dev\/api\/v2\/users?limit=50&offset=50",
        "prev": "http:\/\/ushv3.dev\/api\/v2\/users?limit=50&offset=0"
    }
    

## Search Example

GET  https://ushv3.dev/api/v2/users?q=rob

**Response**
    
    
    {
        "count": 1,
        "results": [{
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1",
            "email": "robbie@ushahidi.com",
            "first_name": "Robbie",
            "last_name": "Mackay",
            "username": "robbie",
            "logins": "0",
            "last_login": null,
            "failed_attempts": "0",
            "last_attempt": null,
            "created": "1970-01-01T00:00:00+00:00",
            "updated": "1970-01-01T00:00:00+00:00"
        }],
        "limit": 50,
        "offset": 0,
        "order": "DESC",
        "orderby": "created",
        "curr": "http:\/\/ushv3.dev\/api\/v2\/users?q=rob&limit=50&offset=0",
        "next": "http:\/\/ushv3.dev\/api\/v2\/users?q=rob&limit=50&offset=50",
        "prev": "http:\/\/ushv3.dev\/api\/v2\/users?q=rob&limit=50&offset=0"
    }
    

# GET users/:id

Get a single user

**METHOD**: GET  
**ENDPOINT**: /api/v2/users/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the user being updated

In a special case this can also be 'me' to get the current user  
  
##### Example Request

GET http://ushv3.dev/api/v2/users/1

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1",
        "email": "robbie@ushahidi.com",
        "first_name": "Robbie",
        "last_name": "Mackay",
        "username": "robbie",
        "logins": "0",
        "last_login": null,
        "failed_attempts": "0",
        "last_attempt": null,
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "1970-01-01T00:00:00+00:00"
    }
    

# PUT users/:id

Update a user

**METHOD**: PUT  
**ENDPOINT**: /api/v2/users/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the user being updated.

In a special case this can also be 'me' to get the current user  
  
##### Example Request

PUT http://ushv3.dev/api/v2/users/1

**Post Data**
    
    
    {
    	"email":"robbie@ushahidi.com",
    	"first_name":"Robbie",
    	"last_name":"Mackay",
    	"username":"rjmackay",
    	"password":"testing"
    }
    

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1",
        "email": "robbie@ushahidi.com",
        "first_name": "Robbie",
        "last_name": "Mackay",
        "username": "rjmackay",
        "logins": "0",
        "last_login": null,
        "failed_attempts": "0",
        "last_attempt": null,
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "2013-08-21T00:25:20+00:00"
    }
    

# DELETE users/:id

Deleting a user

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/users/:id  
**AUTHENTICATED**: YES

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the user being deleted.  
  
##### Example request

DELETE /api/v2/users/1

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1",
        "email": "robbie@ushahidi.com",
        "first_name": "Robbie",
        "last_name": "Mackay",
        "username": "robbie",
        "logins": "0",
        "last_login": null,
        "failed_attempts": "0",
        "last_attempt": null,
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "1970-01-01T00:00:00+00:00"
    }
    

