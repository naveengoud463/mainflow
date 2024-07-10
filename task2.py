import pandas as pd

# Load the CSV file into a DataFrame
file_path = '/mnt/data/customers-100.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Filter the DataFrame to include only customers from Chile
df_chile = df[df['Country'] == 'Chile']

# Display the filtered DataFrame
print("\nFiltered DataFrame (only customers from Chile):")
print(df_chile)

# Handle missing values by filling them with 'Missing'
df_filled = df.fillna('Missing')

# Display the DataFrame with filled missing values
print("\nDataFrame with filled missing values:")
print(df_filled.head())

# Calculate summary statistics
summary_statistics = df.describe(include='all')

# Display summary statistics
print("\nSummary statistics:")
print(summary_statistics)