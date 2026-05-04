import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("netflix_titles.csv")

print(df.head())

print(df.info())

print(df.describe(include="all"))

print(df.isnull().sum())


df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries by Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

df["rating"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


df["year_added"].value_counts().sort_index().plot(kind="line", marker="o")
plt.title("Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


df["release_year"].value_counts().head(10).sort_index().plot(kind="bar")
plt.title("Top 10 Release Years")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.tight_layout()
plt.show()