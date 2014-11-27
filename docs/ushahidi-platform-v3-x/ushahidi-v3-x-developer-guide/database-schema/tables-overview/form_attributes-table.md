# form_attributes table



## Purpose

A form attribute defines a single item that will be described by a post. A
form attribute is essentially a form field.

## Definitions

Column  |  Description  
---|---  
`form_id` |  The form that this attribute belongs to  
`form_group_id` |  The group within a form that this attribute belongs to  
`key` |  A unique key that defines this attribute  
`label` |  The label this attribute will have when it is rendered  
`input` |  The type of form input to use when rendering this attribute  
`type` |  The table type that will be used by the post to store the value of
this attribute  
`required` |  Whether this attribute is required  
`default` |  The default value to use when this attribute is rendered on the
form  
`unique` |  
`priority` |  
`options` |  
  
## Syntax

    
    
    CREATE  TABLE IF NOT EXISTS `form_attributes` (
      `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT ,
      `form_id` INT(11) NOT NULL DEFAULT '0' ,
      `form_group_id` INT(11) NOT NULL DEFAULT '0' ,
      `key` VARCHAR(150) NOT NULL DEFAULT '' ,
      `label` VARCHAR(150) NOT NULL DEFAULT '' ,
      `input` VARCHAR(30) NOT NULL DEFAULT 'text' COMMENT 'text, textarea, select, radio, checkbox, file, date' ,
      `type` VARCHAR(30) NOT NULL DEFAULT 'varchar' COMMENT 'decimal, int, geometry, text, varchar, point' ,
      `required` TINYINT(1) NOT NULL DEFAULT '0' ,
      `default` VARCHAR(255) NULL DEFAULT NULL ,
      `unique` TINYINT(1) NOT NULL DEFAULT '0' ,
      `priority` TINYINT(4) NOT NULL DEFAULT '99' ,
      `options` VARCHAR(255) NULL DEFAULT NULL ,
      PRIMARY KEY (`id`) ,
      UNIQUE INDEX `unq_form_id_key` (`form_id` ASC, `key` ASC) ,
      INDEX `idx_form_group_id` (`form_group_id` ASC) )
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8;
    

