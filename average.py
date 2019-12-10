#excersize
# number1 = int(input("enter first number1"))
# number2 = int(input("enter first number2"))
# number3 = int(input("enter first number3"))

number1,number2,number3 = input("enter three number comma seprated: ").split(",")

#print(number1+number2+number3/3)
print(f"average of three numbers {(int(number1)+int(number2)+int(number3))/3}")