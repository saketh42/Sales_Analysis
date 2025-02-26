import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Run create table SQL
with open("create_table.sql", "r") as f:
    cursor.executescript(f.read())

# Run insert data SQL
with open("insert_data.sql", "r") as f:
    cursor.executescript(f.read())

# Load data into Pandas DataFrame
df = pd.read_sql_query("SELECT strftime('%Y-%m', Date) AS Month, SUM(Total_Sales) AS Revenue FROM Sales GROUP BY Month;", conn)

# Plot sales trends
plt.figure(figsize=(8,4))
plt.plot(df["Month"], df["Revenue"], marker='o', linestyle='-')
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.show()

# Close connection
conn.close()
