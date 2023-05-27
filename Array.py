import array as arr
a = arr.array('i', [1, 2, 3, 4])
print("The Integar Array is: ",end=" ")
for i in range(0, 4):
    print (a[i],end=" ")
print() 
b = arr.array('d', [2.5, 3.2, 3.3,5.6])
print("The float Array is: ",end=" ")
for d in range(0, 4):
    print (b[d],end=" ")
#ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
