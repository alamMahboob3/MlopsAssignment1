# train.py
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import joblib

# Load dataset
data = load_diabetes()
X, y = data.data, data.target
print("Dataset loaded.")

# Train model
model = LinearRegression()
model.fit(X, y)
print("Model training complete.")

# Save model
joblib.dump(model, "model.pkl")
print("Model training complete. Model saved as model.pkl.")