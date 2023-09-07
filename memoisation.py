#create cache memory for storing fibonacci sequence values
fibonacci_cache = {}

def fibonacci(n):
    #function that displays nth term of fibonacci sequence
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0:
        value = 1
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        
    fibonacci_cache[n] = value 
    return value


for i in range(1,1001):
    print(i," : ",fibonacci(i))
    

