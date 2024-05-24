print("Student grade\n")
student_list = {'Hary' : 90 ,
                'Mixy' : 80 ,
                'Shinchan' : 60 ,
                'Himavari' : 40}

student_grade={}
for student in student_list: #iterate through key
    score = student_list[student] #value of key
    #print(score)
    if score >=90:
        student_grade[student] = "Outstanding" #assigning key and value to new dictionary
    elif score <=50:
        student_grade[student] = "Poor"
    else:
        student_grade[student] = "Average"
    #print(student_grade[student])

print(student_grade)
