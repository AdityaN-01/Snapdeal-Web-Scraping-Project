import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("snapdeal_shoes.csv")

print("Before Cleaning:", df.shape)

# Convert Price
df["Price"] = df["Price"].astype(str)
df["Price"] = df["Price"].str.replace(",", "")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Remove only rows where price missing
df.dropna(subset=["Price"], inplace=True)

print("After Cleaning:", df.shape)
print(df.head())

# -------------------------
# Top Brands
# -------------------------
brand_counts = df["Product Name"].str.split().str[0].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=brand_counts.index, y=brand_counts.values)
plt.title("Top Brands")
plt.xticks(rotation=45)
plt.savefig("graphs/top_brands.png")   # SAVE IMAGE
plt.show()

# -------------------------
# Price Distribution
# -------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=20)
plt.title("Price Distribution")
plt.savefig("graphs/price_distribution.png")
plt.show()

