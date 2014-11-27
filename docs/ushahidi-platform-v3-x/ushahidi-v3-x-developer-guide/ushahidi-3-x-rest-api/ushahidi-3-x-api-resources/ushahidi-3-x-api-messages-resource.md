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

**Response**

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

## Search Example

GET  https://ushv3.dev/api/v2/messages?q=abc

**Response**

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

**Response**

# DELETE messages/:id

Deleting amessage

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/messages/:id

Messages cannot be deleted through the API.

