import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("dirty_data.csv")

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Sales with average sales
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

# Standardize city names
df["City"] = df["City"].str.title()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Generate report
report = f"""
Number of records: {len(df)}
Average Age: {df['Age'].mean():.2f}
Average Sales: {df['Sales'].mean():.2f}
Cities:
{df['City'].value_counts()}
"""

with open("report.txt", "w") as file:
    file.write(report)

print(report)

# Create chart
df.groupby("City")["Sales"].mean().plot(kind="bar")
plt.title("Average Sales by City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
