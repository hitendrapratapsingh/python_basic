# for i in range(10):
#     print(f"hello world {i}")

# for i in range(2,10):
#     print(f"hello world {i}")
sum = 0
# for i in range(1,21):
#     sum += i
#     print(sum)

# n = int(input("enter the number: "))
# total = 0
# for i in range(1,n+1):
#     total += i

#     print(total)

# total = 0
# n = input("enter you your number: ")
# for i in range(0,len(n)):
#    total += int(n[i]) 
# print(total)
    


name = input("enter your name: ") 
temp = ""
for i in range(0, len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
