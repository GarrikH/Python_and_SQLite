# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:04:07 2020

@author: Garrik Hoyt
"""

import sqlite3

# Open a database connection
connection = sqlite3.connect('chinook.db')

# cursors allow us to interact with the db
cursor = connection.cursor()

result_set = cursor.execute('SELECT * FROM Track;')

# for row in result_set:
#     # row = tuple object where each element is a value
#     print(row[1]) # print out song names
    
# this must be a tuple
favorite_artist = ('Miles Davis',)
result_set = cursor.execute('SELECT * FROM Track WHERE Composer=?', favorite_artist)
# Don't use Python's format fn or % BC of SQL Injection attacks

# Get one row at a time/ fetch one row at a time
print(result_set.fetchone())
print(result_set.fetchone())

#close the cursor
cursor.close()
# close the db connnection after we are done
connection.close()
