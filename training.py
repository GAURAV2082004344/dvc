import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

try:
    print("Starting training...")

    data = pd.read_csv('final_bmw_dataset.csv')
    print(f"Data loaded: {data.shape} rows and columns")

    x = data[['model_id']]
    y = data[['model_engine_cc']]

    model = LinearRegression()
    model.fit(x, y)

    joblib.dump(model, 'model.pkl')

    print("Model saved successfully as model.pkl")

except Exception as e:
    print("Error:", e)
