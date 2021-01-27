teleBook = {
    "张三丰": 19999997777,
    "李白": 18877776666,
    "周杰伦": 12233334444,
    "蔡徐坤": 19877778873
}

print("************************************")
print("**************我的通讯录**************")
print("************************************")

print("""请输入指令：
        1 - 查找
        2 - 新增
        3 - 修改
        4 - 删除
        5 - 查看全部
        6 - 查看指令
        q - 退出""")

while True:
    cmd = input("->")
    if cmd == 'q':
        break
    if cmd == '1':
        name = input("请输入姓名:")
        print("您要找的电话是：{}".format(teleBook[name]))
    elif cmd == '2':
        name = input("请输入姓名：")
        tele = input("请输入电话:")
        teleBook[name] = tele
        print('添加成功')
    elif cmd == '3':
        name = input("请输入您要修改的姓名：")
        tele = input("你希望将其电话修改为：")
        teleBook[name] = tele
        print("修改成功")
    elif cmd == '4':
        name = input("请输入您想删除的姓名：")
        teleBook.pop(name)
        print('删除成功')
    elif cmd == '5':
        for i, j in teleBook.items():
            print("姓名：{} - 电话：{}".format(i, j))
    elif cmd == '6':
        print("""请输入指令：
        1 - 查找
        2 - 新增
        3 - 修改
        4 - 删除
        5 - 查看全部
        6 - 查看指令
        q - 退出""")
    print("="*88)
