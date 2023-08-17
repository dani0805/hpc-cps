import random

import dask.dataframe as dd
from dask.distributed import Client

# if the file "large_dataset.csv" does not exist, create it
try:
    with open("large_dataset.csv", "r") as f:
        pass
except FileNotFoundError:
    with open("large_dataset.csv", "w") as f:
        f.write("transaction_id,product_id,category,amount\n")
        for i in range(1000000):
            f.write(f"{i},{random.randint(0, 1000)},category{random.randint(0, 10)},{random.randint(0, 1000)}\n")


# Connect to the Dask distributed scheduler
client = Client("tcp://localhost:8786")

# Read CSV file into a Dask DataFrame
# Assume the CSV file has columns: ['transaction_id', 'product_id', 'category', 'amount']
df = dd.read_csv('large_dataset.csv', assume_missing=True)

# Perform data manipulation operations
df_grouped = df.groupby('category')['amount'].agg(['sum', 'mean', 'count'])

# Trigger computation
output = df_grouped.compute()

print(output)