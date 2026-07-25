i =3

if i == 35:
    pass # do nothing
print("End of the program")


#Q1
# a = int((input("Enter a number: ")))
# print(a)
# if(a>0):
#     print("Your number is positive")
# elif(a==0):
#     print("Your number is zero")
# else:
#     print("Your number is negative")


#q2
# age = int((input("Enter your age: ")))
# if(age>=18):
#     print("Yes you vote")
# else:
#     print("You cannot vote")


# #q3
# num = int((input("Enter a number: ")))
# if(num%2 == 0):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


#q4
# day_num = int(input("Enter a day number: "))
# match day_num:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thrusday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print(f"{day_num} does not exsist")

#q5
# a = int(input("enter your firts number: "))
# b = int(input("enter your second number: "))
# operation = input("Choose a operation: ")

# match operation:
#     case "+":
#         print(a + b)
#     case "-":
#         print(a -b )
#     case "*":
#         print(a * b)
#     case "/":
#         print(a / b)


#q6

# for i in range(1,11):
#     print(i)

# a = int(input("Enter a number: "))
# for i in range(1,11):
#     print(a,"X",i,"=",a*i)

#q7
# sum = 0
# for i in range(1,101):
#     print(i)
#     sum+=i
# print(sum)

#q8
'''
print he following pattern
*
**
***
****
'''

# for i in range(1,5):
#     print("*"*i)

#q9
# sum =0
# i = 1
# while i<=100:
#     sum =sum+i
#     i = i+1
# print(sum)

#q10
# password = "Y2K123"
# entered_password = input('enter password: ')

# while (entered_password != password):
#     entered_password = input("Wrong password! try again and enter the correct password: ")
    
# print("success! you have logged in")


#q11
# num = 22256
# print(int(str(num)[::-2]))

#q12
# for i in range(1,11):
#     if (i == 7):
#         break
#     print(i)

#q13
# for i in range(1,11):
#    if (i == 5):
#      continue
#    print(i)

#q14
# for i in range(1,6):
#     match i:
#         case 1:
#             print(1)
#         case 2:
#             print(2)
#         case 3:
#             pass
#         case 4:
#             print(4)
#         case 5:
#             print(5)