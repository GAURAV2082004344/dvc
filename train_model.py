import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train(input_csv, model_output):
    df = pd.read_csv(input_csv)
    y = df["co2_emissions_gpkm"]
    X = df.drop("co2_emissions_gpkm", axis=1)
    X = pd.get_dummies(X)

    model = LinearRegression()
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, model_output)

if __name__ == "__main__":
    train("cleaned_file.csv", "model.pkl")
