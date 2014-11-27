# Ushahidi 3.x API Posts GeoJSON



Posts GeoJSON Api returns Posts in GeoJSON format. The API accepts the same
params as the standard Posts API, but is read-only and only accepts GET
requests.

  * GET posts
    * Bounding Box Search Example
    * Specific 'geometry_attribute' Example
  * GET posts/:id
  * GET posts/geojson/:z/:x/:y

  

# GET posts

Listing all posts

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/geojson  
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
bbox| Optional| Returned posts will have a point attribute within the
specified bounding box. bbox expects lat lon values as follows:
west,north,east,south  
**geometry_attribute**| **Optional**| **Returned GeoJSON will only include geometries for the specified attribute**  
order| Optional| Returned posts will be sorted in this order: ASC or DESC.
Default: DESC  
order_by| Optional| Returned posts will be sorted by this field. Default:
created  
limit| Optional| Limit number of results returned. Default: 50. Max: 500  
offset| Optional| Posts returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/posts/geojson

**Response**
    
    
    {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "GeometryCollection",
                "geometries": [{
                    "type": "Point",
                    "coordinates": [12.123, 21.213]
                }, {
                    "type": "MultiPolygon",
                    "coordinates": [
                        [
                            [
                                [40, 40],
                                [20, 45],
                                [45, 30],
                                [40, 40]
                            ]
                        ],
                        [
                            [
                                [20, 35],
                                [45, 20],
                                [30, 5],
                                [10, 10],
                                [10, 30],
                                [20, 35]
                            ]
                        ],
                        [
                            [
                                [30, 20],
                                [20, 25],
                                [20, 15],
                                [30, 20]
                            ]
                        ]
                    ]
                }]
            },
            "properties": {
                "title": "Test post",
                "description": "Testing post",
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/1"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "GeometryCollection",
                "geometries": [{
                    "type": "Point",
                    "coordinates": [1, 1]
                }, {
                    "type": "Point",
                    "coordinates": [1.2, 0.5]
                }]
            },
            "properties": {
                "title": "OAuth test post",
                "description": "Testing oauth posts api access",
                "id": "95",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/95"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [1, 1]
            },
            "properties": {
                "title": "search by attribute",
                "description": "Some description",
                "id": "97",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/97"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [10.123, 26.213]
            },
            "properties": {
                "title": "another report",
                "description": "Some description",
                "id": "98",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/98"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [11.123, 24.213]
            },
            "properties": {
                "title": "Should be returned when Searching",
                "description": "Some description",
                "id": "99",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/99"
            }
        }]
    }
    

## Bounding Box Search Example

GET  https://ushv3.dev/api/v2/posts/geojson?bbox=-2,-2,2,2

**Response**
    
    
    {
        "type": "FeatureCollection",
        "bbox": [-2, -2, 2, 2],
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "GeometryCollection",
                "geometries": [{
                    "type": "Point",
                    "coordinates": [1, 1]
                }, {
                    "type": "Point",
                    "coordinates": [1.2, 0.5]
                }]
            },
            "properties": {
                "title": "OAuth test post",
                "description": "Testing oauth posts api access",
                "id": "95",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/95"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [1, 1]
            },
            "properties": {
                "title": "search by attribute",
                "description": "Some description",
                "id": "97",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/97"
            }
        }]
    }
    

## Specific 'geometry_attribute' Example

GET  https://ushv3.dev/api/v2/posts/geojson?geometry_attribute=second_point

**Response**
    
    
    {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [1.2, 0.5]
            },
            "properties": {
                "title": "OAuth test post",
                "description": "Testing oauth posts api access",
                "id": "95",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/95"
            }
        }]
    }
    

# GET posts/:id

Get a singlepost

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/:id/geojson  
**AUTHENTICATED**: Yes

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the post being retrieved.  
  
##### Example Request

GET http://ushv3.dev/api/v2/posts/1/geojson

**Response**
    
    
    {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "GeometryCollection",
                "geometries": [{
                    "type": "Point",
                    "coordinates": [12.123, 21.213]
                }, {
                    "type": "MultiPolygon",
                    "coordinates": [
                        [
                            [
                                [40, 40],
                                [20, 45],
                                [45, 30],
                                [40, 40]
                            ]
                        ],
                        [
                            [
                                [20, 35],
                                [45, 20],
                                [30, 5],
                                [10, 10],
                                [10, 30],
                                [20, 35]
                            ]
                        ],
                        [
                            [
                                [30, 20],
                                [20, 25],
                                [20, 15],
                                [30, 20]
                            ]
                        ]
                    ]
                }]
            },
            "properties": {
                "title": "Test post",
                "description": "Testing post",
                "id": "1",
                "url": "http:\/\/ushv3.dev\/api\/v2\/posts\/1"
            }
        }]
    }
    

# GET posts/geojson/:z/:x/:y

Get tiled geojson response

**METHOD**: GET  
**ENDPOINT**: /api/v2/posts/geojson/:z/:x/:y  
**AUTHENTICATED**: No

##### Query Parameters

Name| Type| Description  
---|---|---  
**z**| **Required**| **Zoom level**  
**x**| **Required**| **Tile x offset**  
**y**| **Required**| **Tile y offset**  
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
bbox| Optional| Returned posts will have a point attribute within the
specified bounding box. bbox expects lat lon values as follows:
west,north,east,south  
geometry_attribute| Optional| Returned GeoJSON will only include geometries
for the specified attribute  
order| Optional| Returned posts will be sorted in this order: ASC or DESC.
Default: DESC  
order_by| Optional| Returned posts will be sorted by this field. Default:
created  
limit| Optional| Limit number of results returned. Default: 50. Max: 500  
offset| Optional| Posts returned will be offset by this number of results  
  
##### Example Request

GET  https://ushv3.dev/api/v2/posts/geojson/1/1/0

**Response**
    
    
    {
        "type": "FeatureCollection",
        "bbox": [0, 85.051128779807, 180, 0],
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "GeometryCollection",
                "geometries": [{
                    "type": "Point",
                    "coordinates": [12.123, 21.213]
                }, {
                    "type": "MultiPolygon",
                    "coordinates": [
                        [
                            [
                                [40, 40],
                                [20, 45],
                                [45, 30],
                                [40, 40]
                            ]
                        ],
                        [
                            [
                                [20, 35],
                                [45, 20],
                                [30, 5],
                                [10, 10],
                                [10, 30],
                                [20, 35]
                            ]
                        ],
                        [
                            [
                                [30, 20],
                                [20, 25],
                                [20, 15],
                                [30, 20]
                            ]
                        ]
                    ]
                }]
            },
            "properties": {
                "title": "Test post",
                "description": "Testing post",
                "id": "1",
                "url": "http:\/\/ushv3.dev\/deployment\/httpdocs\/api\/v2\/posts\/1"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [11.123, 24.213]
            },
            "properties": {
                "title": "Should be returned when Searching",
                "description": "Some description",
                "id": "99",
                "url": "http:\/\/ushv3.dev\/deployment\/httpdocs\/api\/v2\/posts\/99"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [10.123, 26.213]
            },
            "properties": {
                "title": "another report",
                "description": "Some description",
                "id": "98",
                "url": "http:\/\/ushv3.dev\/deployment\/httpdocs\/api\/v2\/posts\/98"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "GeometryCollection",
                "geometries": [{
                    "type": "Point",
                    "coordinates": [1, 1]
                }, {
                    "type": "Point",
                    "coordinates": [1.2, 0.5]
                }]
            },
            "properties": {
                "title": "OAuth test post",
                "description": "Testing oauth posts api access",
                "id": "95",
                "url": "http:\/\/ushv3.dev\/deployment\/httpdocs\/api\/v2\/posts\/95"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [1, 1]
            },
            "properties": {
                "title": "search by attribute",
                "description": "Some description",
                "id": "97",
                "url": "http:\/\/ushv3.dev\/deployment\/httpdocs\/api\/v2\/posts\/97"
            }
        }]
    }
    

