import sqlite3
import pandas as pd
# Load the skincare dataset
df = pd.read_csv("data/raw/product_info.csv", encoding="utf-8-sig")

# Create or connect to the Skinlytics database
conn = sqlite3.connect("database/skinlytics.db")
# Save the dataset as a table inside the database
df.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

# Close the database connection
conn.close()

print("Skinlytics database created successfully.")