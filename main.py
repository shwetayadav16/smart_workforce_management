from models.employee import Employee
import pandas as pd
from services.db_manager import DatabaseManager
from services.analytics import AnalyticsEngine
from visuals.charts import ChartGenerator
from services.reports import ReportGenerator


# Step 1: Create DB manager
db = DatabaseManager()

# Step 2: Create table
db.create_table()
db.clear_table()

# Step 2: Load CSV
df = pd.read_csv("employees.csv")

# Step 3: Insert into DB
for _, row in df.iterrows():
    emp = Employee(
        row['id'],
        row['name'],
        row['age'],
        row['department'],
        row['salary']
    )
    db.insert_employee(emp)

# Step 5: Fetch and print
employees = db.fetch_all()

for emp in employees:
    print(emp)

# Initialize analytics
analytics = AnalyticsEngine()

# Load data
df = analytics.load_data()

# Salary stats
stats = analytics.salary_stats(df)
print("Salary Stats:", stats)

# Department analysis
dept = analytics.department_analysis(df)
print("\nAvg Salary by Department:\n", dept)

# High salary employees
high = analytics.high_salary(df)
print("\nHigh Salary Employees:\n", high)

# Sorted data
sorted_df = analytics.sort_by_salary(df)
print("\nSorted by Salary:\n", sorted_df)

charts = ChartGenerator()

charts.bar_chart(df)
charts.histogram(df)
charts.pie_chart(df)
charts.scatter_plot(df)

print("\nCharts generated successfully!")

report = ReportGenerator()
report.generate_report()