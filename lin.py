# Linear regression
import numpy as np

# ============================================================
# Practical 9 - Linear regression with scipy
# ============================================================
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


# ============================================================
# Practical 10 (Q1) - Linear regression from scratch (study hours vs exam score)
# ============================================================
# 1) Manual linear regression (Study Hours vs Exam Score)
import numpy as np
import pandas as pd

x=np.array([1,2,3,4,5])
y=np.array([50,55,65,70,85])
print("Study Hour (x) : ",x)
print("Exam Scores (y):",y)

x_mean=np.mean(x)
y_mean=np.mean(y)
print("Average of x : ",x_mean)
print("Average of y : ",y_mean)

numerator=np.sum((x-x_mean)*(y-y_mean))
denominator=np.sum((x-x_mean)**2)
m=numerator/denominator
print("Slope (m) : ",m)

# //Intercept
b=y_mean-(m*x_mean)
print("Intercept (b):",b)

# Line of best fit
print("Line of best fit:")
print(f"Y^={m}x+{b}")

# Predict exam score

x_new=6
y_predicted=m*x_new+b
print("Study Hours: ",x_new)
print("Predicted Exam Score:",y_predicted)
