#  Sales Analysis Dashboard Streamlit App - Python

##  Introduction
An attempt has been made to recreate the interactive **Sales Analysis Dashboard** originally built in **Power BI**—using Python and Streamlit, developing it into an interactive web-based application. It provides a comprehensive overview of sales performance across different regions, products, time periods and zones. The dashboard enables quick insights into revenue trends, top-performing categories, customer segmentation, and KPIs such as total sales, profit margins, and monthly growth.

##  Files Included
- `Sreamlit_dashboard.py` – Python sourse file
- `SalesDash1.png` – A preview of the dashboard
- `SalesDash2.png` – Another preview of the dashboard
##  Key Features

- Total Sales, Profit, and Units Sold by year, month and region
- Dynamic filtering by product category and customer segment
- Year-over-Year comparison and percentage growth
- Top 5 performing products and customers by revenue
- Region-wise breakdown using interactive maps
- Monthly trend analysis using line chart

 ##  Dashboard_Screenshot
<img width="800" alt="Dashboard" src="https://github.com/shince455/Hardware-Sales-Analysis-Dashboard-Streamlit-Python/blob/main/SalesDash1.png" />
<img width="800" alt="Dashboard" src="https://github.com/shince455/Hardware-Sales-Analysis-Dashboard-Streamlit-Python/blob/main/SalesDash2.png" />

## Key takeaways from the analysis:

- Top-Performing Products: Identified the highest revenue-generating products and categories, helping prioritize inventory and marketing strategies.
- Sales by Region: Revealed regional sales trends and highlighted high-performing states, enabling location-based decision-making.
- Revenue Growth: Tracked monthly and yearly revenue trends to evaluate the company’s growth trajectory over time.
- Customer Segments: Analyzed customer types and their impact on total revenue.
- Profitability Analysis: Used DAX to calculate profit margins and compare performance across different product categories and customer segments.
- Currency Normalization: A custom column was created to standardize foreign currency sales into a single currency (INR), using conditional logic.
All results were validated using SQL queries on the original dataset, ensuring accuracy and consistency between raw data and visual representation.

##  Data Source

The original dataset was taken from:
[codebasics.io – Sales Insights Data Analysis Project](https://codebasics.io/resources/sales-insights-data-analysis-project)

##  How to Use

1. Download the .sql file (db_dump_version_2) to your local machine from the link provided.
2. Import the .sql file into a local SQL database (e.g., MySQL, SQLite, PostgreSQL).
3. Once the dependencies are installed and your database is running, you can launch the application locally by executing the Python script using Streamlit.
4. In your terminal or command prompt, navigate to the project directory and run: streamlit run "path/to/your/Sreamlit_dashboard.py"
5. Once the Streamlit web app is launched, a browser window will automatically open (or you can manually open http://localhost:port_number in your browser).

From there:
- Use the sidebar on the left to navigate through the available options, filters, and analysis views.
- You’ll be able to interact with and explore a variety of data visualizations.

💡 The sidebar acts as the control panel for customizing and interacting with the dashboard visuals.

 
 **Note**: 
- *This app connects to a local MySQL database using SQLAlchemy and PyMySQL*
- *Make sure your MySQL server is running and accessible at your localhost and port*
- *In the Python script, replace with your own credentials:*
  engine = create_engine("mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>")
- *You can run the Sreamlit_dashboard.py script using any Python-compatible development environment,*
- *You can freely modify or extend the Python script and tailor the dashboard to better suit your specific analysis goals.*


##  Disclaimer

- The data used in this project is publicly available and intended solely for educational and portfolio purposes.


---

## Contact

Created by **[Shince Joseph]**  
[shincejosephv@gmail.com] 
