# Design process



**Ushahidi 3.0's** UI is based on the crossbrowser, front-end framework [Foundation](http://foundation.zurb.com/docs/index.html) and utilizes [Sass](http://example.net/), which compiles to CSS via [Compass](http://example.net/). Foundation provides Sass mixins, which are an intergral part of **Ushahidi 3.0's** grid and design.

## Install Dependencies

##### Compass

Follow [these directions](http://compass-style.org/install/) to install
Compass on your machine.

> NOTE: Both Ruby and RubyGems Library are required before installation.

##### Install Grunt and grunt plugins

You'll need [nodejs and npm](http://nodejs.org/) installed.

In terminal run:

    
    
    cd modules/UshahidiUI  
    npm install -g grunt-cli  
    npm install

## Install Ushahidi 3.0

Follow the [install instructions](/display/WIKI/Installing+Ushahidi+3.x)

## Directory Structure

  * All design files are located in `modules/UshahidiUI/media`

  * HTML files are located in `modules/UshahidiUI/media/js/app/templates`

  * [Sass](http://sass-lang.com/) files are located in `amu/modules/UshahidiUI/media/scss`

## How to make style changes?

**IMPORTANT!! - Do not edit the `.css` files directly. Always make style changes within the `scss` directory**

  * In your terminal, navigate to the `UshahidiUI` folder and run `grunt watch` (this [Grunt](http://gruntjs.com/) command will use Compass to compile all `.scss` files into `css/style.css` upon saving your documents).

  * Then make all style changes within the individual `.scss` files, creating new ones and importing them into `style.scss` as needed. (Reference current `css/style.css` for _@import_ structure).

  * Now when you save your changes to your document, Grunt will run Compass to compile all of your `.scss` files into `css/style.css`. Your changes will take effect upon browser refresh.

## Semantic HTML Grid

* * *

**IMPORTANT!! - "Semantic Grid" means that the grid code is in the Sass/CSS and stays out of the HTML, making the HTML markup more semantic**

**Ushahidi 3.0** is a responsive, device agnostic application, meaning it is flexible and optimized for usability regardless of the device. It looks good on desktop, mobile phones and everything in between.

It is important to know that the **Ushahidi 3.0** grid is semantic, meaning it
is controlled via the `.scss` files, **not the HTML**. If you need to adjust
or add to the grid, please do so via [Sass mixins provided by
Foundation](http://foundation.zurb.com/docs/components/grid.html). Please keep
the grid out of the markup and in the CSS.

When in doubt reference **Ushahidi 3.0's** existing codebase and the
Foundation docs.

** _If you have any questions feel free to contact Seth Hall_ **

  * [@middle8media](https://twitter.com/middle8media) on Twitter
  * middle8media on Skype
  * seth(at)ushahidi.com

