
# import random 

# student = [["name" , "roll" , 12]]

# def show () :
#     for i in range (0 , len(student)):
#         print(student[i])

# def add ():
#     name = str(input())
#     roll = str(input())
#     age = int(input())
#     student.append([name, roll , age ])

# def delete ():
#     print("write name to delte data ")
#     name = input()
#     for  i in  range (0 , len (student)):
#         if student[i][0] == name :
#             del student[i]

# while 1 :
#     print ("Enter option :")
#     val = input()
#     match val :
#         case "1":
#             show()
#             continue
#         case "2":
#             add()
#             continue 
#         case "3":
#             delete()
#             continue 
#         case _:
#             print("You choose wrong option ")
#             continue 



# tuple example
# it is immutable 

# val = tuple ([1, 2, 3,4] )
# val2= list (val)
# print(val2)


# map - values()  keys()  items()

spam = {'color': 'red', 'age': 42}
for k , v in spam.items():
    spam['color'] = 'black'
    spam.setdefault()
    print (spam.get('color'))