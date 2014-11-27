# Creating a Migration



1\. From your Ushahidi root folder run this from the commandline:  
`./minion --task=migrations:new --group=3-0`

  * 3-0 defines the current version of the application
  * So version 3.1 would be 3-1 and version 3.1.2 would be 3-1-2

2\. A migration template will be created in this folder:  
`/application/migrations/[group]`

In our example above, the migration template would be created in:  
`/application/migrations/3-0`

4\. Open the template:

    
    
    <?php defined('SYSPATH') OR die('No direct script access.');
    
    class Migration_3_0_20130318155930 extends Minion_Migration_Base {
    
    	/**
    	 * Run queries needed to apply this migration
    	 *
    	 * @param Kohana_Database $db Database connection
    	 */
    	public function up(Kohana_Database $db)
    	{
    		// $db->query(NULL, 'CREATE TABLE ... ');
    	}
    
    	/**
    	 * Run queries needed to remove this migration
    	 *
    	 * @param Kohana_Database $db Database connection
    	 */
    	public function down(Kohana_Database $db)
    	{
    		// $db->query(NULL, 'DROP TABLE ... ');
    	}
    
    }
    

5\. Add the necessary queries to the up an down methods

  * Queries in the UP method apply the migration
  * Queries in the DOWN method undo the migration

6 Next we [run the migration](/display/WIKI/Running+a+Migration)

