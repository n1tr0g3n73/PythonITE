class number:
    def __init__(self):
        self._number =0
    def increment(self):
        self._number+=1
    def decrement(self):
        self._number-=1
    def get_value(self):
        return self._number
    
num = number()
num.increment()
print(num.get_value())