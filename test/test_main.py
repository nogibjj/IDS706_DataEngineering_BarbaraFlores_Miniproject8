"""
Test

"""
import sqlite3
import unittest

class TestDatabaseQuery(unittest.TestCase):
    def setUp(self):
        self.db_path = "src/data/WorldSmallDB.db"

    def test_query_random_records(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM WorldSmallDB ORDER BY RANDOM() LIMIT 5")
        data = cursor.fetchall()
        conn.close()
        self.assertEqual(len(data), 5)

    def test_query_records_per_continent(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT region, COUNT(*) AS N FROM WorldSmallDB GROUP BY region")
        data = cursor.fetchall()
        conn.close()
        self.assertTrue(len(data) > 0)

    def test_query_gdp_per_continent(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT region, AVG(gdppcap08), MIN(gdppcap08), MAX(gdppcap08) FROM WorldSmallDB GROUP BY region"
        )
        data = cursor.fetchall()
        conn.close()
        self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    unittest.main()
