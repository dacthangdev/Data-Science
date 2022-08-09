# used when file data have date of birth or age

with open("clean_data_test.csv",encoding="utf8") as file: 
    datas = file.read().split('\n')
header = datas[0]
students = datas[1:]

total_student = len(students)

# split header

header = header.split(',')
subject = header[2:]

for i in range(total_student):
    students[i] = students[i].split(',')


# remove empty list (end of file)
students.pop()

# get number of student per age group
num_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
average_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
for s in students:
    age = 2022 - int(s[4])
    if age >= 27:
        age = 27
    num_of_student_per_age_group[age - 17] +=1
    
    sum_score = 0
    count_score = 0
    for i in range(11):
        if s[i+5] != '-1':
            count_score += 1
            sum_score += float(s[i+5])
    average = sum_score/count_score
    average_of_student_per_age_group[age - 17] += average

print(average_of_student_per_age_group)
print(num_of_student_per_age_group)

for i in range(len(average_of_student_per_age_group)):
    if num_of_student_per_age_group[i] !=0:
        average_of_student_per_age_group[i] = average_of_student_per_age_group[i]/num_of_student_per_age_group[i]


for i in range(len(average_of_student_per_age_group)):
    average_of_student_per_age_group[i] = average_of_student_per_age_group[i] * 10


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

figure, axis = plt.subplots()
# lít from 0-11
x_pos = np.arange(11)
y_pos = np.arange(11)

# plot the barchart using 2 list
plt.bar(x_pos, num_of_student_per_age_group, align='center', alpha=0.5)
# plot chart = line chart
plt.plot(x_pos, average_of_student_per_age_group, color ="red", marker ="o")
# change horizontal category name
plt.xticks(y_pos, ["17",'18','19','20','21','22','23','24','25','26','>26'])

# Lable and title
plt.ylabel('Số học sinh')
plt.ylabel('Tuổi')
plt.title('Số học sinh bỏ thi hoặc không thi')

# right side ticks
ax2 = axis.twinx()
ax2.tick_params("y",colors ='r')
ax2.set_ylabel('Điểm trung bình')
ax2.set_ylim(0,10)

#Draw number of student on top of each bar
rects = axis.patches
# make some lable
labels = num_of_student_per_age_group
for rect, subject in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height, subject, ha="center", va="bottom")
# set limit to vertical axis
axis.set_ylim(0,100)

# show the plot
plt.show()
