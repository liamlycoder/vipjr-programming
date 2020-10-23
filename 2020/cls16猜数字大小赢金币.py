# !/usr/bin/python
# coding: utf8
# Time: 2020/10/23 19:28
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import random

number = random.randint(1, 25)

for i in range(5):
    guess = int(input("猜猜看："))
    if guess == number:
        print("恭喜你，猜对了，获得一枚金币")
        break
    elif guess > number:
        print("很遗憾，猜大了。您还有{}次机会。".format(5-i-1))
    else:
        print("很遗憾，猜小了。您还有{}次机会。".format(5-i-1))
