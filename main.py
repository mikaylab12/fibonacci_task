# defining a Fibonacci variable
def fibonacci(x):
    if x <= 1:
        return x
    else:
        return (fibonacci(x-2)) + fibonacci(x-1)
# number of terms
terms=20
# Fibonacci function in order to receive the first 20 terms and their values
if terms <= 0:
    print("Please enter a positive integer") # Fibonacci sequence does not contain negative integers
else:
    print("This is the fibonacci sequence for", terms, "terms:")
    for i in range(terms):
        print(fibonacci(i), end=" ")