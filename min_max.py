# numbers = [6,58,20]
# # print(min(numbers))
# # print(max(numbers))

# def greast_diff(l):
#     return max(l)-min(l)

# print(greast_diff(numbers))   
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
                count += 1
    return count

mixed = [1,2,3, [2,1], [3,1,3]]
print(sublist_counter(mixed))    