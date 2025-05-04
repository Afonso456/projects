# Let's create a class that encapsulates all the functions we have written so far and add some more complex functionalities

class MathOperations:
    def __init__(self):
        self.memo_factorial = {}
        self.memo_fibonacci = {}

    def factorial(self, n):
        if n in self.memo_factorial:
            return self.memo_factorial[n]
        if n == 0:
            return 1
        else:
            self.memo_factorial[n] = n * self.factorial(n-1)
            return self.memo_factorial[n]

    def fibonacci(self, n):
        if n in self.memo_fibonacci:
            return self.memo_fibonacci[n]
        if n <= 1:
            return n
        else:
            self.memo_fibonacci[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
            return self.memo_fibonacci[n]

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def lcm(self, a, b):
        return abs(a*b) // self.gcd(a, b)

    def power(self, base, exp):
        if exp == 0:
            return 1
        elif exp % 2 == 0:
            half_power = self.power(base, exp // 2)
            return half_power * half_power
        else:
            return base * self.power(base, exp - 1)

# Now let's use this class to perform various operations
math_ops = MathOperations()

# Calculate the factorial of 5
result = math_ops.factorial(5)
print(f"The factorial of 5 is {result}")

# Calculate the 10th Fibonacci number
fib_result = math_ops.fibonacci(10)
print(f"The 10th Fibonacci number is {fib_result}")

# Calculate the GCD of 48 and 18
gcd_result = math_ops.gcd(48, 18)
print(f"The GCD of 48 and 18 is {gcd_result}")

# Check if 29 is a prime number
prime_result = math_ops.is_prime(29)
print(f"Is 29 a prime number? {prime_result}")

# Calculate the LCM of 12 and 15
lcm_result = math_ops.lcm(12, 15)
print(f"The LCM of 12 and 15 is {lcm_result}")

# Calculate 2 raised to the power of 10
power_result = math_ops.power(2, 10)
print(f"2 raised to the power of 10 is {power_result}")
# For example, let's write a simple Python program that prints "Hello, World!":

print("Hello, World!")
# Let's create a more complex function that calculates the factorial of a number using memoization
def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    else:
        memo[n] = n * factorial(n-1, memo)
        return memo[n]

# Now let's use this function to calculate the factorial of 5
result = factorial(5)
print(f"The factorial of 5 is {result}")

# Let's add another function that calculates the nth Fibonacci number using memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

# Now let's use this function to calculate the 10th Fibonacci number
fib_result = fibonacci(10)
print(f"The 10th Fibonacci number is {fib_result}")

# Let's add a function that calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Now let's use this function to calculate the GCD of 48 and 18
gcd_result = gcd(48, 18)
print(f"The GCD of 48 and 18 is {gcd_result}")

# Let's add a function that checks if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Now let's use this function to check if 29 is a prime number
prime_result = is_prime(29)
print(f"Is 29 a prime number? {prime_result}")