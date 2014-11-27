# Ushahidi 3.x API Forms Resource



FEATURE: COMPLETEDOCS: NEED UPDATE

  * POST forms
  * GET forms
  * GET forms/:id
  * PUT forms/:id
  * DELETE forms/:id

# POST forms

Create a Form

**METHOD**: POST  
**ENDPOINT**: /api/v2/forms/  
**AUTHENTICATED**: No

The request body is a JSON representation of the Form being created.Group and
attribute resources can be created at the same time as the form, however these
can only be updated/deleted through their own API endpoints.

##### Example request

POST https://ushv3.dev/api/v2/forms

**Post Data**
    
    
    {
        "name":"Missing Persons Form",
        "type":"report",
        "description":"PFIF Form",
        "groups":[
            {
                "label":"Person Record",
                "priority": 1,
                "attributes":[
                    {
                        "key":"full_name",
                        "label":"Full Name",
                        "type":"varchar",
                        "input":"text",
                        "required":true,
                        "priority":1
                    },
                    {
                        "key":"description",
                        "label":"Description",
                        "type":"text",
                        "input":"textarea",
                        "required":true,
                        "priority":2
                    },
                    {
                        "key":"dob",
                        "label":"Date of Birth",
                        "type":"int",
                        "input":"date",
                        "required":false,
                        "priority":3
                    },
                    {
                        "key":"missing_date",
                        "label":"Missing Date",
                        "type":"int",
                        "input":"date",
                        "required":true,
                        "priority":4
                    },
                    {
                        "key":"last_location",
                        "label":"Last Known Location",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":5
                    },
                    {
                        "key":"status",
                        "label":"Status",
                        "type":"varchar",
                        "input":"select",
                        "required":false,
                        "options":[
                            "Missing",
                            "Alive",
                            "Dead"
                        ],
                        "priority":6
                    }
                ]
            }
        ]
    }
    

**Response**
    
    
    {
        "id":1
        "name":"Missing Persons Form",
        "type":"report",
        "description":"PFIF Form",
        "groups":[
            {
                "label":"Person Record",
                "priority": 1,
                "attributes":[
                    {
                        "key":"full_name",
                        "label":"Full Name",
                        "type":"varchar",
                        "input":"text",
                        "required":true,
                        "priority":1
                    },
                    {
                        "key":"description",
                        "label":"Description",
                        "type":"text",
                        "input":"textarea",
                        "required":true,
                        "priority":2
                    },
                    {
                        "key":"dob",
                        "label":"Date of Birth",
                        "type":"int",
                        "input":"date",
                        "required":false,
                        "priority":3
                    },
                    {
                        "key":"missing_date",
                        "label":"Missing Date",
                        "type":"int",
                        "input":"date",
                        "required":true,
                        "priority":4
                    },
                    {
                        "key":"last_location",
                        "label":"Last Known Location",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":5
                    },
                    {
                        "key":"status",
                        "label":"Status",
                        "type":"varchar",
                        "input":"select",
                        "required":false,
                        "options":[
                            "Missing",
                            "Alive",
                            "Dead"
                        ],
                        "priority":6
                    }
                ]
            }
        ]
    }
    

# GET forms

Listing all Forms

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/  
**AUTHENTICATED**: No

Form attributes and groups are returned along with the form.

##### Query Parameters (no yet implemented)

Name| Type| Description  
---|---|---  
q| Optional| Only forms containing this search string will be returned,
matched against 'tag' property  
order| Optional| Returned forms will be sorted in this order: ASC or DESC.
Default: DESC  
order_by| Optional| Returned forms will be sorted by this field. Default:
created  
limit| Optional| Limit number of results returned. Default: 50. Max: 500  
offset| Optional| Forms returned will be offset by this number of results  
  
##### Example Request

GET https://ushv3.dev/api/v2/forms

**Response**
    
    
    {
        "count": 2,
        "results": [
            {
                "id": "1",
                "name": "Missing Persons Form",
                "description": "PFIF Form",
                "type": "report"
                "groups": [
                    {
                        "id": "1",
                        "label": "Person Record",
                        "priority": "1",
                        "attributes": [
                            {
                                "unique": false,
                                "input": "text",
                                "priority": "99",
                                "id": "1",
                                "options": null,
                                "key": "full_name",
                                "label": "Full Name",
                                "type": "varchar",
                                "required": false,
                                "default": null
                            },
                            {
                                "unique": false,
                                "input": "textarea",
                                "priority": "99",
                                "id": "2",
                                "options": null,
                                "key": "description",
                                "label": "Description",
                                "type": "text",
                                "required": false,
                                "default": null
                            },
                            {
                                "unique": false,
                                "input": "text",
                                "priority": "99",
                                "id": "3",
                                "options": null,
                                "key": "dob",
                                "label": "Date of Birth",
                                "type": "datetime",
                                "required": false,
                                "default": null
                            },
                            {
                                "unique": false,
                                "input": "text",
                                "priority": "99",
                                "id": "4",
                                "options": null,
                                "key": "missing_date",
                                "label": "Missing Date",
                                "type": "datetime",
                                "required": false,
                                "default": null
                            },
                            {
                                "unique": false,
                                "input": "text",
                                "priority": "99",
                                "id": "5",
                                "options": null,
                                "key": "last_location",
                                "label": "Last Known Location",
                                "type": "varchar",
                                "required": false,
                                "default": null
                            },
                            {
                                "unique": false,
                                "input": "select",
                                "priority": "99",
                                "id": "6",
                                "options": [
                                    "Missing",
                                    "Alive",
                                    "Dead"
                                ],
                                "key": "status",
                                "label": "Status",
                                "type": "varchar",
                                "required": false,
                                "default": null
                            }
                        ]
                    }
                ]
            },
            {
                "id": "2",
                ...
            }
        ]
    }
    

  

# GET forms/:id

Get a single form

**METHOD**: GET  
**ENDPOINT**: /api/v2/forms/:id  
**AUTHENTICATED**: Yes

Form attributes and groups are returned along with the form.

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the form being updated.  
  
##### Example Request

GET http://ushv3.dev/api/v2/forms/1

**Response**
    
    
    {
        "id": "1",
        "name": "Missing Persons Form",
        "description": "PFIF Form",
        "type": "report"
        "groups": [
            {
                "id": "1",
                "label": "Person Record",
                "priority": "1",
                "attributes": [
                    {
                        "unique": false,
                        "input": "text",
                        "priority": "99",
                        "id": "1",
                        "options": null,
                        "key": "full_name",
                        "label": "Full Name",
                        "type": "varchar",
                        "required": false,
                        "default": null
                    },
                    {
                        "unique": false,
                        "input": "textarea",
                        "priority": "99",
                        "id": "2",
                        "options": null,
                        "key": "description",
                        "label": "Description",
                        "type": "text",
                        "required": false,
                        "default": null
                    },
                    {
                        "unique": false,
                        "input": "text",
                        "priority": "99",
                        "id": "3",
                        "options": null,
                        "key": "dob",
                        "label": "Date of Birth",
                        "type": "datetime",
                        "required": false,
                        "default": null
                    },
                    {
                        "unique": false,
                        "input": "text",
                        "priority": "99",
                        "id": "4",
                        "options": null,
                        "key": "missing_date",
                        "label": "Missing Date",
                        "type": "datetime",
                        "required": false,
                        "default": null
                    },
                    {
                        "unique": false,
                        "input": "text",
                        "priority": "99",
                        "id": "5",
                        "options": null,
                        "key": "last_location",
                        "label": "Last Known Location",
                        "type": "varchar",
                        "required": false,
                        "default": null
                    },
                    {
                        "unique": false,
                        "input": "select",
                        "priority": "99",
                        "id": "6",
                        "options": [
                            "Missing",
                            "Alive",
                            "Dead"
                        ],
                        "key": "status",
                        "label": "Status",
                        "type": "varchar",
                        "required": false,
                        "default": null
                    }
                ]
            }
        ]
    }
    

# PUT forms/:id

Update a form

**METHOD**: PUT  
**ENDPOINT**: /api/v2/forms/:id  
**AUTHENTICATED**: Yes

Only the form resource itself can be updated. Group and attribute resources
have to be updated through their respective endpoints.

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the form being updated.  
  
##### Example Request

PUT http://ushv3.dev/api/v2/forms/1

**Post Data**
    
    
    {
        "name":"Missing Persons Form",
        "type":"report",
        "description":"PFIF Form",
    }
    

**Response**
    
    
    {
        "id":1
        "name":"Missing Persons Form",
        "type":"report",
        "description":"PFIF Form",
        "groups":[
            {
                "label":"Person Record",
                "priority": 1,
                "attributes":[
                    {
                        "key":"full_name",
                        "label":"Full Name",
                        "type":"varchar",
                        "input":"text",
                        "required":true,
                        "priority":1
                    },
                    {
                        "key":"description",
                        "label":"Description",
                        "type":"text",
                        "input":"textarea",
                        "required":true,
                        "priority":2
                    },
                    {
                        "key":"dob",
                        "label":"Date of Birth",
                        "type":"int",
                        "input":"date",
                        "required":false,
                        "priority":3
                    },
                    {
                        "key":"missing_date",
                        "label":"Missing Date",
                        "type":"int",
                        "input":"date",
                        "required":true,
                        "priority":4
                    },
                    {
                        "key":"last_location",
                        "label":"Last Known Location",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":5
                    },
                    {
                        "key":"status",
                        "label":"Status",
                        "type":"varchar",
                        "input":"select",
                        "required":false,
                        "options":[
                            "Missing",
                            "Alive",
                            "Dead"
                        ],
                        "priority":6
                    }
                ]
            }
        ]
    }
    

# DELETE forms/:id

Deleting a form

**METHOD**: DELETE  
**ENDPOINT**: /api/v2/forms/:id  
**AUTHENTICATED**: YES

Form groups will be deleted along with the form itself. Attributes can belong
to many forms so will not be deleted.

##### Query Parameters

Name| Type| Description  
---|---|---  
id| Required| The numerical id of the form being deleted.  
  
##### Example request

DELETE /api/v2/forms/2

**Response**
    
    
    {
        "id":1
        "name":"Missing Persons Form",
        "type":"report",
        "description":"PFIF Form",
        "groups":[
            {
                "label":"Person Record",
                "priority": 1,
                "attributes":[
                    {
                        "key":"full_name",
                        "label":"Full Name",
                        "type":"varchar",
                        "input":"text",
                        "required":true,
                        "priority":1
                    },
                    {
                        "key":"description",
                        "label":"Description",
                        "type":"text",
                        "input":"textarea",
                        "required":true,
                        "priority":2
                    },
                    {
                        "key":"dob",
                        "label":"Date of Birth",
                        "type":"int",
                        "input":"date",
                        "required":false,
                        "priority":3
                    },
                    {
                        "key":"missing_date",
                        "label":"Missing Date",
                        "type":"int",
                        "input":"date",
                        "required":true,
                        "priority":4
                    },
                    {
                        "key":"last_location",
                        "label":"Last Known Location",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":5
                    },
                    {
                        "key":"status",
                        "label":"Status",
                        "type":"varchar",
                        "input":"select",
                        "required":false,
                        "options":[
                            "Missing",
                            "Alive",
                            "Dead"
                        ],
                        "priority":6
                    }
                ]
            }
        ]
    }
    

