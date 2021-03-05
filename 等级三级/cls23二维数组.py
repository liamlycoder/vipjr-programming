a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)  # 打包为元组的列表
# print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]
zip2 = zip(a, c)  # 元素个数与最短的列表一致
# print(list(zip2))  # [(1, 4), (2, 5), (3, 6)]
# print(list(zip(*zipped)))


"""矩阵的操作"""
# a=[[0,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
a = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]


def printArr(arr):
    for line in arr:
        print(line)


def transpose(arr):
    lst = []
    for i in zip(*arr):
        lst.append(i)
    return lst


def invert(arr):
    lst = []
    for i in arr:
        lst.append(i[::-1])
    return lst


def tighten(row):
    new_row = []
    for i in row:
        if i != 0:
            new_row.append(i)
    n = []
    for i in range(len(row) - len(new_row)):
        n.append(0)
    new_row += n
    return new_row


def left(arr):
    lst = []
    for row in arr:
        lst.append(tighten(row))
    return lst


printArr(a)
print('-' * 88)
printArr(left(a))
