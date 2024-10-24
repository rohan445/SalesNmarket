import sqlite3
import pandas as pd

# Load the Walmart Sales Dataset from a CSV file
file_path = 'path_to_walmart_sales_dataset.csv'
data = pd.read_csv(file_path)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('walmart_sales.db')
cursor = conn.cursor()

# Create the sales_data table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_data (
        Store INTEGER,
        Date TEXT,
        Holiday INTEGER,
        Temperature REAL,
        Fuel_Price REAL,
        MarkDown1 REAL,
        MarkDown2 REAL,
        MarkDown3 REAL,
        MarkDown4 REAL,
        MarkDown5 REAL,
        CPI REAL,
        Unemployment REAL,
        IsHoliday INTEGER,
        Weekly_Sales REAL
    )
''')

# Insert data into the sales_data table
data.to_sql('sales_data', conn, if_exists='replace', index=False)

# Commit and close connection
conn.commit()
conn.close()
