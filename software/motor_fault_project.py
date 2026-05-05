import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.preprocessing import StandardScaler

# -----------------------
# 1. Load dataset
# -----------------------
df = pd.read_csv("final_dataset.csv")

# -----------------------
# 2. Split features & label
# -----------------------
X = df.drop("label", axis=1)
y = df["label"]

# -----------------------
# 3. Train-test split
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------
# 4. Feature scaling
# -----------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------
# 5. Models
# -----------------------
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)

# -----------------------
# 6. Train
# -----------------------
rf_model.fit(X_train, y_train)
gb_model.fit(X_train, y_train)

# -----------------------
# 7. Predictions
# -----------------------
rf_pred = rf_model.predict(X_test)
gb_pred = gb_model.predict(X_test)

# -----------------------
# 8. Accuracy
# -----------------------
rf_acc = accuracy_score(y_test, rf_pred)
gb_acc = accuracy_score(y_test, gb_pred)

print("Random Forest Accuracy:", rf_acc)
print("Gradient Boost Accuracy:", gb_acc)

# -----------------------
# 9. Classification report
# -----------------------
print("\nRandom Forest Report:\n", classification_report(y_test, rf_pred))
print("\nGradient Boost Report:\n", classification_report(y_test, gb_pred))

# -----------------------
# 10. Confusion Matrix
# -----------------------
cm_rf = confusion_matrix(y_test, rf_pred)
cm_gb = confusion_matrix(y_test, gb_pred)

ConfusionMatrixDisplay(cm_rf).plot()
plt.title("Random Forest Confusion Matrix")
plt.show()

ConfusionMatrixDisplay(cm_gb).plot()
plt.title("Gradient Boost Confusion Matrix")
plt.show()

# -----------------------
# 11. Accuracy comparison plot
# -----------------------
models = ["Random Forest", "Gradient Boost"]
accuracies = [rf_acc, gb_acc]

plt.figure()
plt.bar(models, accuracies)
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Model Comparison")
plt.show()
joblib.dump(rf_model, "rf_model.pkl")
joblib.dump(scaler, "scaler.pkl")