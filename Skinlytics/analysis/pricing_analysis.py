import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/product_info.csv", encoding="utf-8-sig")

# Keep only skincare products
skincare_df = df[df["primary_category"] == "Skincare"]

# Create price ranges
price_ranges = [0, 25, 50, 100, 1000]
labels = ["Under $25", "$25-$50", "$50-$100", "Over $100"]

# Create a new column called Price Range
skincare_df["price_range"] = pd.cut(
    skincare_df["price_usd"],
    bins=price_ranges,
    labels=labels
)

# Calculate the average rating for each price range
price_summary = skincare_df.groupby("price_range").agg({
    "rating": "mean",
    "product_id": "count"
})

print(price_summary)