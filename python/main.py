import sqlite3
from prettytable import PrettyTable
import time
import psutil

def print_table(cursor, data):
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in data:
        table.add_row(row)
    print(table)

def execute_query(cursor, query):
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss
    cursor.execute(query)
    data = cursor.fetchall()
    end_time = time.time()
    elapsed_time = end_time - start_time
    memory_after = process.memory_info().rss
    memory_diff = memory_after - memory_before
    print_table(cursor, data)
    print(f"Query completed in {elapsed_time:.6f} seconds")
    print(f"Memory used: {memory_diff / (1024 * 1024):.8f} MB")  # Aumento de precisión a 4 decimales

def main():
    db_path = "data/WorldSmallDB.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("Querying data...")
    
    print("\nLet's quickly review our database. Let's take a sample of how it is constructed.\n")
    execute_query(cursor, "SELECT * FROM WorldSmallDB ORDER BY RANDOM() LIMIT 5")
    
    print("\nHow many records per continent does our database have?\n")
    execute_query(cursor, "SELECT region, COUNT(*) AS N FROM WorldSmallDB GROUP BY region")
    
    conn.close()

if __name__ == "__main__":
    main()
