import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("1776311302-Car Market Trends Analysis with Car Dekho Data.csv")

# Basic inspection
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Correlation with selling price
print(df[["Year","Selling_Price","Present_Price","Kms_Driven","Owner"]].corr()["Selling_Price"].sort_values(ascending=False))

# Grouped analysis
print(df.groupby("Fuel_Type")["Selling_Price"].mean())
print(df.groupby("Transmission")["Selling_Price"].mean())
print(df.groupby("Seller_Type")["Selling_Price"].mean())

# Visualizations
plt.scatter(df["Present_Price"], df["Selling_Price"])
plt.xlabel("Present Price"); plt.ylabel("Selling Price")
plt.title("Present Price vs Selling Price")
plt.show()

df.groupby("Fuel_Type")["Selling_Price"].mean().plot(kind="bar")
plt.title("Average Selling Price by Fuel Type")
plt.show()

df.groupby("Transmission")["Selling_Price"].mean().plot(kind="bar")
plt.title("Average Selling Price by Transmission")
plt.show()

df.groupby("Seller_Type")["Selling_Price"].mean().plot(kind="bar")
plt.title("Average Selling Price by Seller Type")
plt.show()

df.groupby("Year")["Selling_Price"].mean().plot(marker="o")
plt.title("Average Selling Price by Manufacturing Year")
plt.show()
