# Ushahidi 3.x Updates Resource



FEATURE: COMPLETEDOCS: UP TO DATE

The Updates endpoint is an extension of the Posts endpoint. Updates are just
Posts attached to some parent, these could be sensor updates, incidents around
a central location, etc.

  * POST posts/:post_id/updates
  * GET posts/:post_id/updates
  * GETposts/:post_id/updates/:id
  * PUT posts/:posts_id/updates:id
  * DELETE posts/:posts_id/updates/:id

# POST posts/:post_id/updates

Create a updates

**METHOD**: POST  
**ENDPOINT**: /api/v2/posts/:post_id/updates  
**AUTHENTICATED**: No

The request body is a JSON representation of the reportbeing created.

##### Example request

POST https://ushv3.dev/api/v2/posts/99/updates

**Post Data**
    
    
    {
        "form": 1,
        "title": "Test update",
        "content": "Some description",
        "status": "published",
        "type": "report",
        "locale":"en_US",
        "values": {
            "dummy_varchar": "testing"
        },
        "tags": ["update-test"]
    }
    

**Response**
    
    
    {
    
        "id": 103,
        "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/103",
        "parent": {
            "id": "99",
            "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/99"
        },
        "user": null,
        "form": {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/forms\/1"
        },
        "title": "Test update",
        "content": "Some description",
        "status": "published",
        "type": "report",
        "email": null,
        "author": null,
        "slug": "test-update",
        "locale": "en_us",
        "created": "2013-05-08T01:58:56+00:00",
        "updated": null,
        "values": {
            "dummy_varchar": "testing"
        },
        "tags": ["update-test"]
    }
    

# GET posts/:post_id/updates

Listing all posts

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:post_id/updates/  
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

    
    
    GET /api/v2/posts/1/updates?full_name=David

##### Example Request

GET https://ushv3.dev/api/v2/posts/99/updates

**Response**
    
    
    {
        "count": 2,
        "results": [{
            "id": "101",
            "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/101",
            "parent": {
                "id": "99",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/99"
            },
            "user": null,
            "form": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/forms\/1"
            },
            "title": "Child dummy report",
            "content": "Some description",
            "status": "published",
            "type": "report",
            "email": null,
            "author": null,
            "slug": "child-dummy-report",
            "locale": "en_us",
            "created": "2013-05-08T01:58:56+00:00",
            "updated": "1970-01-01T00:00:00+00:00",
            "values": {
                "dummy_varchar": "dummy string"
            },
            "tags": []
        }, {
            "id": "102",
            "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/102",
            "parent": {
                "id": "99",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/99"
            },
            "user": null,
            "form": {
                "id": "2",
                "url": "http:\/\/ushv3.dev\/api\/v2\/forms\/2"
            },
            "title": "Child missing person report",
            "content": "Some description",
            "status": "published",
            "type": "report",
            "email": null,
            "author": null,
            "slug": "child-missing-person-report",
            "locale": "en_us",
            "created": "2013-05-08T01:58:56+00:00",
            "updated": "1970-01-01T00:00:00+00:00",
            "values": {
                "full_name": "missing"
            },
            "tags": []
        }],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "created",
        "curr": "http:\/\/ushv3.dev\/api\/v2\/posts\/99\/updates?limit=50&offset=0",
        "next": "http:\/\/ushv3.dev\/api\/v2\/posts\/99\/updates?limit=50&offset=50",
        "prev": "http:\/\/ushv3.dev\/api\/v2\/posts\/99\/updates?limit=50&offset=0"
    }
    

# GETposts/:post_id/updates/:id

Get a single post

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:post_id/updates/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the post being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/posts/99/updates/101

**Response**
    
    
    {
    
        "id": "101",
        "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/101",
        "parent": {
            "id": "99",
            "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/99"
        },
        "user": null,
        "form": {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/forms\/1"
        },
        "title": "Child dummy report",
        "content": "Some description",
        "status": "published",
        "type": "report",
        "email": null,
        "author": null,
        "slug": "child-dummy-report",
        "locale": "en_us",
        "created": "2013-05-08T01:58:56+00:00",
        "updated": "1970-01-01T00:00:00+00:00",
        "values": {
            "dummy_varchar": "dummy string"
        },
        "tags": []
    }
    

# PUT posts/:posts_id/updates:id

Update a post

**METHOD**: PUT  
**ENDPOINT**: /api/v2/posts/:post_id/updates/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the post being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/posts/99/updates/101

**Post Data**
    
    
    {
       "form": 1,
        "title": "Test update updated",
        "content": "Some description",
        "status": "published",
        "type": "report",
        "locale":"en_US",
        "values": {
            "dummy_varchar": "testing"
        },
        "tags": ["update-test"]
    }
    

**Response**
    
    
    {
       "id": "101",
        "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/101",
        "parent": {
            "id": "99",
            "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/99"
        },
        "user": null,
        "form": {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/forms\/1"
        },
        "title": "Test update updated",
        "content": "Some description",
        "status": "published",
        "type": "report",
        "email": null,
        "author": null,
        "slug": "child-dummy-report",
        "locale": "en_us",
        "created": "2013-05-08T01:58:56+00:00",
        "updated": "2013-05-08T01:58:57+00:00",
        "values": {
            "dummy_varchar": "testing"
        },
        "tags": ["update-test"]
    }
    

# DELETE posts/:posts_id/updates/:id

Deleting a post

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/posts/:post_id/updates/:id  
**AUTHENTICATED**: YES

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the post being deleted.  
  
##### Example request

DELETE /api/v2/posts/:post_id/updates/2

**Response**
    
    
    {
        "id": "101",
        "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/101",
        "parent": {
            "id": "99",
            "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/99"
        },
        "user": null,
        "form": {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/forms\/1"
        },
        "title": "Test update updated",
        "content": "Some description",
        "status": "published",
        "type": "report",
        "email": null,
        "author": null,
        "slug": "child-dummy-report",
        "locale": "en_us",
        "created": "2013-05-08T01:58:56+00:00",
        "updated": "2013-05-08T01:58:57+00:00",
        "values": {
            "dummy_varchar": "testing"
        },
        "tags": ["update-test"]
    }
    

