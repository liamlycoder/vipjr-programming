hobby1 = {"玩游戏", "看电视", "听音乐"}
hobby2 = {"唱歌", "购物", "看电视"}
hobby3 = {"玩游戏", "听音乐"}

# print(hobby1 | hobby2)
# print(hobby1 & hobby2)
# print(hobby1 ^ hobby2)
# print(hobby1 - hobby2)

lst = [
    {'姓名': "兰陵王", "爱好": hobby1},
    {"姓名": "东皇太一", "爱好": hobby2},
    {'姓名': "钢铁侠", "爱好": hobby3}
]

for i in range(len(lst) - 1):
    for j in range(i+1, len(lst)):
        if lst[i]['爱好'] & lst[j]['爱好']:
            print("{}和{}会成为好朋友".format(lst[i]['姓名'], lst[j]['姓名']))


