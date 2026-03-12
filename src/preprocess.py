import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/LOAN_DATAS.csv")

le = LabelEncoder()

df["employment_status"] = le.fit_transform(df["employment_status"])
df["collateral"] = le.fit_transform(df["collateral"])
df["loan_type"] = le.fit_transform(df["loan_type"])

X = df.drop(["default","loan_id"], axis=1)
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train.shape)
print("Test data:", X_test.shape)



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/LOAN_DATAS.csv")

le = LabelEncoder()

df["employment_status"] = le.fit_transform(df["employment_status"])
df["collateral"] = le.fit_transform(df["collateral"])
df["loan_type"] = le.fit_transform(df["loan_type"])

X = df.drop(["default","loan_id"], axis=1)
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Test Data:", X_test.shape)