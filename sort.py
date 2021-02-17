li = [2,5,3,1,4]
li.sort()
print (li)
print(sorted(li))


li = li * 2
print(li)
li.append( [3,4] )
print(li)

for i in li:
    print(i)


li = [1,2]
li.extend( [3,4])
print(li)



for n, value in enumerate(li):
    print(str(n) + " "  + str(value))
    

a = 154 + 553
print(a)
