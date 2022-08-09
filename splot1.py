# read file
with open("clean_data.csv",encoding="utf8") as file:
    datas = file.read().split("\n")
header = datas[0]
students = datas[1:]

# remove last student (empty student)
students.pop()

total_students = len(students)

#split header
header = header.split(",")
subjects = header[2:]

# split each student in list
for i in range(total_students):
    students[i] = students[i].split(",")

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]


# loop through all students
for student in students:
    # iterate through all subjects
    for i in range(2,13):
        if student[i] == "-1":
            not_take_exam[i-2] += 1

not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,11):
    not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_students, 2)


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

figure, axis = plt.subplots()
# lít from 0-11
y_pos = np.arange(len(subjects))

# plot the barchart using 2 list
plt.bar(y_pos, not_take_exam_percentage, align='center', alpha=0.5)

# change horizontal category name
plt.xticks(y_pos, subjects)

# Lable and title
plt.ylabel('Percentage')
plt.title('Số học sinh bỏ thi hoặc không thi')

#Draw number of student on top of each bar
rects = axis.patches
# make some lable
for rect, subject in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, subject, ha="center", va="bottom")
# set limit to vertical axis
axis.set_ylim(1,100)

# show the plot
plt.show()