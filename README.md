## Background

'snippets-app-python' is a simple program that is based on a thinkful task for programming in python3. 

The app enables users to run the program from the command line, providing commands and queries as arguments, in order to interact with a postgres database that contains 'snippets'. The app also demonstrates basic logging. 

The app utilises [logging](https://docs.python.org/3/library/logging.html), [argparse](https://docs.python.org/3/library/argparse.html) & [psycopg2](http://initd.org/psycopg/docs/) libraries. 

Snippets are stored in a simple format: keyword, message. 

Given that the program is downloaded, any of the following commands can be executed from the project's root folder, in order to utilise the program: 

Get a list of the names of all snippets: 

     python3 snippets.py catalogue


Get the details of a snippet, using a specific name
Note that the names can be found via the previous command

     python3 snippets.py get <snippet_name>


Search for a snippet using any string, to find matching snippets that contain the string in the message

     python3 snippets.py search <search_query>

Add a new snippet to the database, providing snippet name and snippet message

     python3 snippets.py put <snippet_name>  <snippet_message>

## Pre-requisites

1) Download the project
2) Postgres database installed/started
