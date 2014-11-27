# People Finder



## Creating The Forms

These forms adhere to the [People Finder Interchange
Format](http://zesty.ca/pfif/)  
Consists of two form:

  * Person Records
  * Note Records

## Person Record

    
    
    METHOD: POST
    ENDPOINT: /api/v2/forms
    AUTHENTICATED: NO
    
    
    
    {
        "name":"Person Record",
        "type":"report",
        "description":"Information that identifies a missing person",
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
                        "key":"given_name",
                        "label":"Given Name",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":2
                    },
                    {
                        "key":"family_name",
                        "label":"Family Name Name",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":3
                    },
                    {
                        "key":"alternate_names",
                        "label":"Alternate Names",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":4
                    },
                    {
                        "key":"description",
                        "label":"Description",
                        "type":"text",
                        "input":"textarea",
                        "required":true,
                        "priority":5
                    },
                    {
                        "key":"sex",
                        "label":"Sex",
                        "type":"varchar",
                        "input":"select",
                        "required":false,
                        "options":[
                            "female",
                            "male"
                        ],
                        "priority":6
                    },
                    {
                        "key":"date_of_birth",
                        "label":"Date of Birth",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":7
                    },
                    {
                        "key":"age",
                        "label":"Age",
                        "type":"varchar",
                        "input":"text",
                        "required":true,
                        "priority":8
                    },
                    {
                        "key":"home_street",
                        "label":"Home Street",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":9
                    },
                    {
                        "key":"home_neighborhood",
                        "label":"Home Neighborhood",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":10
                    },
                    {
                        "key":"home_city",
                        "label":"Home City",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":11
                    },
                    {
                        "key":"home_state",
                        "label":"Home State/Province",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":12
                    },
                    {
                        "key":"home_postal_code",
                        "label":"Home Postal Code",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":13
                    },
                    {
                        "key":"home_country",
                        "label":"Home Country",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":14
                    }
                ]
            }
        ]
    }
    

## Note Record (Child form of Person Record)

    
    
    METHOD: POST
    ENDPOINT: /api/v2/forms
    AUTHENTICATED: NO
    
    
    
    {
        "parent_id":99,
        "name":"Note Record",
        "type":"report",
        "description":"Information about the current status of a missing person",
        "groups":[
            {
                "label":"Note Record",
                "priority": 1,
                "attributes":[
                    {
                        "key":"status",
                        "label":"Status",
                        "type":"varchar",
                        "input":"select",
                        "required":false,
                        "options":[
                            "information_sought",
                            "is_note_author",
                            "believed_alive",
                            "believed_missing",
                            "believed_dead",
                        ],
                        "priority":1
                    },
                    {
                        "key":"email_of_found_person",
                        "label":"Email of Found Person",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":2
                    },
                    {
                        "key":"phone_of_found_person",
                        "label":"Phone of Found Person",
                        "type":"varchar",
                        "input":"text",
                        "required":false,
                        "priority":3
                    },
                    {
                        "key":"last_known_location",
                        "label":"Last Known Location",
                        "type":"varchar",
                        "input":"text",
                        "required":true,
                        "priority":4
                    },
                    {
                        "key":"text",
                        "label":"Comments",
                        "type":"text",
                        "input":"text",
                        "required":false,
                        "priority":5
                    }
                ]
            }
        ]
    }
    

