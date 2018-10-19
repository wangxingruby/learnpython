print("hello python");

print('\taha\nintresting');

list = ['ab','cd','ef']

for l in list:
    print(l)

print('\n');
list[0] = 'gh';
list.append('ij'); #list末尾加元素
list.insert(1,'kl');


for l in list:
    print(l)
print('\n');
del list[4];

for l in list:
    print(l)
#list.pop删除末尾元素并取出末尾元素
#list.sort() 排序  list.sort(reverse=True) 逆向排序 sorted(临时排序)
#reverse(list) 逆序



def hello():
    print('hello')

hello()

#位置实参顺序很重要，可以用关键字实参

# x与y 数值转换，x,y = y,x

#python 中的进制转换，
# 0b10代表二进制数，对应十进制的2
# 0b11代表二进制数，对应十进制的3

# 0o10代表八进制数，对应十进制的8
# 0o10代表八进制数，对应十进制的9

# 0x10代表十六进制数，对应十进制的16
# 0x11代表十六进制数，对应十进制的17

# 使用bin()方法来将任意进制转换为二进制
# 使用oct()方法来将任意进制转换为八进制
# 使用int()方法来将任意进制转换为十进制
# 使用hex()方法来将任意进制转换为十六进制
# 使用bool()方法来将任意进制转换为布尔类型
               
# tuple 	 元组，数组
# dict 	字典，词典
# number：int float bool
# str
# 在字符串外面加一个 r ，它就不是普通字符串，它是原始字符串
# set 集合，两个集合元素相同顺序不同用==来运算，等于True

# 算数运算符
# 赋值运算符
# 比较（关系）运算符
# 逻辑运算符 and or not 
# 成员运算符 in、 not in
# 身份运算符 is、 is Not
# 位运算符
# 符
