# StudyHours| Marks
# 1	        | 40
# 2	        | 45
# 3	        | 50
# 4	        | 55
# 5	        | 65
# 6	        | 70
# 7	        | 75
# 8	        | 85
# 9	        | 90
# 10	    | 95

import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([40,45,50,55,65,70,75,85,90,95])
model = LinearRegression()
model.fit(X, y)
predicted = model.predict([[7]])
print("Predicted Marks for 7 study hours:", predicted[0])