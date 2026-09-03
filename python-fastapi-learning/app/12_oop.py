
class Car:
    def __init__(self, company , model , year):
        self.company = company
        self.model = model
        self.year = year 
    
    def info(self):
        print(f'{self.company} {self.model} was manufractured in {self.year}')


class ElecTricCard(Car):
    def charge(self):
        print(f'{self.company} is charging')


car=ElecTricCard('Audi' , "HW001" , 2016)
# car1=ElecTricCard('BMW' , "BMW001" , 2026)

car.info()
car.charge()


