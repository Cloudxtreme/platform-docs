# Ushahidi 3.x API Tags Resource



FEATURE: COMPLETEDOCS: UP TO DATE

  * POST tags
  * GET tags
    * Search Example
  * GET tags/:id
  * PUT tags/:id
  * DELETE tags/:id

# POST tags

Create a Tag

**METHOD**: POST  
**ENDPOINT**: /api/v2/tags/  
**AUTHENTICATED**: No

The request body is a JSON representation of the [Ushahidi 3.x API Tags
Resource](/display/WIKI/Ushahidi+3.x+API+Tags+Resource) being created.

##### Example request

POST https://ushv3.dev/api/v2/tags

**Post Data**
    
    
    {
        "tag":"Boxes",
        "slug":"boxes",
        "type":"category",
        "priority":1
    }
    

**Response**
    
    
    {
        "id": 7,
        "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/7",
        "parent": null,
        "tag": "Boxes",
        "slug": "boxes",
        "type": "category",
        "priority": 1,
        "created": "2013-05-07T22:06:14+00:00"
    }
    

# GET tags

Listing all tags

**METHOD**: GET  
**ENDPOINT**: /api/v2/tags/  
**AUTHENTICATED**: No

##### Query Parameters

Name| Type| Description  
---|---|---  
q| Optional| Only Tags containing this search string will be returned, matched
against 'tag' property  
type| Optional| Only tags of this type will be returned: category, status  
parent| Optional| Only tags with a matching parent_id will be returned  
tag| Optional| Only tags with a matching tag will be returned  
order| Optional| Returned tags will be sorted in this order: ASC or DESC.
Default: ASC  
order_by| Optional| Returned tags will be sorted by this field. Default:
priority  
limit| Optional| Limit number of results returned. Default: 50. Max: 500  
offset| Optional| Tags returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/tags

**Response**
    
    
    {
        "count": 8,
        "results": [{
            "id": "2",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/2",
            "parent": null,
            "tag": "Duplicate",
            "slug": "duplicate",
            "type": "category",
            "priority": "0",
            "created": "2013-05-07T22:06:14+00:00"
        }, {
            "id": "3",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/3",
            "parent": null,
            "tag": "Disaster",
            "slug": "disaster",
            "type": "category",
            "priority": "0",
            "created": "2013-05-07T22:06:14+00:00"
        }, {
            "id": "4",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/4",
            "parent": {
                "id": "3",
                "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/3"
            },
            "tag": "Explosion",
            "slug": "explosion",
            "type": "category",
            "priority": "0",
            "created": "2013-05-07T22:06:14+00:00"
        }, {
            "id": "5",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/5",
            "parent": null,
            "tag": "Todo",
            "slug": "todo",
            "type": "status",
            "priority": "0",
            "created": "2013-05-07T22:06:14+00:00"
        }, {
            "id": "6",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/6",
            "parent": null,
            "tag": "Done",
            "slug": "done",
            "type": "status",
            "priority": "0",
            "created": "2013-05-07T22:06:14+00:00"
        }, {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/1",
            "parent": null,
            "tag": "Updated",
            "slug": "updated",
            "type": "status",
            "priority": "1",
            "created": "2013-05-07T22:06:14+00:00"
        }, {
            "id": "7",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/7",
            "parent": null,
            "tag": "Boxes",
            "slug": "boxes",
            "type": "category",
            "priority": "1",
            "created": "2013-05-07T22:06:14+00:00"
        }, {
            "id": "8",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/8",
            "parent": null,
            "tag": "My magical tag",
            "slug": "my-magical-tag",
            "type": "category",
            "priority": "1",
            "created": "2013-05-07T22:06:14+00:00"
        }],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "priority",
        "curr": "http:\/\/ushv3.dev\/api\/v2\/tags?limit=50&offset=0",
        "next": "http:\/\/ushv3.dev\/api\/v2\/tags?limit=50&offset=50",
        "prev": "http:\/\/ushv3.dev\/api\/v2\/tags?limit=50&offset=0"
    }
    

## Search Example

GET  https://ushv3.dev/api/v2/tags?q=Explo

**Response**
    
    
    {
        "count": 1,
        "results": [{
            "id": "4",
            "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/4",
            "parent": {
                "id": "3",
                "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/3"
            },
            "tag": "Explosion",
            "slug": "explosion",
            "type": "category",
            "priority": "0",
            "created": "2013-05-07T22:06:14+00:00"
        }],
        "limit": 50,
        "offset": 0,
        "order": "ASC",
        "orderby": "priority",
        "curr": "http:\/\/ushv3.dev\/api\/v2\/tags?q=Explo&limit=50&offset=0",
        "next": "http:\/\/ushv3.dev\/api\/v2\/tags?q=Explo&limit=50&offset=50",
        "prev": "http:\/\/ushv3.dev\/api\/v2\/tags?q=Explo&limit=50&offset=0"
    }
    

# GET tags/:id

Get a single tag

**METHOD**: GET  
**ENDPOINT**: /api/v2/tags/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the tag being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/tags/1

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/1",
        "parent": null,
        "tag": "Updated",
        "slug": "updated",
        "type": "status",
        "priority": "1",
        "created": "2013-05-07T22:06:14+00:00"
    }
    

# PUT tags/:id

Update a tag

**METHOD**: PUT  
**ENDPOINT**: /api/v2/tags/:id  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the tag being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/tags/1

**Post Data**
    
    
    {
        "tag":"Updated",
        "slug":"updated",
        "type":"status",
        "priority":1
    }
    

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/1",
        "parent": null,
        "tag": "Updated",
        "slug": "updated",
        "type": "status",
        "priority": 1,
        "created": "2013-05-07T22:06:14+00:00"
    }
    

# DELETE tags/:id

Deleting a tag

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/tags/:id  
**AUTHENTICATED**: YES

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the tag being deleted.  
  
##### Example request

DELETE /api/v2/tags/2

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/tags\/1",
        "parent": null,
        "tag": "Updated",
        "slug": "updated",
        "type": "status",
        "priority": "1",
        "created": "2013-05-07T22:06:14+00:00"
    }
    

