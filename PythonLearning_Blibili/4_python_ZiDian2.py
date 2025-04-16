print("可查询成绩的学生名单:小明，小红，小亮。")
accomplishment=dict
var = {"小明":{"语文": 85, "数学": 96, "英语": 88},"小红":{"语文":72,"数学":80,"英语":91},"小亮":{"语文":83,"数学":69,"英语":75}}
n=int(input('请输入需要查询成绩的学生数量'))
sum_number=0
for i in range(0, n):
    name=input("请输入查询成绩的学生%d姓名："%(i+1))
    chengji=input("请输入查询成绩的科目%d名称："%(i+1))
    if chengji in accomplishment:
        sum_number += accomplishment[chengji]*1
print('总成绩为%d' % sum_number)