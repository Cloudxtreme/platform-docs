# Ushahidi v3.x Under The Hood



The Ushahidi 3.x web application is written in
the[php](http://www.w3schools.com/php/)programming language, using the[Kohana
version 3.3](https://wiki.ushahidi.com/kohanaframework.org/3.3/guide/)
framework as a backend, with a
[Backbone.js](http://backbonejs.org/#introduction) and
[Javascript](http://www.w3schools.com/js/) frontend over
a[SQL](http://www.w3schools.com/sql/default.asp)(currently MySQL) database
(see [Code Organisation](/display/WIKI/Code+Organisation)for more details on
this).

Kohana is a[Model-View-Controller](http://en.wikipedia.org/wiki/Model%E2%80%93
view%E2%80%93controller)(MVC) framework, where a framework is like a structure
that you can build your code on, that handles lots of otherwise time-consuming
things like making all your pages have a similar look-and-feel. MVC gets its
name because it splits application code into Model, View and Controller files.
Simply put (there are some complications to this, but not enough to change the
basic explanation), Model files contain code that describes the data
structures being used by the application; View files contain code that tell
the framework how to display information to the user; and controller files
contain code that converts system inputs (e.g. you clicking a mouse or data
coming into a feed) into actions.

