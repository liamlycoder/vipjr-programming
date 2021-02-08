lstNum = [12, 2, 45, 2, 678, 5, 34, 7]

"""
求和
"""


def sum(lst, l):
    if l == 1:
        return lst[0]
    num1 = lst.pop()
    return sum(lst, len(lst)) + num1


"""
求阶乘
"""


def jc(n):
    if n == 1:
        return 1
    return jc(n - 1) * n

# 汉诺塔
def hanoi(n, x, y, z):
    if n == 1:
        print(x, "--->", z)
    else:
        hanoi(n - 1, x, z, y)
        print(x, "--->", z)
        hanoi(n - 1, y, x, z)

# print(sum(lstNum, len(lstNum)))
print(jc(5))
