# Installing Ushahidi 3.x



### System Requirements

To install the platform on your computer/server, the target system must meet
the following requirements:

  * PHP version 5.4.0 or greater
  * MySQL database version 5.5 or greater (PostgreSQL support planned)
  * An HTTP server, we develop Ushahidi using Apache 2.2+ and nginx
  * Unicode support in the operating system (UTF-8 charset, PCRE, iconv extension, etc)

### Getting the code

First, you will need a copy of the source code, which lives in our Github
repository:

    
    
    % git clone https://github.com/ushahidi/platform.git

Once you have the code, the next step is to prepare a web server.

### Preparing the Server

By default, there are two options for running the Ushahidi platform locally.
You can either run the [Vagrant](http://www.vagrantup.com/) virtual machine,
or you can run it locally.

#### Using the Vagrant virtual machine

To run the virtual machine, install Vagrant following the instructions on
their website, check the settings in the
[Vagrantfile](http://docs.vagrantup.com/v2/vagrantfile/index.html) then start
the VM from your console:

`% bundle install`

`% librarian-puppet install  
`

`% vagrant up && vagrant provision  
`

This should set up a server, and install all the dependencies too.

#### Using a local server

If you want to run Ushahidi locally, you will need to make sure that you have
a recent version of PHP, a database server, and a web server available. Then,
follow these steps:

To create a database, first login to MySQL as root.

% mysql -u root -p

Icon

Using the `-p` is only required when your MySQL configuration requires it. You
may need to use the `-h` option to specify `localhost` or `127.0.0.1` if you
are unable to connect.

Next, create a new user and database for Ushahidi. The username and database
can be anything; we will use `ushahidi` for both in this example:

CREATE DATABASE ushahidi;  
GRANT ALL ON ushahidi.* to ushahidi@localhost IDENTIFIED BY 'set-a-custom-
password-here';  
quit;

Now copy the database.phpconfig file into `environments/development/` and edit
it. Make sure that the database, username, and password match the database you
just created.

`% cp``application/config/database.php``application/config/environments/develo
pment/database.php`  
`% $EDITOR application/config/environments/development/database.php`

You should also rename`template.htaccess`in httpdocs to`.htaccess`(for Apache)
to enable rewriting of all non-existent files to`index.php.`If you do not want
to, or are unable to, enable rewriting, then customize the initialization
settings by also copying the `init.php` config file
into`environments/development/` and editing it,
setting`index_file`to`"index.php"`

Icon

**A note on urls, docroots and base_url**

Typically, Ushahidi is run under a separate virtual host / domain name. Be
sure to make `platform/httpdocs/` the `DocumentRoot` (for Apache) or `root`
(for nginx) setting in your virtual host.

If you are running Ushahidi via <http://localhost/>then the `base_url`will be
<http://localhost/platform/httpdocs/>

Enable writing to the logs, cache, and upload directories:

`% chmod 0777 application/logs application/cache application/media/uploads`

Icon

If you are running in shared or production environment, it is better to use
`chown` to set the owner of the directories to the user that runs the web
server runs as, rather than making them globally writable.

### Installing dependencies

We use[Composer](https://getcomposer.org/)to manage server side dependencies.
Onceyou have installed composer, you can run the update script with:

    
    
    % bin/update

_Whenever the repository is updated using`git pull`, run the update script to
ensure that your installation stays updated!_

If you are updating a production deployment, you will want to avoid installing
developer dependencies (testing tools, etc) by using the "deploy" option:

    
    
    % bin/update --production

Logging in the first time

The default install creates a user **admin**with password **admin**. Once
logged in this user can create further user accounts or give others admin
permissions too.

### Configuration

Base config files are in `application/config/`.

You can add per-environment config overrides in
`application/config/environments/`. The environment is switched based on the
`KOHANA_ENV` environment variable.

Routes are configured in `application/routes/default.php`. Additional routes
can be added in per-environment routing files ie.
`application/routes/development.php`

