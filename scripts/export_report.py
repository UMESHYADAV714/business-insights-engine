from datetime import datetime

report = f"""
=========================================
 BUSINESS INSIGHTS ENGINE REPORT
=========================================

Generated On: {datetime.now()}

Key Insights:
-----------------------------------------

1. Sales performance analyzed successfully.

2. Regional sales trends identified.

3. Top customers and products evaluated.

4. Monthly and yearly sales trends calculated.

5. Profitability metrics generated.

6. Forecasting completed.

=========================================
END OF REPORT
=========================================
"""

with open("Reports/business_report.txt", "w") as file:
    file.write(report)

print("Report generated successfully!")