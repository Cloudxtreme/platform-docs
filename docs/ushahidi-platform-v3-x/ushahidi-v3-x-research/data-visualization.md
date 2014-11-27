# Data Visualization



We've built data science ideas into Ushahidi v3.x - starting with better
built-in data visualization.

A persistent ask among our partners and clients has been better data vis in
addition to mapping provided by Ushahidi V2/3. We're adding this to V3, with
hopeful beta integration by July. To quickly answer some basic questions,
we've created this page with some basic updates.

More to come! Stay tuned! ~ Aurelia (3/28/14)

**What data is available?**

  * Reports (with words, categories, user, message, location, time, custom form entries)

  * Users

  * Messages (with channels, reporter, time)

  * Reporters (with location)

  * Categories (with report volumes)

  * Locations (lat/long, name)

  * Comments (with words, user, time)

  * External data (including map data)

(see _[this wiki page](/display/WIKI/Ushahidi+Data+Upload+and+Download)_for
current list of downloadable Ushahidi data)

**What are some essential stats?**

  * Message creation rates

  * Report creation rates by day/week/month

  * Number of reports per category

  * Number/percentage of reports per source type (facebook, twitter, SMS etc)

  * Word frequencies (non-stopwords) in reports

  * Number/percentage of verified/unverified reports (big + if thats also available by category)

**What has been requested?**

  * Cross correlations. Weve shown # of reports / category and prioritized categories

  * Time filters

  * Cut-and-paste versions of infographics/exportable charts for including in word docs

  * Compare locations over time

  * Develop automated data dashboards, showing volume of reports in y-axis and time in x-axis, with ability to compare different categories

  * Admin can view graphs of custom form field values

  * Downloadable reports

**What are some inspiration pieces, reference links (feel free to add to this please)?  
**Link list of data visualization resources: [urli.st/Pd9.](http://urli.st/Pd9)

CoderGeek [resource list ](http://blog.scrapinghub.com/2014/04/01/announcing-
portia/)of data viz links.  

**What are we doing now?**

For now, we are piloting a few quick starts using sample data from an election
monitoring group. You can explore the temporary code and look forward to
additional custom charts in the future, we're looking at multiple JS
libraries, including the D3/NVD3/reD3 suite, feel free to suggest others in
the comments!)

We'll be adding more visualizations to this repository, but some features for
this use case include:

  * Simple counts and reports time filters
  * Reusable charts with simple Election Monitoring stats
  * Reversable and internationalized charts to support right->left translations
  * Exportable/Downloadable charts (with PNG/JPG/PDF formats)

Repository for current code:<https://github.com/auremoser/ifes>

Demo visualization set:<http://auremoser.github.io/ifes/>

