from services.analytics import AnalyticsEngine
from visuals.charts import ChartGenerator

class ReportGenerator:

    def __init__(self):
        self.analytics = AnalyticsEngine()
        self.charts = ChartGenerator()

    def generate_report(self):
        # Load data
        df = self.analytics.load_data()

        # Generate stats
        stats = self.analytics.salary_stats(df)
        dept_analysis = self.analytics.department_analysis(df)
        sorted_data = self.analytics.sort_by_salary(df)

        # Generate charts
        self.charts.bar_chart(df)
        self.charts.histogram(df)
        self.charts.pie_chart(df)
        self.charts.scatter_plot(df)

        # Print report (console)
        print("\n===== WORKFORCE ANALYTICS REPORT =====")

        print("\n--- Salary Statistics ---")
        print(f"Mean Salary: {stats['mean']}")
        print(f"Median Salary: {stats['median']}")
        print(f"Std Deviation: {stats['std_dev']}")

        print("\n--- Department-wise Average Salary ---")
        print(dept_analysis)

        print("\n--- Top Employees (Sorted by Salary) ---")
        print(sorted_data.head(5))

        print("\nCharts saved in 'static/' folder")