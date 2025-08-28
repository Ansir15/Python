# match statement
# def http_status(status):
#     match status:
#        case 200:
#         return "OK"
#        case 404:
#         return "Not Found"
#        case 500:
#          return "Internal Server Error"
#        case _:
#             return "Unknown status"
# print(http_status(200)) 
# print(http_status(404)) 
# print(http_status(500)) 
# print(http_status(403)) 


# # merged dictionar
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged = dict1 | dict2
# print(merged) 


# # Exception hadling
# try:
#     a=int(input("Enter the number: "))
#     print(a)
# except ValueError as v:
#     print(v)
# # except Exception as e:
# #     print(e)
# print("Thank you")


# # Raising Exception
# a=int(input("Enter first number: "))
# b=int(input("Enter the second number: "))

# if(b==0):
#     raise ZeroDivisionError(" number cannot divide by zero")
# else:
#     print(f"the division a/b is {a/b}")
    

# # try with else
# try:
#     a=int(input("Enter the number: "))
#     print(a)
# except ValueError as v:
#     print(v)
# else:
#     print("else run if try run") 


# # try with finally
# try:
#     a=int(input("Enter the number: "))
#     print(a)
# except ValueError as v:
#     print(v)
# finally :
#     print("finally run in every condition") 


# # IF __NAME__== ‘__MAIN__’ IN PYTHON
# from module import myfunc


# # global keyword
# a=4
# def fun():
#     print("global variable run first")
#     a=45
#     print(a)
# print(a)
# fun()


# # code without enumerate function
# l=[1,344,56,78]
# index=0
# for items in l:
#     print(f"the items at index {index} is {items}")
#     index+=1 
# # # code with enumerate function
# for index,items in enumerate(l):
#     print(f"the items at index {index} is {items}")


# # code without comprehensive list
# mylist= [3,4,7,9,5,1]
# squeredlist=[]
# for item in mylist:
#     squeredlist.append(item*item)
# print(squeredlist)
# # # code with comprehensive list
# mylist= [3,4,7,9,5,1]
# squeredlist=[item*item for item in mylist]
# print(squeredlist)
    
    
# # practice set chapter set 12
# # practice question 01
# try:
#    with open("1.txt","r") as f:
#     print(f.read()) 

# except Exception as e:
#     print(e)    
# try: 
#    with open("1.txt","r") as f:
#     print(f.read())

# except Exception as e:
#     print(e)    
# try:   
#    with open("1.txt","r") as f:
#     print(f.read())
# except Exception as e:
#         print(e)

# # Q 02
# l=[1,2,3,4,5,6,7,8]

# for index,item in enumerate(l):
#     if index==2 or index==4 or index==6:
#         print(item)

# # Q 03

# n=int(input("Enter the number: "))
# table=[i*n for i in range(1,11)]
# print(table)

# # Q 04
# try:
#   n1=int(input("Enter the firstnumber: "))
#   n2=int(input("Enter the second number: "))

#   print(f" the number a/b is {n1/n2}")
# except ZeroDivisionError as z:
#     print("infinite")

# # Q 05
n=int(input("Enter the number: "))
table=[i*n for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(str(table))


