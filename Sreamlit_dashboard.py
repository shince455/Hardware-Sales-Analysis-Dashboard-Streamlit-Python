import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px 
import plotly.graph_objects as go
import sqlalchemy
from sqlalchemy import create_engine
import os
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import streamlit as st
# ------------------------------
# Set the page
# ------------------------------
st.set_page_config(layout="wide")
# st.title("Sample sales Dash Board")
st.markdown(
    "<h1 style='text-align: center; padding-top: 10px; font-size: 40px; color: #2E86C1;'>Sample Sales Dashboard</h1>",
    unsafe_allow_html=True
)
#------------------------------
# Create data frame
#------------------------------
engine = create_engine("mysql+pymysql:xxxxxxxxxxx") # Use your username and password here
customers = pd.read_sql('SELECT * FROM customers', engine)
date = pd.read_sql('SELECT * FROM date', engine)
markets = pd.read_sql('SELECT * FROM markets', engine)
products = pd.read_sql('SELECT * FROM products', engine)
transactions = pd.read_sql('SELECT * FROM transactions', engine)

transactions['order_date'] = pd.to_datetime(transactions['order_date'])
transactions['year'] = transactions['order_date'].dt.year
transactions['month'] = transactions['order_date'].dt.month_name()

new_df = transactions \
    .merge(markets, left_on='market_code', right_on='markets_code', how='left') \
    .merge(customers, on='customer_code', how='left')  # Merge 'transactions', 'markets' and 'customers'

#----------------------------
# Add filters (sidebar)
#----------------------------
months = new_df['month'].dropna().unique()
months = sorted(months)  # sort them if needed
month_options = ["All"] + list(months) # Provide option to select all months
years = new_df['year'].dropna().unique().astype(int)
zones = new_df['zone'].unique()


selected_year = st.sidebar.selectbox("Select Year", years)
selected_months = st.sidebar.multiselect("Select Month", month_options, default="All")
selected_zone = st.sidebar.multiselect("Select Zone(s)", zones, default=zones)
if 'All' in selected_months or not selected_months:
    filtered_df = new_df[(new_df['zone'].isin(selected_zone)) & (new_df['year']==(selected_year)) & (new_df['month'].isin(months))]
else:
    filtered_df = new_df[(new_df['zone'].isin(selected_zone)) & (new_df['year']==(selected_year)) & (new_df['month'].isin(selected_months))]  # Filter required data

# ----------------------------------------------------------
# Display total revenue and sales quantity on the dash board
#-----------------------------------------------------------
total_revenue = filtered_df['sales_amount'].sum() # Find total sales revenue
total_qty = filtered_df['sales_qty'].sum() # Find total sales quantity

figsize = (5,3)
filtered_df['month'] = filtered_df['order_date'].dt.month
monthly_sales = filtered_df.groupby('month')['sales_amount'].sum().sort_index()
fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
monthly_sales.plot(kind='line', color="indigo", ax=ax)

ax.set_title('Total Sales by Month', fontsize=10)
ax.set_xlabel('Month', fontsize=8)
ax.set_ylabel('Total Sales', fontsize=8)
ax.tick_params(axis='x', labelsize=6)
ax.tick_params(axis='y', labelsize=6)
ax.yaxis.get_offset_text().set_fontsize(8)
ax.set_xticks(range(1,13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.tight_layout()

# Pie chart
sales_by_zones = filtered_df.groupby('zone')['sales_amount'].sum().sort_values(ascending=False)
figpie, ax = plt.subplots(figsize=figsize,constrained_layout=True)
palette = ["#1f77b4","#ff7f0e","#877676ff"]
ax.pie(
    sales_by_zones, 
    labels=sales_by_zones.index, 
    colors = palette, 
    autopct='%1.1f%%', 
    startangle=0,
    textprops={'fontsize': 8}, radius=0.5)
ax.set_title('Total Revenue by Zone', fontsize=12)
ax.axis('equal')



col1, col2 = st.columns(2)  
# Left column: display plot
with col1:
    st.markdown(
        f"""
        <div style= 'background-color: orange;'>
            <div style='text-align: center;'>
                <span style='font-size:18px;'>
                    Total Revenue: <b>{total_revenue:,.0f}</b><br>
                    Total Sales Quantity: <b>{total_qty:,}</b>
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)
    st.pyplot(fig)
# Right column: display totals
with col2:
     st.markdown("<div style='height:75px;'></div>", unsafe_allow_html=True)
     st.pyplot(figpie)

#------------------------------------------
#Plot Total revenue and sales quantity
#------------------------------------------
# Data prep
sales_by_city = filtered_df.groupby('markets_name')['sales_amount'].sum().sort_values(ascending=False)
qty_by_city = filtered_df.groupby('markets_name')['sales_qty'].sum().sort_values(ascending=False)

# Sort for horizontal bar chart (largest at top)
sales_by_city_sorted = sales_by_city.sort_values(ascending=True)
qty_by_city_sorted = qty_by_city.sort_values(ascending=True)

# Create two columns in Streamlit
col1, col2 = st.columns(2)
# -------------------------------
# Plot 1: Total Sales by City
# -------------------------------
with col1:
    fig1, ax1 = plt.subplots(figsize=figsize, constrained_layout=True)
    sales_by_city_sorted.plot(kind='barh', color= 'darkorange', ax=ax1)

    ax1.set_title('Revenue by Markets', fontsize=10)
    ax1.set_xlabel('Revenue', fontsize=8)
    ax1.set_ylabel('City', fontsize=8)
    ax1.tick_params(axis='x', labelsize=6)
    ax1.tick_params(axis='y', labelsize=6)
    ax1.xaxis.get_offset_text().set_fontsize(8)
    plt.tight_layout()
    st.pyplot(fig1)

# -------------------------------
# Plot 2: Total Sales Quantity by City
# -------------------------------
with col2:
    fig2, ax2 = plt.subplots(figsize=figsize, constrained_layout=True)
    qty_by_city_sorted.plot(kind='barh', color= 'darkorange', ax=ax2)

    ax2.set_title('Sales Quantity by Markets', fontsize=10)
    ax2.set_xlabel('Quantity', fontsize=8)
    ax2.set_ylabel('City', fontsize=8)
    ax2.tick_params(axis='x', labelsize=6)
    ax2.tick_params(axis='y', labelsize=6)
    ax2.xaxis.get_offset_text().set_fontsize(8)
    plt.tight_layout()
    st.pyplot(fig2)

#------------------------------------------
# Show Top customers and products
#------------------------------------------
sales_by_customer = filtered_df.groupby('custmer_name')['sales_amount'].sum().sort_values(ascending=False)
top_customers = sales_by_customer.head().sort_values(ascending=True)
sales_by_products = filtered_df.groupby('product_code')['sales_amount'].sum().sort_values(ascending=False)
top_products = sales_by_products.head().sort_values(ascending=True)

# Create two columns in Streamlit
col1, col2 = st.columns(2)
# -------------------------------
# Plot 1: Total Sales by City
# -------------------------------

with col1:
    fig1, ax1 = plt.subplots(figsize=figsize, constrained_layout=True)
    top_customers.plot(kind='barh', color= 'cornflowerblue', ax=ax1)

    ax1.set_title('Tpo 5 customers by revenue', fontsize=10)
    ax1.set_xlabel('Revenue', fontsize=8)
    ax1.set_ylabel('Customer', fontsize=8)
    ax1.tick_params(axis='x', labelsize=6)
    ax1.tick_params(axis='y', labelsize=6,labelrotation=50)
    ax1.xaxis.get_offset_text().set_fontsize(8)
    plt.tight_layout()
    st.pyplot(fig1)

# -------------------------------
# Plot 2: Total Sales Quantity by City
# -------------------------------
with col2:
    fig2, ax2 = plt.subplots(figsize=figsize, constrained_layout=True)
    top_products.plot(kind='barh', color= 'cornflowerblue', ax=ax2)

    ax2.set_title('Tpo 5 products by revenue', fontsize=10)
    ax2.set_xlabel('Revenue', fontsize=8)
    ax2.set_ylabel('Product', fontsize=8)
    ax2.tick_params(axis='x', labelsize=6)
    ax2.tick_params(axis='y', labelsize=6)
    ax2.xaxis.get_offset_text().set_fontsize(8)
    plt.tight_layout()
    st.pyplot(fig2)

