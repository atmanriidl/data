# Pandas: Series, DataFrames, selection, filtering, grouping, merging
import numpy as np
import pandas as pd

# ============================================================
# Practical 3 - Creation of dataframes using pandas
# ============================================================
import pandas as pd
import numpy as np

#Creating an Empty Series
s=pd.Series()
print(s)

#Create series from from ndarry
data=np.array(['a','b','c','d'])
s=pd.Series(data)
print(s)

#Create series from from ndarry with index
dat=np.array(['a','b','c','d'])
s=pd.Series(data,index=[100,101,102,103])
print(s)

#Create a Series from dict
data={'a':0,'b':1,'c':2}
s=pd.Series(data)
print(s)

#Create a series from dictionary with custom index
data={'a':0,'b':1,'c':2}
s=pd.Series(data,index=['b','c','d','a'])
print(s)

#Create a series from scalar
s=pd.Series(5,index=[0,1,2,3])
print(s)

#Accessing data from series with position
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s[:3])

#Retrieve last three elements
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s[-3:])

#Retrieve Data Using Label (Index)
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['a'])

#Retrieve multiple elements using a list of index label values.
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[['a','c','d']])

#Create an Empty DataFrame
df = pd.DataFrame()
print (df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)

#create an indexed DataFrame using arrays.
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

#create a DataFrame by passing a list of dictionaries.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

#DataFrame by passing a list of dictionaries and the row indices.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print (df)

#example shows how to create a DataFrame with a list of dictionaries, row indices, and column indices.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print (df1)
print (df2)

#Create a DataFrame from Dict of Series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print (df)

#Column Selection
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),

'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print (df ['one'])

#Column Addition
d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(d)
print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print (df)

#Column Deletion
d={'one':pd.Series([1,2,3],index=['a','b','c']),
   'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
   'three':pd.Series([10,20,30],index=['a','b','c'])}

df=pd.DataFrame(d)
print("Our dataframe is : ")
print(df)

#Column Deletion
d={'one':pd.Series([1,2,3],index=['a','b','c']),
   'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
   'three':pd.Series([10,20,30],index=['a','b','c'])}

df=pd.DataFrame(d)
print("Our dataframe is : ")
print(df)
print("Deleting another column using POP function: ")
df.pop('two')
print(df)

#Selection by Label
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df=pd.DataFrame(d)
print(df.loc['b'])

#Selection by integer location
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df=pd.DataFrame(d)
print(df.iloc[2])

#Slice Rows
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df=pd.DataFrame(d)
print(df[2:4])

#Addition of Rows
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])

df = pd.concat([df, df2], ignore_index=True)

print(df)

#Create a DataFrame from a dictionary containing student names, their ages, and test score
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 21, 19, 22],
    'Test Score': [85, 90, 78, 92]
}
df = pd.DataFrame(student_data)
print(df)

student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 19],
    'Test Score': [85, 90, 78]
}
df = pd.DataFrame(student_data,index=['student_1', 'student_2', 'student_3'])
print(df)

student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 19],
    'Score': [85, 90, 78]
}
df = pd.DataFrame(student_data,index=['student_1', 'student_2', 'student_3'])
selected_df = df[['Name', 'Score']]

print(selected_df)

import pandas as pd

# Student DataFrame
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 19],
    'Score': [85, 90, 78]
}

df = pd.DataFrame(
    student_data,
    index=['student_1', 'student_2', 'student_3']
)

# Filter students older than 18 and scored above 80
filtered_df = df[(df['Age'] > 18) & (df['Score'] > 80)]

print(filtered_df)

df = pd.DataFrame({'Score': [85, np.nan, 78, 92, np.nan]})
df['Score'] = df['Score'].fillna(df['Score'].mean())
print(df)

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Age': [20, 21, 20, 19, 21],
    'Score': [85, 90, 85, 78, 90]
})
df = df.drop_duplicates(subset=['Name'])

print(df)

sales_data = {
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Clothing', 'Furniture'],
    'Sales': [500, 300, 700, 200, 400]
}

df = pd.DataFrame(sales_data)
total_sales = df.groupby('Category')['Sales'].sum()
print(total_sales)

data={
    'Name':['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
    'Age': [21, 19, 20, 18, 17, 21],
    'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
    'Percentage': [88, 92, 95, 70, 65, 78]
}
df=pd.DataFrame(data)
#1)Select rows where Percentage > 80
result1=df[df['Percentage']>80]
print("Rows where percentage>80 : \n",result1,"\n")
# 2)Select rows where Percentage > 80    Using .loc []
result2=df.loc[df['Percentage']>80]
print("Rows where percentage>80 using loc: \n",result2,"\n")
# 3)Select rows where Percentage > 80 Using .query()
result3=df.query('Percentage > 80')
print(result3)


# ============================================================
# Practical 4 - Manipulation of DataFrames using pandas
# ============================================================
import pandas as pd
import numpy as np

data={
    'Name':["Alice","Bob",np.nan,"David"],
    'Age':[25,np.nan,30,22],
    'City':["New York","London","Paris",np.nan]
}

df=pd.DataFrame(data)
print("DataFrame:")
print(df,"\n")

print("Missing values in each column: ")
print(df.isnull().sum(),"\n")

print("Total missing values: ")
print(df.isnull().sum().sum())

data={
    'Name':['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
    'Age': [21, 19, 20, 18, 17, 21],
    'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
    'Percentage': [88, 92, 95, 70, 65, 78]
}
df=pd.DataFrame(data)
#1)Select rows where Percentage > 80
result1=df[df['Percentage']>80]
print("Rows where percentage>80 : \n",result1,"\n")
# 2)Select rows where Percentage > 80    Using .loc []
result2=df.loc[df['Percentage']>80]
print("Rows where percentage>80 using loc: \n",result2,"\n")
# 3)Select rows where Percentage > 80 Using .query()
result3=df.query('Percentage > 80')
print(result3)

data={
    'ID':[101,102,103,104,105,106,107,108,109,110],
    'Score':[67,89,43,69,68,90,94,77,89,95]
}
df=pd.DataFrame(data)
print("First 5 rows:\n")
print(df.head(5))
print("Last 5 rows:\n")
print(df.tail(5))

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
             'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
                  'horsepower': [141, 80, 182 , 160]}

df_price=pd.DataFrame(Car_Price)
df_hp=pd.DataFrame(car_Horsepower)

merged_df=pd.merge(df_price,df_hp,on='Company')
print("Merged DataFrame:\n",merged_df,"\n")
df_price['horsepower']=df_hp['horsepower']
print("First DataFrame with Horsepower Column Appended",df_price)


# ============================================================
# Practical 6 (Q2) - Student DataFrame
# ============================================================
import numpy as np
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [20, 21, 19, 22, 20],
    'Math': [90, 78, 85, 92, 88],
    'Python': [95, 82, 90, 87, 91],
    'SQL': [88, 79, 84, 90, 86]
}
df=pd.DataFrame(data)

print("First 3 rows : ",df.head(3))
print("Last 3 rows : ",df.tail(3))

print("\n Average marks in each subject: \n")
print(df[['Math','Python','SQL']].mean())

print("\nStudents who scored marks greater than 85\n")
print(df[df['Python']>85])

#Adding average column

df['Average'] = df[['Math', 'Python', 'SQL']].mean(axis=1)

print(df)

df_sorted = df.sort_values(by='Average', ascending=False)

print("\nStudents sorted by average marks:")
print(df_sorted)
