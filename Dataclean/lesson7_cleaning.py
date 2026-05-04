import pandas as pd

data = {
    "Employee": ["Ahmed", "Sara", "Khalid", "Ahmed", None],
    "Department": ["IT", "HR", None, "IT", "Finance"],
    "Salary": [5000, None, 7000, 5000, 6500],
    "Experience": [2, 4, None, 2, 5]
}


# Print Original Data
df = pd.DataFrame(data)

print(df)
# Print Missing Values

print("\nMissing Values")

print(df.isnull().sum())

# Fill Missing Values

df["Employee"] = df["Employee"].fillna("Unknown")
df["Department"] = df["Department"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

# Drop Duplicates

df = df.drop_duplicates()

# Convert Salary and Experience into Integer

df["Salary"] = df["Salary"].astype(int)
df["Experience"] = df["Experience"].astype(int)

print(df)