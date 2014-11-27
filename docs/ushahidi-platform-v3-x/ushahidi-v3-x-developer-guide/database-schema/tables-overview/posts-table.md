# posts table



## Purpose

Posts are the core piece of data stored within the Ushahidi system. The
following are all types of posts:

  * reports
  * revisions (of reports)
  * comments
  * alerts

## Definitions

Column

|

Description  
  
---|---  
  
`parent_id`

|

The parent that this post belongs to. Useful for revisions, comments and
alerts  
  
`form_id`

|

The form that was used to create this post  
  
`user_id`

|

The user that created this post  
  
`type`

|

primary post types are **report,****entity** and **revision**. Other Types.  
  
`title`

|  
  
`slug`

|  
  
`content`

|  
  
`author`

|  
  
`ip_address`

|  
  
`status`

|  
  
`locale`

|  
  
## Syntax

## Post 'Types'

#### Primary Types

  * report
  * entity
  * revision

#### Secondary Types

  * stream
  * translation

#### _Other_ Types

  * sms
  * email
  * rss
  * tweet
  * facebook_post
  * etc.

