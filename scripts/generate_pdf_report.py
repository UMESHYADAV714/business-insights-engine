import pandas as pd
from sqlalchemy import create_engine
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# PDF Setup
pdf_file = "reports/Business_Insights_Report.pdf"
doc = SimpleDocTemplate(pdf_file)
styles = getSampleStyleSheet()
elements = []

# ==========================
# KPI QUERY
# ==========================

kpi_query = """
SELECT
    ROUND(SUM("Sales")::numeric,2) AS total_sales,
    ROUND(SUM("Profit")::numeric,2) AS total_profit,
    COUNT(*) AS total_orders
FROM global_superstore;
"""

kpi_df = pd.read_sql(kpi_query, engine)

total_sales = float(kpi_df["total_sales"][0])
total_profit = float(kpi_df["total_profit"][0])
total_orders = int(kpi_df["total_orders"][0])

profit_margin = round((total_profit / total_sales) * 100, 2)

# ==========================
# TOP PRODUCTS
# ==========================

products_query = """
SELECT
    "Product Name",
    ROUND(SUM("Sales")::numeric,2) AS sales
FROM global_superstore
GROUP BY "Product Name"
ORDER BY sales DESC
LIMIT 5;
"""

products_df = pd.read_sql(products_query, engine)

# ==========================
# TOP CUSTOMERS
# ==========================

customers_query = """
SELECT
    "Customer Name",
    ROUND(SUM("Sales")::numeric,2) AS sales
FROM global_superstore
GROUP BY "Customer Name"
ORDER BY sales DESC
LIMIT 5;
"""

customers_df = pd.read_sql(customers_query, engine)

# ==========================
# TITLE PAGE
# ==========================

elements.append(
    Paragraph("Business Insights Report", styles["Title"])
)

elements.append(
    Paragraph(
        f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
        styles["Normal"]
    )
)

elements.append(Spacer(1, 20))

elements.append(
    Paragraph("Executive Summary", styles["Heading1"])
)

elements.append(
    Paragraph(
        """
        This report contains automated business insights generated
        from the Global Superstore dataset.
        """,
        styles["BodyText"]
    )
)

elements.append(Spacer(1, 20))

# ==========================
# KPI SUMMARY
# ==========================

elements.append(
    Paragraph("Business KPI Summary", styles["Heading1"])
)

elements.append(
    Paragraph(
        f"""
        Total Sales: ${total_sales:,.2f}<br/>
        Total Profit: ${total_profit:,.2f}<br/>
        Total Orders: {total_orders:,}<br/>
        Profit Margin: {profit_margin}%
        """,
        styles["BodyText"]
    )
)

# ==========================
# SALES CHART
# ==========================

elements.append(PageBreak())

elements.append(
    Paragraph("Sales by Category", styles["Heading1"])
)

elements.append(
    Image(
        "charts/sales_by_category.png",
        width=450,
        height=300
    )
)

# ==========================
# PROFIT CHART
# ==========================

elements.append(PageBreak())

elements.append(
    Paragraph("Profit by Category", styles["Heading1"])
)

elements.append(
    Image(
        "charts/profit_by_category.png",
        width=450,
        height=300
    )
)

# ==========================
# MONTHLY TREND
# ==========================

elements.append(PageBreak())

elements.append(
    Paragraph("Monthly Sales Trend", styles["Heading1"])
)

elements.append(
    Image(
        "charts/monthly_sales_trend.png",
        width=450,
        height=300
    )
)

# ==========================
# AI INSIGHTS
# ==========================

elements.append(PageBreak())

elements.append(
    Paragraph("AI Insights", styles["Heading1"])
)

elements.append(
    Paragraph(
        """
        • Technology generates the highest revenue.<br/>
        • Technology generates the highest profit.<br/>
        • Furniture shows lower profitability.<br/>
        • Monthly sales trend indicates healthy business performance.<br/>
        • Focus on high-margin categories to improve profitability.
        """,
        styles["BodyText"]
    )
)

# ==========================
# TOP PRODUCTS
# ==========================

elements.append(PageBreak())

elements.append(
    Paragraph("Top 5 Products", styles["Heading1"])
)

product_data = [["Product Name", "Sales"]]

for _, row in products_df.iterrows():
    product_data.append([
        row["Product Name"],
        f"${row['sales']:,.2f}"
    ])

product_table = Table(product_data)

product_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(product_table)

# ==========================
# TOP CUSTOMERS
# ==========================

elements.append(PageBreak())

elements.append(
    Paragraph("Top 5 Customers", styles["Heading1"])
)

customer_data = [["Customer Name", "Sales"]]

for _, row in customers_df.iterrows():
    customer_data.append([
        row["Customer Name"],
        f"${row['sales']:,.2f}"
    ])

customer_table = Table(customer_data)

customer_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(customer_table)

# ==========================
# BUILD PDF
# ==========================

doc.build(elements)

print("Business Insights PDF Report Generated Successfully!")