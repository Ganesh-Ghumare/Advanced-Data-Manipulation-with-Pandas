import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("customer_churn.csv")
sales = pd.read_csv("sales_data (1).csv")



# Convert Date
sales["Date"] = pd.to_datetime(sales["Date"])

# Extract numeric part from CUST001 → 001
sales["CustomerID"] = sales["Customer_ID"].str.extract(r"(\d+)")

# Convert to integer then format as C00001
sales["CustomerID"] = sales["CustomerID"].astype(int)
sales["CustomerID"] = sales["CustomerID"].apply(lambda x: f"C{x:05d}")



merged_data = pd.merge(
    sales,
    customers,
    on="CustomerID",
    how="inner"
)

print("Merged rows:", len(merged_data))  # MUST be > 0

total_revenue = merged_data["Total_Sales"].sum()
total_customers = merged_data["CustomerID"].nunique()
average_order_value = merged_data["Total_Sales"].mean()

customer_revenue = (
    merged_data.groupby("CustomerID")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

region_revenue = merged_data.groupby("Region")["Total_Sales"].sum()



top_customers = customer_revenue.head(5)


merged_data["Month"] = merged_data["Date"].dt.month

monthly_pivot = pd.pivot_table(
    merged_data,
    values="Total_Sales",
    index="Month",
    columns="Region",
    aggfunc="sum"
)

if not top_customers.empty:
    plt.figure()
    top_customers.plot(kind="bar")
    plt.title("Top 5 Customers by Revenue")
    plt.xlabel("Customer ID")
    plt.ylabel("Revenue")
    plt.show()

plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

plt.figure()
monthly_pivot.plot()
plt.title("Monthly Sales Trend by Region")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

print("\nCUSTOMER SALES ANALYSIS REPORT")
print("--------------------------------")
print(f"Total Revenue: ${total_revenue:,.0f}")
print(f"Total Customers: {total_customers}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print("Top 5 Customers:")
print(top_customers)
