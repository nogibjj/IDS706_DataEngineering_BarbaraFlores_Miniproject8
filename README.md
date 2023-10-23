[![CI](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/actions/workflows/cicd.yml)

IDS706_DataEngineering_BarbaraFlores_Miniproject8
## 📂 Rewrite a Python Script in Rust

This project involves rewriting an existing Python data processing script in the Rust programming language. The goal is to assess the improvements in terms of speed and resource usage achieved by moving from Python to Rust. The scripts are designed to process data from a SQLite database and display the results.

### 1. Take an existing Python script for data processing
We will use the Python script [main.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/blob/main/python/main.py) from previous tasks, which connects to an SQLite database named [WorldSmallDB.db](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/blob/main/data/WorldSmallDB.db) and executes various SQL queries. The primary purpose is to summarize the database and provide descriptive statistics about it.

### 2. Rewrite it in Rust
Starting from the previous script and utilizing the Copilot tool, the code was rewritten in the Rust language. To accomplish this, the environment was set up with Rust's package manager, Cargo, and necessary dependencies were added. The Python code was then translated and adapted into Rust code [main.rs](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/blob/main/rust/main.rs). The performance was monitored, and a comparison report was generated to assess any improvements in execution speed and resource efficiency. The primary goal was to maintain functionality while optimizing the code's performance.

### 3. Highlight improvements in speed and resource usage
In the following images, we provide a comparative analysis of the Python script [main.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/blob/main/python/main.py) and its Rust counterpart [main.rs](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/blob/main/rust/main.rs). The analysis focuses on execution speed and resource usage.

#### Python
![Python Performance](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/main/images/python_performance.png)

#### Rust

![Rust Performance](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject8/main/images/rust_performance.png)

The following table clearly shows the differences in execution times between Python and Rust. In both queries, Rust significantly outperforms Python in terms of speed, with execution times in microseconds (µs) rather than milliseconds (ms) as in Python. This highlights the efficiency of Rust in handling database queries compared to Python.

| Script | Query | Execution Time |
|--------|-------|-----------------|
| Python |   1   | 0.000310 seconds |
| Python |   2   | 0.000105 seconds |
| Rust   |   1   | 307.30µs seconds |
| Rust   |   2   | 100.10µs seconds |


