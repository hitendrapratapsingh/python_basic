# matrix = [[1,2,3],[6,5,4],[56,58,54]]
# print(matrix[2])
# for i in matrix:
#     #print(i)
#     for j in i:
#         print(j)

# print(matrix[1][2])

# s = "string"
# print(type(s))
# print(type(matrix))

number = list(range(1,11))
# print(number)
# poped_item = number.pop()
# print(number)
# print(poped_item)
# print(number.index(1))
# print(number.index(1, 5, 10))

# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative

# print(negative_list(number))   

# def squar_list(l):
#     squar = []
#     for i in l:
#         squar.append(i**2)
#     return squar

# number = list(range(1,11))
# print(squar_list(number))


# n = list(range(1,5))
# print(n)
# print(n[::-1])

# def reverse_list(l):
#      l.reverse()
#      return l

# number = [1,2,3,4]
# print(reverse_list(number))     


# def reverse_elements(l):
#     elements = []

#     for i in l:
#         elements.append(i[::-1])
#     return elements

# words = ['abc','des','asd']
# print(reverse_elements(words))


# def filter_odd_even(l):
#     odd_num = []
#     even_num = []
#     for i in l:
#         if i % 2 == 0:
#             even_num.append(i)
#         else:
#             odd_num.append(i)  
#     output = [odd_num, even_num] 
#     return output

# num = [1,2,3,4,5,6] 

# print(filter_odd_even(number))


# def get_num(num):
#     oddnum = []
#     evennum = []
#     for i in num:
#         if i % 2 !=0:
#             oddnum.append(i)
#         else:
#             evennum.append(i)
#     return   [oddnum, evennum]

# tete = [1,2,3,4,5,6]
# print(get_num(tete))        

def comman_value(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

num1 = [1,5,6,2,8]
num2 = [2,6,1,3,4]   
print(comman_value(num1,num2)) 

