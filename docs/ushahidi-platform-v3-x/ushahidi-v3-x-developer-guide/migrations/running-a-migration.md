# Running a Migration



The Run task compares the current version of the database with the target
version and then executes the necessary commands to bring the database up to  
date.

To run all the migrations and upgrade the database use:  
`./minion --task=migrations:run --up`

This command will run all the migrations in the group folders within
`/application/migrations/*`. The command will also create the migrations table
in your database (if it doesn't exist) to keep track of the version of your
database.

To run migrations only on a particular group for example to run migrations on
version 3.0 alone run:  
`./minion --task=migrations:run --up --group=3-0`

You can also dry-run the migration by using:  
`./minion --task=migrations:run --up --dry-run`  
The SQL that the migration runs is output to the console

To migrate only to a specific timestamp use:  
`./minion --task=migrations:run --up --to=[timestamp]`

Available migration options:

  * \--down
  * \--up
  * \--to=(timestamp|+up_migrations|down_migrations)
  * \--group=group
  * \--groups=group[,group2[,group3...]]
  * \--dry-run
  * \--quiet

