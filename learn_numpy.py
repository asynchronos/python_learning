import numpy as np 
a = np.array([1,2,3]) 
print(f"array: {a}")

# more than one dimensions 
a = np.array([[1, 2], [3, 4]]) 
print(f"more than one dimension: {a}")

# minimum dimensions 
a = np.array([1, 2, 3, 4, 5], ndmin = 2) 
print(f"minimum dimensions: {a}")

# dtype parameter 
a = np.array([1, 2, 3], dtype = complex) 
print(f"dtype parameter: {a}")

############    dtype    ############
# using array-scalar type 
dt = np.dtype(np.int32) 
print(f"type: {dt}")

#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. 
dt = np.dtype('i4')
print(f"i4 type: {dt}")

# first create structured data type 
dt = np.dtype([('age',np.int8)]) 
print(f"structured type: {dt}")

# now apply it to ndarray object 
dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt)
#a = np.array([(10),(20),(30)], dtype = dt)
#a = np.array([('10'),('20'),('30')], dtype = dt)
#a = np.array([('OO'),(20),(30)], dtype = dt)
print(f"ndarray with structured type: {a}")
# file name can be used to access content of age column 
print(f"ndarray content: {a['age']}")
print(f"ndarray content: {a['age'][0]}")
