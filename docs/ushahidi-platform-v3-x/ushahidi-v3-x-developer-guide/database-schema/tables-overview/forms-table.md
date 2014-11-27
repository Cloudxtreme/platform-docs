# forms table



## Purpose

Forms describe all the posts in the system. A form describes the structure of
a post.

## Definitions

Column

|

Description  
  
---|---  
  
`name`

|

Name of the form  
  
`description`

|

Description of the form  
  
`type`

|

primary form types are **report**, **entity** and **stream**. Descriptions of
the types.  
  
## Syntax

    
    
    CREATE  TABLE IF NOT EXISTS `forms` (
      `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT ,
      `name` VARCHAR(255) NOT NULL DEFAULT '' ,
      `description` TEXT NULL DEFAULT NULL ,
      `type` VARCHAR(30) NOT NULL DEFAULT 'report' COMMENT 'report, entity, stream' ,
      `created` INT(10) UNSIGNED NOT NULL DEFAULT '0' ,
      `updated` INT(10) UNSIGNED NOT NULL DEFAULT '0' ,
      PRIMARY KEY (`id`) )
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8;
    

## Form Types

  * **report** \- form/template for reports
  * **entity** \- form/template for entities. Entities have streams that are defined by a stream form. Examples: 
    * hospital
    * missing person
    * field worker
    * sensor
    * runner
    * bike rider
  * **stream** \- form/template for the streams attached to an entity

