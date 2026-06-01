#condition statement
#Nested if

student_age=int(input("enter the student age:"))
branch="cse"
if student_age > 18:
    if branch=="cse":
        print("cse student")
    else:
        print("ece student")
else:
    print("not a cse student")






username=str(input("enter username"))
password=str(input("enter your password"))
if username=="apple":
    if password=="12345":
        print("login successfull")
    else:
        print("wrong password")
else:
    print("invalid")



#simple calculator
first_number=int(input("enter the first number:"))
second_number=int(input("entr the second number:"))
operation=str(input("enter  your operator:+,-,*,/"))
if operation=="+":
    print(first_number+second_number)
elif operation=="-":
    print(first_number-second_number)
elif operation=="*":
    print(first_number*second_number)
else :
    print(first_number/second_number)




#grading marks
marks=int(input("please enter the marks:"))
if marks>90:
    print("A grade")
elif marks>75 and marks<=90:
    print("B grade")
elif marks>35 and marks<=75:
    print("C grade")
else:
    print("fail")

