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


def user_info(name,age,city):
    return f'{name} is {age} year old lives in {city}'
print(user_info(city='kolkata' , name='mohan',age=33))
