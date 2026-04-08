import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

class ChartGenerator:

    def __init__(self):
        os.makedirs("static", exist_ok=True)

    def bar_chart(self, df):
        plt.figure()

        dept = df.groupby('department')['salary'].mean()
        dept.plot(kind='bar')

        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Salary")

        plt.savefig("static/bar_chart.png")
        plt.close()

    def histogram(self, df):
        plt.figure()

        df['salary'].plot(kind='hist')

        plt.title("Salary Distribution")
        plt.xlabel("Salary")

        plt.savefig("static/histogram.png")
        plt.close()

    def pie_chart(self, df):
        plt.figure()

        dept_count = df['department'].value_counts()
        dept_count.plot(kind='pie', autopct='%1.1f%%')

        plt.title("Employee Distribution by Department")

        plt.savefig("static/pie_chart.png")
        plt.close()

    def scatter_plot(self, df):
        plt.figure()

        plt.scatter(df['age'], df['salary'])

        plt.title("Age vs Salary")
        plt.xlabel("Age")
        plt.ylabel("Salary")

        plt.savefig("static/scatter_plot.png")
        plt.close()