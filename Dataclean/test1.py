import pandas as pd

data = {
    "Name": ["Ali", "Sara", "John", None, None],
    "Age": [22, 24, None, 22, 30],
    "Marks": [80, None, 70, 80, 90],
    "City": ["Riyadh", "Jeddah", "Dammam", "Riyadh", None]
}

df = pd.DataFrame(data)

print(df)


print(df.isnull().sum())


# Clean the Null Rows

clean_row = df.dropna()
print(clean_row)
# Fill Missing rows

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Name"] = df["Name"].fillna("Unknown")

# Drop Duplicates

df.drop_duplicates()
print(df)
