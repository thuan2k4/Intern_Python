#create a list
a = [1, 2, 3, 4, 5]

#List comprehension
even = [i for i in a if i % 2 == 0]
odd = [i for i in a if i % 2 != 0]

print(even)
print(odd)

#While loop
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        print(f"{a[i]} is even")
    else:
        print(f"{a[i]} is odd")
    i += 1

#Bubble Sort
b = [2,6,1,3,8,42,23]

for i in range(0, len(b)-1):
    for j in range(i + 1, len(b)):
        if (b[i] > b[j]):
            b[i], b[j] = b[j], b[i]

print(b)

#function sort
c = [5,12,53,2,1,3,6]
c.sort()
print(c)