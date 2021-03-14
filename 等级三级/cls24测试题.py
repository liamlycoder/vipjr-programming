import csv
from random import randint

valid = ''
for i in range(4):
    num = randint(0, 9)
    valid += str(num)

# print(valid)

# with open('test.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow([valid])

def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:
        mid = l + (r - l) // 2
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # 不存在
        return -1

nums = [12, 4, 1, 5, 8, 3, 9, 7, 2, 1]
nums.sort()
res = binarySearch(nums, 0, len(nums) - 1, 5)
if res != -1:
    print("数字5的索引为：", res)
else:
    print('该数字不存在')
binNums = [bin(i) for i in nums]
print(binNums)
with open("test.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(binNums)







