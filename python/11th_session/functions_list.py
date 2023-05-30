my_list = [10,1,3,8,2,4]

def print_list(list):
    for element in list:
        print(element)

def sum_list(list):
    s = 0
    for element in list:
        s += element
    return s

print_list(my_list)
sum = sum_list(my_list)
print("sum1:",sum)
print("sum2",sum_list(my_list))
