extern crate rusqlite;
extern crate prettytable;

use rusqlite::Connection;
use prettytable::{Table, Row, Cell};

fn print_table(_cursor: &rusqlite::Statement, data: Vec<Vec<String>>) {
    let mut table = Table::new();
    for row in data.iter() {
        let cells: Vec<Cell> = row.iter().map(|value| Cell::new(value)).collect();
        table.add_row(Row::new(cells));
    }
    table.printstd();
}

fn query() -> Result<(), rusqlite::Error> {
    let db_path = "data/WorldSmallDB.db";
    let conn = Connection::open(db_path)?;

    // Query 1
    let mut cursor = conn.prepare("SELECT * FROM WorldSmallDB ORDER BY RANDOM() LIMIT 5")?;
    let rows = cursor
        .query_map([], |row| {
            let mut values = Vec::new();
            for i in 0..row.column_count() {
                values.push(row.get(i)?);
            }
            Ok(values)
        })?
        .collect::<Result<Vec<Vec<String>>, rusqlite::Error>>()?;

    println!("\nLet's quickly review our database. Let's take a sample of how it is constructed.\n");
    print_table(&cursor, rows);

    // Query 2
    let mut cursor = conn.prepare("SELECT region, COUNT(*) AS N FROM WorldSmallDB GROUP BY region")?;
    let rows = cursor
        .query_map([], |row| {
            let region: String = row.get(0)?;
            let count: i64 = row.get(1)?;
            Ok((region, count))
        })?
        .collect::<Result<Vec<(String, i64)>, rusqlite::Error>>()?;

    println!("\nHow many records per continent does our database have?\n");
    print_table(&cursor, rows.iter().map(|(r, c)| vec![r.clone(), c.to_string()]).collect());

    // Query 3
    let mut cursor = conn.prepare("SELECT region, AVG(gdppcap08), MIN(gdppcap08), MAX(gdppcap08) FROM WorldSmallDB GROUP BY region")?;
    let rows = cursor
        .query_map([], |row| {
            let region: String = row.get(0)?;
            let avg: f64 = row.get(1)?;
            let min: f64 = row.get(2)?;
            let max: f64 = row.get(3)?;
            Ok((region, avg, min, max))
        })?
        .collect::<Result<Vec<(String, f64, f64, f64)>, rusqlite::Error>>()?;

    println!("\nHow does Gross Domestic Product per capita behave in 2008 in each continent? What are its mean, maximum, and minimum values?\n");
    print_table(
        &cursor,
        rows
            .iter()
            .map(|(r, avg, min, max)| vec![r.clone(), avg.to_string(), min.to_string(), max.to_string()])
            .collect(),
    );

    Ok(())
}

fn main() {
    // Query
    println!("Querying data...");
    if let Err(err) = query() {
        eprintln!("Error: {:?}", err);
    }
}
