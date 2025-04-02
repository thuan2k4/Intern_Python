#function
a = 10
b = 20
print(a + b)

def add(a, b):
    return a+b

print(add(1,2))
print(add(3,4))
print(add(5,6))

#function with Pass by Value
def PV(a,b,c,d):
    a = 10
    b = 1.1
    c = "World"
    d = (6,7,8,9)
    print(a,b,c,d)

a = 1
b = 2
c = "Hello"
d = (1,2,3,4)
PV(a,b,c,d)
print(a,b,c,d)

#function with Pass of Reference
def PR(a,b,c):
    a.append(10)
    b["a"] = 111
    c.append(11)

a = [1,2,3,4,5]
b = {"a":1,"b":2,"c":3}
c = [6,7,8,9,10]
PR(a,b,c)
print(a,b,c)

#Try_except
try:
    a = int(input())
    b = int(input())
    print(add(a,b))
except:
    print("Invalid input")

#Debugging (use breakpoint)
k = input()
l = int(input())
print(k,l)