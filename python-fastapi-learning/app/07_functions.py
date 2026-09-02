# def addion(a,b):
#     return a+b


# added =addion(10,20)
# print(added)

# def checkAdult(age):
#     if age >=18:
#         print('adult')
#     else:
#         print('minor')
        
        
# checkAdult(25)
# checkAdult(10)


# def calculate(a,b,operation):
#     if(operation=='add'):
#         return a+b
#     elif(operation == 'subtract'):
#         return a-b
#     else:
#         return a*b
    
# result =calculate(10, 20 , 'multiply')

# print(result)


# def check(a,b=50):
#     return a+b

# print(check(10))

# def name(name= "mohan"):
#     return f'hello {name}'
# wholename = name()
# print(wholename)


# def user_info(name,age,city):
#     return f'{name} is {age} year old lives in {city}'
# print(user_info(city='kolkata' , name='mohan',age=33))


# def add(*numbers ):
#    multiply = 1
#    for numb in numbers:
#           multiply*=numb
#    return multiply
   
   

# print(add(10,20 , 30 , 40))

# def show_info(**info):
#     for userinfo in info.items():
#         print('thats the data===>' , userinfo)
        
    


# show_info(name='Mohan', age = 22)



# def profile(*skills , **details):
#     for skill in skills:
#         print(skill)
#     for key, value in details.items():
#         print(key, value)
        
        
        
# profile("Python" , "FastAPI", name = 'Mohan', age = 22)
        
        





def student_info(*args , **kwargs):
    for arg in args:
        print(arg)
    for key , value in kwargs.items():
        print(key, value )
        
    






student_info(
    "Mohan",
    "Python",
    "FastAPI",
    city="Kolkata",
    age=22
)











