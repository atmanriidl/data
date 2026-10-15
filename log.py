# Logistic regression
import numpy as np
import pandas as pd

# ============================================================
# Practical 10 - Logistic regression: predict, odds, probability
# ============================================================
import numpy as np
import pandas as pd
from sklearn import linear_model

X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69,
5.88]).reshape(-1,1)

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()

logr.fit(X,y)

predicted = logr.predict(np.array([3.46]).reshape(-1,1))
print(predicted)

# Coefficient
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69,
5.88]).reshape(-1,1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr=linear_model.LogisticRegression()

logr.fit(X,y)

log_odds=logr.coef_
odds=np.exp(log_odds)
print(odds)

# Probability
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69,
5.88]).reshape(-1,1)

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()

logr.fit(X,y)

def logit2prob(logr,x):
    log_odds=logr.coef_*x+logr.intercept_
    odds = np.exp(log_odds)
    probability=odds/(1+odds)
    return (probability)

print(logit2prob(logr, X))



# ============================================================
# Practical 10 (Q2) - Logistic regression (sleep hours vs alert)
# ============================================================
# 2) Logistic regression (Sleep Hours vs Alert)
import pandas as pd
from sklearn.linear_model import LogisticRegression

data={"Sleep_Hours":[3,4,5,6,7,8],"Alert":[0,0,0,1,1,1]}
df=pd.DataFrame(data)
print(df)

x=df[["Sleep_Hours"]]
y=df["Alert"]

model=LogisticRegression()
model.fit(x,y)

model=LogisticRegression()
model.fit(x,y)

new_student=[[5]]
prediction=model.predict(new_student)
print("Preicted Label: ",prediction[0])
if prediction[0]==0:
    print("Result: Tired")
else:
    print("Result: Alert")

probability=model.predict_proba(new_student)
print("Predicted Probability: ",probability)
