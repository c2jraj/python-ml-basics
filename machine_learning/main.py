import pandas as pd
from sklearn.linear_model import LinearRegression

data = {"size":[1000,1500,2000,2500,3000],"price":[200000,300000,400000,500000,600000]}
df = pd.DataFrame(data)
X = df[["size"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

house_size = float(input("Enter house size in sq ft: "))
prediction = model.predict([[house_size]])
print(f"Predicted price: {prediction[0]}")