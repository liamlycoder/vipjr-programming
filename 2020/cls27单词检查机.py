# Time: 2020/3/14 20:16
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
# 下面的needCheck为一个状态标志，用来表示是否需要复习的状态；如果值为"y"表示需要复习，如果值为"n"表示不需要复习。
needCheck = 'y'
wordBook = {'red': '红色', 'desk': '桌子', 'food': '食物'}   # 生词本

# 下面这样写的错误在哪里？
# while needCheck == 'y':
#     for i in wordBook.keys():
#         print(i + '是什么意思？')
#         yourAnswer = input('回答：\n')
#         if yourAnswer == wordBook[i]:
#             del wordBook[i]
#             print('回答正确')
#         else:
#             print('回答错误')
#     if len(wordBook.keys()) == 0:
#         print('恭喜你，全部复习完了')
#         needCheck = 'n'
#     else:
#         needCheck = input(' '.join(wordBook.keys()) + '这些单词还需要再巩固一下嘛？y/n：\n')

while needCheck == 'y':
    checkBook = wordBook.copy()   # 复制一份单词本
    for i in checkBook.keys():
        print(i + '是什么意思？')
        yourAnswer = input('回答：\n')
        if yourAnswer == checkBook[i]:
            print('回答正确')
            del wordBook[i]
        else:
            print('回答错误')

    if len(wordBook.keys()) == 0:
        needCheck = 'n'
        print('恭喜你，全部复习完啦')
    else:
        needCheck = input(' '.join(wordBook.keys()) + '这些单词还需要再巩固一下嘛？')
