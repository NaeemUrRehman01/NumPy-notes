import numpy as np

array=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])

#For Slicing we use subscript operator
# array[start:end:step]
#-----------------------------Row Slicing-----------------------------------
# print(array[0:3]) #End row is exlusive so print from 0 to 2
# print(array[1:4]) #First row is exlusive so print from 1 to 3
# print(array[0:4:2]) #If we need to print every secand row
# print(array[::2]) #If we omit the colons like (array[2]) numpy thinks we print 2 row .
#print(array[::-1])#This will return all the rows reversed
#print(array[::-2])#This will return all the rows reversed and select starting secand rows from  bottom

#---------------------------Coloumn Slicing---------------------------------
#print(array[0,0])#When acessing our 2d array ,we will nedd two indices .for example 0 comma 0
#print(array[:,2])#For selecting all rows we use colon otherwise sytax error occur
#print(array[:,0:3])#For writing first 3 coloumns we have =[strat 0: end 3]
#print(array[:,1:4])#for last 3 coloumns
#print(array[:,1:])#If you want all coloumns of your data
#print(array[:,::2])#now we select every secand colomn
#print(array[:,1::2])#now would like every secand coloumn but we will start with coloumn 1
#print(array[:,::-1])#Now we reverse the order

#-------------------------------Row and Coloumn Slicing------------------------
#Now we are combining both row and coloumn =array[row_start:row_end, col_start:col_end],array[1, :] → row 1, all columns →,array[1, :] → row 1, all columns →
#print(array[0:2,  0:2])#now we print first two rows and coloumn
#print(array[0:2,2:])#we print upper last two rows and coloumn
print(array[2:4,2:4])