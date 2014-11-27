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
    
    
    {
       "id":1
    }
    

**Response**
    
    
    {
        "id": "1",
        "url": "http://localhost/Lamu/httpdocs/api/v2/posts/1",
        "parent": null,
        "user": null,
        "form": {
            "id": "1",
            "url": "http://localhost/Lamu/httpdocs/api/v2/forms/1"
        },
        "title": "Test post",
        "content": "Testing post",
        "status": "published",
        "type": "report",
        "slug": null,
        "locale": "en_us",
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "1970-01-01T00:00:00+00:00",
        "values": {
            "missing_status": "believed_missing",
            "links": [
                {
                    "id": "11",
                    "value": "http://google.com"
                },
                {
                    "id": "12",
                    "value": "http://ushahidi.com"
                }
            ],
            "geometry_test": "MULTIPOLYGON(((40 40,20 45,45 30,40 40)),((20 35,45 20,30 5,10 10,10 30,20 35),(30 20,20 25,20 15,30 20)))",
            "last_location_point": {
                "lon": 12.123,
                "lat": 21.213
            }
        },
        "tags": []
    }
    

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
    
    
    {
        "count": 2,
        "results": [
            {
                "id": "1",
                "url": "http://localhost/Lamu/httpdocs/api/v2/posts/1",
                "parent": null,
                "user": null,
                "form": {
                    "id": "1",
                    "url": "http://localhost/Lamu/httpdocs/api/v2/forms/1"
                },
                "title": "Test post",
                "content": "Testing post",
                "status": "published",
                "type": "report",
                "slug": null,
                "locale": "en_us",
                "created": "1970-01-01T00:00:00+00:00",
                "updated": "1970-01-01T00:00:00+00:00",
                "values": {
                    "missing_status": "believed_missing",
                    "links": [
                        {
                            "id": "11",
                            "value": "http://google.com"
                        },
                        {
                            "id": "12",
                            "value": "http://ushahidi.com"
                        }
                    ],
                    "geometry_test": "MULTIPOLYGON(((40 40,20 45,45 30,40 40)),((20 35,45 20,30 5,10 10,10 30,20 35),(30 20,20 25,20 15,30 20)))",
                    "last_location_point": {
                        "lon": 12.123,
                        "lat": 21.213
                    }
                },
                "tags": []
            }
        ],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "created",
        "curr": "https://ushv3.dev/api/v2/sets/1/posts/?limit=50&offset=0",
        "next": "https://ushv3.dev/api/v2/sets/1/posts/?limit=50&offset=50",
        "prev": "https://ushv3.dev/api/v2/sets/1/posts/?limit=50&offset=0"
    }
    

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
    
    
    {
        "id": "1",
        "url": "http://localhost/Lamu/httpdocs/api/v2/posts/1",
        "parent": null,
        "user": null,
        "form": {
            "id": "1",
            "url": "http://localhost/Lamu/httpdocs/api/v2/forms/1"
        },
        "title": "Test post",
        "content": "Testing post",
        "status": "published",
        "type": "report",
        "slug": null,
        "locale": "en_us",
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "1970-01-01T00:00:00+00:00",
        "values": {
            "missing_status": "believed_missing",
            "links": [
                {
                    "id": "11",
                    "value": "http://google.com"
                },
                {
                    "id": "12",
                    "value": "http://ushahidi.com"
                }
            ],
            "geometry_test": "MULTIPOLYGON(((40 40,20 45,45 30,40 40)),((20 35,45 20,30 5,10 10,10 30,20 35),(30 20,20 25,20 15,30 20)))",
            "last_location_point": {
                "lon": 12.123,
                "lat": 21.213
            }
        },
        "tags": []
    }
    

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
    
    
    {
        "id": "1",
        "url": "http://localhost/Lamu/httpdocs/api/v2/posts/1",
        "parent": null,
        "user": null,
        "form": {
            "id": "1",
            "url": "http://localhost/Lamu/httpdocs/api/v2/forms/1"
        },
        "title": "Test post",
        "content": "Testing post",
        "status": "published",
        "type": "report",
        "slug": null,
        "locale": "en_us",
        "created": "1970-01-01T00:00:00+00:00",
        "updated": "1970-01-01T00:00:00+00:00",
        "values": {
            "missing_status": "believed_missing",
            "links": [
                {
                    "id": "11",
                    "value": "http://google.com"
                },
                {
                    "id": "12",
                    "value": "http://ushahidi.com"
                }
            ],
            "geometry_test": "MULTIPOLYGON(((40 40,20 45,45 30,40 40)),((20 35,45 20,30 5,10 10,10 30,20 35),(30 20,20 25,20 15,30 20)))",
            "last_location_point": {
                "lon": 12.123,
                "lat": 21.213
            }
        },
        "tags": []
    }
    

