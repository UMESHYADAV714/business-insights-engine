from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

@app.route("/")
def home():

    # REGION ANALYSIS
    region_query = """
    SELECT "Region",
           SUM("Sales") AS total_sales,
           SUM("Profit") AS total_profit
    FROM global_superstore
    GROUP BY "Region"
    ORDER BY total_sales DESC;
    """

    # CATEGORY ANALYSIS
    category_query = """
    SELECT "Category",
           SUM("Profit") AS total_profit
    FROM global_superstore
    GROUP BY "Category"
    ORDER BY total_profit DESC;
    """

    # KPI QUERIES
    total_sales_query = """
    SELECT SUM("Sales") AS total_sales
    FROM global_superstore;
    """

    total_profit_query = """
    SELECT SUM("Profit") AS total_profit
    FROM global_superstore;
    """

    total_orders_query = """
    SELECT COUNT(DISTINCT "Order ID") AS total_orders
    FROM global_superstore;
    """

    total_customers_query = """
    SELECT COUNT(DISTINCT "Customer ID") AS total_customers
    FROM global_superstore;
    """

    total_quantity_query = """
    SELECT SUM("Quantity") AS total_quantity
    FROM global_superstore;
    """

    # PROFIT BY CATEGORY
    profit_category_query = """
    SELECT "Category",
           SUM("Profit") AS total_profit
    FROM global_superstore
    GROUP BY "Category"
    ORDER BY total_profit DESC;
    """

    # MONTHLY SALES
    monthly_sales_query = """
    SELECT "Month",
           SUM("Sales") AS total_sales
    FROM global_superstore
    GROUP BY "Month";
    """

    # TOP CUSTOMERS
    top_customers_query = """
    SELECT "Customer Name",
           SUM("Sales") AS total_sales
    FROM global_superstore
    GROUP BY "Customer Name"
    ORDER BY total_sales DESC
    LIMIT 10;
    """

    # TOP PRODUCTS
    top_products_query = """
    SELECT "Product Name",
           SUM("Sales") AS total_sales
    FROM global_superstore
    GROUP BY "Product Name"
    ORDER BY total_sales DESC
    LIMIT 10;
    """

    # DATAFRAMES
    region_df = pd.read_sql(region_query, engine)
    category_df = pd.read_sql(category_query, engine)

    sales_kpi = pd.read_sql(total_sales_query, engine)
    profit_kpi = pd.read_sql(total_profit_query, engine)
    orders_kpi = pd.read_sql(total_orders_query, engine)
    customers_kpi = pd.read_sql(total_customers_query, engine)
    quantity_kpi = pd.read_sql(total_quantity_query, engine)

    profit_df = pd.read_sql(profit_category_query, engine)
    monthly_df = pd.read_sql(monthly_sales_query, engine)

    top_customers = pd.read_sql(top_customers_query, engine)
    top_products = pd.read_sql(top_products_query, engine)

    # TOP VALUES
    top_region = region_df.iloc[0]
    top_category = category_df.iloc[0]

    # CHART DATA
    regions = region_df["Region"].tolist()
    sales = region_df["total_sales"].tolist()

    categories = profit_df["Category"].tolist()
    category_profits = profit_df["total_profit"].tolist()

    months = monthly_df["Month"].tolist()
    monthly_sales = monthly_df["total_sales"].tolist()

    return render_template(
        "index.html",

        region=top_region["Region"],
        category=top_category["Category"],

        sales_total=round(float(sales_kpi.iloc[0]["total_sales"]), 2),
        total_profit=round(float(profit_kpi.iloc[0]["total_profit"]), 2),

        total_orders=int(orders_kpi.iloc[0]["total_orders"]),
        total_customers=int(customers_kpi.iloc[0]["total_customers"]),
        total_quantity=int(quantity_kpi.iloc[0]["total_quantity"]),

        regions=regions,
        sales=sales,

        categories=categories,
        category_profits=category_profits,

        months=months,
        monthly_sales=monthly_sales,

        top_customers=top_customers.to_dict(orient="records"),
        top_products=top_products.to_dict(orient="records")
    )

if __name__ == "__main__":
    app.run(debug=True)