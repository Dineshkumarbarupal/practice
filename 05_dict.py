        #  Creating a Dictionary

# student = {
#     "name": "dinesh",
#     "age": 19,
#     "sub": "agriculture"
# }



        # accesing dictionary items

# student = {
#     "name":  "dinesh",
#     "age": 19,
#     "course": "it"
# }
 
# print(student["name"])



      # Adding/Updating Dictionary Items

# student = {
#     "name": "dinesh",
#     "age": 19,

# }
# student["job"] = "Ai"     # adding item
# print(student)            # output = {'name': 'dinesh','age': 19,'jod':Ai} 

#      # updating dict

# student["age"] = 18     

# print(student)            # output = {'name': 'dinesh', 'age': 18,'job':Ai}


        # removing element into dict

# remove spacific element

# student = {
#     "name": "dinesh",
#     "age": 19,
#     "job": "it",
#     "work": "farming"
# }

# student.pop("work")
# print(student)

# # removing last itoms

# student.popitem()
# print(student)



# # 5. Looping Through a Dictionary

# student = {
#     "name": "dinesh",
#     "age": 19,
#     "job": "Ai"
# }
    
# for key in student:
#     print(key)


# for value in student.values():
#     print(value)
    

# for key,value in student.items():
#     print(f"{key} : {value}")




# . Checking if a Key Exists


# student = {
#     "name": "dinesh",
#     "age": 19,
#     "work": "It"
# }
# while True:
#     find_name = input("Enter name which you want to find:") 
#     if find_name in student:
#         print("name is parsent in dictionary")
#     else:
#         print("name don't found")

#     break




# Nested Dictionaries Nested Dictionaries

# students = {
#     "student1":{
#         "name": "amit",
#         "age": 21,
#         "address": "sriganganagar"    
#     },
#     "student2":{
#         "name": "raj",
#         "age": 20,
#         "address": "jaipur"
                
#     }
# }

# print(students["student1"],["student2"])



# Dictionary Comprehension


# squres = {x: x**2 for x in range(1,6)}

# print(squres)



# Merging Two Dictionaries


# dict1 = {
#     "name": "dinesh",
#     "age": 19
# }

# dict2 = {
#     "job": "Ai",
#     "work_place": "alien company"
# }


# merging = dict1|dict2
# print(merging)




# Copying a Dictionary

# original_dict = {
#     "citi": "Srivijaynagar",
#     "state": "Rajasthan"
# }

# copid_dict = original_dict.copy()

# copid_dict["citi"] = "sriganganagar"

# print(original_dict)
# print(copid_dict)



#  Default Values Using setdefault()

# my_dict = {"name":"dinesh"}
# age = my_dict.setdefault("age",19)
# print(my_dict)


# Counting with a Dictionary

# word = "dictionary"
# count_leter = {}

# for letter in word:
#     count_leter[letter] = count_leter.get(letter, 0) +1

# print(count_leter) 


# Sorting a Dictionary
# my_dict = {
#     "name": "raj",
#     "age": 19,
#     "job": "Ai"
# }

# sorted by key

# sorted_by_key = dict(sorted(my_dict.items()))
# print(sorted_by_key)

# sorted by value

# sorted_by_key = dict(sorted(my_dict.items(), key= lambda item:item[1]))
# print(sorted_by_key)










































































