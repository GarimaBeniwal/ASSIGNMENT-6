

m=input("enter student name")
n=input("enter student id")
o=input("enter student class")

def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    if student_name:
        print("Student Name:", student_name)
    if student_class:
        print("Student Class:", student_class)
student_data(student_id=n,student_name=m,student_class=o)
                   