# Tables & Overview



Table  |  Description  |  Comments  
---|---|---  
`[forms](/display/WIKI/forms+table)` |  Defines the forms that posts are
attached to  |  
[form_attributes ](/display/WIKI/form_attributes+table) |  Define the
attributes of the forms  |  
`form_groups` |  Defines the groups that attributes in a form belong to  |  
`[posts](/display/WIKI/posts+table)` |  Reports, Alerts, Comments  |  
`post_comments` |  |  
`post_datetime` |  Post UTC Dates  |  
`post_decimal` |  |  
`post_geometry` |  |  
`post_int` |  |  
`post_media` |  |  
`post_point` |  |  
`post_text` |  |  
`post_varchar` |  |  
`posts_sets` |  Pivot table for posts and sets  |  
`posts_tags` |  Pivot table for posts and tags  |  
`sets` |  Defines groups of posts  |  
`tags` |  Categories, Statuses, User defined tags etc  |  
`tasks` |  |  
  
## SQL Conventions

  * Foreign keys will be prefixed by **fk_**, followed by the name of the table and finally the column with the key 
    * Example: fk_post_text_post_id refers to column post_id in post_text that references id in the posts table
  * Unique keys will be prefixed by **unq_** followed by the column[s]
  * Indexes will be prefixed by **idx**_ followed by the column

