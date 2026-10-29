import pandas as pd


df = pd.read_csv("sales_data.csv")

df["TotalSales"] = df["Quantity"] * df["Price"]

print("SALES DATA")
print(df)

total_sales = df["TotalSales"].sum()
print("\n1. TOTAL SALES:", total_sales)

average_order_value = df["TotalSales"].mean()
print("2. AVERAGE ORDER VALUE:", round(average_order_value, 2))

top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)
print("\n3. TOP-SELLING PRODUCTS")
print(top_products)

category_sales = df.groupby("Category")["TotalSales"].sum()
print("\n4. SALES BY CATEGORY")
print(category_sales)

region_sales = df.groupby("Region")["TotalSales"].sum()
print("\n5. SALES BY REGION")
print(region_sales)


df.to_csv("sales_analysis_results.csv", index=False)

print("\nSales analysis completed!")
