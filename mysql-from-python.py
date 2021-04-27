import os
import pymysql

# get username from gitpod workspace

username = os.getenv('C9_USER')

# Connect to the db

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')


try:
    #Run a query
    with connection.cursor() as cursor:
        list_of_names = ['Fred']
        # Prepare a string with the same number od placeholder as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whatever the above was successful
    connection.close()