import numpy as np
a=np.array([[1,2,3],[3,4,5],[4,5,6]]) ##Array initilization
print(a.shape) #Shape of the array

#Before slicing
print("Before slicing")
print(a)

#Print after slicing
print("after slicing")
print(a[1:])


print("Elemets in the second column are:")
print(a[...,1])

print("Elemets of the second row are:")
print(a[1,...])

print("Elemets after column 1 onwards:")
print(a[...,1:])