#multiple dimentions of arrays : 

#array should be homogenious
import array 

my_array = array.array('i',[1,2,3,4,5,3]) #-------> o(n)  #for empty arry both the time and space complexity is to be constant and it have to be 0(1)
print(my_array)


import numpy as np 
np_array = np.array([], dtype = int) #-------> o(1)
print(np_array)

np_array1 = np.array([1,2,3,4,5,56,7,8,4,2])
print(np_array1)