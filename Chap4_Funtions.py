# def f(x):
#     return x * 2

# result = f(2)
# print(result)



# def even_odd(x):
#     if x % 2 == 0:
#         print("the number is even")
#     else:
#         print("the number is odd")

# even_odd(2)
# even_odd(3)


# def even_or_not(x):
#     if x % 2 == 0:
#         print("this number is even")
#     else:
#         odd(x)

# def odd(x):
#     print("the number is odd")


# even_or_not(3)




# def f():
#     return 1 + 1

# result = f()
# print(result)


# optional parameter
# def f(x=10):
#     if x == 10:
#         print("x is ten")
#     else:
#         print(“x is not ten”)

# default = f()
# pass_in = f(2)
# print(default)
# print(pass_in)  


# def f ():
#     print ( "Inner Function!" )
# def x ():
#     print ( "Nested Function!" )
# x()
# f()


# changing a global variable in a function
# x = 100
# def f():
#     global x
#     x += 1
#     print(x)
# f()


#built in functions

# len("hello") # return length of indices
# type("hello") # return data type of object
# str(100) # convert to string
# int("1") # convert to interger
# float(100) convert to float
# input(how old are you) # collects information from a user 

# age = input("how old are you ")
# age = int(age)
# print(age)


# exception handling

# a = input("enter first number")
# b = input("enter secound number")
# a = int(a)
# b = int(b)
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("b cannot be zero. Try again.")

# challenge: write a function that does something interesting, and use it several times in a program

# import random
# number = (random.randint(1,15))

# def guess(number):
#     run = True
#     while run:
#         guessed = int(input("Enter a number between 1 and 15: \n"))
#         if guessed == number:
#             print("you have guessed the right number")
#             run = False
#         else:
#             print("you have guessed the wrong number. Try again!")
#             continue


# guess(number)