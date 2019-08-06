'''def f(x):
    return 2*x+3
print f(2)
print(3+4*6)
print f(f(6))
v=89
print f(v)

Task 1

def greater(x,y):
    if x>y:
        return x
    else:
        return y

x=float(raw_input("Enter your first number: "))
y=float(raw_input("Enter your second number: "))

print greater(x,y)

Task 2
def echo():
    x= raw_input("Enter a string: ")
    return x + x

print echo()'''

'Task 3'

'''def Display3(x,y,z):
    v = x*y*z + 3
    print v
Display3(2,3,4)''' 

'''l = []
k = list()
j = [1,2,3,4,5,6,7,8,9,10]

print "The lists after clear is called on j"
print "l =", l
print "k =", k
print "j =", j

l.append('a')
k.append('t')
j.append(k)

print "The lists after an append"
print "l =", l
print "k =", k
print "j =", j

l.insert(0,'c')
k.insert(0,'h')
j.insert(5,12)

print "The lists after an insert"
print "l =", l
print "k =", k
print "j =", j

l =[2,3,6,7,8]
k =[4,1,5,12,13]

print "\nThe index of 5 in each list"
#print "l =", l
print "k =", k.index(5)
print "j =", j.index(5)

#Counting to 10 from 1
i = 1
while i <=10:
    print i
    i += 1

#Counting to 20 from 1
i = 1
while i <=20:
    print i
    i += 1

#Counting to 20 from 1, only EVEN numbers 
i = 1
while i <=10:
    if i % 2 == 0:
        print i
    i += 1

#Counting to 20 from 1, only ODD numbers 
i = 1
while i <=10:
    if i % 2 == 1:
        print i
    i += 1

v = ""
while v != "hello":
    v = raw_input("Enter a string: ")'''

'''for i in range(1,10):
    print i
for i in range(1,21):
    print i
for i in range(2,21,2):
    print i
for i in range(1,21):
    if i % 2 == 0:
        print i
for i in range(1,21):
    if i % 2 == 1:
        print i
for i in "This is a string":
    print i

h = []

for i in range(20):
    h.append(0)
print h, len(h)

h[1]=1

for i in range(2,20):
    h[i] = h[i-1]
print h    

d={}
b=dict()
a= {1:2,2:1,3:3,4:5,5:4}
c= {12:"Bob",89:"Jane"}

print a[1]

print c[89]

c[72]="Joe"

print c'''

class Person:
    def __init__(self,name):
        self.name = name
        self.age = 0
    def birthday(self):
        self.age += 1

t= Person("Jane")
print t.name, t.age
s= Person("Roger")
print s.name,s.age

t.birthday()
print t.name, t.age 