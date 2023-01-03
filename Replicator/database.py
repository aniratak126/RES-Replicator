

import sqlite3
from collections import defaultdict

def create_tables(db_name = 'consumers.db'):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    statement_table1 = ("""CREATE TABLE IF NOT EXISTS consumers (id integer PRIMARY KEY,
                                                            name text,
                                                            last_name text,
                                                            street text,
                                                            street_num integer,
                                                            postal_code integer,
                                                            city text)  """)

    statement_table2 = ("""CREATE TABLE IF NOT EXISTS consumption_info (consumer_id integer,
                                                                consumption real,
                                                                month text)""")
    
    cur.execute(statement_table1)
    cur.execute(statement_table2)

    conn.commit()
    conn.close()


def add_consumer(id, name, last_name, street, street_num, postal_code, city, db_name = 'consumers.db'):


    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    try:
        cur.execute("""INSERT INTO consumers (id, name, last_name, street, street_num, postal_code, city)
                                        VALUES(?, ?, ?, ?, ?, ?, ?)""", (id, name, last_name, street, street_num, postal_code, city))
    except sqlite3.IntegrityError:
        raise sqlite3.IntegrityError("User with this id already exists")
    
    conn.commit()
    conn.close()

def update_consumer(id, consumption, month, db_name = 'consumers.db'):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""SELECT * FROM consumers WHERE id = ?""", (id, ))
    consumer = cur.fetchone()
    if consumer == None:
        print("Consumer does not exists.")
        #return 0

    cur.execute("""SELECT * FROM consumption_info WHERE consumer_id = ? AND month = ?""", (id, month))
    data = cur.fetchone()

    if data:
        cur.execute("""UPDATE consumption_info SET consumption = consumption + ? WHERE consumer_id = ? AND month = ?""", (consumption, id, month))
    else:
        cur.execute("""INSERT INTO consumption_info VALUES(?,?,?)""", (id, consumption, month))

    conn.commit()
    conn.close()

#def delete_consumer(id, db_name = 'consumers_db'):
#    conn = sqlite3.connect(db_name)
#    cur = conn.cursor()

#    try:
#        cur.execute("""DELETE FROM consumers WHERE id = ? """,(id))
#    except sqlite3.IntegrityError:
#        print("User with this id does not exists")

#    conn.commit()
#    conn.close()

def read_all_consumers( db_name = 'consumers.db'):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""SELECT * FROM consumers """)
    
    data = cur.fetchall()
    conn.close()
    
    return data

def read_consumer(id, db_name = 'consumers.db'):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""SELECT * FROM consumers WHERE id = ?""", (id,))
    
    data = cur.fetchone()
    conn.close()
    
    return data

def consumption_info(db_name = 'consumers.db'):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""SELECT * FROM consumption_info """)
    
    data = cur.fetchall()
    conn.close()
    
    return data

if __name__ == "__main__": # pragma: no cover
    create_tables()
    #print(read_all_consumers())
    #print(consumption_info())

    