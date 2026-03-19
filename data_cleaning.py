import pandas as pd

df = pd.read_csv('codon_usage.csv', low_memory=False)

print(df.dtypes)