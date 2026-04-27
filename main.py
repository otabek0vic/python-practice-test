print("hello world !")

tuple1 = (213, 123, 12.3, True, 87)
print(tuple1)
print(tuple1[1])
print(tuple1[2:4])
print(tuple1[:4])
print(tuple1[4:])
print(tuple1[2:4:2])
print(tuple1[-1])
# print(tuple1[99]) #errorrrrrr
print(tuple1[::-1])
print(sorted(tuple1))

if 2123 in tuple1:
    print("Oh yeah ")
else:
    print("Nope nothing similar !")

for i in tuple1:
    print(i)

import os
os.system("cls")


# tuple1 = ('olma', 'anor', 'gilos', 'banan', 'uzum',)
# tuple2 = ('ALi', 'Vali', 'Xasan', 'Xusan')
# tuple3 = tuple1 + tuple2
# print(tuple3)

sonlar = (1,2,3,4,5,6,7,8,9)
# a = sonlar[0]
# b = sonlar[1]
# c = sonlar[2]
a,b,*c = sonlar
print(a,b,c)

print(len(sonlar))

sonlar = (1,2,3,4,5,6,7,8,9,'salom', 'hello','bonjur')

print(len(sonlar))

s = 'Hello'
print(len(s))
