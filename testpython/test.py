isinstance(1, (str, int,))

print(bool(3.4))

print(3/2)
print(3//2)

print(3%2)

print(int(0o11))

type(1 * 1.0)


bool(1)
bool(0)
print(bin(0xe))

print('Hello' * 3)

s = 'Hello World'
print(s[-2])

str()

type(4/2)

'Hello ''World'

type(1+1)


{'a': 1, 'b': 2}.get('d', 4)

['hello']*3


type({})

4 in [1,2,3]


{'a': 1, 'b': 2}['a']


type((1, 2))


[1,2,3] + [3,4]


{1, 2, 3, 4} | {4, 5, 6}

t = (1, 2, 4, 5)

set('boy')

set([1,2,3,4])


(1, 2, 3) * 2

type((1,2))

len([1, 2, 3])

{'a': 1, 'b': 2}.get('c',2)

a = {'a': 1, 'b': 2}.get('c')
print(a)
type([1, 2])


['Hello'] + ['World']


{1, 2, 3, 4} - {4, 5, 6}


(1, 2, 3) + (4, 5)

'hello world'[6]

'hello world'[6:6]

'hello world'[6:-1]
'hello world'[6:]

'Hello World'[0:4]

'Hello World'[0:-1]
bin(0xE)
s = 'Hello World'
s[1:5]

'Hello ''World'

['Hello', 'World', 1, 2][0][2]

{1, 2, 3, 4} & {4, 5, 6}

type(('Hello','f'))

l = [1, 2, 4, 5]
l[2] = 3
print(l)


type((1,3,))


type([1])

s = []
type(s)
s = {}
type(s)
s = ()
type(())

type([[1, 2], [3, 4], [True, False]])
0xa & 0o7


[1, 2] + [3, 4]


(1, 2, 3) == (1, 2, 3)




{1, 2, 3} == {2, 3, 1}

2 and 1
'a' > 'b'

isinstance(1, (str, int,))



int(0xa << 2)

import keyword
keyword.kwlist

a = 1
a += 2
print(a)

1 or 2



3 ** 2

b = 2
b+=b>=1
print(b)


str_1 = '1234468723456745'
print(str_1.isdigit())


a, b, m = 10, 3, 5
if a == b:
    m += a
else:
    m *= a
print(m)


def calculatemoney(seconds):
    minites = seconds//60
    sec = seconds%60
    if sec > 0:
        minites+=1

    if minites <=3:
        money = 0.2
    else:
        money = 0.2 + (minites-3)*0.1
    return money 


calculatemoney(seconds = 300)


def daysInMonth(month):
    day31 = ('1','3','5','7','8','10','12')
    day28 = ('2')
    day30 = ('4','6','9','11')

    if month in day28:
        day = 28
    elif month in day30:
        day = 30
    elif month in day31:
        day = 31
    else:
        day = 0
    return day

daysInMonth(month = '5')


def isNumber():
    inp = None
    while inp is None or not inp.isdigit():
        print('请输入一个数字')
        inp = input()

    inp = int(inp)
    if inp%3 == 0 and inp//3 > 0:
        print(inp**2)
    else:
        print(inp**3)

isNumber()


def countDiagonal():
    list = [[1,2,3],[4,5,6],[7,8,9]]
    count = 0
    for i in range(0,3,1):
        for j in range(0,3,1):
            if i == j:
                count += list[i][j]
    print(count)

countDiagonal()


def isLeapYear():
    inp = None
    while inp is None or not inp.isdigit():
        print('请输入一个年份')
        inp = input()
    inp = int(inp)
    if inp%100 == 0 and inp%400 == 0:
        print(str(inp) + '这一年是闰年')
    elif inp%100 != 0 and inp%4 == 0:
        print(str(inp) + '这一年是闰年')
    else:
        print(str(inp) + '这一年不是闰年')

isLeapYear()


def canbedivisionedBy3and7():
    print('请输入一个数字')
    inp = input()
    if not inp.isdigit():
        print('输入的 ' + inp + ' 非数字')
    elif int(inp)<= 0:
        print('输入的 ' + inp + ' 非正数')
    elif int(inp)%3 == 0 and int(inp)%7 == 0:
        print('输入的 ' + inp + ' 可以被3和7整除')
    else:
        print('输入的 ' + inp + ' 不能被3和7整除')

canbedivisionedBy3and7()


num = 10
def fun():
    num = 2
    num += 3
fun()
print(num)




def fun1():
    global num
    num = 2
    num += 3
    
fun1()
print(num)

# 生成随机数，并且
import random
def randomNbr():
    list = []
    for i in range(0,1000,1):
        list.append(random.randint(0, 100))
    map = {}
    for l in list:
        if map.__contains__(l):
            map[l] = map.get(l)+1
        else:
            map[l] = 1
    print(list)
    print(map)

randomNbr()

# 10的阶乘

resultvalue = 1
for i in range(1,11,1):
    resultvalue *= i
print(resultvalue)

# 计算1到1000内所有的奇数求和输出
resultvalue = 0
for i in range(1,1001,2):
    print(i)
    resultvalue += i 
print(resultvalue)

#1到1000以内能同时被3,5,7同时整除的数

result = 0
temporary = 3*5*7
print(temporary)
while temporary < 1000:
    result += temporary
    temporary *=2
print( result)

#字符串按单词逆序
st0= 'I am a boy'
lis = st0.split(' ')
lis.reverse()
print(' '.join(lis))

#一行一个*输出10行

for i in range(1,11,1):
    print('*'*i)

#截取列表的前两个元素返回给使用者

def spllist(list):
    if len(list) > 2:
        return list[0:2]

spllist([1,2,3,4,6,3,5,3])


#斐波那契数列

def fibonacci(nbr1,nbr2,rangenow,rangemax):
    nbr1,nbr2 = nbr2,nbr1
    nbr2 = nbr1 +nbr2
    print(nbr2)
    if rangenow < rangemax:
        return fibonacci(nbr1,nbr2,rangenow+1,rangemax)
    else:
        return nbr2

fibonacci(1,1,3,10)

# 水仙花数
for i in range(100,1000,1):
    hundred = i//100
    ten = i//10%10
    one = i%10
    if i == hundred**3+ten**3+one**3:
        print(i)

def sizeBiggerThan5(list):
    return len(list)>5

# 求是不是质数
import math
def isPrimeNumber(nbr):
    if nbr < 1:
        return '输入错误'
    counts = 0
    a = int(math.sqrt(nbr))+1
    print(a) 
    for i in range(2,a,1):
        if nbr//i > 0 and nbr%i == 0:
            counts +=1
    if counts>=1:
        return '不是质数'
    else:
        return '是质数'

isPrimeNumber(8)


print(int((1+100)*(100-1+1)/2))

import random
list =[]
for i in range(1,51,1):
    list.append(random.randint(0,10000))
print(list)
for l in list:
    if l%2 == 1:
        list.remove(l)
print(list)


import random
money = 1000
i = 1
while money > 0 and money <= 10000:
    i+=1
    print('这是第'+str(i)+'局')
    bets = random.randint(0,101)
    if money < bets:
        bets = money
    print('下注'+ str(bets))
    dice = random.randint(0,7)
    if dice > 3:
        print('这一局赢了')
        money+=bets
    else:
        print('这一局输了')
        money-=bets
    print('当前赌金')    
    print(money)
print(money)
    
add=lambda x, y: x+y

type([1])

def factorial1(max,resvalue):
    print( resvalue)
    if max > 1:
        return factorial1(max-1,resvalue*max)
    else:
        return resvalue

factorial1(10,1)
    
#有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数。
def changeOrder(list ,m):
    n = len(list)
    if n <= m:
        return list
    else:
        return list[-m:]+list[0:n-m]

changeOrder([1,2,3,4,5],3)


# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def reverseStr(str1):
    if len(str1)>1:
        str2 = str1[1:]
        return reverseStr(str2) +str1[0]
    else:
        return str1

reverseStr('abcde')
    


# 求是不是质数
import math
def isPrimeNumber2(nbr):
    counts = 0
    a = int(math.sqrt(nbr))+1
    for i in range(2,a,1):
        if nbr//i > 0 and nbr%i == 0:
            counts +=1
    if counts>=1:
        return 1
    else:
        return 0

def findPrimeNumber(max):
    list = [2]
    for i in range(3,max,2):
        if isPrimeNumber2(i) == 0:
            list.append(i)
    return( list)

print(findPrimeNumber(1000))



def mathSortRoad(twoDimensionList):
    siz = len(twoDimensionList)
    list1 = []
    list1.append({'x':0,'y':0,'value':twoDimensionList[0][0]})
    for i in range(0,siz*2,1):
        list2 = []
        for obj in list1:
            if obj.get('x') < siz:
                obj1={}
                obj1['x'] = obj.get('x')+1
                obj1['y'] = obj.get('y')
                obj1['value'] = obj.get('value')+twoDimensionList[obj1.get('x')][obj1.get('y')]
                list2.append(obj1)
            if obj.get('y') < siz:
                obj2={}
                obj2['x'] = obj.get('x')
                obj2['y'] = obj.get('y')+1
                obj2['value'] = obj.get('value')+twoDimensionList[obj1.get('x')][obj1.get('y')]
                list2.append(obj1)

        list1 = list2
    print(list1)


mathSortRoad([[1,2,3],[4,5,6],[7,8,9]])

    

