from collections import OrderedDict

import itertools

print('1,字典排序:')

my_dict = {"cc": 100, "aa": 200, "bb": 10}
# 表示按照key排序
print(sorted(my_dict.items(), key=lambda x: x[0]))

# 表示按照value排序
print(sorted(my_dict.items(), key=lambda x: x[1]))

# 注意原始的my_dict本身顺序并没有变(不信你可以print看看),
# 排序是通过sorted()返回了一个新的字典
print(my_dict)
print('========================================')
print('========================================')

orderDict1 = OrderedDict()
orderDict1['a'] = 1
orderDict1['b'] = 2
orderDict1['c'] = 3
print(orderDict1)

orderDict2 = dict()
orderDict2['a'] = 1
orderDict2['b'] = 2
orderDict2['c'] = 3
orderDict2['a'] = 1
orderDict2['d'] = 1
orderDict2['e'] = 1
print(orderDict2)
print('========================================')
print('========================================')
print('2.字典的取值:')

# a.使用dict[key]取值,
# 若你取的值不存在，就会发生异常,风险很大
prices = {'apple': 10, 'orange': 5, 'banana': 8}
print(prices['apple'])
# print(prices['a'])

# 因为试图通过索引的方式去取值,比如dict[key],
# 当key不是字典dict的键，会引起异常，
# 有没有什么两全的办法有值的时候取值，
# 没有值的时候即使我取不到也不会发生异常
print(prices.get('a'))  # 当键值不存在时,会返回None,而不是异常

# get还有一个工厂方法,就是dict.get(key,somethingelse)
print(prices.get('apple', 'NOT FOUND'))
print(prices.get('a', 'NOT FOUND'))

# ps:尽量用dict.get()来代替dict[key]
print('========================================')
print('========================================')

print('3字典中提取部分子集:')
students_score = {'jack': 80, 'james': 91, 'leo': 100, 'sam': 60}
# 提取分数超过90分的学生信息，并变成字典
# 我们可以用字典推导式，轻松搞定
good_score = {name: score for name, score in students_score.items() if score > 90}
print(good_score)

print('========================================')
print('========================================')

print('4.字典的计算:')
#比如我们有一个字典是记录股票的价格呢，一般key都是股票的名字,而value是价格，
# 若我们想对价格进行计算，应该如何处理呢,我们还是通过实例来讲解：
#下面是一个股票价格的字典，我们希望得到里面的最大值，最小值

stocks={'wanke':25.6,'wuliangye':32.3,'maotai':299.5,'huatai':18.6}

#a,利用字典的values():
print(min(stocks.values()))
print(max(stocks.values()))

#b,利用神奇的zip()进行翻转
new_stocks = zip(stocks.values(),stocks.keys())
print(type(new_stocks))#zip()翻转keys,values,然后变成一个列表py2
print(max(new_stocks))
new_stocks = zip(stocks.values(),stocks.keys())
print(min(new_stocks))

print('========================================')
print('========================================')

print('5.字典翻转:')
# 在处理复杂的数据结构的时候，
# 有的时候希望把字典翻转,一般用推导列表进行过渡，
# 然后再用dict()函数编程字典

stocks={'wanke':25.6,'wuliangye':32.3,'maotai':299.5,'huatai':18.6}
invert_stocks = dict([(v,k)for k,v in stocks.items()])
print(invert_stocks)

# 若碰到比较大的字典，数据量很多很长的时候，
# 最好用Python标准库里的itertools模块
# (顺便说一下,这个模块非常有用，大家可以关注一下)
#from itertools import zip
invert_stocks2=dict(itertools.zip(stocks.itervalues(),stocks.iterkeys()))
print(invert_stocks2)


