# number_theory.py

# A module containing functions related to number theory
# UBC Math 210 Introduction to Mathematical Computing
# January 27, 2017

def factorial(N):
    """Compute N!=N(N-1) ... (2)(1)."""
    # Initialize the outpout variable to 1
    product = 1
    for n in range(2,N + 1):
        # Update the output variable
        product = product * n
    return product

def n_choose_k(N,K):
    """Compute N choose K."""
    return factorial(N) // (factorial(N - K) * factorial(K))

def divisors(N):
    """Return the list of divisors of N."""
    # Initialize the list of divisors
    divisor_list = [1]
    # Check division by d for d <= N/2
    for d in range(2,N // 2 + 1):
        if N % d == 0:
            divisor_list.append(d)
    divisor_list.append(N)
    return divisor_list

def is_square(N):
    """Determine is N is square."""
    return N == round(N**(0.5))**2

def rep_as_squares(N):
    """Find all representations of N as a sum of squares a**2 + b**2 = N."""
    reps = []
    stop = int((N/2)**0.5) + 1 # a must be less than \sqrt{N/2}
    for a in range(1,stop):
        b_squared = N - a**2
        if is_square(b_squared):
            b = round((b_squared)**(0.5))
            reps.append([a,b])
    return reps

def collatz(a):
    """Compute the Collatz sequence starting at a."""
    # Initialze the sequence with the fist value a.
    x_list = [a]
    # Continue computing values in the sequence until we reach 1.
    while x_list[-1] != 1:
        # Check if the last element in the list is even
        if x_list[-1] % 2 == 0:
            # Compute and append the new values
            x_list.append(x_list[-1] // 2)
        else:
            # Compute and append the new values
            x_list.append(3*x_list[-1] + 1)
    return x_list

def is_prime(N):
    "Determine whether or not N is a prime number."
    if N <= 1:
        return False
    # N is prime if N is only divisible by 1 and itself
    # We should test whether N is divisible by d for all 1 < d < N
    for d in range(2,N):
        # Check if N is divisible by d
        if N % d == 0:
            return False
    # If we exit the for loop, then N is not divisible by any d
    # Therefore N is prime
    return True