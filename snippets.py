import logging
import argparse
import psycopg2


# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")


def put(name, snippet):
    '''Store a snippet with an associated name.'''
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet
  

def get(name):
    '''Retrieve the snippet with a given name to return snippet. 
    If snippet not found, return 404 snippet not found error'''
    logging.info("Retrieving snippet {!r}".format(name))
    cursor = connection.cursor()
    command = "select message from snippets where keyword=%s"
    cursor.execute(command, (name,))
    row = cursor.fetchone()
    if not row:
        # No snippet was found with that name.
        return "404: Snippet Not Found"
    return row[0]
    #return cursor.fetchone()
    #logging.error("FIXME: Unimplemented - get({!r})".format(name))
    #return ""
    
def catalogue():
    '''Get the list of snippet names in order to search snippet by name'''
    logging.info("Retrieving list of snippet name(s)")
    cursor = connection.cursor()
    command = "select keyword from snippets order by keyword desc"
    cursor.execute(command, ())
    results = cursor.fetchall()
    keywords = ''
    for keyword in results: 
        keywords = keywords + keyword[0] + '; '
    return keywords[:-1]
        
        

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")
    
    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="Name of the snippet")
    
    # Subparser for the catalogue command
    logging.debug("Constructing catalogue subparser")
    get_keys_parser = subparsers.add_parser("catalogue", help="Retrieve the list of names for snippets")
    # no arguments required


    arguments = parser.parse_args()   
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    if command == "catalogue":
        keywords = catalogue()
        print("Retrieving all snippet names: {!r}".format(keywords))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
    

if __name__ == "__main__":
    main()