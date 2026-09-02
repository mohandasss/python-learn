import json

# user = {
#     "name": "Mohan",
#     "age": 22,
#     "role": "Developer"
# }

# with open("user.json" , "w") as file:
#     json.dump(user,file)

with open("user.json", "r") as file:
     data=json.load(file)
    
print(data)