# def add(a,b):
#     return a+b

# getval = add(5,8)
# print(getval)
#--------------------------------------
# a  = int(input("enter first number"))
# b  = int(input("enter two number"))

# def add_two(a,b):
#     return a+b

# total = add_two(a,b)
# print(total)


# def add_two(a,b):
#     return a + b

# a  = input("enter first name ")
# b  = input("enter last name ")

# print(add_two(a,b))


# def add_three(a,b,c):
#         return a+b+c

# print(add_three(4,5,6))

# def add_three(a,b,c):
#         print(a+b+c)

# add_three(4,5,6)


# def name(a):
#     return a[-1]

# a = input("Enter your name")

# print(name(a))


# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     else:
#         return "odd"   
        
# print(odd_even(13))    
# 

# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"   
        
# print(odd_even(16))       


# def is_even(num):
#     if num%2 == 0:
#         return "True"
#     return "False"

# print(is_even(16))        

# def is_even(num):
#     return num%2 == 0

# print(is_even(12))    

# def last_char(name):
#         return name[-1]

# print(last_char("Hitendra"))


# def greater(a,b):
#         if  a > b:
#             return a
#         else:     
#             return b

# num1 = int(input("enter 1 number")) 
# num2 = int(input("enter 2 number")) 

# number = greater(num1,num2)
# print(f"{number} ig greater")


# def greater(a,b,c):
#         if a > b and a > c:
#             return a
#         elif b > a and b > c:
#             return b
#         else:
#              return c

# print(greater(100,20,30))           

def is_palindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else: 
        return False

print(is_palindrom("naman"))           
print(is_palindrom("senaman"))       