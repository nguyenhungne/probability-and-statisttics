import pandas as pd

# Load the dataset
df = pd.read_csv('iris.csv')

# Display the first 5 data points
print("First 5 data points:")
print(df.head())

# Compute the descriptive statistics
summary_stats = df.describe().transpose()

# Filter the summary statistics for count, mean, std, min, and max
summary_stats_filtered = summary_stats[['count', 'mean', 'std', 'min', 'max']]

# Display the result
print("\nSummary statistics (count, mean, std, min, max):")
print(summary_stats_filtered)

# Load the dataset
df = pd.read_csv('population.csv')

# Display the first 5 data points
print("First 5 data points:")
print(df.head())

# Compute statistics by 'Year' and 'Country Name'
summary_stats = df.groupby('Country Name').agg(
    count=('Value', 'count'),
    mean=('Value', 'mean'),
    std=('Value', 'std'),
    min=('Value', 'min'),
    max=('Value', 'max')
)

# Display the result
print("\nSummary statistics by country:")
print(summary_stats)
