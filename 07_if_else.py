# try:

#     while True:
#         age = int(input("Enter your age:"))
#         if age<18:
#             print("you are minor")
#         elif age>18 and age<67:
#             print("you are adult")
#         else:
#             break 
# except:
#     print("Error invalid number....")

# number = 10
# result = "positive" if number > 0 else "negtive"
# print(result)


def switch(day):
    days={
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thrusday",
        5: "friday",
        6: "saturday",
        7: "sunday"
    }
    return days.get(day, "invalid day")

print(switch(3))