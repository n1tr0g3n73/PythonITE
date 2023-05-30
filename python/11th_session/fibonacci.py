import time

st = time.process_time()
def fib(n):
    if(n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
et = time.process_time()
print("excution time is:",(et - st)*1000)
