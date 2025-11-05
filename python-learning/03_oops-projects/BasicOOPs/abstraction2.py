from abc import ABC, abstractmethod
import csv
import json
import sqlite3


class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass

class CSVDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        print(f"Reading data from CSV file: {self.filename}")
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)


class JSONDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        print(f"Reading data from JSON file: {self.filename}")
        with open(self.filename, 'r') as file:
            return json.load(file)


class DatabaseDataSource(DataSource):
    def __init__(self, db_name, table):
        self.db_name = db_name
        self.table = table

    def read_data(self):
        print(f"Reading data from database: {self.db_name}, table: {self.table}")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        conn.close()
        return [dict(zip(columns, row)) for row in rows]


# --- Higher-level code (uses abstraction) ---
def process_data(source: DataSource):
    data = source.read_data()
    print(f"Loaded {len(data)} records.")
    # Do something with the data
    for record in data[:2]:  # just preview first 2
        print(record)


# --- Usage ---
csv_source = CSVDataSource("data.csv")
json_source = JSONDataSource("data.json")
db_source = DatabaseDataSource("example.db", "users")

# You can switch sources easily without touching process_data()
process_data(csv_source)
process_data(json_source)
process_data(db_source)


"""
The DataSource class defines what must be done (read_data()), but not how.
Each subclass (CSV, JSON, DB) handles its own complex implementation.
The process_data() function doesn’t care where the data comes from — it just uses the abstraction.
That’s true abstraction: you hide the messy internal logic (file parsing, DB connection, etc.) and expose only a simple interface.
"""
