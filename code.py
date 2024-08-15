# First, install necessary libraries
!pip install -U seaborn scikit-learn matplotlib

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Step 1: Data Collection and Preparation

# Simulate some data
np.random.seed(42)

data_size = 1000
data = {
    'Crop': np.random.choice(['Wheat', 'Corn', 'Rice'], data_size),
    'Temperature': np.random.uniform(15, 35, data_size),
    'Precipitation': np.random.uniform(0, 200, data_size),
    'SoilQuality': np.random.uniform(0, 1, data_size),
    'Yield': np.random.uniform(1, 5, data_size)  # Yield in tons per hectare
}

df = pd.DataFrame(data)

# Display the first few rows
df.head()

# Step 2: Data Exploration and Visualization

# Visualize relationships in the data
sns.pairplot(df, hue='Crop')
plt.show()

# Step 3: Building a Predictive Model

# Convert categorical 'Crop' feature to numerical
df = pd.get_dummies(df, columns=['Crop'], drop_first=True)

# Split the data
X = df.drop('Yield', axis=1)
y = df['Yield']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Step 4: Optimization Recommendations

# Example function to recommend resources based on predicted yield
def recommend_resources(predicted_yield):
    water_needed = predicted_yield * 100  # in liters
    fertilizer_needed = predicted_yield * 10  # in kg
    return water_needed, fertilizer_needed

# Predict yield for a new sample
new_sample = pd.DataFrame({
    'Temperature': [25],
    'Precipitation': [150],
    'SoilQuality': [0.8],
    'Crop_Corn': [1],
    'Crop_Rice': [0]
})

# Ensure new_sample has the same columns as training data
new_sample = new_sample.reindex(columns=X.columns, fill_value=0)

# Make the prediction
predicted_yield = model.predict(new_sample)

# Get the recommended resources
water, fertilizer = recommend_resources(predicted_yield[0])

print(f'Predicted Yield: {predicted_yield[0]:.2f} tons/hectare')
print(f'Recommended Water: {water:.2f} liters')
print(f'Recommended Fertilizer: {fertilizer:.2f} kg')

# Step 5: Visualization of Predictions

# Visualize feature importance
importances = model.feature_importances_
features = X.columns
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(12, 6))
plt.title('Feature Importance')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), features[indices], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.show()
