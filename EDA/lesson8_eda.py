import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["Ali", "Sara", "John", "Faizan", "Ahmed"],
    "Age": [22, 24, 21, 30, 28],
    "Marks": [80, 95, 70, 88, 60],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)
# Data Information
print(df.info())

# Data Description

print(df.describe())

# Print Unique Values

print(df["Department"].unique())

# Print Count Value

print(df["Age"].value_counts())

# Groupby Data 

print(df.groupby("Department")["Marks"].mean())

print(df.groupby("Age")["Department"])

print(df.corr(numeric_only=True))


plt.bar(df["Name"], df["Marks"])
plt.title("Marks Distribution")
plt.show()