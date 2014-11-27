# Creating a Migration



1\. From your Ushahidi root folder run this from the commandline:  
`./minion --task=migrations:new --group=3-0`

  * 3-0 defines the current version of the application
  * So version 3.1 would be 3-1 and version 3.1.2 would be 3-1-2

2\. A migration template will be created in this folder:  
`/application/migrations/[group]`

In our example above, the migration template would be created in:  
`/application/migrations/3-0`

4\. Open the template:

5\. Add the necessary queries to the up an down methods

  * Queries in the UP method apply the migration
  * Queries in the DOWN method undo the migration

6 Next we [run the migration](/display/WIKI/Running+a+Migration)

