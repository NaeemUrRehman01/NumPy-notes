import numpy as np

# Filtering = Refers to the processes of selecting elements
#from an array that match a given condition

ages = np.array([[12,34,66,45,78,75,44,78],
                [43,55,65,23,13,15,66,54]])

# teenagers=ages[ages < 18]
# adults= ages[(ages >= 18) & (ages <  65)]
# seniors=ages[ages>=65] 
# evens=ages[ages % 2 == 0]
# odds=ages[ages % 2 != 0]
adults = np.where(ages >= 18,ages,0)
#np.where(condition, x, y)

# This is a vectorized if-else in NumPy.

# Syntax:

# np.where(condition, value_if_true, value_if_false)


# It checks each element of the condition:

# If True, take the value from x

# If False, take the value from y
#print(teenagers)
print(adults)


