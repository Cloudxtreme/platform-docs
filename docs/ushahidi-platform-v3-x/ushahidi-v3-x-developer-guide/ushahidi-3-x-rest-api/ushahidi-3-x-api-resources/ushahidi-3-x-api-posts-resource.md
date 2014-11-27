# Ushahidi 3.x API Posts Resource



  * POST posts
  * GET posts
    * Search Example
  * GET posts/:id
  * PUT posts/:id
  * DELETE posts/:id

# POST posts

Create a Post

**METHOD**: POST  
**ENDPOINT**: /api/v2/posts/  
**AUTHENTICATED**: No

The request body is a JSON representation of the [Ushahidi 3.x API Posts
Resource](/display/WIKI/Ushahidi+3.x+API+Posts+Resource) being created.

##### Example request

POST https://ushv3.dev/api/v2/posts

**Post Data**
    
    
    {
    	"form":1,
    	"locale":"en_US",
    	"type":"report",
    	"title":"David is Missing",
    	"status":"published",
    	"content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    	"values":{
    		"full_name":"David Kobia",
    		"description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    		"dob":"272332800",
    		"missing_date":"1365543083",
    		"last_location":"atlanta",
    		"status":"missing"
    	},
    	"tags":["missing"]
    }
    

**Response**
    
    
    {
    	"id":1,
    	"url":"http://ushv3.dev/api/v2/posts/1",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"locale":"en_US",
    	"type":"report",
    	"title":"David is Missing",
    	"status":"publish",
    	"content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    	"values":{
    		"full_name":"David Kobia",
    		"description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    		"dob":"unknown",
    		"missing_date":"2012/09/25",
    		"last_location":"atlanta",
    		"status":"missing"
    	},
    	"tags":["missing"]
    }
    

# GET posts

Listing all posts

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/  
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
tags| Optional| Filter posts by one or more tags. Accepts a comma separated
list of tag id's. By default we will return posts matching any of the tag ids.  
You can also use tags[all] or tags[any] to specify if posts should match
all/any of the tag ids.  
  
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

    
    
    GET /api/v2/posts?full_name=David

##### Example Request

GET https://ushv3.dev/api/v2/posts

**Response**
    
    
    {
        "count": 2,
        "results": [
            {
              "id":1,
              "url":"http://ushv3.dev/api/v2/posts/1",
              "form":{
                "id":1,
                "url":"http://ushv3.dev/api/v2/forms/1",
              },
              "locale":"en_US",
              "type":"report"
              "title":"David is Missing",
              "status":"publish",
              "content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
              "values":{
                "full_name":"David Kobia",
                "description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
                "dob":"unknown",
                "missing_date":"2012/09/25",
                "last_location":"atlanta",
                "status":"missing"
              },
              "tags":["missing"]
            },
            {
              "id":
              "form":{
                "id":1,
                "url":"http://ushv3.dev/api/v2/forms/1",
              },
              "url":"http://ushv3.dev/api/v2/posts/2",
              "locale":"en_US",
              "type":"report",
              "title":"Robbie lost in Nairobi",
              "status":"publish",
              "content":"Confused jetlagged New Zealander, last seen new the iHub",
              "values":{
                "full_name":"Robbie Mackay",
                "description":"Confused jetlagged New Zealander, last seen new the iHub",
                "dob":"01/01/1985",
                "missing_date":"2013/01/30",
                "last_location":"Nairobi",
                "status":"missing"
              },
              "tags":["missing","nairobi"]
            }
        ],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "created",
        "curr": "https://ushv3.dev/api/v2/posts/?limit=50&offset=0",
        "next": "https://ushv3.dev/api/v2/posts/?limit=50&offset=50",
        "prev": "https://ushv3.dev/api/v2/posts/?limit=50&offset=0"
    }
    

## Search Example

GET  https://ushv3.dev/api/v2/posts?q=David

  

**Response**
    
    
    {
        "count": 1,
        "results": [
            {
              "id":1,
              "url":"http://ushv3.dev/api/v2/posts/1",
              "form":{
                "id":1,
                "url":"http://ushv3.dev/api/v2/forms/1",
              },
              "locale":"en_US",
              "type":"report",
              "title":"David is Missing",
              "status":"publish",
              "content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
              "values":{
                "full_name":"David Kobia",
                "description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
                "dob":"unknown",
                "missing_date":"2012/09/25",
                "last_location":"atlanta",
                "status":"missing"
              },
              "tags":["missing"]
            }
        ],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "created",
        "curr": "https://ushv3.dev/api/v2/posts/?q=David&limit=50&offset=0",
        "next": "https://ushv3.dev/api/v2/posts/?q=David&limit=50&offset=50",
        "prev": "https://ushv3.dev/api/v2/posts/?q=David&limit=50&offset=0"
    }
    

# GET posts/:id

Get a single post

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:id  
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

GET http://ushv3.dev/api/v2/posts/1

**Response**
    
    
    {
    	"id":1,
    	"url":"http://ushv3.dev/api/v2/posts/1",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"locale":"en_US",
    	"type":"report",
    	"title":"David is Missing [RESOLVED: NOW FOUND]",
    	"status":"publish",
    	"content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station. Found in Nairobi",
    	"values":{
    		"full_name":"David Kobia",
    		"description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    		"dob":"unknown",
    		"missing_date":"2012/09/25",
    		"last_location":"Nairobi",
    		"status":"found"
    	},
    	"tags":["found"]
    }
    

# PUT posts/:id

Update a post

**METHOD**: PUT  
**ENDPOINT**: /api/v2/posts/:id  
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

PUT http://ushv3.dev/api/v2/posts/1

**Post Data**
    
    
    {
    	"form":1,
    	"locale":"en_US",
    	"type":"report",
    	"title":"David is Missing [RESOLVED: NOW FOUND]",
    	"status":"publish",
    	"content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station. Found in Nairobi",
    	"values":{
    		"full_name":"David Kobia",
    		"description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    		"dob":"unknown",
    		"missing_date":"2012/09/25",
    		"last_location":"Nairobi",
    		"status":"found"
    	},
    	"tags":["found"]
    }
    

**Response**
    
    
    {
    	"id":1,
    	"url":"http://ushv3.dev/api/v2/posts/1",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"locale":"en_US",
    	"type":"report",
    	"title":"David is Missing [RESOLVED: NOW FOUND]",
    	"status":"publish",
    	"content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station. Found in Nairobi",
    	"values":{
    		"full_name":"David Kobia",
    		"description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    		"dob":"unknown",
    		"missing_date":"2012/09/25",
    		"last_location":"Nairobi",
    		"status":"found"
    	},
    	"tags":["found"]
    }
    

### TODO

  * Document deleting an attribute value

# DELETE posts/:id

Deleting a post

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/posts/:id  
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

The numerical id of the post being deleted.  
  
##### Example request

DELETE /api/v2/posts/2

**Response**
    
    
    {
    	"id":2,
    	"url":"http://ushv3.dev/api/v2/posts/2",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"locale":"en_US",
    	"type":"report",
    	"title":"David is Missing",
    	"status":"publish",
    	"content":"Disheveled, skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    	"values":{
    		"full_name":"David Kobia",
    		"description":"Skinny, homeless Kenyan last seen in the vicinity of the greyhound station",
    		"dob":"unknown",
    		"missing_date":"2012/09/25",
    		"last_location":"atlanta",
    		"status":"missing"
    	},
    	"tags":["missing"]
    }
    

