# 选择法排序
"""
选择排序的不稳定例子很简单。
比如A 80 B 80 C 70 这三个卷子从小到大排序
第一步会把C和A做交换 变成C B A
第二步和第三步不需要再做交换了。所以排序完是C B A
但是稳定的排序应该是C A B
但是选择法排序可以实现为稳定的排序，但是非常复杂
"""


# 插入法排序
def insertionSort(arr):
    for i in range(1, len(arr)):
        num = arr[i]
        j = i - 1
        while j >= 0 and num < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num


"""
时间复杂度：O(n**2)
空间复杂度：O(1)
稳定性：稳定
优点：在已经有序的情况下，复杂度为O(n)
"""


# 希尔排序
def shellSort(arr):
    n = len(arr)
    gap = n // 2
    # gap变化到0之前，插入算法执行的次数
    while gap > 0:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap, n):
            # j=[gap,gap+1,gap+2,gap+3.....,n-1]
            i = j
            while i > 0 and arr[i] < arr[i - gap]:
                arr[i], arr[i - gap] = arr[i - gap], arr[i]
                i -= gap
        # 缩短gap步长
        gap //= 2


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # 创建临时数组
    L = [0] * n1
    R = [0] * n2

    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # 归并临时数组到 arr[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # 拷贝 L[] 的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # 拷贝 R[] 的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def _mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        _mergeSort(arr, l, m)
        _mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def mergeSort(arr):
    l, r = 0, len(arr) - 1
    _mergeSort(arr, l, r)
"""
时间复杂度：O(nlogn)
空间复杂度：O(n)
稳定性：稳定
"""

def quickSort(arr, low, high):
    if low < high:
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
"""
时间复杂度：O(nlogn)
空间复杂度：O(logn)-O(n)
稳定性：不稳定
"""


a = [324, 2314, 534, 23, 7654, 2]
quickSort(a, 0, len(a) - 1)
print(a)
