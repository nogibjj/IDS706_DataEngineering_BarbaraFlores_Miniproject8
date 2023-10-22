"""
ETL-Query script
"""

import os
import requests
import sqlite3
import csv
from prettytable import PrettyTable


def extract(url="https://raw.githubusercontent.com/nickeubank/practicaldatascience/master/Example_Data/world-small.csv", 
            file_path="EtlTool/data/WorldSmall.csv"):
    """Extract a URL to a file path"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    timeout = 100
    with requests.get(url, timeout=timeout) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



def load(dataset="EtlTool/data/WorldSmall.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Imprime el directorio de trabajo actual y la ruta completa
    print(os.getcwd())

    with open(dataset, 'r', encoding='utf-8', newline='') as file:
        payload = csv.reader(file, delimiter=',')

        db_path = "EtlTool/data/WorldSmallDB.db"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS WorldSmallDB")
        c.execute("CREATE TABLE WorldSmallDB (country, region, gdppcap08, polityIV)")
        
        data = list(payload)
        
        for _, row in enumerate(data):
            country = row[0]
            region = row[1]
            gdppcap08 = row[2]
            polityIV = row[3]
            
            c.execute("INSERT INTO WorldSmallDB VALUES (?, ?, ?, ?)", (country, region, gdppcap08, polityIV))

        conn.commit()
        conn.close()

    return "WorldSmallDB.db"


def update_region_column(cursor):
    cursor.execute("""
        UPDATE WorldSmallDB
        SET region = 
            CASE 
                WHEN region = 'C&E Europe' THEN 'Central and Eastern Europe'
                WHEN region = 'N. America' THEN 'North America'
                WHEN region = 'S. America' THEN 'South America'
                WHEN region = 'W. Europe' THEN 'Western Europe'
                ELSE region
            END;
    """)
    print("\nColumn 'region' updated successfully.")

def query():
    db_path = "EtlTool/data/WorldSmallDB.db"
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

    print("We are going to transform the 'region' column to make it more explanatory, replacing 'C&E Europe' with 'Central and Eastern Europe', 'N. America' with 'North America',\n'S. America' with 'South America', and 'W. Europe' with 'Western Europe.")
    update_region_column(cursor)

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
    # Extract
    print("Extrayendo datos...")
    extract()

    # Transform and load
    print("Transformando datos...")
    load()

    # Query
    print("Consultando datos...")
    query()

if __name__ == "__main__":
    main()