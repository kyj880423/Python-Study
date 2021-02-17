x = 100
if x > 0:
    print('wow this is elegant')
else:
    print('Oranization is the key.')


print('hello ' + ' ' + 'world')


def my_function(a='zz'):
    print(a)

my_function()


class my_class:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        print('초기화 함수 ')

    def mul(self):
        print(self.x * self.y)

    def add(self):
        print(self.x + self.y)


ob1 = my_class(7,8)
ob1.mul()

ob1.add()

decimalValue = 10
stringValue = "10"
floatValue = 10.0

print ('String of text goes here %d %s %f' % (decimalValue, stringValue, floatValue))


x = 3
y = 0
try:
    print('로켓의 궤도 : %f' % (x/y))
except Exception as ex:
    print(ex.__str__() )



print(range(1,5))


items = [1,2,3,4,5, 10]
for item in items:
    print(item)
items.append(11)

print(items)

items = [ y**2 for y in range(1,10)]
print(items)

pairs = []
A = ['blue', 'yellow', 'red']
B = ['red', 'green', 'blue']

for a in A:
    for b in B:
        if a != b:
            pairs.append((a,b))
print (pairs)


pairs = []
pairs = [(a,b) for a in A for b in B if a!=b]
print(pairs)


a = {x for x in 'abracatabra' if x not in 'abc'}
print(a)

print("###############################################")
alpa = 2

for a in range(1,10):
    print("%d x %d = %d" % (alpa , a , (alpa*a)) )


print('###############################################')
print('abcdefg'.upper())
print("%s %s %s" % (ord('a'), ord('b'), ord('c')))


print("########################################")
str = "abcde"
newStr = ""
for a in range(len(str) - 1,  -1 , -1):
    newStr += str[a]
print("print newStr : %s " %  (newStr))


books = [ {
    "제목":"개발자의 코드",
    "출판연도": "2013.02.28",
    "출판사":"A",
    "쪽수":200,
    "추천유무":False
},  {
    "제목":"클린코드",
    "출판연도": "2010.03.04",
    "출판사":"B",
    "쪽수":584,
    "추천유무":True
}, {
    "제목":"빅데이터 마케팅",
    "출판연도": "2014.07.10",
    "출판사":"A",
    "쪽수":296,
    "추천유무":True
},
]

print("############################################")
many_page = []
my_recommand = []
for book in books:
    if book["쪽수"] > 250:
        many_page.append(book)

    if book["추천유무"]:
        my_recommand.append(book)

print(many_page)
print(my_recommand)
