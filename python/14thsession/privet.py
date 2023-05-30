class numbers:
    
    def __init__(self):
        self.__number =0
    def increment(self):
        self.__number+=1
    def decrement(self):
        self.__number-=1
    def get_value(self):
        return self.__number
    
num = numbers()
num.increment()
print(num.get_value())

print(num.__number)