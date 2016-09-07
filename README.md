## Background

'snippets-app-python' is a simple program that is based on a thinkful task for programming in python3. 

The app enables users to run the program from the command line, providing commands and queries as arguments, in order to interact with a postgres database that contains 'snippets'. The app also demonstrates basic logging. 

The app utilises [logging](https://docs.python.org/3/library/logging.html), [argparse](https://docs.python.org/3/library/argparse.html) & [psycopg2](http://initd.org/psycopg/docs/) libraries. 

Snippets are stored in a simple format: keyword, message. 

## User Guide

### Pre-requisites

1) Download the project

2) Postgres database installed/started

3) Database created: 

      createdb snippets
      
4) On command line, run the schema.sql file in order to create the basic tables

      psql -d snippets < schema.sql
      
5) Use the post commands below to set up some basic records in the snippets database. 
      

### Commands

Given that the program is downloaded, any of the following commands can be executed from the project's root folder, in order to utilise the program: 

Get a list of the names of all snippets: 

     python3 snippets.py catalogue


Get the details of a snippet, using a specific name
Note that the names can be found via the previous command
Note that only snippets allowed to be found via search will be returned (eg, 'hidden = false')

     python3 snippets.py get <snippet_name>


Search for a snippet using any string, to find matching snippets that contain the string in the message
Note that only snippets allowed to be found via search will be returned (eg, 'hidden = false')

     python3 snippets.py search <search_query>

Add a new snippet to the database, providing snippet name and snippet message
Note that if no optional arguments are supplied, the snippet will be searchable by default (eg, hidden = false)

     python3 snippets.py post <snippet_name>  <snippet_message>


Add a new snippet to the database, with optional hidden argument, so that snippet cannot be searched

     python3 snippets.py post <snippet_name>  <snippet_message>  --hide
     

## Future updates
A lot more work can be done to this code! 
Ideas include: 

create a function to update snippet
- include an optional argument to update the hidden flag to true or false

add error handling for
- duplicate snippet name
- database cannot be contacted
- unexpected error from database

improve data storage
- store keys, messages in standard format (eg, convert user input to all lower case)
- search for keys in standard format (eg, convert user input to all lower case)
- do not allow duplicate keys to be created in DB for same value, different capitalisation

improve logging

