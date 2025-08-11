import pandas as pd
data = pd.read_csv("final_bmw_dataset.csv")

#print(data.head())

data["model_id"]= 2*data["model_id"]

data.to_csv("final_bmw_dataset.csv",index=False)
