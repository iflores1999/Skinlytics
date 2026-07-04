import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/product_info.csv", encoding="utf-8-sig")

# Keep only skincare products
skincare_df = df[df["primary_category"] == "Skincare"]

# Show the first 5 ingredient lists
# Get the first ingredient list
ingredients = skincare_df["ingredients"].iloc[0]

# Remove the extra characters
ingredients = ingredients.replace("[", "")
ingredients = ingredients.replace("]", "")
ingredients = ingredients.replace("'", "")

# Show the cleaned result
ingredient_list = ingredients.split(", ")

print(ingredient_list)