import numpy as np
# #In multidimension array we have four dimensions 

# # Zero Dimensional
# array = np.array('A')
# print(array.ndim) #ndim=no of dimensions in array

# # One dimensional
# array = np.array(['A','B','C',])
# print(array.ndim) #ndim=no of dimensions in array

# # Two Dimensional also peoplre called matrix
# array = np.array([['A','B','C'],
#                   ['D','E','F'],
#                   ['G','H','I']])
# print(array.ndim) #ndim=no of dimensions in array

# # Three Dimensional
# array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
#                   [['J','K','L'],['M','N','O'],['P','Q','R']],
#                   [['S','T','U'],['V','W','X'],['Y','Z',' ']]
#                   ])#WE MUST FOLLOW THE SAME SEQUENCE
# print(array.shape) #shape of dimensions in array Like we 3 rows and 3 clolumns

 

#  #-------------------Chain Indexing-------------------

# array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
#                   [['J','K','L'],['M','N','O'],['P','Q','R']],
#                   [['S','T','U'],['V','W','X'],['Y','Z',' ']]
# ])
# print(array[0][0][0])

#Multiindexing
#Multidimensional indexing is faster then chain indexing
#[0,0,0]=First zero shows index,secnad rows and third coloumn and starts indexses from 0.

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z',' ']]
])
print(array[2,2,1])


#Exercise: use string concatenation to write your name by multidimensional indexing

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z',' ']]
])

Name= array[1,1,1]+array[0,0,0]+array[0,1,1]+array[0,1,1]+array[1,1,0]  #print = NAEEM
print("Name = ",Name)