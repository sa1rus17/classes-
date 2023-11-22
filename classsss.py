class Student:

    def __init__(self,id, name, var, group):
        self.id = id
        self.name = name
        self.var = var
        self.group = group
    
fs=open('studentss.txt','r',encoding='utf-8')
students = []


for student in fs:
    l = student.split(';')
    s = Student(l[0], l[1], l[2], l[3])
    students.append(s)
    
print('------------------------------------------------------------')
print('| ID | FIO                               | VARIANT | GROUP |')
print('------------------------------------------------------------')

for student in students:
    s1 = 2 - len(student.id)
    s2 = 33 - len(student.name)
    s3 = 7 - len(student.var)
    s4 = 5 - len(student.group)
    print(f"| {student.id + ' '*s1} | {student.name + ' '*s2} | {student.var + ' '*s3} | {student.group + ' '*s4} |")

print('------------------------------------------------------------')
