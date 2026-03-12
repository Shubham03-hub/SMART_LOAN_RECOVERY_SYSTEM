import pandas as pd
import sqlite3

df = pd.read_csv("data/LOAN_DATAS.csv")

conn = sqlite3.connect("database/loan_database.db")

df.to_sql("loans", conn, if_exists="replace", index=False)

print("Data inserted into SQL database")
print(df.shape)
print(df.head())