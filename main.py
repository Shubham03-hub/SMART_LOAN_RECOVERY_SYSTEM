import pandas as pd

df = pd.read_csv("data/LOAN_DATAS.csv")

print("Dataset Loaded Successfully")
print(df.head())

print("Dataset Shape:", df.shape)