import pandas as pd
from sklearn.linear_model import LinearRegression

# Training data
data = {"size":[1000,1500,2000,2500,3000],
"price":[200000,300000,400000,500000,600000]}
df = pd.DataFrame(data)

X = df[["size"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict prices for multiple sizes
new_sizes = [1200, 1800, 2200]
for s in new_sizes:
    print(f"Predicted price for {s} sq ft: {model.predict([[s]])[0]}")