# Ushahidi 3.x API Form Attributes Resource



FEATURE: COMPLETEDOCS: UP TO DATE

  * POST attributes
  * GET attributes
  * GET attributes/:id
  * PUT attributes/:id
  * DELETE attributes/:id

# POST attributes

Create a attribute

**METHOD**: POST  
**ENDPOINT**: /api/v2/attributes/  
**AUTHENTICATED**: No

The request body is a JSON representation of the attribute being created.

The "form_group" is required when creating an attribute, since attribute
creation without a group isn't very useful. However attributes can be in
multiple forms/groups, and can be orphaned later when a group is removed.

##### Example request

POST https://ushv3.dev/api/v2/attributes

**Post Data**
    
    
    {
        "form_group":1,
        "key":"full_name",
        "label":"Full Name",
        "type":"varchar",
        "input":"text",
        "required":true,
        "default":"",
        "unique":false,
        "priority":1
        "options":{}
    }
    

**Response**
    
    
    {
        "id":2,
        "url":"https://ushv3.dev/api/v2/attributes/2",
        "key":"full_name",
        "label":"Full Name",
        "input":"text",
        "type":"varchar",
        "required":true,
        "default":null,
        "unique":false,
        "priority":1
        "options":{}
    }
    

# GET attributes

Listing all attributes

**METHOD**: GET  
**ENDPOINT**: /api/v2/attributes/  
**AUTHENTICATED**: No

##### Query Parameters (not yet implemented)

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

Only attributes containing this search string will be returned, matched
against 'tag' property  
  
type

|

Optional

|

Only attributes of this type will be returned: report, revision, comment or
alert  
  
order

|

Optional

|

Returned attributes will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned attributes will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

attributes returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/attributes

**Response**
    
    
    {
        "count": 4,
        "results":[
            {
                "url":"https://ushv3.dev/api/v2/forms/1/attributes/1",
                "id":"1",
                "key":"full_name",
                "label":"Full Name",
                "type":"varchar",
                "input":"text",
                "required":true,
                "default":null,
                "unique":false,
                "priority":1
                "options":{}
            },
            {
                "url":"https://ushv3.dev/api/v2/forms/1/attributes/2",
                "id":"2",
                "key":"last_name",
                "label":"Last Name",
                "type":"varchar",
                "input":"text",
                "required":false,
                "default":null,
                "unique":false,
                "priority":2
                "options":{}
            },
            {
                "url":"https://ushv3.dev/api/v2/attributes/3",
                "id":"3",
                "key":"address",
                "label":"Address",
                "type":"varchar",
                "input":"text",
                "required":false,
                "default":"",
                "unique":false,
                "priority":3
                "options":{}
            },
            {
                "url":"https://ushv3.dev/api/v2/attributes/4",
                "id":"4",
                "key":"phone",
                "label":"Phone",
                "type":"varchar",
                "input":"text",
                "required":false,
                "default":"",
                "unique":false,
                "priority":4
                "options":{}
            }
        ]
    }
    

  

# GET attributes/:id

Get a singleattribute

**METHOD**: GET  
**ENDPOINT**: /api/v2/attributes/:id  
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

The numerical id of the attribute being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/attributes/1

**Response**
    
    
    {
        "url":"https://ushv3.dev/api/v2/attributes/2",
        "id":2,
        "key":"full_name",
        "label":"Full Name",
        "type":"varchar",
        "input":"text",
        "required":true,
        "default":null,
        "unique":false,
        "priority":1
        "options":{}
    }
    

# PUT attributes/:id

Update aattribute

**METHOD**: PUT  
**ENDPOINT**: /api/v2/attributes/:id  
**AUTHENTICATED**: Yes

Note: form_group isn't required or used when updating an attribute. To
add/remove attributes from groups use the Groups api resource.

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

The numerical id of the attribute being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/attributes/1

**Post Data**
    
    
    {
        "key":"full_name",
        "label":"Full Name",
        "type":"varchar",
        "input":"text",
        "required":true,
        "default":"",
        "unique":false,
        "priority":1
        "options":{}
    }
    

**Response**
    
    
    {
        "url":"https://ushv3.dev/api/v2/attributes/2",
        "id":2,
        "key":"full_name",
        "label":"Full Name",
        "type":"varchar",
        "input":"text",
        "required":true,
        "default":null,
        "unique":false,
        "priority":1
        "options":{}
    }
    

# DELETE attributes/:id

Deleting aattribute

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/attributes/:id  
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

The numerical id of the attribute being deleted.  
  
##### Example request

DELETE api/v2/attributes/2

**Response**
    
    
    {
        "url":"https://ushv3.dev/api/v2/attributes/2",
        "id":2,
        "key":"full_name",
        "label":"Full Name",
        "type":"varchar",
        "input":"text",
        "required":true,
        "default":null,
        "unique":false,
        "priority":1
        "options":{}
    }
    

