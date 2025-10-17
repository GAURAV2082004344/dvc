import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error


def evaluate(input_csv, model_file):
    df = pd.read_csv(input_csv)
    y_true = df["co2_emissions_gpkm"]
    X = df.drop("co2_emissions_gpkm", axis=1)
    X = pd.get_dummies(X)

    model = joblib.load(model_file)
    y_pred = model.predict(X)

    mse = mean_squared_error(y_true, y_pred)
    print(f"Mean Squared Error: {mse}")


if __name__ == "__main__":
    evaluate("cleaned_file.csv", "model.pkl")
