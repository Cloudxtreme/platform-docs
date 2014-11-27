# Installing Ushahidi 3.x on OSX with MAMP Pro



# Install Git

If git is not installed on your machine or the version you have installed by
default requires XCode, download and install this version:

  * <http://git-scm.com/download/mac>

# Setting up MAMP Pro

  * **GENERAL** \- no need to change anything here:  
![](/download/attachments/10256393/MAMP_PRO_and_Edit_-
_Installing_Ushahidi_3_x_on_OSX_with_MAMP_Pro_-_Community_Wiki_-
_Ushahidi.png?version=1&modificationDate=1397682555000&api=v2)  
  

  * **HOSTS**  

    * Create a new host by clicking the[+] at bottom left
    * Give your server a name - in our case (ushahidi.dev)
    * Create a folder to hold the site by clicking the folder icon - in our case** /Applications/MAMP/ushahidi**  
![](/download/attachments/10256393/MAMP_PRO_and_Edit_-
_Installing_Ushahidi_3_x_on_OSX_with_MAMP_-_Community_Wiki_-
_Ushahidi.png?version=1&modificationDate=1397680981000&api=v2)

  * At this point we don't need to modify anything else

# Create a Database

  * Click on the **phpMyAdmin** link at the bottom of the MySQL screen above
  * Click on the **Databases** tab within phpMyAdmin
  * Create an **ushahidi** database  
  
![](/download/attachments/10256393/Screenshot%202014-04-16%2017.11.25.png?vers
ion=1&modificationDate=1397682725000&api=v2)

# Downloading and installing Ushahidi

  * Open the 'Terminal' app by going to **Applications > Utilities > _Terminal_**
  * Change to our document root folder
    
        cd /Applications/MAMP/ushahidi

  * Remove the default MAMP Pro files from this directory
    
        rm MAMP-PRO-Logo.png
    rm index.php

  * Clone the Ushahidi Platform repository from Github
    
        git clone --recursive https://github.com/ushahidi/platform ./

  * Follow the rest of the instructions listed here with the exception of using the database.php file listed below:
    
        <?php defined('SYSPATH') or die('No direct access allowed.');
    /**
     * Database Config
     * 
     * @author     Ushahidi Team <team@ushahidi.com>
     * @package    Ushahidi\Application\Config
     * @copyright  2013 Ushahidi
     * @license    https://www.gnu.org/licenses/agpl-3.0.html GNU Affero General Public License Version 3 (AGPL3)
     */
    return array
    (
    	'default' => array
    	(
    		'type'       => 'MySQLi',
    		'connection' => array(
    			'hostname'   => 'localhost',
    			'database'   => 'ushahidi',
    			'username'   => 'root',
    			'password'   => 'root',
    			'socket'     => '/Applications/MAMP/tmp/mysql/mysql.sock',
    			'persistent' => FALSE,
    		),
    		'table_prefix' => '',
    		'charset'      => 'utf8',
    		'caching'      => TRUE,
    		'profiling'    => TRUE,
    	)
    );

  * Your new site will be accessible at**<http://ushahidi.dev:8888/>**

## **** Please leave feedback below ****

