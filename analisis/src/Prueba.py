import pandas as pd

df = pd.DataFrame({
    'Name': ['Jane', 'Mitch', 'Alex', 'Evan', 'Melissa'],
    'Location': ['Toronto', 'New York', 'Los Angeles', 'Vancouver', 'Seattle'],
    'Amount': [99.99, 123.12, 150.23, 52.34, 12.34]
})

df['Company'].loc[0] = 'datagy'
print(df)
