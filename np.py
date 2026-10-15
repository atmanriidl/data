# NumPy: arrays, slicing, statistics, matrix operations
import numpy as np

# ============================================================
# Practical 1 - Creation & manipulation of arrays using NumPy
# ============================================================
import numpy as np

#Creating 1-D array

arr=np.array([1,2,3,4],dtype=np.float32)
print("Array : ",arr)

#Creating multi-dimensionl array

arr=np.array([[1,2,3,],[4,5,6]])
print("2-D array : \n",arr)

#Creating array of zeros

arr=np.zeros((2,3))
print("Array of zeros : \n",arr)

#Creating array of ones

arr=np.ones(5,dtype=np.int32)
print("Array of ones : \n",arr)

#Creating array of random numbers
random=np.random.rand(2,3)
print("Array of rndom number : \n",random)

#Creating arraof choice
arr=np.full((2,2),7)
print("Arrat :\n",arr)

#Creating identity matrix

arr=np.eye(3,dtype=np.int32)
print("Array : \n",arr)

#Evenly spaced ndarray

arr=np.arange(5)
print("Evenly spaced array : \n",arr)

#Dimensions of Numpy array

arr=np.array([[5,10,15],[20,25,20]])
print("Array: \n",arr)
print("Dimension : \n",arr.ndim)

#Shape of Numpy array
a=np.array([[1,2,3],[4,5,6]])
print("Array:\n",a)
print("Shape:\n",a.shape)
print("Rows:\n",a.shape[0])
print("Columns:\n",a.shape[1])

#Size of Numpy array

a=np.array([[5,10,15],[20,25,30]])
print("Size of array:\n",a.size)

#Reshaping a Numpy rray
a=np.array([3,6,9,12])
reshape=np.reshape(a,(2,2))
print("Reshaped array: \n",reshape)

#Flattening a Numpy array
a=np.ones((2,2))
b=a.flatten()
c=a.ravel()
print("Original shape:",a.shape)
print("Array:\n",a,"\n")
print("Shape after flatten:",b.shape)
print("Array:\n",b,"\n")
print("Shape after ravel:",c.shape)
print("Array: \n",c)

#Transpose of a Numpy array
arr=np.array([[1,2,3],[4,5,6]])
transpose=np.transpose(arr)
print("Transpose of array :\n",transpose)

#Expanding a Numpy array

a=np.array([1,2,3])
b=np.expand_dims(a,axis=0)
c=np.expand_dims(a,axis=1)
print('Original:','\n','Shape',a.shape,'\n',a)
print('Expand along columns:','\n','Shape',b.shape,'\n',b)
print('Expand along rows:','\n','Shape',c.shape,'\n',c)

#Slicing 1-D array
a = np.array([1,2,3,4,5,6])
print(a[1:5:2])

a = np.array([1,2,3,4,5,6])
print(a[1:6:2])

a = np.array([1,2,3,4,5,6])
print(a[:6:2])
print(a[1::2])
print(a[1:6:])

#Slicing 2-D Numpy array
a = np.array([[1,2,3],
[4,5,6]])
print(a[0,0])
print(a[1,2])
print(a[1,0])

a = np.array([[1,2,3],[4,5,6]])
# print first row values
print('First row values :','\n',a[0:1,:])
# with step-size for columns
print('Alternate values from first row:','\n',a[0:1,::2])
#
print('Second column values :','\n',a[:,1::2])
print('Arbitrary values :','\n',a[0:1,1:3])

#Negative slicing of Numpy arrays
a = np.array([[1,2,3,4,5],
[6,7,8,9,10]])
print(a[:,-1])

a = np.array([[1,2,3,4,5],
[6,7,8,9,10]])
print('Original array :','\n',a)

print('Reversed array :','\n',a[::-1,::-1])

#Using flip() method
a = np.array([[1,2,3,4,5],
[6,7,8,9,10]])
print('Original array :','\n',a)
print('Reversed array vertically :','\n',np.flip(a,axis=1))
print('Reversed array horizontally :','\n',np.flip(a,axis=0))

#Stacking of Numpy array
a = np.arange(0,5)
b = np.arange(5,10)
print('Array 1 :','\n',a)
print('Array 2 :','\n',b)
print('Vertical stacking :','\n',np.vstack((a,b)))
print('Horizontal stacking :','\n',np.hstack((a,b)))

#Concatenating Numpy array
a=np.arange(0,5).reshape(1,5)
b=np.arange(5,10).reshape(1,5)
print("Array 1:\n",a)
print("Array 2 :\n",b)
print('Concatenate along rows :','\n',np.concatenate((a,b),axis=0))
print('Concatenate along columns :','\n',np.concatenate((a,b),axis=1))

#Using append method
a = np.array([[1,2],
[3,4]])
np.append(a,[[5,6]], axis=0)

#Broadcasting n Numpy array
a = np.arange(10,20,2)
b = np.array([[2],[2]])
print('Adding two different size arrays :','\n',a+b)
print('Multiplying an ndarray and a number :',a*2)

#Basic arithemetic operations on Numpy array
print('Subtract :',a-5)

print('Multiply :',a*5)
print('Divide :',a/5)
print('Power :',a**2)
print('Remainder :',a%5)

#Mean ,Median,Standard Deviation
a=np.arange(5,15,2)
print("Mean",np.mean(a))
print('Standard deviation :',np.std(a))
print('Median :',np.median(a))

#Min-Max values and their indexes
a=np.array([[1,6],[4,3]])
print("Min:",np.min(a,axis=0))
print("Max:",np.max(a,axis=1))

#determine the index of the minimum or maximum value
a = np.array([[1,6,5],
[4,3,7]])
# minimum along a column
print('Min :',np.argmin(a,axis=0))
# maximum along a row
print('Max :',np.argmax(a,axis=1))

#Sorting in Numpy array
a = np.array([1,4,2,5,3,6,8,7,9])
np.sort(a, kind='quicksort')

#Finding the Median in Numpy
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("The array is: ")
print(arr)

print("\n")
print("Median function applied: ")
print(np.median(arr))

#Finding the Mean in Numpy
arr = np.array([[10,20,30],[40,50,60],[70,80,99]])
print("The array is: ")
print(arr)
print("\n")
print("Mean function applied: ")
print(np.mean(arr))
print("Mean function applied on axis 1: ")
print(np.mean(arr, axis=1))

#Finding Variance in Numpy
arr = np.array([10,20,30])
print("The variance of the array is: ")
print(np.var(arr))


# ============================================================
# Practical 2 - Basic Statistics using NumPy
# ============================================================
#1)Replace all odd numbers in arr with -1 without changing array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2!=0]=-1
print(arr)

#2)Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

common = []

for i in a:
    if i in b and i not in common:
        common.append(int(i))

print(common)

a = np.array([2, 6, 1, 9, 10, 3, 27])

print(a[(a >= 5) & (a <= 10)])

#4)Reverse the rows of a 2D array arr.

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

result = arr[::-1]

print(result)

#Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
zero=np.zeros(10)
one=np.ones(10)
fives=np.full(10,5)
print("Array of 10 zeros:")
print(zero,"\n")
print("Array of 10 ones : ")
print(one,"\n")
print("Array of 10 fives:")
print(fives)

#Write a NumPy program to create an array of integers from 30 to 70.
arr=np.arange(30,71)
print("Array of integers from 30 to 70:")
print(arr)

#Write a NumPy program to create an array of all even integers from 30 to 70.
arr=np.arange(30,71,2)
print("Array of even integers from 30 to 70:")
print(arr)

#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
matrix=np.arange(10,22).reshape(3,4)
print("3x4 Matrix:")
print(matrix)

#Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
matrix=np.zeros((5,5),dtype=int)
np.fill_diagonal(matrix,[1,2,3,4,5])
print("5X5 Matrix: \n",matrix)


# ============================================================
# Practical 6 (Q1) - Matrix operations with NumPy
# ============================================================
import numpy as np

a=np.random.randint(1,10,(3,3))
b=np.random.randint(1,10,(3,3))
print("Matrix A :\n",a)
print("Matrix B :\n",b)
#Adding two matrix
print("\n Addition:\n",a+b)
print("\nSubtraction:\n",a-b)
print("\nMultiplication:\n",a*b)
print("\nTranspose of a:\n",np.transpose(a))
print("\nInverse of a :\n",np.linalg.inv(a))
