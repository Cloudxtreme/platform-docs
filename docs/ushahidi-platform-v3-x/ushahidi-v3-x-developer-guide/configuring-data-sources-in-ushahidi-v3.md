# Configuring data sources in Ushahidi V3



Ushahidi is all about data.. a beautiful map is only useful if you can get the
data or messages you want and make them in to posts.

In Ushahidi V3 SMS, Twitter, Email, RSS and other incoming data is all handled
through data providers. Each data provider plugin handles a different source
(ie. SMSSync, Twillio, etc). We currently have support for SMS and Email
message types, and plugins for email, twilio, smssync and nexmo data
providers.

Enabling and configuring data providers is handled through the data-
provider.php config file. By default all data providers are disabled, you'll
need to enable and configure the ones you need. The base data-provider.php
looks like this:

**application/config/data-provider.php**

  1. To start configuring data providers, first copy this file from application/config/data-provider.php to application/config/environments/development/data-provider.php
  2. Editapplication/config/environments/development/data-provider.php and enable the providers you need. Here's an example config to enable SMSSync and email providers.

**application/config/environments/development/data-provider.php**

  3. Once you've configured providers, run  
_./minion DataProvider:incoming_ \- to check incoming messages  
_./minion DataProvider:outgoing_ \- to send outgoing messages

For a real deployment you probably want to set up a cronjob to run _./minion
[DataProvider:incoming](http://dataproviderincoming)_ regularly.

At the moment there isn't any UI for sending outgoing messages, so there's not
much use creating a cronjob for that.

