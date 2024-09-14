# my_list = [1,2,4,"dinesh","kumar",3.45,58,45j,3]
# print(my_list)
# print(type(my_list))


# Basic List Creation and Accessing Elements

# my_list = [1,2,3,4,5]
# print(my_list[0])        # output = 1



# my_list = [1,2,3,4,5]
# print(my_list[-1])         # output = 5


# my_list = [1,2,3,4,5]
# print(my_list[0:5])           # output = [1,2,3,4,5]



# my_list = [1,2,3,4,5,6]
# print(my_list[2:5])             # output = [3,4,5]

# my_list = [1,2,3]
# my_list.append(4)
# print(my_list)                    # output = [1,2,3,4]


                        #   clear() method
# my_list = [1,2,3,4,5]
# my_list.clear()
# print(my_list)



                         # pop method

# my_list = [1,2,3,4,5]
# my_list.pop(1)
# print(my_list)


                    #   insert() method

# my_list = [1,2,4]
# my_list.insert(2,3)
# print(my_list)

                          

                    #  extend() methods    add multipale elements in list


# my_list = [1,2,3,54]
# my_list.extend([2,3,34,5,6,7,4])
# print(my_list)                             #   [1,2,3,54,2,3,34,5,6,7,4]



#                              # index() method  
# my_list = [1,2,3,4,5]
# print(my_list.index(4))             # output = 3

                          


                               #  sort() method       

# my_list =  [1,2,3,4,34,56,73,5]
# my_list.sort()
# print(my_list)
                              


#                                    # reverse() method  
# my_list = [1,2,3,4,5,6,7]
# my_list.reverse()
# print(my_list)



                               # copy() method


# my_list = [1,2,3,4,5,6]
# new_list = my_list.copy()
# print(new_list)


                            #  count()  method 

# new_list = [1,2,3,2,4,2,6,2,]
# print(new_list.count(2))           # output = 4




# new_list = [1,2,3,4,5,6]
# print(new_list.count(2))          # output = 1



                            
# new_list = [1,2,3,4,5]
# new_list.extend([1,2,3,4])
# print(new_list)

 
                      # max() method in list


# new_list = [1,2,3,4,5]
# print(max(new_list))


                      # min() method in list


# new_list = [1,2,3,4,5]
# print(min(new_list))


                      # sorted() method in list

# my_list = [1,53,354,2,34,4,5,356]
# new_list = sorted(my_list)
# print(new_list)





                       # list() method   kise bhi itereble ko list me convert karane ke liye

# my_tuple = (1,2,3,4,5,6)
# conver_list = (list(my_tuple))
# print(conver_list)              # output =     [1,2,3,4,5,6]

# print(type(conver_list))        # output = <class, list>

                



                          # sum() method in list

# new_list = [1,2,3,4,5,6,7]
# print(sum(new_list))     # output = 28

#                       # any(): Agar list mein koi bhi element True ho, to True return karta hai, otherwise False.

# new_list = [1,2,3,4,5]
# print(any(new_list))          # output = True



#                         # all(): Agar list ke saare elements True ho, to True return karta hai, otherwise False.

# my_list = [1,2,3,4,5,6]
# print(all(my_list))           # output = True


#                        # len() method for count lengh of list

# my_list = [1,2,3,4,5,6]
# print(len(my_list))      # output = 6





                      # sorted(): List ke elements ko sort karke ek nayi list return karta hai (original list ko change nahi karta).



# my_list = [1,2,3,4,5]
# new_list = sorted(my_list)
# print(new_list)               # output = [1,2,3,4,5]




                                # Built-in Functions:

#       # map(function, iterable)

# my_list = [1,2,3,4,5]   
# new_list = list(map(lambda x: x * 2, my_list ))
# print(new_list)   # output = [1,4,6,8,10]


# my_list = [1,2,3,4]
# print(len(my_list))  # output = 4


        # filter()  methods 

# my_list = [1,2,3,4,5,6]
# new_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(new_list)      # output = [2,4,6]


# my_list = [12134,2345,376,423,5456,69534]
# new_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(new_list)            # output [12134, 376, 5456, 69534]


# my_list = ["a","e",2,2,3]
# for index,value in enumerate(my_list):
#     print(index,value,end=" ")      # output 0 a 1 e 2 3 2 4 3

                       

            #   reversed()mathod
               
# my_list = [1,2,3,4,5]
# for value in reversed(my_list):
#     print(value,end=" ")        # output = 5 4 3 2 1

# my_list = [1,2,3,4,5]
# for value in enumerate(reversed(my_list)):
#     print(value,end=" ")        # output = (0, 5) (1, 4) (2, 3) (3, 2) (4, 1)




               # zip() method

# fist_list = [1,2,3]
# second_list = [4,5,6]

# zipped = list(zip(fist_list,second_list))
# print(zipped)       # output [(1,4),(2,5),(3,6)]     


                 # list comprehanse

# my_list = [1,2,3,4,5]
# new_list = [x *2 for x in my_list]
# print(new_list)     # output = [2,4,6,8,10]





    #  slice() method

# my_list = [1,2,3,4,5,6,7,8]
# print(my_list[1:6])  # output = [2,3,4,5,6]
# print(my_list)     # output = [1,2,3,4,5,6,7,8]    































































                           







































