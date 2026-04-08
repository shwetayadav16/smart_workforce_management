from flask import Flask, render_template
from services.analytics import AnalyticsEngine
from visuals.charts import ChartGenerator
import os

app = Flask(__name__)

@app.route('/')
def home():
    analytics = AnalyticsEngine()
    df = analytics.load_data()

    # Generate charts
    charts = ChartGenerator()

    # Save charts into static folder
    charts.bar_chart(df)
    charts.histogram(df)
    charts.pie_chart(df)
    charts.scatter_plot(df)
    top_emp = analytics.highest_salary_by_department(df)

    stats = analytics.salary_stats(df)

    return render_template("index.html", stats=stats,top_emp=top_emp)

if __name__ == "__main__":
    app.run(debug=True)