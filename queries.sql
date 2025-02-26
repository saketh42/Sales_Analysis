-- Total Revenue
SELECT SUM(Total_Sales) AS Total_Revenue FROM Sales;

-- Top-Selling Products
SELECT Product, SUM(Total_Sales) AS Revenue 
FROM Sales 
GROUP BY Product 
ORDER BY Revenue DESC 
LIMIT 5;

-- Monthly Sales Trend
SELECT strftime('%Y-%m', Date) AS Month, SUM(Total_Sales) 
FROM Sales 
GROUP BY Month;

-- Total Sales by Category
SELECT Category, SUM(Total_Sales) AS Total_Category_Sales 
FROM Sales 
GROUP BY Category;
