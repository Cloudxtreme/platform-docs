# Ushahidi 3.x Translations Resource



FEATURE: COMPLETEDOCS: UP TO DATE

The Translations endpoint is an extension of the Posts endpoint. This means
most of the methods behave the same except they're limited to translations of
the parent post.

  * POST posts/:post_id/translations
  * GET posts/:post_id/translations
  * GETposts/:post_id/translations/:id
  * PUT posts/:posts_id/translations:id
  * DELETE posts/:posts_id/translations/:id

# POST posts/:post_id/translations

Create a Translations

**METHOD**: POST  
**ENDPOINT**: /api/v2/posts/:post_id/translations  
**AUTHENTICATED**: No

The request body is a JSON representation of the [Ushahidi 3.x Translations
Resource](/display/WIKI/Ushahidi+3.x+Translations+Resource) being created.

##### Example request

POST https://ushv3.dev/api/v2/posts/1/translations

**Post Data**
    
    
    {
    	"form":1,
    	"locale":"en_US",
    	"type":"translation",
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
    	"id":5,
    	"url":"http://ushv3.dev/api/v2/posts/1/translations/5",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"parent":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/posts/1"
    	},
    	"locale":"en_US",
    	"type":"translation",
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
    

# GET posts/:post_id/translations

Listing all posts

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:post_id/translations/  
**AUTHENTICATED**: No

##### Query Parameters

Name| Type| Description  
---|---|---  
q| Optional| Only Posts containing this search string will be returned,
matched against post title and content  
type| Optional| Only posts of this type will be returned: report, revision,
comment or alert  
locale| Optional| Only posts with matching locale will be returned  
slug| Optional| Only posts with a matching slug will be returned  
form_id| Optional| Only posts with this form_id will be returned  
user_id| Optional| Only posts created by this user_id will be returned  
created_before| Optional| Returned posts will have a created date smaller than
this date  
created_after| Optional| Returned posts will have a created date greater than
this date  
updated_before| Optional| Returned posts will have an updated date smaller
than this date  
updated_after| Optional| Returned posts will have an updated date greater than
this date  
order| Optional| Returned posts will be sorted in this order: ASC or DESC.
Default: DESC  
order_by| Optional| Returned posts will be sorted by this field. Default:
created  
limit| Optional| Limit number of results returned. Default: 50. Max: 500  
offset| Optional| Posts returned will be offset by this number of results  
  
Posts can also be filtered by form attributes by using the attribute as a
parameter. ie

    
    
    GET /api/v2/posts/1/translations?full_name=David

##### Example Request

GET https://ushv3.dev/api/v2/posts/1/translations

**Response**
    
    
    {
        "count": 2,
        "results": [
            {
              "id":5,
              "url":"http://ushv3.dev/api/v2/posts/1/translations/6",
              "form":{
                "id":1,
                "url":"http://ushv3.dev/api/v2/forms/1",
              },
              "parent":{
                  "id":1,
                  "url":"http://ushv3.dev/api/v2/posts/1"
              },
              "locale":"en_US",
              "type":"translation",
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
              "id":6,
              "url":"http://ushv3.dev/api/v2/posts/1/translations/5",
              "form":{
                "id":1,
                "url":"http://ushv3.dev/api/v2/forms/1",
              },
              "parent":{
                  "id":1,
                  "url":"http://ushv3.dev/api/v2/posts/1"
              },
              "locale":"fr_FR",
              "type":"translation",
              "title":"David est manquant",
              "status":"publish",
              "content":"Disheveled, maigre, sans-abri Kenyan vu la dernire fois dans le voisinage de la station lvrier",
              "values":{
                "full_name":"David Kobia",
                "description":"maigre, sans-abri Kenyan vu la dernire fois dans le voisinage de la station lvrier",
                "dob":"unknown",
                "missing_date":"2012/09/25",
                "last_location":"atlanta",
                "status":"missing"
              },
              "tags":["missing","manquant"]
            }
        ],
    	"limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "created",
        "curr": "https://ushv3.dev/api/v2/posts/1/translations?limit=50&offset=0",
        "next": "https://ushv3.dev/api/v2/posts/1/translations?limit=50&offset=50",
        "prev": "https://ushv3.dev/api/v2/posts/1/translations?limit=50&offset=0"
    }
    

# GETposts/:post_id/translations/:id

Get a single post

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:post_id/translations/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the post being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/posts/1/translations/5

**Response**
    
    
    {
    	"id":5,
    	"url":"http://ushv3.dev/api/v2/posts/1/translations/5",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"parent":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/posts/1"
    	},
    	"locale":"en_US",
    	"type":"translation",
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
    

# PUT posts/:posts_id/translations:id

Update a post

**METHOD**: PUT  
**ENDPOINT**: /api/v2/posts/:post_id/translations/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the post being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/posts/1/translations/5

**Post Data**
    
    
    {
    	"form":1,
    	"locale":"en_US",
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
    	"id":5,
    	"url":"http://ushv3.dev/api/v2/posts/1/translations/5",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"parent":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/posts/1"
    	},
    	"locale":"en_US",
    	"type":"translation",
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

# DELETE posts/:posts_id/translations/:id

Deleting a post

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/posts/:post_id/translations/:id  
**AUTHENTICATED**: YES

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the post being deleted.  
  
##### Example request

DELETE /api/v2/posts/:post_id/translations/2

**Response**
    
    
    {
    	"id":2,
    	"url":"http://ushv3.dev/api/v2/posts/:post_id/translations/2",
    	"form":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/forms/1",
    	},
    	"parent":{
    		"id":1,
    		"url":"http://ushv3.dev/api/v2/posts/1"
    	},
    	"locale":"en_US",
    	"type":"translation",
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
    

