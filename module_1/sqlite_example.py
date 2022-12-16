# Step 0: Import sqlite
import sqlite3
import queries as q

# step 1: connect to database
# triple-check spelling because if the database
# does not exist, then sqlite3 will create a new database
# with that misspelled name
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2: create a cursor
# cursor is like a bank teller who goes to the vault to get your withdrawal
# you are not allowed to go to the vault, but the teller can because he/she
# knows the protocol and safety procedures that need to be followed in order
# to access the money (or in this case, data) in a safe, appropriate manner.
# So we can never directly touch or query the database, it must be done
# through a cursor.
cursor = connection.cursor()

# step 3: create the query
# but it might be nice to have all queries in their own file
# query = 'SELECT character_id, name FROM charactercreator_character;' # end with ;

# step 4: execute the query and fetch the results (grab the money)
# but don't repeat yourself
results = cursor.execute(q.SELECT_ALL).fetchall()


if __name__ == '__main__':
    print(results[:5])