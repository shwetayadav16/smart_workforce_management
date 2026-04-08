import pandas as pd
import numpy as np
import sqlite3

class AnalyticsEngine:
    def __init__(self):
        self.conn = sqlite3.connect("database/workforce.db")

    def load_data(self):
        query = "SELECT * FROM employees"
        df = pd.read_sql(query, self.conn)
        return df
    def salary_stats(self, df):
        salaries = df['salary']

        return {
            "mean": np.mean(salaries),
            "median": np.median(salaries),
            "std_dev": np.std(salaries)
        }
    def department_analysis(self, df):
        return df.groupby('department')['salary'].mean()
    def high_salary(self, df):
        return df[df['salary'] > 60000]

    def sort_by_salary(self, df):
        return df.sort_values(by='salary', ascending=False)
    def highest_salary_by_department(self, df):
        # Get index of max salary in each department
        idx = df.groupby('department')['salary'].idxmax()
    
        # Return those rows
        return df.loc[idx][['department', 'name', 'salary']]