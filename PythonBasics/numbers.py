#Addtion
print(2+4)

#Substraction
print(10-5)

#Multiplication
print(10*8)

#Division
print(10/5)

#String 

print("ksdfjv")
print("jjddkklldc")

for i in range(6):
    print(i)
s ="string"
print(s[0])

print(s[2:])
print(s[::-1])




p = "abcde"
s = " "
for i in p:
    print(type(i))
    s = i + s
print(s)

s = "Highlighted is the new {}".format("String")
print(s)

print("{2} {0} {1}".format("quick","brown","fox"))

print(f"the is {p}")

o = "OpPosite"
print(f"What is {o} ?")

print("I like %s" ).'%Apple'

mydict = {"Game":"CR","Food":"pizza"}
print(mydict["Game"])

mydict['K3'] = "df"
print(mydict)
mydict.values()

r = (1,2,3,5,6,2,3)
print(type(t))
len(t)

t.count(2)
list = [1,2,3,4,5,2,3]
for i in list

x = set(list)
print(x)



myfile = open('C:\\Users\\HP\\Desktop\\Python_course\\new.txt')
myfile.read()
myfile.seek(0)
myfile.read()

with open('C:\\Users\\HP\\Desktop\\Python_course\\new.txt',mode = 'r') as f:
    print(f.read())

with open('C:\\Users\\HP\\Desktop\\Python_course\\new.txt',mode = 'a') as f:
    f.write('\n this is a new line')

    
with open('C:\\Users\\HP\\Desktop\\Python_course\\newwww.txt',mode = 'w') as f:
    f.write('I created this file')



print('h'<'i')

print(2<4>5)

help(list.insert)

mylist = range(4) 

seclist = [0,1,2,3]
print (seclist)

mylist.append(4)
print (seclist)
seclist = mylist[:]
print (seclist)
mylist.append(5)
print (seclist)

def f(n):
  for x in range(n):
    yield x**3

for x in f(6):
  print(x)


c=input()
n=c.count("e",0,len(c)) 
if n==2:
  print("True")
else:
  print("False")

















counter = 1
def dolots(count):
    global counter
    for i in (1, 2, 3):
        counter = count + i

print(dolots(4))
print(counter)

filename = open('C:\\Users\\HP\\Desktop\\Python_course\\new.txt')
writefile = open('C:\\Users\\HP\\Desktop\\Python_course\\output.txt.txt','w')


words = 0
charecter = 0
i=1
for line in filename:
    charecter=len(line)
    words=len(line.split())
    print("line %d contains %d charcters and %d words "%(i,charecter,words))
    writefile.write("line %d contains %d charcters and %d words "%(i,charecter,words))
    i=i+1

filename.close()
writefile.close()




l1 = [1,2,30,42,5]
l2 = [6,7,81,92,10]
l3 = [11,112,123,14,15]

l1.sort()
l2.sort()
l3.sort()
maxlist = [l1[-1],l1[-2],l2[-1],l2[-2],l3[-1],l3[-2]]
print(maxlist)

minlist = [l1[0],l1[1],l2[0],l2[1],l3[0],l3[1]]
print(minlist)

Maxaverage = sum(maxlist)/len(maxlist)
print(Maxaverage)

Minaverage = sum(minlist)/len(minlist)
print(Minaverage)

Sample = [1,2,3,4,2,4,1,6,7,89,90]
lists = set(Sample)
print(lists)


import os
path  = input("Enter the path to check empty file")
filelist = os.listdir(path)
print("\n the list of files in %s  is %s" %(path,filelist))
 for file in filelist:
   if os.path.isfile(file) and os.path.getsize(file) == 0:
     print("the file is 0 bytes"%file)



import xml.etree.ElementTree as ET 
bookstore= ET.parse("C:\\Users\\HP\\Desktop\\Python_course\\test.xml")
root = bookstore.getroot()

for book in root:
  print("category :%s"%book.attrib['category'])
  category=book.attrib['category']
  for vals in book:
    print("%s :%s "% (vals.tag.title(),vals.text.title()))







import socket
import struct
host_bits = 32 - int(16)
netmask = socket.inet_ntoa(struct.pack("!I", (1 << 32) - (1 << host_bits)))
print(netmask) 

import math
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return(x/y)
def sqroot(x):
    return math.sqrt(x)



print(add(3,4))





















































