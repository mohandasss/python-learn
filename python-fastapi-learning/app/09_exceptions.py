# try:
#     userinput = int(input('enter the age'))
# except ValueError :
#     print('something went wrong')
    
    
# try:
#     age =30
#     if age >18:
#         raise ValueError("you must be 18 ")
        
# except ZeroDivisionError:
#     print('that was good')
    
    
age = 19
if age > 18:
    raise ValueError('18 or old')
    