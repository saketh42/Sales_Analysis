# Sales Data Analysis - SQL & Python

## 📌 Project Overview
This project analyzes sales data using **SQL & SQLite** and visualizes trends with **Python**. The dataset contains sales transactions, and SQL queries extract meaningful insights.

## 📂 Files Included
- **sales.db** → SQLite database with tables:
  - `Sales` → Raw sales data
  - `Sales_Analysis` → Aggregated insights
- **create_table.sql** → SQL script to create the `Sales` table
- **insert_data.sql** → SQL script to insert sample records
- **queries.sql** → SQL script with analysis queries
- **sales_analysis.py** → Python script for visualization

## 🛠 Setup & Usage
### 1️⃣ Load the Database
```bash
sqlite3 sales.db
```
Run SQL scripts (for MySQL, use `mysql -u root -p`):
```bash
sqlite3 sales.db < create_table.sql
sqlite3 sales.db < insert_data.sql
```

### 2️⃣ Run SQL Queries
```bash
sqlite3 sales.db < queries.sql
```

### 3️⃣ Run Python Analysis (Optional)
```bash
python sales_analysis.py
```

## 📊 Key Features
- **Data Cleaning**: Handles duplicates & missing values
- **SQL Analysis**:
  - Total revenue
  - Top-selling products
  - Monthly sales trends
- **Visualization** (Python, Matplotlib)

## 🔮 Future Improvements
- Expand dataset with more categories
- Implement real-time dashboard using Power BI/Tableau

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify!

