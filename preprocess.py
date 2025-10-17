import pandas as pd

def preprocess():
    # Load the cleaned dataset that already has the target
    df = pd.read_csv("final_bmw_dataset_with_new_features.csv")

    # Add or modify any preprocessing steps as needed here
    # For example, feature engineering, cleaning, renaming columns, etc.

    # Save to the output used by the pipeline
    df.to_csv("cleaned_file.csv", index=False)

if __name__ == "__main__":
    preprocess()
