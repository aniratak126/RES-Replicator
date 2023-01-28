import unittest, unittest.mock, sqlite3
from reports import *
from database import *

class TestReports(unittest.TestCase):
    def free_tables(self):
        conn = sqlite3.connect('test_database.db')
        cur = conn.cursor()
        
        create_tables('test_database.db')

        cur.execute("DELETE FROM consumers;")
        cur.execute("DELETE FROM consumption_info;")

        conn.commit()
        conn.close()

    def test_monthlyConsumptionByStreet(self):
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        update_consumer(1,10,1,'test_database.db')
        
        _, temp = monthly_consumption_by_street('Novosadska', 'test_database.db')

        self.assertIsInstance(temp, dict)
        self.assertEqual(temp, {1: 10.0})

    def test_monthlyConsumptionByConsumer(self):
        self.free_tables()
        add_consumer(1, 'Marko', 'Markovic', 'Novosadska', 22, 21000, 'Novi Sad', 'test_database.db')
        update_consumer(1,10,1,'test_database.db')
        
        _, temp = monthly_consumption_by_consumer(1,'test_database.db')
        self.assertIsInstance(temp, dict)
        self.assertEqual(temp, {1: 10.0})

    @unittest.mock.patch('reports.monthly_consumption_by_street')
    @unittest.mock.patch('reports.monthly_consumption_by_consumer')
    @unittest.mock.patch('builtins.input')
    def test_menu(self, input_patch, func_patch_1, func_patch_2):
        
        input_patch.side_effect = ['1', 'Partizanskih baza', '2', '5', '0']
        x = menu()
        y = menu()
        
        func_patch_1.assert_called_once()
        func_patch_2.assert_called_once()
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        

if __name__ == "__main__":
    unittest.main()