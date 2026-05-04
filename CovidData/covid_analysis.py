import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("owid-covid-data.csv")

df = df[[
    "location",
    "date",
    "total_cases",
    "new_cases",
    "total_deaths",
    "population"
]]


df["date"] = pd.to_datetime(df["date"])


df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)

df["death_rate"] = df["total_deaths"] / df["total_cases"] * 100

df["cases_per_million"] = df["total_cases"] / df["population"] * 1_000_000
df.replace([float('inf')], 0, inplace=True)


# top_cases = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)

# top_cases.plot(kind="bar")
# plt.title("Top 10 Countries by Total Cases")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig("output/charts/bar_top_cases.png")
# plt.clf()



top_cases = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)

# top_cases.plot(kind="bar")
# plt.title("Top 10 Countries by Total Cases")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig("output/charts/bar_top_cases.png")
# plt.clf()



# df["new_cases"].hist(bins=50)
# plt.title("Distribution of Daily Cases")
# plt.savefig("output/charts/histogram.png")
# plt.clf()

sample = df.sample(10000)

# plt.scatter(sample["total_cases"], sample["total_deaths"])
# plt.xlabel("Total Cases")
# plt.ylabel("Total Deaths")
# plt.title("Cases vs Deaths")
# plt.savefig("output/charts/scatter.png")
# plt.clf()


top5 = top_cases.head(5)

top5.plot(kind="pie", autopct="%1.1f%%")
# plt.title("Top 5 Countries Share")
# plt.ylabel("")
# plt.savefig("output/charts/pie.png")
# plt.clf()


df.boxplot(column="new_cases")
# plt.title("Outliers in Daily Cases")
# plt.savefig("output/charts/boxplot.png")
# plt.clf()

corr = df[["total_cases", "new_cases", "total_deaths"]].corr()

plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Matrix")
plt.savefig("output/charts/correlation.png")
plt.clf()