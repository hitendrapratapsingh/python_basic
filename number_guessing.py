# import random
# winning_number = random.randint(1,100)
# # winning_number = 55
# guess = 1
# number = int(input("guess a number bitween 1 and 100: "))
# game_over = False

# while not game_over:
#     if number == winning_number:
#         print(f"You win and you gussed this number in {guess} time")
#         game_over =  True
#     else:
#         if number < winning_number:
#             print("too low")
#             guess += 1
#             number = int(input("guess again"))
#         else:
#             print("too high")
#             guess += 1
#             number = int(input("guess again"))


# import random
# winning_number = random.randint(1,100)
# # winning_number = 55
# guess = 1
# number = int(input("guess a number bitween 1 and 100: "))
# game_over = False

# while not game_over:
#     if number == winning_number:
#         print(f"You win and you gussed this number in {guess} time")
#         game_over =  True
#     else:
#         if number < winning_number:
#             print("too low")
#         else:
#             print("too high")
        
#         guess += 1
#         number = int(input("guess again"))


# import random
# winning_number = random.randint(1,100)
# # winning_number = 55
# guess = 1
# number = int(input("guess a number bitween 1 and 100: "))
# game_over = False

# while True:
#     if number == winning_number:
#         print(f"You win and you gussed this number in {guess} time")
#         break
#     else:
#         if number < winning_number:
#             print("too low")
#         else:
#             print("too high")
        
#         guess += 1
#         number = int(input("guess again"))


import random
winning_number = random.randint(1,100)
# winning_number = 55
guess = 1
game_over = False

while True:
    number = int(input("guess a number bitween 1 and 100: "))
    if number == winning_number:
        print(f"You win and you gussed this number in {guess} time")
        break
    else:
        if number < winning_number:
            print("too low")
        else:
            print("too high")
        
        guess += 1
        continue