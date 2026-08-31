from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"message" : "Hello, World!"}


# name = "FastAPI Learning App"
# salary = 80000
# isDeveloper= False
age = int("25")
price = float("99.5")
number = str(100)



print('helloooooo' , type(number)) 