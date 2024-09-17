        #   creating a set


# my_set = {1,2,3,4,5}
# print(my_set)       # {1,2,3,4,5}

# print(type(my_set))  # <class 'set'>


       # add element

# my_set = {1,2,3}
# my_set.add(4)
# print(my_set)     # output = {1,2,3,4}


       #   update mathod

# my_set = {1,2,3,5,6}
# my_set.update([7,8,9,10,11,12])
# print(my_set)           # output = {1,2,3,4,5,6,7,8,9,10,11,12}



        #    remove method

# my_list = {1,2,3,4,5,6}
# my_list.remove(6)
# print(my_list)          # output = {1,2,3,4,5}



# discard(): Removes a specific element but doesn't raise an error if the element doesn't exist.


# my_set = {1,2,3,4,5,6}
# my_set.discard(10)       # no error
# print(my_set)            # output = {1,2,3,4,5,6}


# pop(): Removes and returns an arbitrary element from the set.

# my_set = {1,2,3,4,5,6}
# popped_set = my_set.pop()
# print(popped_set)            # output  = 1

   



          # clear() method

# my_set = {1,2,3,4,5,5,6,7}
# my_set.clear()
# print(my_set)

# print(type(my_set))


           # set operetions




       # union() method

# my_set1 = {1,2,3}
# my_set2 = {4,5,6}
# union_set = my_set1.union(my_set2)
# print(union_set)      # output  {1,2,3,4,5,6}


# Intersection (intersection()): Returns elements common to both sets.

# my_set1 = {1,2,3,4}
# my_set2 = {4,5,6,7}
# inter_set = my_set1.intersection(my_set2)
# print(inter_set)            # output = 4




# Difference (difference()): Returns elements present in the first set but not in the second.

# my_set1 = {1,2,4,5,6}
# my_set2 = {1,2,3,6}

# diff_set = my_set1.difference(my_set2)
# print(diff_set)




# Symmetric Difference (symmetric_difference()): Returns elements present in either of the sets but not in both.

# my_set1 = {1,2,3,4}
# my_set2 = {5,6,7,8}
# symm_diff_set = my_set1.symmetric_difference(my_set2)
# print(symm_diff_set)



# issubset(): Checks if one set is a subset of another.



# my_set1 = {1,2,3}
# my_set2 = {1,2,3,4,5}
# print(my_set1.issubset(my_set2))   # output  = True

 

# issuperset()
#             Returns True if the set contains all elements of another set.



# my_set1 = {1,2,3,4}
# my_set2 = {1,2,3}
# super_set = my_set1.issuperset(my_set2)   
# print(super_set)           # output = True



#  isdisjoint()
#              Returns True if two sets have no elements in common.


# my_set1 = {1,2,3}
# my_set2 = {4,5,6}
# isdis_set = my_set1.isdisjoint(my_set2)
# print(isdis_set)             # output  = True


# copy()
# Returns a shallow copy of the set.


# my_set = {1,2,3,4}
# copy_set = my_set.copy()
# print(copy_set)


# len()  methods


# my_set = {1,2,3,4,5,6}
# print(len(my_set))


# . frozenset()
# Creates an immutable set. Once a frozenset is created, no elements can be added or removed

# my_set = {1,2,3,4,5}
# frozenset = frozenset(my_set)
# print(frozenset)      # output = frozenset({1,2,3,4,5})


# in operator

# my_set = {1,2,3,4,5}
# print(2 in my_set)            # output = True




# not in operator
# my_set = {1,2,3,4,5,6}
# print(8 not in my_set)   # output = True



      # itersactio_update()

# my_set1 = {1,2,3}
# my_set2 = {1,2,4}
# my_set1.intersection_update(my_set2)
# print(my_set1)              # output = {1,2}

       

      # diffrence_update()


# my_set1 = {1,2,3,4,5}
# my_set2 = {1,2,6,7,8}
# my_set1.difference_update(my_set2)
# print(my_set1)               # output = {3,4,5}





        #  symmetric_difference_update()

# my_set1 = {1,2,3,4,5}
# my_set2 = {1,2,3,7,8}
# my_set1.symmetric_difference_update(my_set2)
# print(my_set1)        # output = {4,5,7,8}

 



#         # min() method 

# my_set = {1,2,3,4,5,6}
# print(min(my_set))    # output = 1


        #    max() methods


# my_set = {1,2,3,4,5,6}
# print(max(my_set))        # output = 6



 
           # sum() methods

# my_set = {1,2,3,4,5,6}
# print(sum(my_set))    # output = 21


       # sorted method

# my_set = {1,6,5,4,2,8}
# print(sorted(my_set))



  #   enumerate()
# my_set = {1,2,4,5,6,7}
# for index,value in enumerate(my_set):
#     print(f"{index}:{value}")



            #    any() method










