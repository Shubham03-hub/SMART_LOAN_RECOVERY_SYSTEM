import pandas as pd

# Load dataset
df = pd.read_csv("data/LOAN_DATAS.csv")

# Feature 1
df["debt_income_ratio"] = df["loan_amount"] / df["income"]

# Feature 2
df["payment_ratio"] = df["on_time_payments"] / (
    df["on_time_payments"] + df["past_due_payments"]
)

print(df.head())
print("Feature Engineering Completed")