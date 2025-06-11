'''
P203 問題2
'''

from studentclass import Student
f = open('students.txt', encoding='utf-8')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()

sline = line3.split(',')
stu = Student(sline[0], int(sline[1]), int(sline[2]), int(sline[3]))
stu.showdetail()
f.close()