import numpy as np

#------------------ Scalar arithmatic(single value)------------------------

# array=np.array([1,2,3])

# print(array+1)
# print(array-2)
# print(array*3)
# print(array/4)
# print(array**5)



#-----------------Vectorized math Function----------------------

#array =np.array([1,2,3])

#print(np.sqrt(array))#Here we call mathfunc from numpy sqrt= square root 
#print(np.round(array))#Round an array to the given number of decimals.
#print(np.floor(array))#To alwys round down
#print(np.ceil(array))#To always round up 
#print(np.pi)

#Exercise

# radii=np.array([1,2,3])

# print(np.pi *radii ** 2)#to find the radius of all list

#----------------------Element wise Arithmatic-------------------------

# array1= np.array([1,2,3])
# array2= np.array([4,5,6])

# print(array1+array2)
# print(array1-array2)
# print(array1*array2)
# print(array1/array2)
# print(array1**array2)

#----------------------------Comparison Operator---------------------
 #used for data cleansing

scores=np.array([89,78,90,100,66,34,97,68])

# print(scores == 100)
# print(scores >= 60)#Give output in boolean

# we also use conditional Statement
scores[scores < 60] = 0
print(scores)