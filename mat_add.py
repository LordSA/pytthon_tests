import numpy as np
def arr(x,y):
    l = []
    for i in range(a*b):
       l.append(int(input("Enter the no : ")))
    ar = np.array(l)
    a1 = ar.reshape(a,b)
    return a1

a = int(input("Enter the raw : "))
b = int(input("Enter the column : "))
c = int(input("Enter the raw : "))
d = int(input("Enter the column : "))
if a==c and b==d:
  print(f'MAtrix 1 with {a},{b}')
  l1 = arr(a,b)
  print(f'MAtrix 2 with {c},{d}')
  l2 = arr(c,d)
sum = np.add(l1,l2)
print(sum)
