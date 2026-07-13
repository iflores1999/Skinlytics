# Skinlytics

## Overview

Skinlytics is a data analytics portfolio project that analyzes skincare product data from Sephora to uncover business insights. The goal is to demonstrate how data can be cleaned, analyzed, and visualized to help retailers better understand product performance, customer preferences, and market trends.

This project showcases practical data analytics skills using Python, SQL, and business analysis techniques.

---

## Business Problem

Beauty retailers sell thousands of skincare products across many brands, making it difficult to identify trends through manual analysis.

Skinlytics helps answer important business questions by organizing and analyzing product data, allowing decision-makers to quickly identify high-performing brands, popular products, pricing trends, and common ingredients.

---

## Dataset

- **Source:** Kaggle
- **Dataset:** Sephora Products and Skincare Data
- **File Used:** `product_info.csv`

The dataset contains information about skincare products including:

- Brand
- Product Name
- Price
- Customer Rating
- Number of Reviews
- Ingredients
- Product Category

---

## Technologies Used

- Python
- Pandas
- SQL
- SQLite
- VS Code
- Git
- GitHub

---

## Project Structure

```
Skinlytics/
│
├── analysis/
│   ├── brand.py
│   ├── ingredient_analysis.py
│   ├── pricing_analysis.py
│   └── product_analysis.py
│
├── data/
│   └── raw/
│       └── product_info.csv
│
├── database/
│   ├── create_database.py
│   └── skinlytics.db
│
├── docs/
│   ├── findings.md
│   └── project_overview.md
│
├── sql/
│   ├── brand_analysis.sql
│   ├── category_analysis.sql
│   └── pricing_analysis.sql
│
├── main.py
└── README.md
```

---

## Business Questions Answered

This project answers the following questions:

- Which skincare brands have the highest average customer ratings?
- Which skincare products have the most customer reviews?
- Does product price influence customer ratings?
- Which ingredients appear most frequently in skincare products?
- Which skincare categories contain the most products?

---

## Key Findings

### Highest Rated Brands

Brands such as MARA, Hourglass, and StriVectin consistently received some of the highest average customer ratings.

### Customer Reviews

Several products accumulated thousands of customer reviews, showing which products have the strongest customer engagement.

### Price vs Rating

Higher-priced skincare products did not always receive higher customer ratings, suggesting that product quality is not determined by price alone.

### Common Ingredients

Ingredients such as Glycerin, Phenoxyethanol, Butylene Glycol, Sodium Hyaluronate, and Squalane appeared frequently across highly rated skincare products.

---

## Skills Demonstrated

- Data Cleaning
- Data Exploration
- Business Analysis
- Python Programming
- SQL Queries
- Data Aggregation
- Data Visualization Preparation
- Git Version Control
- Project Documentation

---

## Future Improvements

Future versions of Skinlytics may include:

- Interactive Power BI dashboard
- Product recommendation analysis
- Sentiment analysis using customer reviews
- Machine learning models for product rating prediction
- Additional skincare datasets for comparison

---

## Author

**Isela Flores**

Bachelor of Science in Computer Science

GitHub: https://github.com/iselaflores
