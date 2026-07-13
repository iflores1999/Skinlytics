import pandas as pd


def load_skincare_data():
    """
    Load the Sephora product dataset and keep only skincare products.
    """

    file_path = "data/raw/product_info.csv"

    # Read the original CSV dataset
    df = pd.read_csv(file_path, encoding="utf-8-sig")

    # Keep only products in the Skincare category
    skincare_df = df[
        df["primary_category"] == "Skincare"
    ].copy()

    return skincare_df
