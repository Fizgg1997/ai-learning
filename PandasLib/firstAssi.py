import pandas as pd


data = {
    "Name": ["Ali", "Sara", "John", "Faizan", "Umair"],
    "Marks": [80, 95, 70,80,90],
    "City": ["Riyadh", "Jeddah", "Dammam", "Gujrat", "karachi"]
}

df = pd.DataFrame(data)
# print(df)

# Print First Row of data

print(df.head())
print(df["Name"])
print(df["Marks"])
print(df["City"])

# Average Marks
print(df["Marks"].mean())
# Highest Marks
print(df["Marks"].max())
# Lowest Marks
print(df["Marks"].min())
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]


print(df)


# Write data into csv

df.to_csv("save.csv", index=False)