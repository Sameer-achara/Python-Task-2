name=input("enter your name:")
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))
print("name:",name)
print("age:",age)
print("marks:",marks)

marks=int(input("enter the marks of Student +:"))
if(marks>=90):
    grade='A'
elif(marks>=80 and marks<90):
    grade='B'
elif(marks>=70 and marks<80):
    grade='C'
else:
    grade='D'

print("Student grade is:",grade)
