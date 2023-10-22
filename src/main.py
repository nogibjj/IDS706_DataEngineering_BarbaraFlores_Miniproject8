"""
ETL-Query script
"""
import sqlite3
from prettytable import PrettyTable


def query():
    db_path = "src/data/WorldSmallDB.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("\nLet's quickly review our database. Let's take a sample of how it is constructed.\n")
    cursor.execute("SELECT * FROM WorldSmallDB ORDER BY RANDOM() LIMIT 5")
    print_table(cursor, cursor.fetchall())

    print("\nHow many records per continent does our database have?\n")
    cursor.execute(
        "SELECT region, COUNT(*) AS N FROM WorldSmallDB GROUP BY region"
    )
    print_table(cursor, cursor.fetchall())

    print("\nHow does Gross Domestic Product per capita behave in 2008 in each continent? What are its mean, maximum, and minimum values?\n")
    cursor.execute(
        "SELECT region, AVG(gdppcap08), MIN(gdppcap08), MAX(gdppcap08) FROM WorldSmallDB GROUP BY region"
    )
    print_table(cursor, cursor.fetchall())
    conn.close()

def print_table(cursor, data):
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in data:
        table.add_row(row)
    print(table)

def main():

    # Query
    print("Consultando datos...")
    query()

if __name__ == "__main__":
    main()