# Ushahidi 3.x API Sets Resource



  * POST sets
  * GET sets
    * Search Example
  * GET sets/:id
  * PUT sets/:id
  * DELETE sets/:id

# POST sets

Create a sets

**METHOD**: POST  
**ENDPOINT**: /api/v2/sets/  
**AUTHENTICATED**: No

The request body is a JSON representation of the sets being created.

##### Example request

POST https://ushv3.dev/api/v2/sets

**Post Data**
    
    
    {
    	"name":"Test set",
    	"filter":"Test filter"
    }
    

**Response**
    
    
    {
     	"id": "1",
    	"url": "http://ushv3.dev/api/v2/sets/1",
    	"name": "Test set",
    	"filter": Test filter,
    	"user": null,
    	"created": "1970-01-01T00:00:00+00:00",
    	"updated": "1970-01-01T00:00:00+00:00"
    }
    

# GET sets

Listing all sets

**METHOD**: GET  
**ENDPOINT**: /api/v2/sets/  
**AUTHENTICATED**: No

##### Query Parameters

Name| Type| Description  
---|---|---  
q| Optional| Only sets containing this search string will be returned, matched
against 'name' property  
name| Optional| Only sets with a matching 'name' will be returned  
user_id| Optional| Only sets with this user_id will be returned  
order| Optional| Returned sets will be sorted in this order: ASC or DESC.
Default: DESC  
order_by| Optional| Returned sets will be sorted by this field. Default:
created  
limit| Optional| Limit number of results returned. Default: 50. Max: 500  
offset| Optional| Sets returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/sets

**Response**
    
    
    {
        "count": 2,
        "results": [
    		{
                "id": "1",
                "url": "http://lamu.dev/api/v2/sets/1",
                "name": "Test set",
                "filter": Test filter,
                "user": null,
                "created": "1970-01-01T00:00:00+00:00",
                "updated": "1970-01-01T00:00:00+00:00"
            },
            {
                "id": "2",
                "url": "http://ushv3.dev/api/v2/sets/2",
                "name": "Explosion",
                "filter": null,
                "user": null,
                "created": "1970-01-01T00:00:00+00:00",
                "updated": "1970-01-01T00:00:00+00:00"
            }
    
    
        ],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "created",
        "curr": "https://ushv3.dev/api/v2/sets/?limit=50&offset=0",
        "next": "https://ushv3.dev/api/v2/sets/?limit=50&offset=50",
        "prev": "https://ushv3.dev/api/v2/sets/?limit=50&offset=0"
    }
    

## Search Example

GET  https://ushv3.dev/api/v2/sets?q=Explo

**Response**
    
    
    {
        "count": 1,
        "results": [
            {
    			"id": "2",
                "url": "http://ushv3.dev/api/v2/sets/2",
                "name": "Explosion",
                "filter": null,
                "user": null,
                "created": "1970-01-01T00:00:00+00:00",
                "updated": "1970-01-01T00:00:00+00:00"
            }
        ],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "created",
        "curr": "https://ushv3.dev/api/v2/sets/?q=David&limit=50&offset=0",
        "next": "https://ushv3.dev/api/v2/sets/?q=David&limit=50&offset=50",
        "prev": "https://ushv3.dev/api/v2/sets/?q=David&limit=50&offset=0"
    }
    

# GET sets/:id

Get a single set

**METHOD**: GET  
**ENDPOINT**: /api/v2/sets/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the set being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/sets/1

**Response**
    
    
    {
    	"id": "1",
    	"url": "http://lamu.dev/api/v2/sets/1",
    	"name": "Test set",
    	"filter": Test filter,
    	"user": null,
    	"created": "1970-01-01T00:00:00+00:00",
    	"updated": "1970-01-01T00:00:00+00:00"
    }
    

# PUT sets/:id

Update a set

**METHOD**: PUT  
**ENDPOINT**: /api/v2/sets/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the set being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/sets/1

**Post Data**
    
    
    {
        "name": "Updated Set One",
        "filter": "updated set filter"
    }
    

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/sets\/1",
        "name": "Updated Set One",
        "filter": "updated set filter",
        "user": null,
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "2013-08-21T00:37:35+00:00"
    }
    

# DELETE sets/:id

Deleting a set

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/sets/:id  
**AUTHENTICATED**: YES

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the set being deleted.  
  
##### Example request

DELETE /api/v2/sets/2

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/sets\/1",
        "name": "Test set",
        "filter": null,
        "user": null,
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "1970-01-01T00:00:00+00:00"
    }
    

