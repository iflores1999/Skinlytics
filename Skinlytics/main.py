# Skinlytics
# Created by Isela Flores

import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/product_info.csv", encoding="utf-8-sig")

# Keep only skincare products
skincare_df = df[df["primary_category"] == "Skincare"]

# Average rating and number of products by brand
brand_summary = skincare_df.groupby("brand_name").agg({
    "rating": "mean",
    "product_id": "count"
})

# Keep only brands with at least 10 products
brand_summary = brand_summary[brand_summary["product_id"] >= 10]

# Sort from highest to lowest rating
brand_summary = brand_summary.sort_values(
    by="rating",
    ascending=False
)

# Show the top 10
print(brand_summary.head(10))

# -----------------------------
# Products with the most reviews
# -----------------------------
top_reviewed = skincare_df.sort_values(
    by="reviews",
    ascending=False
)
print(
    top_reviewed[
        ["product_name", "brand_name", "reviews", "rating"]
    ].head(10)
)