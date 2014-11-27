# Configuring Apache, PHP, and MySQL Using Homebrew



#### Install Homebrew

The first thing you will need to do is install [Homebrew](http://brew.sh/).
Open up your terminal and run this:

Icon

Do **not** run any of these commands with`sudo`! Repeat: **DO NOT USE`sudo`!**

    
    
    % ruby -e "$(curl -fsSL<https://raw.github.com/Homebrew/homebrew/go/install>)"

Pay attention to all the instructions, run the `brew doctor` command as
required, and be sure to configure your `PATH` afterwards (you might not need
to do this).

#### Install MySQL with Homebrew

OSX does not come with MySQL installed by default, so we will need to install
it using Homebrew:

    
    
    % brew install mysql

Follow all of the instructions that are output by this process, including the
parts about [securing your database](http://benjsicam.me/blog/how-to-install-
mysql-on-mac-os-x-using-homebrew-tutorial/). Once installed you might want to
use[LaunchRocket.prefPane](https://github.com/jimbojsb/launchrocket)to manage
MySQL and other services you install with Homebrew.

#### Install PHP with Homebrew

Next you will need to install PHP. Because OSX comes with PHP preinstalled,
and Homebrew does not duplicate preinstalled packages, you will need to "tap"
a new repository first:

    
    
    % brew tap josegonzalez/homebrew-php  
    % brew install php54 php54-http php54-mcrypt

Again, follow all of the instructions that are output by this process. Once
successful, you will also want to install composer:

    
    
    % brew install composer

Icon

Installing composer this way is optional, but will ensure that your local
version of Composer stays updated when you run `brew upgrade`.

You should also edit `/usr/local/etc/php/5.4/php.ini` and set
`date.timezone`to your local timezone. Check the[list of supported
timezones](http://php.net/manual/en/timezones.php) and choose the one most
appropriate.

#### Enable the Built-in Apache Server

Mac OSX comes with Apache installed by default, but disabled. The easiest way
to enable it it is to use[WebSharing.prefPane](http://clickontyler.com/web-
sharing/). If you want to start Apache manually, you can use:

    
    
    sudo apachectl start

To add a new virtual host, you will need to edit the Apache configuration
in`/etc/apache2`. You might want to use either[osx-vhost-
manager](https://github.com/jamiemill/osx-vhost-
manager)(free)or[VirtualHostX](http://clickontyler.com/virtualhostx/)(paid) to
help manage virtual hosts.

#### Finished

Once these steps are completed, have you have properly updated your`PATH` to
include`/usr/local/bin`, you can follow the rest of the install process.
Double check that everything is installed properly with:

    
    
    % php --version  
    % mysql --version

You should end up with PHP 5.4.x and MySQL 5.6.x (or higher).

**Now Install and Run Ushahidi**

Go to [Installing Ushahidi 3.x ](/display/WIKI/Installing+Ushahidi+3.x)and
follow the instructions there, starting with downloading the Ushahidi code.

