student_dict = [{'name': 'xiaoming','yuwen': 85,'shuxue': 96,'waiyu':88},{'name': 'xiaohong','yuwen': 72,'shuxue': 80,'waiyu':91},{'name': 'xiaoliang','yuwen': 83,'shuxue': 69,'waiyu':90}]
max_score = 0
max_score_student_name = ''
for student_info in student_dict:
    score = student_info['yuwen'] + student_info['shuxue'] + student_info['waiyu']
if score > max_score:
    max_score = score
max_score_student_name = student_info['name']
print(f'总分最高的是{max_score_student_name},分数为{max_score}')