# import array as arr
# arr = (23,45,6,67,5,4)
# print(arr)


# from array import *

# vars = array("i",[23,3])
# print(vars)



# from array import *
# var = array("i",[456, 56,-8,33,553, 53453])
# print(var.buffer_info())

#             this is a count mathod
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


# for e in num:
#     num.reverse()
#     print(e)
# reverse_array = num[::-1]
# print(reverse_array) 



# Write a program to check if an element exists in the array.


# def chack_element():
#     import array
#     num = array.array("i",[1,2,3,4,5,6,7])

#     ckeck_element = int(input("Enter element which you want to check: "))

#     if ckeck_element in num:
#         print("element exists in array   ")

#     else:
#         print("element not found")

# chack_element()
# chack_element()
# chack_element()
# chack_element()
# chack_element()
# chack_element()



# Find the index of the first occurrence of an element in an array.

# import array
# num = array.array("i",[10,20,30,40,20,50])
# num_index = num.index(20)
# print(num_index)

# Sort an array in ascending order without using built-in methods.

# import array
# num = array.array("i",[1,34,6,432,77,8,546,23,435])
# def booble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]

# booble_sort(num)
# print("sorted array in ascending order")
# for i in num:
#     print(i,end= " ")


# Sort an array in descending order.

# import array
# num = array.array("i",[1,34,6,432,77,8,546,23,435])
# def booble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] < arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     print(arr[2])
    
# booble_sort(num)
# print("sorted array in ascending order")
# for i in num:
#     print(i,end= " ")

# Merge two arrays into one.

# import array
# num1 = array.array("i",[1,2,3,4])
# num2 = array.array("i",[5,6,7,8])
# new_array = num1 + num2

# print(f"new array is = {new_array}")

# Rotate an array by a certain number of positions.
# import array 
# num = array.array("i",[1,2,3,4,5,6])

# n = 2

# array_rotate = num[n:] + num[:n]
# print(array_rotate)                     # output  array("i",[3,4,5,1,2])


# import array
# num = array.array("i",[1,2,3,4,5])

# n = 2

# array_rotete = num[-n:] + num[:-n]
# print(array_rotete)



# Shift all elements of the array by one position to the right.

# import array
# arr = array.array("i",[1,2,3,4,5,6,7])
# change_position = arr[-1:] +arr[:-1]
# print(change_position)

# import array
# num = array.array("i",[1,2,3,34,5,6,])
# print(num)

# import array 
# num = array.array("i",[1,2,3,4,5,6])
# x = max(num)
# print(x)
# y = min(num)
# print(y)


# import array
# num = array.array("i",[1,2,4,5,])
# x = num.insert(2,3)
# print(num)



# Find the second largest element in an array



# import array
# arr = array.array("i",[10, 20, 4, 45, 99, 99])

# def find_second_largest(arr):
#     if len(arr) < 2:
#         return "array must have at least two element"
    
#     largest = second_largest = float("-inf")
#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num
        

#         if second_largest == float("-inf"):
#             return "there is no second largest number"

#         else:
#             return second_largest        

# result = find_second_largest(arr)
# print(f"The second largest element = {result}")


# Check if an array is a palindrome (same forwards and backwards).



# import array
# arr = array.array("i",[1,2,3,2,1])
# def is_palindrome(arr):
#     return arr == arr[::-1]

# if is_palindrome(arr):
#     print("this array is a palindrome")

# else:
#     print("this is not a palindrome")


# Write a program to shift negative numbers to one side and positive to the other.

# import array
# arr = array.array("i",[1,-2,3,-4,5,-6])
# def shift_negetive_positive(arr):
#   negetive_number = array.array("i",[num for num in arr if num < 0 ])
#   positive_number = array.array("i",[num for num in arr if num > 0 ])
#   return negetive_number + positive_number


# shifted_array = shift_negetive_positive(arr)
# print("Array after shifting negative and positive numbers:")
# for num in shifted_array:
#   print(num,end= " ")


# import array 
# def create_array():
#     a = array.array("i",[])
#     for i in range(5):
#        num = int(input("Enter number"))
#        return num

#     print(a.append(i))

# create_array()
        
# for i in range(1,10):
#     for a in range(1,10):
#         print(f"{i} x {a} = {i * a}", end="")

# dict = {
#     "name": "dinesh",                  # name is a key and dinesh is it's velue 
#     "age": "19",                       # it is call keyvalue pairs
#     "work": "python devloper"

# }

# for i in dict:
#     print(i)
    

# print(dict["name"])
# print(dict["age"])
# print(dict["work"])

# print(dict)
# x = dict.clear()
# print(dict)

# import time
# time_now = time.localtime()
# print(time_now)

# next = time.process_time()
# print(next)

# dict = {
#     "name": "dinesh",
#     "age": "19",
#     "work": "python devloper"
# }

# print(dict)
# c = dict.copy()

# for i in range(1,10):
#     for a in range(1,10):
#         print(f"{i * a}")

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
   
# ]

# print(type(matrix))

# for row in matrix:
#     for value in row:
#         print(value ,end="")
#     print() 


# my_dict = {
#     "name": "dinesh",
#     "age": "19",
#     "work": "python developer"
# }

# for key,value in my_dict.items():
#     print(key,value)

                         # List Comprehensions (लिस्ट कंप्रीहेंशन):
# squares = []

# for i in range(1,6):
#     squares.append(i ** 2)
# print(squares)

# squares = [i ** 2 for i in range(1,6)]
# print(squares)

# Looping with enumerate() (इन्म्यूरेट के साथ लूपिंग):

# fruits = ["apple","banana","mango"]

# for index,fruit in enumerate (fruits):
#     print(f"index = {index} , fruits = {fruit}")


# name = ["dinesh","mukesh","ram"]
# scores = [100,67,40]

# for name,score in zip (name,scores):
#     print(f"{name} scored {score} points")


#  Dictionary Iteration (डिक्शनरी के साथ लूपिंग):

# student_scores = {"dinesh": 13,"jaspal":24, "haris":2}

# for name,score in student_scores.items():
#     print(f"{name} scores {score} scores")


# student_rollno = {"dinesh": 101,"jaspal": 102 }

# for name,rollno in student_rollno.items():
#     print(f"{name} ka rollno {rollno} hai  ")

# # Looping with Conditions (शर्तों के साथ लूपिंग):

# number = [1,2,3,4,5,6,7,8,9,10]
# even_number = [num for num in number if num % 2 == 0]
# print(even_number)

number = [126,236,822,904,523,645,712,874]
even_number = [num for num in number if num  % 2 == 0]   # % iska matalab hai ki divide karane ke bad ka total
print(even_number)



























