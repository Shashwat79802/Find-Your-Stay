import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('FindYourStay/data/oyo.csv')

# Drop the rows where any cell in the first or last column is empty
df.dropna(subset=[df.columns[0], df.columns[-1]], inplace=True)

# Write the updated dataframe back to the CSV file
df.to_csv('data/oyo.csv', index=False)
