print('1.列表推导:')
print()
print('例子1:利用一个列表生成一个新的列表')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 有一个1到10的序列
squares = [x ** 2 for x in a]  # 利用列表推导快速生成一个新的list ** 平方
print(squares)

print('例子2:过滤一些列表中的元素')
# 取出序列中是2的倍数的元素,然后再取平方
new_list = [x ** 2 for x in range(1, 12) if x % 2 == 0]
print(new_list)

print('例子3：若需要对序列里面的内容进行循环处理时，也可以加一个函数进行组合完成')


def change(x, y):
    return '%d:%s' % (x, y)


seq = ['one', 'two', 'three', 'four']
print([change(x, y) for x, y in enumerate(seq)])

print('==========================================')
print('==========================================')

print('2.with用法:')
# 一般我们处理文件都是先打开->然后处理->然后关闭.比较麻烦，
# 还需要防止异常保护try/finally，
# 很多时候我们都把精力集中在如何处理文件这样会忘掉关闭文件.
# Python里面有一种非常简洁的方法:

# print('普通的打开，关闭文件处理:')
# filename = raw_input('Enter file name:')
# try:
#     f = open(filename,'r')
#     for eachline in f:
#         #do something
#         print()
# except IOError as e:
#     print('could not open file:',e)
# finally:
#     f.close()

#  print('使用with:')
#  filename = raw_input('Enter file name:')
#  with open(filename,'r')as f:
#      for each in f:
#          //do something
print('==========================================')
print('==========================================')
print('3.匿名函数lambda:')
# 以map()函数为例，
# 若要计算一个列表里面的每个元素的平方，
# 可以直接传入匿名函数：
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
map(lambda x: x * x, list)
print('==========================================')
print('==========================================')
print('4.生成器:')


# 生成器是python里面一个比较难理解的概念，
# 也是Python中引入的两个强大的特性之一
# （猜猜另外一个特性是啥，对了就是装饰器)
def fac1(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


for i, f in enumerate(fac1(10)):
    print(f)

print('用了生成器的函数:')


def fac2(n):
    a, b = 1, 1
    while a < n:
        yield a  # 注意关键字yield
        a, b = b, a + b


for i, f in enumerate(fac2(10)):
    print(f)
#如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，
# 而是一个生成器函数,打印看一下.
print(fac2(10))
#生成器函数和普通函数的执行流程非常不一样：
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成生成器的函数，只会相应迭代操作时才运行,一般都是配合for使用(也有配合sum(),list())
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。