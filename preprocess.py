import pandas as pd

# Load raw data
df = pd.read_csv('final_bmw_dataset.csv')

# Data cleaning steps here (examples)
df = df.dropna()            # Remove missing values
df = df.drop_duplicates()   # Remove duplicate rows

# Save cleaned output
df.to_csv('cleaned_file.csv', index=False)
