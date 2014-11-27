# Ushahidi 3.x API Media Resource



FEATURE: IN PROGRESSDOCS: UP TO DATE

  * POST media
  * GET media
  * GET media/:id
  * DELETE media/:id

# POST media

Create a media

**METHOD**: POST  
**ENDPOINT**: /api/v2/media/  
**AUTHENTICATED**: YES

Make a **multipart/form-data****POST** request with the following parameters.

##### Form Parameters

Name| Type| Description  
---|---|---  
file| Required| The path to the image. Supported types are gif,jpg,jpeg,png  
caption| Optional| A short title or caption for the image to be uploaded  
  
POST https://ushv3.dev/api/v2/media

**Response**
    
    
    {
       "id": "3",
       "url": "https://ushv3.dev/api/v2/media/3",
       "caption": "ihub",
       "mime": "image/jpeg",
       "original_file_url": "https://ushv3.dev/api/v2/media/kohana/uploads/9ze_1381815819_o.jpg",
       "original_width": "600",
       "original_height": "700",
       "medium_file_url": "https://ushv3.dev/api/v2/imagefly/w800/uploads/9ze_1381815819_o.jpg",
       "medium_width": 800,
       "medium_height": null,
       "thumbnail_file_url": "https://ushv3.dev/api/v2/imagefly/w70/uploads/9ze_1381815819_o.jpg",
       "thumbnail_width": 70,
       "thumbnail_height": null,
       "created": "2013-10-15T05:43:41+00:00",
       "updated": "2013-10-15T05:43:39+00:00"
    }
    

##### Example request

# GET media

Listing all media

**METHOD**: GET  
**ENDPOINT**: /api/v2/media/  
**AUTHENTICATED**: No

##### Query Parameters

Name

|

Type

|

Description  
  
---|---|---  
  
order

|

Optional

|

Returned media will be sorted in this order: ASC or DESC. Default: DESC  
  
order_by

|

Optional

|

Returned media will be sorted by this field. Default: created  
  
limit

|

Optional

|

Limit number of results returned. Default: 50. Max: 500  
  
offset

|

Optional

|

Media returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/media

**Response**
    
    
    {
        "count": 2,
        "results":
        [
          {
                "url": "https://ushv3.dev/api/v2/media/3",
                "caption": "ihub",
                "mime": "image/jpeg",
                "original_file_url": "https://ushv3.dev/media/kohana/uploads/9ze_1381815819_o.jpg",
                "original_width": "600",
                "original_height": "700",
                "medium_file_url": "https://ushv3.dev/imagefly/w800/uploads/9ze_1381815819_o.jpg",
                "medium_width": 800,
                "medium_height": null,
                "thumbnail_file_url": "https://ushv3.dev/Lamu/httpdocs/imagefly/w70/uploads/9ze_1381815819_o.jpg",
                "thumbnail_width": 70,
                "thumbnail_height": null,
                "created": "2013-10-15T05:43:41+00:00",
                "updated": "2013-10-15T05:43:39+00:00"
            },
            {
                "id": "2",
                "url": "https://ushv3.dev/api/v2/media/2",
                "caption": "at sendai",
                "mime": "image/jpeg",
                "original_file_url": "https://ushv3.dev/media/kohana/uploads/9ze_1381815819_o.jpg",
                "original_width": "500",
                "original_height": "600",
                "medium_file_url": "https://ushv3.dev/imagefly/w800/uploads/9ze_1381815819_o.jpg",
                "medium_width": 800,
                "medium_height": null,
                "thumbnail_file_url": "https://ushv3.dev/imagefly/w70/uploads/9ze_1381815819_o.jpg",
                "thumbnail_width": 70,
                "thumbnail_height": null,
                "created": "2013-10-15T05:43:41+00:00",
                "updated": "2013-10-15T05:43:39+00:00"
            }
        ],
        "limit": 50,
        "offset": 0,
        "order": "DESC",
        "orderby": "id",
        "curr": "https://ushv3.dev/api/v2/media?access_token=testingtoken&limit=50&offset=0",
        "next": "https://ushv3.dev/api/v2/media?access_token=testingtoken&limit=50&offset=50",
        "prev": "https://ushv3.dev/api/v2/media?access_token=testingtoken&limit=50&offset=0"
    }
    

# GET media/:id

Get a single media

**METHOD**: GET  
**ENDPOINT**: /api/v2/media/:id  
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

The numerical id of the media being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/media/1

**Response**
    
    
    {
        "id": "3",
        "url": "https://ushv3.dev/api/v2/media/3",
        "caption": "ihub",
        "mime": "image/jpeg",
        "original_file_url": "https://ushv3.dev/media/kohana/uploads/9ze_1381815819_o.jpg",
        "original_width": "600",
        "original_height": "700",
        "medium_file_url": "https://ushv3.dev/imagefly/w800/uploads/9ze_1381815819_o.jpg",
        "medium_width": 800,
        "medium_height": null,
        "thumbnail_file_url": "https://ushv3.dev/imagefly/w70/uploads/9ze_1381815819_o.jpg",
        "thumbnail_width": 70,
        "thumbnail_height": null,
        "created": "2013-10-15T05:43:41+00:00",
        "updated": "2013-10-15T05:43:39+00:00"
    }
    

# DELETE media/:id

Deleting a media

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/media/:id  
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

The numerical id of the media being deleted.  
  
##### Example request

DELETE /api/v2/media/2

**Response**
    
    
    {
    	
        "id": "2",
        "url": "https://ushv3.dev/api/v2/media/2",
        "caption": "at sendai",
        "mime": "image/jpeg",
        "original_file_url": "https://ushv3.dev/media/kohana/uploads/9ze_1381815819_o.jpg",
        "original_width": "500",
        "original_height": "600",
        "medium_file_url": "https://ushv3.dev/imagefly/w800/uploads/9ze_1381815819_o.jpg",
        "medium_width": 800,
        "medium_height": null,
        "thumbnail_file_url": "https://ushv3.dev/imagefly/w70/uploads/9ze_1381815819_o.jpg",
        "thumbnail_width": 70,
        "thumbnail_height": null,
        "created": "2013-10-15T05:43:41+00:00",
        "updated": "2013-10-15T05:43:39+00:00"
    }
    

