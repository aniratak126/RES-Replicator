import sqlite3
import unittest
from database import *

class TestDatabase(unittest.TestCase):
    """def drop(self):
        conn = sqlite3.connect('test_database.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE consumers;')
        cur.execute('DROP TABLE consumption_info;')
        conn.commit()
        conn.close()"""

    def free_tables(self):
        conn = sqlite3.connect('test_database.db')
        cur = conn.cursor()
        
        create_tables('test_database.db')

        cur.execute("DELETE FROM consumers;")
        cur.execute("DELETE FROM consumption_info;")

        conn.commit()
        conn.close()

    def test_add_consumer(self):
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        consumer = read_consumer(1, 'test_database.db')

        #print(consumer)
        self.assertEqual(consumer[1],"Marko")

    def test_update_consumer_first(self):
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        update_consumer(1,10,1,'test_database.db')

        conn = sqlite3.connect('test_database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM consumption_info WHERE consumer_id = 1 AND month = 1 ")
        data = cur.fetchone()

        #print(data)
        self.assertEqual(data, (1,10,1))
        conn.close()

    def test_update_consumer_second(self):

        # update 2 puta (sabira potrosnju)
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        update_consumer(1,10,1,'test_database.db')
        update_consumer(1,10,1,'test_database.db')

        conn = sqlite3.connect('test_database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM consumption_info WHERE consumer_id = 1 AND month = 1 ")
        data = cur.fetchone()

        #print(data)
        self.assertEqual(data, (1,20,1))
        conn.close()

    def test_read_consumer(self):
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        data = read_consumer(1, 'test_database.db')

        self.assertEqual(data,(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad'))

    def test_read_consumer_second(self):
        # user sa odgovaracujim id-em ne postoji
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        data = read_consumer(2, 'test_database.db')

        self.assertEqual(data, 0)

    def test_read_all_consumers(self):
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        add_consumer(2, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        add_consumer(3, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')

        data = read_all_consumers('test_database.db')

        self.assertEqual(data,[(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad'), (2, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad'), (3, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad')])



if __name__ == "__main__":
    unittest.main()