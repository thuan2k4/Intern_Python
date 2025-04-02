#If, elif, else
a = 10
if a < 10:
    print("a is less than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is greater than 10")

#For, While Loop
for i in range(1, 11):
    print(i)

while a < 10:
    print(a)
    a += 1

#List
n = [1, 2, 3, 4, 5]
for i in range(len(n)):
    print(n[i])

#for each loop
for i in n:
    print(i)

#List comprehension (create a list)
string = "Hello World!"
a = [string[i] for i in range(len(string)) if i % 2 ==0]
print(a)

square = [i**2 for i in range(1, 11)]
print(square)

