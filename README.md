E-commerce Return Analysis Project 

📌 Objective The goal of this project is to analyze product return behavior in an e-commerce business using data science techniques. It identifies return trends, predicts high-risk products, and presents interactive dashboards to help reduce return rates and optimize decision-making.

🛠️ Tools & Technologies

Python: Data cleaning, analysis, modeling
Pandas: Data manipulation
Scikit-learn: Predictive modeling (Logistic Regression)
Power BI: Visualization and dashboard creation
VS Code: Development environment
📂 Datasets

orders.csv: Contains order details (order_id, product_id, order_date, category, supplier, price, region, marketing_channel)
returns.csv: Contains return details (order_id, product_id, return_date)
✅ Key Steps

Data Preparation
Loaded orders and returns CSVs
Removed nulls and duplicates
Fixed date formats (order_date, return_date)
Merged datasets on order_id
Created is_returned flag (1 = returned, 0 = not)
Return Rate Analysis
Grouped by:
Category
Supplier
Region
Marketing Channel
Calculated return percentages
Predictive Modeling
Built a Logistic Regression model
Features: price, category, supplier
Created a new column: return_probability
Identified high-risk products (probability > 0.5)
Power BI Dashboard
Bar Charts: Return rate by category/supplier
Line Chart: Monthly return trends
Table: High-risk product list
Slicers: Category, Region, Supplier
Drill-through page for category-level insights
📊 Outputs

merged_orders_returns.csv: Cleaned & merged dataset with return flags
high_risk_products.csv: Products with return probability > 0.5
Power BI interactive dashboard
Final report: [Ecommerce_Return_Analysis_Report.pdf]
🚀 Future Enhancements

Use Random Forest or XGBoost for improved predictions
Add customer-level behavior and feedback data
Deploy dashboard via Power BI Service for team access
📌 Conclusion This project offers actionable insights into customer return behavior. The interactive Power BI dashboard allows users to explore trends, identify problematic segments, and use predictive analytics to anticipate future returns.
