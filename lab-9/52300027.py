import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the iris.csv file
df = pd.read_csv('iris.csv')

# Step 2: Plot a simple scatter of 'sepal_length' vs 'sepal_width'
plt.figure(figsize=(6, 4))
plt.scatter(df['sepal_length'], df['sepal_width'], color='blue', label='Data points')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width')
plt.legend()
plt.grid(True)
plt.show()

# Step 3: Plot a histogram of 'sepal_length' with bin=20
plt.figure(figsize=(6, 4))
plt.hist(df['sepal_length'], bins=20, color='green', edgecolor='black')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.grid(True)
plt.show()


# Read the company_sales_data.csv file
df = pd.read_csv('company-sales_data.csv')

# a. Total profit of all months using a line plot
plt.figure(figsize=(10, 6))
plt.plot(df['month_number'], df['total_profit'], marker='o', color='b', label='Total Profit')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Total Profit Over Months')
plt.xticks(df['month_number'])  # Show all months
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# b. Toothpaste sales data using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['month_number'], df['toothpaste'], color='r', label='Toothpaste Sales')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales Over Months')
plt.xticks(df['month_number'])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# c. Facecream and Facewash product sales using a bar chart
plt.figure(figsize=(10, 6))
width = 0.35  # Bar width
x = df['month_number']

plt.bar(x - width/2, df['facecream'], width, label='Facecream Sales', color='g')
plt.bar(x + width/2, df['facewash'], width, label='Facewash Sales', color='y')

plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.title('Facecream and Facewash Sales Over Months')
plt.xticks(df['month_number'])
plt.legend()
plt.tight_layout()
plt.show()