-- Question 1: Which products generate the highest total sales?

SELECT Product,
       SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC;


-- Question 2: Which product categories generate the highest total sales?

SELECT Category,
       SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;


-- Question 3: Which cities generate the highest total sales?

SELECT City,
       SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY City
ORDER BY Total_Sales DESC;


-- Question 4: Which products have the highest quantity sold?

SELECT Product,
       SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Product
ORDER BY Total_Quantity DESC;


-- Question 5: What is the monthly sales trend?

SELECT Order_Year,
       Order_Month,
       Order_Month_Name,
       SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Order_Year, Order_Month, Order_Month_Name
ORDER BY Order_Year, Order_Month;


-- Question 6: How do total sales compare between male and female customers?

SELECT Gender,
       SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Gender
ORDER BY Total_Sales DESC;


-- Question 7: Which products have the highest average unit price?

SELECT Product,
       AVG(Unit_Price) AS Average_Unit_Price
FROM sales
GROUP BY Product
ORDER BY Average_Unit_Price DESC;