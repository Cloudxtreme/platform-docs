# Technical Feedback - Dev meetup



**This is Feedback based on a meet-up held in Nairobi on 20th May 2014**

**Installer**

Have option for both server installation and regular installation

  * Server Installation : Install platform without the UI (just backend)
  * Use-Case : Clients who have custom tools to pull data directly from the API rather than having a pre-made front-end

**Custom-forms**

Robust implementation of custom forms

  * Using opensource form buildere.g. xforms
  * Needs the simplicity/usabilty of something like excel spreadsheets

**Task management for post curation**

This is when an admin can 'lock' onto a report, making it unavailable to all
other admins.Current locking mechanism on 2.x does not work well, need a
different mechanism

  * Queueing -Look at open-source queueing mechanismper source channel e.g queue for twitter, queue for sms feeds
  * Integration with chambua -Try deployment within Nairobi (a known area)
  * Automatic posts with sensors -With sensor integration, posts generated from sensors wouldn't need to be curated

**Migration**

  * Crazy Idea: Using the ability to prefix database tables in 2.x having the new v3 tables in the same schema, then figure out a way to integrate the two.
  * One click installation is necessary,integrateimport of data while setting up v3

**Sensors**

  * Should they be supported by the schema?Alternatively, sensor data can leverage custom forms
  * Check out Cloud-based sensor network for monitoring ->Valarm ([www.valarm.net](http://www.valarm.net/))
  * Incorporation with BRCK - a great use case

  

