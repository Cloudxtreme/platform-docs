# Installing Ushahidi 3.X on a Windows Wampserver



Follow the [V3 install instructions](/display/WIKI/Installing+Ushahidi+3.x),
with these few changes:

## Database

I'm assuming that you've cloned Lamu into folder c:\wamp\www\Lamu

Use localhost/phpmyadmin to create a database. I've called mine lamutest. Your
database.php should look something like this:

    
    
    return array  
    (  
     'default' => array  
     (  
     'type' => 'MySQLi',  
     'connection' => array(  
     'hostname' => 'localhost',  
     'database' => 'lamutest',  
     'username' => 'root',  
     'password' => 'mypassword',  
     'persistent' => FALSE,  
     ),  
     'table_prefix' => '',  
     'charset' => 'utf8',  
     'caching' => TRUE,  
     'profiling' => TRUE,  
     )  
    );

Where 'database' is the database name that you chose; 'username' is the user
that you set up in phpmyadmin (look at the 'users' tab: my user is
root@127.0.0.1) and 'password' is the password that you set up for that
phpmyadmin user.

## Base_url

Like with Ushahidi v2.x, your baseurl is going to be slightly different to
everyone else's.

In init.php, for Ushahidi v3 installed atc:\wamp\www\Lamu, it's

    
    
    'base_url'  => '/lamu/httpdocs',

In .htaccess, it's

    
    
    RewriteBase /lamu/httpdocs/

## Minion

Minion won't work if you can't run php (you can test this by trying "php -v"
in your terminal window). To make this happen in wamp, find your system path
(on windows 7, that'scontrol panel > system and security > system, then
advanced system settings, (lhs list) and add a link to your php to it: for my
Wamp install, that means adding the text ";C:\wamp\bin\php\php5.3.13" to my
path; you might want to look in C;\wamp\bin\php to see what the right address
for you is (e.g. you might have a different version of php).

In your terminal window, go to your top-level directory (in this case,
c:/wamp/www/Lamu) and run minion with this command:

    
    
    phpminion --task=migrations:run --up
    
    
      
    

Go to<http://localhost/lamu/httpdocs/>

Smile: you've got your own copy of V3 working on Windows!

