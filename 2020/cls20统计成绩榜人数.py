# 上节课作业：
# 选择排序
numbers = [64, 25, 12, 22, 11]

for i in range(len(numbers)):

    min_idx = i
    for j in range(i + 1, len(numbers)):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print("排序后的数组：")
for i in range(len(numbers)):
    print("%d" % numbers[i]),


import random

score = [random.randint(0, 100) for _ in range(50)]

print("分数列表：")
print(score)

print("="*44)

# c = 0
# for i in score:
#     if i == 89:
#         c += 1
# print("成绩为89分的同学一共有{}人".format(score.count(89)))

for i in range(101):
    if i in score:
        print("分数为{}的学生有{}人".format(i, score.count(i)))

print("="*44)

score.sort(reverse=True)
print(score[1:4])

print("="*44)

ok = 0
for i in score:
    if i >= 60:
        ok += 1
print("及格的人数为{}，不及格的人数为{}".format(ok, 50-ok))

print("="*44)

# count_table = []
# for i in range(101):
#     count_table.append(score.count(i))
count_table = [score.count(i) for i in range(101)]
print("得{}分的人数是最多的".format(count_table.index(max(count_table))))

