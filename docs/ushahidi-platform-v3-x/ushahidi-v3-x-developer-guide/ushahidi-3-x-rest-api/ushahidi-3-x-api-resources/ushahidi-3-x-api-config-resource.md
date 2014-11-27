# Ushahidi 3.x API Config Resource



The config API endpoint is a special case. Because we're using Kohana's config
classes under the hood we only really have 2 operations: get - HTTP GET - and
set - HTTP PUT. You can use PUT to both create or update a config item.

  * POST config
  * GET config/:group
    * Config group example
  * GET config/:group/:id
  * PUT config/:group/:id
  * DELETE config/:group/:id

# POST config

The config API does not support POST.

**METHOD**: POST  
**ENDPOINT**: /api/v2/config/

# GET config/:group

Listing all config entries

**METHOD**: GET  
**ENDPOINT**: /api/v2/config/:group  
**AUTHENTICATED**: No

##### Query Parameters

Name

|

Type

|

Description  
  
---|---|---  
  
group

|

Optional

|

The group name to return config entries for  
  
##### Example Request

GET https://ushv3.dev/api/v2/config  

**Response**

## Config group example

GET  https://ushv3.dev/api/v2/config/test

**Response**

# GET config/:group/:id

Get a single config entry

**METHOD**: GET  
**ENDPOINT**: /api/v2/config/:group/:id  
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

The config key of the config entry  
  
group| Required| The group name of the config entry  
  
##### Example Request

GET http://ushv3.dev/api/v2/config/site/site_name

**Response**

# PUT config/:group/:id

Update a config entry

**METHOD**: PUT  
**ENDPOINT**: /api/v2/config/:group/:id  
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

The config key of the config entry being updated.  
  
group| Required| The group name of the config entry  
  
##### Example Request

PUT http://ushv3.dev/api/v2/config/site/site_name

**Post Data**

**Response**

# DELETE config/:group/:id

The config API does not support DELETE.

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/config/:id  

