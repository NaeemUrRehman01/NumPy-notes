import numpy as np

rng = np.random.default_rng()#seed is used if your reproduce the same results ,seed=1


#print(rng.integers(1,7))
#print(rng.integers(low=1,high=101,size=4))#we also write it as this

#If we need dimensions we write as, size=(rows,coloumns)
#print(rng.integers(low=1,high=101,size=(3,2)))
#print(np.random.uniform(low=1,high=1,size=(3,2)))

# How to shuffle an array
# 

#For chooosing randomly
fruits=np.array(["Apple🍎","Banana🍌","Coconut🥥","Grapes🍇"])
# fruit=rng.choice(fruits)#For chosing randomly one
# fruits=rng.choice(fruits, size=3)#For chosing randomly three
fruits=rng.choice(fruits, size=(3,3))#For dimensions 
print(fruits)