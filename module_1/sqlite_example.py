import sqlite3
import queries as q
import pandas as pd

# Create a DB function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    # create the cursor
    curs = conn.cursor()

    # use the cursor to execute a particular query
    curs.execute(query)

    return curs.fetchall()

if __name__ == '__main__':
    # create a connection to the database
    conn = connect_to_db()
    # execute a specific query
    # print(execute_q(conn, q.SELECT_ALL)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHAR)
    df = pd.DataFrame(results)
    print(df.head())


# step 1: connect to database
# triple-check spelling because if the database
# does not exist, then sqlite3 will create a new database
# with that misspelled name
# connection = sqlite3.connect('rpg_db.sqlite3')

# step 2: create a cursor
# cursor is like a bank teller who goes to the vault to get your withdrawal
# you are not allowed to go to the vault, but the teller can because he/she
# knows the protocol and safety procedures that need to be followed in order
# to access the money (or in this case, data) in a safe, appropriate manner.
# So we can never directly touch or query the database, it must be done
# through a cursor.
# cursor = connection.cursor()

# step 3: create the query
# but it might be nice to have all queries in their own file
# query = 'SELECT character_id, name FROM charactercreator_character;' # end with ;

# step 4: execute the query and fetch the results (grab the money)
# but don't repeat yourself
# results = cursor.execute(q.SELECT_ALL).fetchall()
