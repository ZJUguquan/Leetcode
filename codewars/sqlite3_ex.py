'passed solution'

import sqlite3
from contextlib import closing

with sqlite3.connect('/tmp/movies.db') as db:
  with closing(db.cursor()) as cursor:
    cursor.execute('''
        CREATE TABLE MOVIES(id INTEGER PRIMARY KEY,
                            Name TEXT unique,
                            Year INTEGER,
                            Rating INTEGER)
    ''')

    movies = [("Rise of the Planet of the Apes", 2011, 77),
              ("Dawn of the Planet of the Apes", 2014, 91),
              ("Alien", 1979, 97),
              ("Aliens", 1986, 98),
              ("Mad Max", 1979, 95),
              ("Mad Max 2: The Road Warrior", 1981, 100)]

    cursor.executemany("INSERT INTO MOVIES(Name, Year, Rating) VALUES(?,?,?)", movies)
    db.commit()


# import sqlite3

# conn = sqlite3.connect('example.db')
# c = conn.cursor()

# # SQL

# for row in c.execute('SELECT * FROM MOVIES'):
#         print(row)

# # Create table
# c.execute('''CREATE TABLE MOVIES
#              (name text, year text, rating real)''')

# # Insert a row of data
# c.execute("INSERT INTO MOVIES VALUES ('Rise of the Planet of the Apes','2011',77)")
# c.execute("INSERT INTO MOVIES VALUES ('Dawn of the Planet of the Apes','  2014',91)")
# c.execute("INSERT INTO MOVIES VALUES ('Alien','1979',97)")
# c.execute("INSERT INTO MOVIES VALUES ('Aliens','1986',98)")
# c.execute("INSERT INTO MOVIES VALUES ('Mad Max','1979',95)")
# c.execute("INSERT INTO MOVIES VALUES ('Mad Max 2: The Road Warrior','1981',100)")
# # Save (commit) the changes
# conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


#Movies match the list in the table
# set([(u'Mad Max', 1979, 95), (u'Dawn of the Planet of the Apes', 2014, 91), (u'Mad Max 2: The Road Warrior', 1981, 100), (u'Rise of the Planet of the Apes', 2011, 77), (u'Alien', 1979, 97), (u'Aliens', 1986, 98)]) should equal set([(u'Aliens', u'1986', 98.0), (u'Rise of the Planet of the Apes', u'2011', 77.0), (u'Dawn of the Planet of the Apes', u'  2014', 91.0), (u'Alien', u'1979', 97.0), (u'Mad Max 2: The Road Warrior', u'1981', 100.0), (u'Mad Max', u'1979', 95.0)])