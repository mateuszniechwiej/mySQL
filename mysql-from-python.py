import os
import datetime
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
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # the above will display as a warning(not an error) if the
        # table already exists
finally:
    # Close the connection, regardless of whatever the above was successful
    connection.close()