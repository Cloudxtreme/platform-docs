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

    
    
    CREATE  TABLE IF NOT EXISTS `posts` (
      `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT ,
      `parent_id` INT(11) UNSIGNED NOT NULL DEFAULT '0' ,
      `form_id` INT(11) UNSIGNED NOT NULL DEFAULT '0' ,
      `user_id` INT(11) UNSIGNED NOT NULL DEFAULT '0' ,
      `type` VARCHAR(20) NOT NULL DEFAULT 'report' COMMENT 'report, revision, comments, alerts' ,
      `title` VARCHAR(255) NULL DEFAULT NULL ,
      `slug` VARCHAR(255) NULL DEFAULT NULL ,
      `content` TEXT NULL DEFAULT NULL ,
      `author` VARCHAR(150) NULL DEFAULT NULL ,
      `email` VARCHAR(150) NULL DEFAULT NULL ,
      `ip_address` INT(11) UNSIGNED NOT NULL DEFAULT '0' ,
      `status` VARCHAR(20) NOT NULL DEFAULT 'draft' COMMENT 'draft, publish, pending' ,
      `created` INT(10) UNSIGNED NOT NULL DEFAULT '0' ,
      `updated` INT(10) UNSIGNED NOT NULL DEFAULT '0' ,
      PRIMARY KEY (`id`) ,
      INDEX `idx_parent_id` (`parent_id` ASC) ,
      INDEX `idx_form_id` (`form_id` ASC) ,
      INDEX `idx_user_id` (`user_id` ASC) ,
      INDEX `idx_type` (`type` ASC) ,
      INDEX `idx_status` (`status` ASC) )
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8;
    

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

