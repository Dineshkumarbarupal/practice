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

# # removing itoms

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




# Nested DictionariesNested Dictionaries

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








































