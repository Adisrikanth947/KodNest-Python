def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)

#factorial
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
#fibonacci series
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))

