import numpy as np
from sklearn.linear_model import LinearRegression


area = np.array([500, 800, 1000, 1200, 1500]).reshape(-1, 1)
price = np.array([50, 80, 100, 120, 150])

model = LinearRegression()
model.fit(area, price)

new_area = int(input("Enter area of house (sq.ft): "))
predicted_price = model.predict([[new_area]])

print(f"Predicted Price: {predicted_price[0]:.2f} lakhs")