def digui(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return n * digui(n-1)

number = int(input("请输入一个正整数:"))
result = digui(number)
print("%d 的阶乘是 : %d" % (number,result))
