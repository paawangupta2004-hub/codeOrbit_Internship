import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Original Data:")
print(df)

df = df.drop_duplicates()

df["Quantity"] = df["Quantity"].fillna(0)
df["Region"] = df["Region"].fillna("Unknown")

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nData cleaning completed!")
