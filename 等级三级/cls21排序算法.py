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


a = [324, 2314, 534, 23, 7654, 2]
shellSort(a)
print(a)
