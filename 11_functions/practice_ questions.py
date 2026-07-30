# def greet():
#     return f"Hello, Python Learner!"
# print(greet())



# def square(num):
#     return num*num
# print(square(5))
# print(square(6))
# print(square(7))



# def full_name(First, last):
#     return f"{First} {last}"
# print(full_name("Puneet", "Singh"))



# def calculate_area(length, width=10):
#     return length*width
# print(f"The area of the rectangle is {calculate_area(13,20)}")
# print(calculate_area(13))



# add = lambda x,y : x+y
# print(add(5,3))



# list1 = [1, 2, 3, 4, 5]
# square = lambda x : x*x
# print(list(map(square,list1)))



# def factorial(n):
#     if n == 1:
#         return n
#     return n*factorial(n-1)
# print(factorial(6))



# def sum_of_digits(n):
#     if n ==0:
#         return n
#     return (n%10) + sum_of_digits(n // 10)
# print(sum_of_digits(7532))



# import math
# a = math.sqrt(144)
# b = math.sin(math.radians(90))
# print(a,b)



# import requests
# a = requests.get("https://api.github.com/")
# print(a.json())



# def increment():
#     counter = 0
#     counter+=1
#     print(counter)
# increment()
# increment()
# increment()
# increment()



# def multiply(a, b):
#     """
#     Returns the product of two numbers.
#     Parameters:
#     a (int): The first number.
#     b (int): The second number.
#     Returns:
#     int: The product of the two numbers.
#     """
#     return a * b
# print(multiply(5, 6))
# print(multiply(2, 4)) 
# help(multiply)



# def fibonacci(n):

#     def fib(k):
#         if k <=1:
#             return k
#         return fib(k-2) + fib(k-1)
#     for i in range(n):
#         print(fib(i), end=" ")

# fibonacci(10)





# def safe_divide(a, b):
#     if b == 0:
#         return "cannot divide by zero"
#     return a/b
# print(safe_divide(4, 2))
# print(safe_divide(4, 0))



# import mymodule
# print(mymodule.is_even(11))
