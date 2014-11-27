# How do I add a new view ? (on the frontend)



Adding a new view to the frontend is probably one of the first things you'll
want to do when building anything new into Ushahidi 3.x. By adding a view, I
really mean adding a new URL on the frontend of the application.

Technically this means adding a route, controller and view.. so lets walk
through the process:

### The (Backbone) view and template

All the HTML in the Ushahidi 3.x UI is rendered by a backbone view. We're
using [backbone marionette](http://marionettejs.com/)'s layouts and regions to
nest views within each other. For most purposes you'll only need to modify the
HTML that goes into the main region, that is the contents of div#main-region
shown below.

**Base app view html (AppLayout.html)**

### Creating a new view

Lets create a simple ExampleView. We'll add this to the media in the
UshahidiUI module, so the path ends up like this:
modules/Ushahidi/media/js/app/views/ExampleView.js

The example code below creates a super simple view, that just loads
templates/Example.html and compiles it with Handlebars.

**modules/Ushahidi/media/js/app/views/ExampleView.js**

The HTML for this can be anything we need really.. here's a quick example

**modules/UshahidiUI/media/js/app/templates/Example.html**

### Displaying the view

Now lets add an example controller and route to display our new view. Most of
the existing controllers are a bit more complicated.. using layouts, and
multiple views.. but we just want to get something on the screen.

Add this to controllers/Controller.js

**modules/UshahidiUI/media/js/app/controllers/Controller.js**

Then add the following to routes/AppRouter.js

**modules/UshahidiUI/media/js/app/routers/AppRouter.js**

Now if you load your V3 site, and got to #example you should see your new
view! \o/

### Extra: how routing works..

When you hit a particular url, say "posts/1", this is matched to a route, in
this case 'posts/:id'. The router directs that request to a matching function
on the Controller class.

**routers/AppRouter.js**

**Extract of controllers/Controller.js**

In our example: the URL '/posts/1' is matched to the 'posts/:id' route. This
triggers a call to Controller.postDetail(1)

