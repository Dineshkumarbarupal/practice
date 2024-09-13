# import array as arr
# arr = (23,45,6,67,5,4)
# print(arr)


# from array import *

# vars = array("i",[23,3])
# print(vars)



# from array import *
# var = array("i",[456, 56,-8,33,553, 53453])
# print(var.buffer_info())

            # this is a count mathod
# from array import *
# var1 = array("i",[12,3,23,23,3,3,3])
# var2 = array("i",[2,34,3,2,34,23,23,2,2])
# print(var2.count(2))
# print(var1.count(3))


# from array import *
# number = array("i",[23,234,34,234,234])
# print(number)                   # output = array("i",[23,234,34,234,234])
# print(number.buffer_info())    # output = (2636686598320, 5)
# print(number.typecode)         # output = i 


# from array import *
# number = array("i",[23,34,456,234,567,24,])
# number.reverse()
# print(number)



# from array import *
# number = array("i",[12,345,46,567,234])

# for i in range(5):
#     print(number[i])


# from array import *
# num = array("i",[1,2,3,4,5,6,7,8,9])
# for e in num:
#     print(e)


# import array as arr
# number = arr.array("i",[1,2,3,4,5,6,7,8])
# print(number)
# # for i in number:
# #     print(i)
# for i in range(8):
#     print(number[i])


# from array import *
# number = array("u",["e","w","w","f"])
# for e in number:
#     print(e)



# from array import *
# num = array("i",[2,4,7,6,9,5,3,])
# newarr = array(num.typecode,(a for a in num))
# for e in newarr:
#     print(e)










# from array import *
# number = array("u",["e","r","f","h","v"])
# print(number)

# for e in number:
#     print(e)



# from array import *
# num = array("i",[12,3,345,567,34])
# print(num)


# from array import *
# num = array("i",[2,34,46,678,89])
# num.append(34)
# print(num)
# for i in range(len(num)):
#     print(num[i])


# print(num.count(2))

#                     # array ka type pta karna
# from array import *
# cars = ArrayType
# print(cars)         # output = <class 'array.array'>



# from array import *
# num = array("i",[12,32,345,7,6,45,23])
# for e in num:
#     print(e)

# print(num.index(7)) 

# for i in range(len(num)):
#     print(i)




# import array as arr
# a = arr.array("d"[1.2,2.34,34.3,5.46,])
# for i in range(3):
#     print(a)





# from array import *
# num = array("i",[1,2,3])
# print(num)

# for i in num:
#     print(i)      # output = 1
#                   #          2
#                   #          3

#                     #  add element in list
# # sirf ekl element ko add akrana
# x = num.append(4)
# print(num)           # output = 1 2 3 4 

# # multipal value add karana
# x = num.fromlist([5,6,7])
# print(num)


# # add an element at the specific index

# y = num.insert(7,8)
# print(num)                 # yah sirf ek idex par value insert karega





# remove an element by value

# from array import *
# num = array('i',[1,2,3,4,5])
# y = num.remove(4)
# print(num)


# remove an element by index

# from array import *
# num = array("i", [1,2,3,4,])
# y = num.pop(2)
# print(num)


# Write a program to iterate through an array and print each element.

# from array import *
# num = array("i",[1,2,3,4,6])
# for i in num:
#     print(i)


# Find the sum and average of all elements in an array

# from array import *
# num = array("i",[1,2,3,4,5,6])
# print(num)                        # output = array("i",[1,2,3,4,5,6])   

# a = num[2]
# b = num[1]
# print(a + b)                      # output = 5



# sum_of_element = sum(num) 
# averege_of_element = sum_of_element / len(num)

# print(f"sum = {sum_of_element}")
# print(f"average = {averege_of_element}")




# Count occurrences of a specific element in an array.

# from array import *
# num = array("i", [1,2,3,4,5,2,2,7])
# print(num.count(2))


# Find the maximum and minimum elements in an array

# import array
# num = array.array("i",[12,234,456,678,345])
# print(max(num)) 
# print(min(num))

# Extract a subarray using slicing.
# import array
# num = array.array("i",[12,34,45,7,67,435,])
# new_num = num[0:6]
# print(new_num)

# Remove duplicate elements from an array.

# import array 
# num = array.array("i",[2,34,4,2,5,6,2,3])
# x = num.append(34)
# print(num)





# Remove duplicate elements from an array.

# import array
# num = array.array("i",[1,2,3,4,2,5,6,7,])
# print(num)
# array_list = num.tolist()
# unique_list = list(set(array_list))

# unique_array = array.array("i", unique_list)

# print(unique_array)


# Reverse an array using slicing.

# import array
# num = array.array("i",[1,2,3,4,5,6,7])
# print(num.buffer_info())


# # for e in num:
# #     num.reverse()
# #     print(e)
# reverse_array = num[::-1]
# print(reverse_array) 




import array

num = array.array("i",[1,2,3,4,5,6])
lenth = len(num)
print(lenth)

mid = lenth // 2
print(mid)

first_haf = num[:mid]
second_haf = num[mid:]
print(first_haf)
print(second_haf)





























































































