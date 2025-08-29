# # lambda function
# # without lambda
# def square(n):
#     return n*n
# print(square(5))
# # with lambda function
# square=lambda x:x*x
# print(square(5))

# # join method only for string
# list=["Ansir","umair","daud"]
# final="::".join(list)
# print(final)

# # format method
# a="{0} is a good {1}".format("Ansir" , "boy")
# print(a)


# # map 

# l=[1,2,3,4,5]
# square=list(map(lambda x:x*x , l))
# print(square)

# # fiter

# l=[1,2,3,4,5,6,7,8]
# even=list(filter(lambda x:x%2==0 , l))
# print(even)

# # reduce
from  functools import reduce
# l=[1,2,3,4,5]
# sum_numbers=reduce(lambda acc,x:acc+x ,l, 0)
# print(sum_numbers)

# # pracice questions
# # Q 02

# a=" the name of the students is {0} , his marks are {1} and phone number is {2}".format("Ansir",95,"454574050")
# print(a)

# # Q 03

# table= [str(7*i) for i in range(1,11)]
# s="\n".join(table)
# print(s)

# # Q 04
# l=[111,25,34,44,45,566,67,78]
# even=list(filter(lambda x:x%5==0 , l))
# print(even)


# # Q 05 
# l=[111,25,34,44,45,566,67,78]
# maximum=reduce(lambda a,b:a if a>b else b ,l, 0)
# print(f"Maximum number : {maximum}")

# # OR
# l=[111,25,34,44,45,566,67,78] 
# def maximum_num(a,b):
#     if (a>b):
#         return a
#     return b
# print(reduce(maximum_num,l,0))


# # Q 06 install freeze

# # Q 07 
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
# app.run()
 


from flask import Flask, request
from markupsafe import escape

# ✅ yeh line missing thi tumhari code me
app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

if __name__ == "__main__":
    app.run(debug=True)
