from array import *
arr =array("i",[])
user_input = int(input("Enter the lenth of array:"))
for element in range(user_input):
    value = int(input("Enter the valeu of array:"))
    arr.append(value)

print(arr)


s = int(input("Enter number for search:"))
k = 0
for e in arr:
    if e == s:
        print(k)
        break

    k += 1

print(arr.index(s))







