import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/product_info.csv", encoding="utf-8-sig")
# Keep only skincare products
skincare_df = df[df["primary_category"] == "Skincare"]

# Calculate the average rating and number of products for each brand
brand_summary = skincare_df.groupby("brand_name").agg({
    "rating": "mean",
    "product_id": "count"
})

# Keep only brands with at least 10 products
brand_summary = brand_summary[brand_summary["product_id"] >= 10]

# Sort by highest average rating
brand_summary = brand_summary.sort_values(
    by="rating",
    ascending=False
)

# Display the top 10 brands
print(brand_summary.head(10))
