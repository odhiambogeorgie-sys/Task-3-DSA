"""
CCS 2214 - Task 3
Question 4: Recursive programs
(a) Sum of first N natural numbers
(b) Factorial of a number
(c) Nth term of the Fibonacci series
(d) Generate N terms of the Fibonacci series
"""


def sum_natural(n):
    """(a) Sum of the first n natural numbers."""
    if n <= 0:                  # base case
        return 0
    return n + sum_natural(n - 1)


def factorial(n):
    """(b) Factorial of n."""
    if n <= 1:                  # base case: 0! = 1! = 1
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """(c) Nth Fibonacci term (1st term = 0, 2nd term = 1)."""
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_series(n, i=1):
    """(d) Print n terms of the Fibonacci series recursively."""
    if i > n:                   # base case
        return
    print(fibonacci(i), end=" ")
    fibonacci_series(n, i + 1)


def main():
    n = int(input("(a) Enter N for sum of natural numbers: "))
    print(f"Sum of first {n} natural numbers = {sum_natural(n)}")

    n = int(input("\n(b) Enter a number for factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers")
    else:
        print(f"{n}! = {factorial(n)}")

    n = int(input("\n(c) Enter N for the Nth Fibonacci term: "))
    if n < 1:
        print("N must be at least 1")
    else:
        print(f"Term {n} of the Fibonacci series = {fibonacci(n)}")

    n = int(input("\n(d) Enter number of Fibonacci terms: "))
    print("Fibonacci series:", end=" ")
    fibonacci_series(n)
    print()


if __name__ == "__main__":
    main()
