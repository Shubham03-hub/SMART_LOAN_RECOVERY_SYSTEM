from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

pred = model.predict(X_test)

print(classification_report(y_test, pred))

print("ROC AUC:", roc_auc_score(y_test, pred))