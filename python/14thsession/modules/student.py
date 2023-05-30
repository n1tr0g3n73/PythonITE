from person import Person
from teacher import teacher

class student(Person,teacher):
    def __init__(self,first_name,last_name,modules):
        self._modules = modules
        super().__init__(first_name,last_name)
    def __str__(self):
        return f"{self._modules}\n {super().__str__()}"