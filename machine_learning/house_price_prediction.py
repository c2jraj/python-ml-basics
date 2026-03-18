# house_price_prediction.py
# Predicts house prices using scikit-learn's Linear Regression model.
# Features: square footage, number of bedrooms, number of bathrooms, age (years).

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ── Dataset ───────────────────────────────────────────────────────────────────
# Columns: [sqft, bedrooms, bathrooms, age_years]
# Prices in thousands of USD

np.random.seed(42)
n_samples = 100

sqft = np.random.randint(800, 4000, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 4, n_samples)
age = np.random.randint(0, 50, n_samples)

# Price is a linear combination of features plus some noise
price = (
    0.1 * sqft
    + 10 * bedrooms
    + 15 * bathrooms
    - 0.5 * age
    + np.random.normal(0, 15, n_samples)
    + 50  # base price offset
)

X = np.column_stack([sqft, bedrooms, bathrooms, age])
y = price  # in thousands of USD

feature_names = ["sqft", "bedrooms", "bathrooms", "age_years"]

# ── Train / test split ────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Feature scaling ───────────────────────────────────────────────────────────
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ── Model training ────────────────────────────────────────────────────────────
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# ── Evaluation ────────────────────────────────────────────────────────────────
y_pred = model.predict(X_test_scaled)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("=" * 50)
print("  House Price Prediction — Linear Regression")
print("=" * 50)
print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")

print("\nModel coefficients:")
for feature_name, coef in zip(feature_names, model.coef_):
    print(f"  {feature_name:12}: {coef:+.4f}")
print(f"  {'intercept':12}: {model.intercept_:+.4f}")

print("\nEvaluation metrics:")
print(f"  MAE  : {mae:.2f}k")
print(f"  RMSE : {rmse:.2f}k")
print(f"  R²   : {r2:.4f}")

# ── Sample predictions ────────────────────────────────────────────────────────
sample_houses = np.array([
    [1500, 3, 2, 10],   # 1500 sqft, 3 bed, 2 bath, 10 yrs old
    [2500, 4, 3, 5],    # 2500 sqft, 4 bed, 3 bath,  5 yrs old
    [900,  2, 1, 30],   # 900  sqft, 2 bed, 1 bath, 30 yrs old
])
sample_scaled = scaler.transform(sample_houses)
predictions = model.predict(sample_scaled)

print("\nSample predictions:")
for house, pred in zip(sample_houses, predictions):
    sqft_, beds, baths, age_ = house
    print(
        f"  {sqft_} sqft | {beds} bed | {baths} bath | {age_} yrs "
        f"=> ${pred:.1f}k"
    )
