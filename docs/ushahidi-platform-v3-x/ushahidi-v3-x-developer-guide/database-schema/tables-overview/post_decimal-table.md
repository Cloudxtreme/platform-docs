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

    
    
    CREATE  TABLE IF NOT EXISTS `post_decimal` (
      `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT ,
      `post_id` INT(11) UNSIGNED NOT NULL DEFAULT '0' ,
      `form_attribute_id` INT(11) UNSIGNED NOT NULL DEFAULT '0' ,
      `value` DECIMAL(12,4) NULL DEFAULT '0.0000' ,
      `created` INT(10) UNSIGNED NOT NULL DEFAULT '0' ,
      PRIMARY KEY (`id`) ,
      INDEX `fk_post_decimal_post_id` (`post_id` ASC) ,
      INDEX `idx_form_attribute_id` (`form_attribute_id` ASC) ,
      CONSTRAINT `fk_post_decimal_post_id`
        FOREIGN KEY (`post_id` )
        REFERENCES `posts` (`id` )
        ON DELETE CASCADE)
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8;
    

