import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. E-COMMERCE DATA
# --------------------------------

data = {
    "Product": [
        "Laptop", "Mobile", "Headphones", "Shoes",
        "Laptop", "Mobile", "T-Shirt", "Shoes",
        "Headphones", "Mobile"
    ],

    "Category": [
        "Electronics", "Electronics", "Electronics", "Fashion",
        "Electronics", "Electronics", "Fashion", "Fashion",
        "Electronics", "Electronics"
    ],

    "Quantity": [2, 3, 5, 4, 1, 2, 6, 3, 4, 2],

    "Price": [
        50000, 20000, 2000, 3000,
        50000, 20000, 800, 3000,
        2000, 20000
    ],

    "Region": [
        "South", "North", "West", "East",
        "South", "North", "South", "West",
        "East", "South"
    ]
}

df = pd.DataFrame(data)

# --------------------------------
# 2. CALCULATE SALES
# --------------------------------

df["Sales"] = df["Quantity"] * df["Price"]

print("\n===== E-COMMERCE SALES DATA =====")
print(df)

# --------------------------------
# 3. BASIC ANALYTICS
# --------------------------------

total_sales = df["Sales"].sum()
total_quantity = df["Quantity"].sum()
total_products = df["Product"].nunique()

print("\n===== KEY INFORMATION =====")
print("Total Sales     : ₹", total_sales)
print("Products Sold   :", total_quantity)
print("Total Products  :", total_products)

# --------------------------------
# 4. PRODUCT ANALYSIS
# --------------------------------

product_sales = df.groupby("Product")["Sales"].sum()
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\n===== SALES BY PRODUCT =====")
print(product_sales)

best_product = product_sales.idxmax()

print("\nBest Selling Product:", best_product)

# --------------------------------
# 5. CATEGORY ANALYSIS
# --------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

print("\n===== SALES BY CATEGORY =====")
print(category_sales)

best_category = category_sales.idxmax()

print("Best Category:", best_category)

# --------------------------------
# 6. REGION ANALYSIS
# --------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\n===== SALES BY REGION =====")
print(region_sales)

best_region = region_sales.idxmax()

print("Best Region:", best_region)

# --------------------------------
# 7. DASHBOARD GRAPHS
# --------------------------------

plt.figure(figsize=(12, 8))

# Product Sales
plt.subplot(2, 2, 1)
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)

# Category Sales
plt.subplot(2, 2, 2)
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (₹)")

# Region Sales
plt.subplot(2, 2, 3)
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales (₹)")

# Quantity Sold
plt.subplot(2, 2, 4)
product_quantity.plot(kind="bar")
plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# --------------------------------
# 8. FINAL SUMMARY
# --------------------------------

print("\n================================")
print("     E-COMMERCE ANALYTICS")
print("================================")

print("Total Sales        : ₹", total_sales)
print("Total Products     :", total_products)
print("Total Quantity     :", total_quantity)
print("Best Product       :", best_product)
print("Best Category      :", best_category)
print("Best Region        :", best_region)

print("================================")