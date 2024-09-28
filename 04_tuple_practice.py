# What is a Tuple?
# Tuples are like lists, but they are immutable, meaning once created, you cannot modify their elements (no adding, removing, or changing elements).

          #   creating tuple 


# my_tuple = (1,2,3,4)
# print(my_tuple)         # output = (1,2,3,4)
# print(type(my_tuple))   # output = <class 'Tuple'>

  


        # one value in tuple

# my_tuple = (5)
# print(my_tuple)
# print(type(my_tuple))    # output = <class 'int'>


# my_tuple = (5,)
# print(my_tuple)   # output = (5,)
# print(type(my_tuple))



       # count() method in tuple

# my_tuple = (1,2,3,2,5,2,7)
# print(my_tuple.count(2))     # output = 3


      
      # index() method 
    
# my_tuple = (1,2,3,4,5)
# print(my_tuple.index(3))     # output = 2



# # Accessing Tuple Elements

# my_tuple = ("dinesh","vihaan","suraj")
# print(my_tuple[1])      # output = vihaan


# 4. Slicing Tuples

# my_tuple = (1,2,3,4,5,6)
# print(my_tuple[1:5])      # output = (2,3,4,5) 



         # Tuple Operations


#  # concatination
# my_tuple = (1,2,3)
# my_tuple2 = (4,5,6)

# combined = my_tuple + my_tuple2
# print(combined)                    # output = (1,2,3,4,5,6)

    # repetition

# #repeted
# my_tuple = (1,2)
# print(my_tuple * 3)  # output = (1,2,1,2,1,2)



# Checking Membership

# my_tuple = (1,2,3,4,5,6)
# print(2 in my_tuple)      # output = True
# print(3 in my_tuple)      # output = True
# print(10 in my_tuple)      # output = False




# Iterating Through a Tuple

# my_tuple = (1,2,3,4,5,6)
# for item in my_tuple:
#     print(item,end=" ")  # output = 1 2 3 4 5 6




# Unpacking Tuples
# You can unpack a tuple into individual variables.


# my_tuple = (1,2,3)
# a,b,c = my_tuple
# print(a,b,c)       # output = 1 2 3



# Length of a Tuple

# my_tuple = (1,2,3,4,5,6)
# print(len(my_tuple))      #  output = 6 


      


      #  Nesting Tuples

# my_tuple = ((1,2,),(3,4,5),(12,32))
# print(my_tuple[0])        # output = (1,2)
# print(my_tuple[0][1])     # output = 2 


#    sorted metnods

# my_tuple = (1,2,3,4,5)
# sortted_list = sorted(my_tuple)
# print(sortted_list)                 # output [1,2,3,4,5]
# print(type(sortted_list))           # output <class 'list'>

my_tuple = (1,2,3,4,5,6)
print(my_tuple)


















































