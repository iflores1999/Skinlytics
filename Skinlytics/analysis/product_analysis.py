import pandas as pd

df = pd.read_csv("data/raw/product_info.csv", encoding="utf-8-sig")

skincare_df = df[df["primary_category"] == "Skincare"]

top_reviewed = skincare_df.sort_values(
    by="reviews",
    ascending=False
)

print(
    top_reviewed[
        ["product_name", "brand_name", "reviews", "rating"]
    ].head(10)
)