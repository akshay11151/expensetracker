import pandas as pd

# Load the CSV file into a pandas dataframe
df = pd.read_csv('expenses.csv')

# Group the expenses by category and calculate the total expenses for each category
expenses_by_category = df.groupby('Category')['Amount'].sum()

# Print the results
print('Expenses by category:')
print(expenses_by_category)
