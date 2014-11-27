# Ushahidi v3.x Wishlist



_**Not sure how best to add "wishes"? Just edit the page and add your wish in
an appropriate section or 'Miscellaneous' .**_

_The core team will check this list occasionally.__If we feel a wish is not a
good fit for Ushahidi, we will _<s>_strikeout the wish_</s> so others can see
it is proposed, but not likely to happen.

# Desired Features for Ushahidi Platform v3

## Deployment

  * Automated upgrade in a couple of clicks
  * Increase quantity and quality of documentation - how to guides, trouble shooting etc
  * I dream to see the option to get the same sub/categories of my crowdmap deployments in the new Ushahidi 3.0  

## Admin

  * New Admin UI - a whole redesign of the backend **Definitely planned. 3.0 is a full rebuild**
  * Spatially-aware administration - Improving the admin part for approval&verification workflow management by regulating the grants only to those reports that are located in a defined area (for example per countries)
  * Add Admin "Healthmeters" to monitor the system where information is being added SMS, voice, reports, emails etc. Perhaps use a sliding time related scale to set the acceptable timeline. This will allow easy way to assess where resource is best utilised to optimise the system performance. Simple Colour grading green (processes clearing faster or at same speed as incoming requests), Orange (processes clearing at a slower rate to incoming requests), Red (Process overloading or clearing at a rate that is below acceptable levels - example SMS queue has 6 hours of processing based on current clearance rate
  * Rework people tracking (USER roles/registration) Currently Users = people with access to site. Reporters = people who report via email/SMS and Report Person = Person listed on a report that might actually have been entered by a different user...  
Propose:

    * Any interaction with the site (comment, report, send SMS) creates a new USER in one USER table. All users are by default 'public (no admin access)'
    * Each USER can have multiple phone numbers, email, twitter, facebook, etc associated with that user profile. USERS can create passwords that do nothing more than allow them to change their personal info and associations (would need some system of varification: ask them to send a one-time code from their SMS, ask them to post a one-time code on their twitter account, etc) that would then link in all their reports from various media.
    * USERS can then easily be granted more access by elevating their position to a different ROLE
    * Thus if a USER sends an SMS, email, twitter, facebook post, it is linked to their account (assuming their phone number / email / twitter account is already registered with that account) it if is not, a separate user might exist for phone # 123, and [email123@gmail.comand](mailto:email123@gmail.comand) twitter account@123 and this is fine, but once a USER submits registration info, they can link all of these accounts under one profile.
    * Reports can be sorted by USER (whether via email, sms or submitted on site)
    * Ability to search user lists (uchaguzi has over 200 user accounts). You have to page search. There is no user search. You also cannot mass edit roles by users. Hard to manage large teams.
    * Propose to allow admin editing of an anon / email / SMS post to allocate the ID of a current author/user (links to suggestion for every author/user to have their own hub page showing their contributions)
  * Map on Admin side for better report finding / filtering (currently handled by JEtherton plugin for some versions) this is related to "Front-End Admin" below. **Planned: 3.x will have lessseparationbetween back and frontend.**
  * Front-end admin?!?! Users with higher roles are granted morefunctionality, but otherwise thegenerallayout looks the same. (Currently feels like Windows 8 split personality).**Planned. Though there may still be something like a 'Tools' UI section for configuring site settings**

## Database

  * Rework the DB Schema**Planned/In progress**

## Plugins

  * Update Plugin functionality to make it easier for community contribution and ease of use.
    * We do need far more filters/actions in the core code, but it's hard to know where these are needed until a plugin dev asks for them
    * Document it better, and provide better examples
    * Make it easier to search and find plugins
    * Write a clear process for plugin contribution and submission, testing and acceptance.  
  

## Themes

  * Update Theme functionality to make it easier to completely change the theme (clean base theme, easy to override CSS) - some of this might happen in 2.x
  * Include Usability analysis of Gabriel White - Toolboxes Design

## Reports

  * Adding the option to set a duration/deadline for a report; useful for example when you create a crisismap for lost/find poeples or pets; then the possibility to send an alert when the deadline is reached; after it the report has to be automatically removed from the map;
  * Keeping the geofencing feature of the 2.X Ushahidi (polygon etc.) in order to make the 3.X the new reference for the new crisismaps and crisismappers;
  * Add the ability to create reports for "dynamic events", that is reports that can be updated over time to reflect changing conditions or circumstances. **Planned in form of 'Posts' with 'Updates'**
    * Any edits to the report should be reflected in a "history" of updates to provide a record as to whether a situation is improving, worsening or unchanged.
    * If tabular or quantitative data could be accommodated, the capability to support visualizations (charts, graphs) beyond the existing geo-location mapping capability might be feasible.
    * This might also create the potential for automated sensor generated updates submitted via SMS such as monitoring the temperature of vaccines stored in rural clinics or the output of a village well.
    * we could use the wiki-model here for the dynamic events , this will shift us to the collaborative reporting that's means people around the event could update the intial report .
    * could you make it possible for another Author to add an image to an existing post? As is possible with post comments. This would be very useful for longer lived posts like heritage assets where you would have a main post for the heritage site, then other visitors / authors could add their images to an existing page.
    * It would also be a good idea for each author to have a Profile / Hub / User page where all their posts,images and comments are shown on one page. This would encourage people to add posts as they can see everything they have contributed in one place. Of course this can only be done for posts that have been submitted while the person is logged in

## Mapping

  * Decoupling the timeline from the main map - and improving the UX of the timeline
  * Refactor the mapping code to make it extensible and reusable
    * "Have an api that makes it possible to pass a function a list of incident id's and category preferences and get back a map" from #186 **Something like this should be possible using the core backbone views**
    * Override-able template for map popups
  * Being able to apply filters to map on front page (like you currently can on reports page)**Planned: less separation between 'main' and 'reports' pages in 3.x**
  * Add capability for generating incident heat maps by category (ies), and time. Allow time to be customised to combine any parameters, e.g. looking at incidents on a sunday for the past 4 years, and then being able to narrow it down to 3pm (3-4pm) on a Sunday for the past 4 years. With a good database this will allow us to do predictive modeling;
  * adding more map markers others than the default ones like the ones of google map; **Planned - possibly after 3.0 though**
  * giving the capability when uploading a custom marker for a category to render its alpha channel too (it seems that .PNG looses its transparency when you upload a custom marker). **We'll rely on Leaflet for this, so if it works in Leaflet it should work in Ushahidi.**

## Miscellaneous

  * <s>Removing the sharing feature from core and building it as a plugin</s>**Done in 2.x**
  * Improving the 'import data' into Crowdmap functionality to work with custom form creation. E.g user has a csv or xls file and would like to import into Ushahidi, that at the time of import, they can dynamically create custom forms and autogeolocate data as they import data. matching fields in the CSV with custom form designations and category allocation.
    * Auto-geolocation is already in the current codebase
  * RESTful API**Planned/In progress.**
    * Rewrite the API to use REST properly (Use HTTP GET, POST, PUT, DELETE; Use HTTP status codes; Unique URIs for resources)
    * Preferably match the URL paths expected by Backbone.js
    * Support custom fields for both GETting and POSTing
    * Make each single report available as geojson object to easily add to third-party webmapping sites (Es. Those using Leaflet and OpenLayers) 
  * Encourage secure code through architecture**Planned: much of this is aided by building on the API.**
    * Bake access checks into models (ie. always filter reports for approved=1 unless user is admin)
    * Black list urls by default at a high level (ie. controller have to explicitly grant access, not explicitly deny), don't rely on controllers including the correct access checks.
  * From the forums - <http://forums.ushahidi.com/forums/forum/apps/plugin-wish-list/?view=all> and <http://forums.ushahidi.com/forums/forum/feature-requests/>
  * From GitHub -[https://github.com/ushahidi/Ushahidi_Web/issues?labels=Feature&page=1&state=open](https://github.com/ushahidi/Ushahidi_Web/issues?labels=Feature&page=1&state=open)
  * _**Reputation and points system**_
    * Is there any discussion around implementing a points and reputation system functionality for Ushahidi.I understand the implicit anonymity required with many Ushahidi deployments. If folk are posting reports in a dangerous political or violent climate they may need to report anonymously. However, surely not all deployments are for these situations. The actions tab in the back end for example, gives option to assign badges on report submission. I'd love to be able to implement this but the vast majority of reports to my deployment are submittedanonymously. I don't believe that the reporter has chosen to be anonymous, but that the design of the platform basically leads them down that path. If there was an option to assign points, in addition to badges, under the actions tab that'd be a nice to have for us at least. I'm convinced that others would value this functionality too. This is against a backdrop of popular discussion around online "reputation". To promote loyalty, action (report submissions, for example) **and a feeling of being part off**, a points system would be really helpful. To overlap a feature request above, this would have to be tied to any site action such as clicking on a vote button, report submission, commenting etc. Points could behierarchal with badges being assigned at various milestones or once certain level of points are reached. Our experience has shown that folk really like our deployment and wish to be involved in some way beyond just signing up for alerts.
    * Robbie: I think this is outside the scope of the Ushahidi core. However options about requiring user registration for reports will likely be built in, the rest could be built as a plugin for V3.  
  

