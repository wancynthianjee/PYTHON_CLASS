class Student:
    name ="Marrion"
    age = 23
    school ="AkiraChix"
    nationality ="Kenyan"

class Student:
    school="AkiraChix"
    def __init__(self,name,age,country):
        self.name =name
        self.age =age
        self.country =country
    def greet_student(self):
        return (f"Hello{self.name}from{self.country}.We welcome you to {self.school}")
