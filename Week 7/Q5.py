import pandas as pd


employee_df = pd.read_csv("Week 7\employees.csv")
department_df = pd.read_csv("Week 7\department.csv")


merged_df = pd.merge(employee_df, department_df, on='DID')


avg_salary_per_dept = merged_df.groupby('DName')['Salary'].mean()

print("Average salary for each department:")
print(avg_salary_per_dept)
