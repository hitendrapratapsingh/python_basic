# for i in range(1,11):
#     print(i, end = ", ")

def fibonacci_deq(n):
    a = 0 # firstnum
    b = 1 # second
    if n ==1:
        print(a)
    elif n == 2:
        print(a, b) #a b, 01
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b # c= 1
            a = b # A = 1
            b = c # b = 1
            print(b, end = " ")

fibonacci_deq(10)


