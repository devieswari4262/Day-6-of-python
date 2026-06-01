#exception handling
#try block
#except block
#else block
#final block

'''try:
    a=int(input("enter the number"))
    print(10/a)
except:
    print("cannot divide by zero")
    print("code is running successfull")
o/p:enter the number7
1.4285714285714286
enter the numberapple
cannot divide by zero
code is running successfull

try:
    number=int(input("enter the number:"))
    print(1000/number)
except:
    print("enter numbers other than 0")
    print("alphabets not divisible by zero")
o/p:enter the number:100
10.0
enter the number:cat
enter numbers other than 0
alphabets not divisible by zero

try:
    number=int(input("enter the number:"))
    print(1000/number)
except:
    print("enter numbers other than 0")
    print("alphabets not divisible by zero")
else:
    print("code is running:",number)
o/p:enter the number:555
1.8018018018018018
code is running: 555
enter the number:red
enter numbers other than 0
alphabets not divisible by zeroenter the number:red
enter numbers other than 0
alphabets not divisible by zero'''

try:
    number=int(input("enter the number:"))
    a=1000/number
except:
    print("enter the number other than 0")
    print("alphabets not divisible by zero")
else:
    print("code is running:",a)
finally:
    print("executing completed")

