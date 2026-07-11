import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/product_info.csv", encoding="utf-8-sig")

# Keep only skincare products
skincare_df = df[df["primary_category"] == "Skincare"]

# Create an empty list to store every ingredient
all_ingredients = []

# Go through each product's ingredient list
for ingredients in skincare_df["ingredients"]:

    # Skip products that don't have ingredients listed
    if pd.isna(ingredients):
        continue

    # Remove extra characters
    ingredients = ingredients.replace("[", "")
    ingredients = ingredients.replace("]", "")
    ingredients = ingredients.replace("'", "")

    # Split one long string into a list of ingredients
    ingredient_list = ingredients.split(", ")

    # Add those ingredients to our master list
    all_ingredients.extend(ingredient_list)

# Show the first 20 ingredients we collected
from collections import Counter

# Count how many times each ingredient appears
ingredient_counts = Counter(all_ingredients)

# Show the 20 most common ingredients
from collections import Counter

# Count how many times each ingredient appears
ingredient_counts = Counter(all_ingredients)

# Show the 20 most common ingredients
print(ingredient_counts.most_common(20))