# post_decimal table



## Purpose

The post_decimal table stores EAV decimal values for the post table. The
decimal table is especially useful for storing **sensor data** \- like
temperature, humidity, accelerometer settings, etc... There are cases where it
would be advisable to use this for storing lat/lons as well outside of the
spatial table (post_point/post_geometry).

## Definitions

Column

|

Description  
  
---|---  
  
`post_id`

|

The post that this value belongs to  
  
`form_attribute_id`

|

The form_attribute that this value belongs to  
  
`value`

|

The value  
  
`created`

|  
  
## Syntax

