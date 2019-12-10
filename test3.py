# name = "Gaurav"
# print(f"{name}")
# print(name[::-1])
# print(name[6::-1])

# name = input("enter your name")
# reserve = name[-1::-1]
# print(f"reserve of your name is {name[-1::-1]}")
# print(f"reserve of your name is {reserve}")

# name, chars = input("enter your name comma seprate: ").split(",")
# print(f"length of name : {len(name)}")
# print(f"charcount of char : {name.lower().count(chars)}")
# print(f"charcount of char : {chars.count(chars.lower())}")
# print(f"charcount of char : {name.strip().lower().count(chars.strip().lower())}")

# num = input("enter your number")
# num = int(num)
# i = 1
# while i <= num:
#     print(i)
#     i = i+1

# num = input("enter your number")
# num = int(num)
# i = 1
# total = 0
# while i <= num:
#     total +=i
#     i = i+1
#     print(total)


# num = input("enter your number")
# #print(num[::-1])

# total = 0
# i = 0

# while i < len(num):
#         total += int(num[i])
#         i = i+1

# print(total)


name = input("enter your name: ")
    # len(name)
temp = ""    
i = 0
while i < len(name):
    if name[i] not in temp:
            temp += name[i]

    print(f"{name[i]} : {name.count(name[i])}")
    i = i + 1




