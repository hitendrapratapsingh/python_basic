# name = "  hite   ndra  "
# dot = "................"

# print(name + dot)
# # lstrip() method = remove left side space
# # rstrip() method
# # strip() method  = left+right space removed
# replace(" ","_")

# print(name.lstrip() + dot)
# print(name.rstrip() + dot)
# print(name.strip() + dot)
# print(name.replace(" ","") + dot)


strss = "Buy gifts and for wife and surprise her. Choose from amazing gift ideas or wife on a"
# print(strss.replace(" ","_"))
# print(strss.replace("and","OR")) # for all  replace
# print(strss.replace("and","OR", 1 )) # for custom like 1 time replace
# print(strss.find("and")) # find position "and" 
#print(strss.find("and",12))
isposition1 = strss.find("and",1)
isposition2 = strss.find("and",isposition1 + 1)
print(isposition2)
