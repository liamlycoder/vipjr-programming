city = ["北京", "上海", "广州", "深圳"]


# with open("data.csv", "w", encoding="utf-8") as f:
#     content = ",".join(city) + "\n"
#     f.write(content)
#
# with open("data.csv", "r") as f:
#     content = f.read().strip("\n").split(",")
#     print(content)

"""二维数据"""
score = [
    ["孙悟空", "100", "100", "99", "23"],
    ["兰陵王", "45", "67", "34", "92"],
    ["孙尚香", "87", "34", "25", "77"]
]
# with open("data.csv", "w", encoding="gbk") as f:
#     for row in score:
#         line = ",".join(row) + "\n"
#         f.write(line)

score2 = []
with open("data.csv", "r", encoding="gbk") as f:
    for row in f:
        score2.append(row.strip("\n").split(","))
print(score2)

