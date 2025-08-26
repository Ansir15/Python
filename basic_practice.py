# def avg():
#     while True:
        
#        n1=int(input("Enter Number: "))
#        n2=int(input("Enter Number: "))
#        n3=int(input("Enter Number: "))
    
#        average=n1+n2+n3/3
    
#        print("Average ",average)
       
# avg()


# def name(n,ending):
#     print("good by "+n+" "+ending)
    
# name("ansir"," jao")
# name("Khurram"," jao")




# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n*factorial(n-1)

# n=int(input("Enter the number: "))
# print(f"Entered factorial number is :{factorial(n)} ")





# def func(n1,n2,n3):
#     if(n1>n2 and n1>n3):
#         print(str(n1)+" is the greatest.")
#     elif(n2>n1 and n2>n3):
#         print(str(n2)+" is the greatest. ")
#     elif(n3>n1 and n3>n2):
#         print(str(n3)+" is the greatest.")
# n1=int(input("Enter the number: "))        
# n2=int(input("Enter the number: "))        
# n3=int(input("Enter the number: "))
# func(n1,n2,n3)        
        
        
        
# def temp(c):
#     Fahrenheit = (c * 9/5) + 32
#     print(f"{c}°C is equal to {Fahrenheit:.2f}°F")
    
# c=int(input("Enter the number: "))
# temp(c)    



# def table(n):
#     for i in range(1,11):
#         print(f" {i}*{n}={n*i}")
        
# n=int(input("Enter the number: "))
# table(n)




import random

# computer=random.choice([-1,0,1])

# youstr=input("Enter your choice: ")

# youDict={"s":1,"w":-1,"g":0}

# reverseDict={1:"Snake",-1:"Water",0:"gun"}

# you=youDict[youstr]
# print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")
# if(computer==you):
#     print("its draw")
# else:
#     if(computer==-1 and you==1):
#         print("you win")
#     elif(computer==-1 and you==0):
#         print("you loss")
#     elif(computer==1 and you==-1):
#         print("you loss")
#     elif(computer==1 and you==0):
#         print("you win")
#     elif(computer==0 and you==1):
#         print("you win")
#     elif(computer==0 and you==-1 ):
#         print("you loss")
#     print("you something went wrong!")



# File i/o


# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()


# st="hello ,today climate is  very good "

# f=open("write.txt","w")
# f.write(st)
# f.close()

# st="hello ,today climate is  very good "

# f=open("write.txt","+")
# f.write(st)
# f.close()


# practice set 9

# with open("file.txt") as f:
#   content= f.read()
#   if("twinkle" in content):
#       print("the word twinkle is present in the content ")
#   else:
#       print("the word twinkle not present")



# def game():
#     print("you are playing the game...")
#     score=random.randint(1,62)
    
#     with open("file.txt") as f:
#         hiscore =f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print(f"your score: {score}")
#     if(score>hiscore):
#          with open("file.txt","w") as f:
#             f.write(str(score))
#     return score         
# game()        
            
            
            
# def generatetsble(n):
#     table=""
#     for i in range(1,11):
#         table+=f"{n} X {i}={n*i}\n"
#     with open(f"tables/table_{n}.txt", "w")as f:
#         f.write(table)
# for i in range(2,21):
#       generatetsble(i)                 





# word="Donkey"
# with open("file.txt","r") as f:
#     content=f.read()
# contentNew=content.replace(word,"######")

# with open("file.txt","w") as f:
#     f.write(contentNew)


with open("file.txt","r") as f:
    lines=f.readlines()
line_no=1
for line in lines:
    if("python" in line.lower()):
        print(f" yes python word is present. \n line no {line_no}")
        break
    line_no+=1

else:
    print("the word pyhton not found")


