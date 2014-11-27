# Ushahidi 3.x API Messages Resource



  * POST messages
  * GET messages
    * Search Example
  * GET messages/:id
  * PUT messages/:id
  * DELETE messages/:id

# POST messages

Create a message

Note: Only outgoing messages can be created through the API. Incoming messages
are created by data provider modules.

**METHOD**: POST  
**ENDPOINT**: /api/v2/messages/  
**AUTHENTICATED**: No

The request body is a JSON representation of the message being created.

##### Example request

POST https://ushv3.dev/api/v2/messages

**Post Data**
    
    
    {
        "message": "Test creating outgoing",
        "type": "sms",
        "direction": "outgoing",
        "contact_id": "1"
    }
    

**Response**
    
    
    {
        "id": 9,
        "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/9",
        "parent": null,
        "contact": {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/1",
            "user": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1"
            },
            "contact": "123456789",
            "type": "phone",
            "data_provider": "",
            "created": "1970-01-01T00:00:00+00:00"
        },
        "data_feed": null,
        "post": null,
        "data_provider": null,
        "data_provider_message_id": null,
        "title": null,
        "message": "Test creating outgoing",
        "datetime": null,
        "type": "sms",
        "status": "pending",
        "direction": "outgoing",
        "created": "2014-01-17T03:23:43+00:00",
        "allowed_methods": {
            "get": true,
            "post": true,
            "put": true,
            "delete": true
        }
    }
    

# GET messages

Listing all messages

**METHOD**: GET  
**ENDPOINT**: /api/v2/messages/  
**AUTHENTICATED**: No

##### Query Parameters

Note with no parameters the messages API defaults to returning messages with
_direction =_ _incoming_ and _status != archived._

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

Only messages containing this search string will be returned, matched against
'title' and 'message' properties  
  
type

|

Optional

|

Only messages of this type will be returned: report, revision, comment or
alert  
  
direction| Optional| Filter messages based on direction. incoming or outgoing.
Default: incoming  
status| Optional|

Filter messages based on status.  
Options: pending, pending_poll, archived, received, expired, cancelled,
failed, unknown, sent, all.  
Default: != archived  
  
parent| Optional| Filter by parent message id  
contact| Optional| Filter by contact id  
data_feed| Optional| Filter by data feed id  
data_provider| Optional| Filter by data provider id  
post| Optional| Filter by post id  
  
order

|

Optional

|

Returned messages will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned messages will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

messages returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/messages

**Response**
    
    
    {
        "count": 5,
        "total_count": 5,
        "results": [{
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/1",
            "parent": null,
            "contact": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/1",
                "user": {
                    "id": "1",
                    "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1"
                },
                "contact": "123456789",
                "type": "phone",
                "data_provider": "",
                "created": "1970-01-01T00:00:00+00:00"
            },
            "data_feed": null,
            "post": null,
            "data_provider": null,
            "data_provider_message_id": null,
            "title": "abc",
            "message": "A test message",
            "datetime": null,
            "type": "sms",
            "status": "received",
            "direction": "incoming",
            "created": "1970-01-01T00:00:00+00:00",
            "allowed_methods": {
                "get": true,
                "post": true,
                "put": true,
                "delete": true
            }
        }, {
            "id": "2",
            "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/2",
            "parent": null,
            "contact": {
                "id": "3",
                "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/3",
                "user": null,
                "contact": "773456789",
                "type": "phone",
                "data_provider": "",
                "created": "1970-01-01T00:00:00+00:00"
            },
            "data_feed": null,
            "post": null,
            "data_provider": null,
            "data_provider_message_id": null,
            "title": "",
            "message": "Another test message",
            "datetime": null,
            "type": "sms",
            "status": "received",
            "direction": "incoming",
            "created": "1970-01-01T00:00:00+00:00",
            "allowed_methods": {
                "get": true,
                "post": true,
                "put": true,
                "delete": true
            }
        }, {
            "id": "3",
            "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/3",
            "parent": null,
            "contact": {
                "id": "2",
                "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/2",
                "user": null,
                "contact": "somejunkemail@v3.ushahidi.com",
                "type": "email",
                "data_provider": "",
                "created": "1970-01-01T00:00:00+00:00"
            },
            "data_feed": null,
            "post": null,
            "data_provider": null,
            "data_provider_message_id": null,
            "title": "Test email",
            "message": "test email body abc",
            "datetime": "2013-01-02T07:07:00+00:00",
            "type": "email",
            "status": "received",
            "direction": "incoming",
            "created": "1970-01-01T00:00:00+00:00",
            "allowed_methods": {
                "get": true,
                "post": true,
                "put": true,
                "delete": true
            }
        }, {
            "id": "4",
            "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/4",
            "parent": null,
            "contact": {
                "id": "3",
                "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/3",
                "user": null,
                "contact": "773456789",
                "type": "phone",
                "data_provider": "",
                "created": "1970-01-01T00:00:00+00:00"
            },
            "data_feed": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/datafeeds\/1"
            },
            "post": {
                "id": "110",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/110"
            },
            "data_provider": null,
            "data_provider_message_id": null,
            "title": "",
            "message": "Another message with a post",
            "datetime": null,
            "type": "sms",
            "status": "received",
            "direction": "incoming",
            "created": "1970-01-01T00:00:00+00:00",
            "allowed_methods": {
                "get": true,
                "post": true,
                "put": true,
                "delete": true
            }
        }, {
            "id": "5",
            "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/5",
            "parent": null,
            "contact": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/1",
                "user": {
                    "id": "1",
                    "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1"
                },
                "contact": "123456789",
                "type": "phone",
                "data_provider": "",
                "created": "1970-01-01T00:00:00+00:00"
            },
            "data_feed": null,
            "post": null,
            "data_provider": "smssync",
            "data_provider_message_id": null,
            "title": "",
            "message": "A test message with provider",
            "datetime": null,
            "type": "sms",
            "status": "received",
            "direction": "incoming",
            "created": "1970-01-01T00:00:00+00:00",
            "allowed_methods": {
                "get": true,
                "post": true,
                "put": true,
                "delete": true
            }
        }],
        "limit": 50,
        "offset": 0,
        "order": "DESC",
        "orderby": "created",
        "curr": "http:\/\/ushv3.dev\/api\/v2\/messages?limit=50&offset=0",
        "next": "http:\/\/ushv3.dev\/api\/v2\/messages?limit=50&offset=50",
        "prev": "http:\/\/ushv3.dev\/api\/v2\/messages?limit=50&offset=0"
    }
    

## Search Example

GET  https://ushv3.dev/api/v2/messages?q=abc

**Response**
    
    
    {
        "count": 2,
        "total_count": 2,
        "results": [{
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/1",
            "parent": null,
            "contact": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/1",
                "user": {
                    "id": "1",
                    "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1"
                },
                "contact": "123456789",
                "type": "phone",
                "data_provider": "",
                "created": "1970-01-01T00:00:00+00:00"
            },
            "data_feed": null,
            "post": null,
            "data_provider": null,
            "data_provider_message_id": null,
            "title": "abc",
            "message": "A test message",
            "datetime": null,
            "type": "sms",
            "status": "received",
            "direction": "incoming",
            "created": "1970-01-01T00:00:00+00:00",
            "allowed_methods": {
                "get": true,
                "post": true,
                "put": true,
                "delete": true
            }
        }, {
            "id": "3",
            "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/3",
            "parent": null,
            "contact": {
                "id": "2",
                "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/2",
                "user": null,
                "contact": "somejunkemail@v3.ushahidi.com",
                "type": "email",
                "data_provider": "",
                "created": "1970-01-01T00:00:00+00:00"
            },
            "data_feed": null,
            "post": null,
            "data_provider": null,
            "data_provider_message_id": null,
            "title": "Test email",
            "message": "test email body abc",
            "datetime": "2013-01-02T07:07:00+00:00",
            "type": "email",
            "status": "received",
            "direction": "incoming",
            "created": "1970-01-01T00:00:00+00:00",
            "allowed_methods": {
                "get": true,
                "post": true,
                "put": true,
                "delete": true
            }
        }],
        "limit": 50,
        "offset": 0,
        "order": "DESC",
        "orderby": "created",
        "curr": "http:\/\/ushv3.dev\/api\/v2\/messages?q=abc&limit=50&offset=0",
        "next": "http:\/\/ushv3.dev\/api\/v2\/messages?q=abc&limit=50&offset=50",
        "prev": "http:\/\/ushv3.dev\/api\/v2\/messages?q=abc&limit=50&offset=0"
    }
    

# GET messages/:id

Get a singlemessage

**METHOD**: GET  
**ENDPOINT**: /api/v2/messages/:id  
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

The numerical id of the message being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/messages/1

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/1",
        "parent": null,
        "contact": {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/1",
            "user": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1"
            },
            "contact": "123456789",
            "type": "phone",
            "data_provider": "",
            "created": "1970-01-01T00:00:00+00:00"
        },
        "data_feed": null,
        "post": null,
        "data_provider": null,
        "data_provider_message_id": null,
        "title": "abc",
        "message": "A test message",
        "datetime": null,
        "type": "sms",
        "status": "received",
        "direction": "incoming",
        "created": "1970-01-01T00:00:00+00:00",
        "allowed_methods": {
            "get": true,
            "post": true,
            "put": true,
            "delete": true
        }
    }
    

# PUT messages/:id

Update amessage

**METHOD**: PUT  
**ENDPOINT**: /api/v2/messages/:id  
**AUTHENTICATED**: Yes

Messages updates are subject to special rules depending on if they are
incoming or outgoing

  * Incoming messages only allow updates to 'status'. The message itself cannot be edited
  * Outgoing messages allow most values to be updated as normal

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

The numerical id of the message being updated.  
  
##### Example Request

Archive message, and try to edit the message text.. In this case the message
is status is changed but other changes are ignored.

PUT http://ushv3.dev/api/v2/messages/1

**Post Data**
    
    
    {
        "message": "Overwrite message",
        "status": "archived"
    }
    

**Response**
    
    
    {
        "id": "1",
        "url": "http:\/\/ushv3.dev\/api\/v2\/messages\/1",
        "parent": null,
        "contact": {
            "id": "1",
            "url": "http:\/\/ushv3.dev\/api\/v2\/contacts\/1",
            "user": {
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/users\/1"
            },
            "contact": "123456789",
            "type": "phone",
            "data_provider": "",
            "created": "1970-01-01T00:00:00+00:00"
        },
        "data_feed": null,
        "post": null,
        "data_provider": null,
        "data_provider_message_id": null,
        "title": "abc",
        "message": "A test message",
        "datetime": null,
        "type": "sms",
        "status": "archived",
        "direction": "incoming",
        "created": "1970-01-01T00:00:00+00:00",
        "allowed_methods": {
            "get": true,
            "post": true,
            "put": true,
            "delete": true
        }
    }
    

# DELETE messages/:id

Deleting amessage

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/messages/:id

Messages cannot be deleted through the API.

