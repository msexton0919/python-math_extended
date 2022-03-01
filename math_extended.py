import math
from functools import reduce


# Function used to validate the input of other functions.
# Specifcally, checks to see if the input is less than some other integer. If so, raises an exception.
def validation(num, less_than=1):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num < less_than:
        raise ValueError(f'Argument must be greater than or equal to {less_than}')


# Returns the prime factors, with repeats, of a specific integer in the form of a list, by trial division.
# Example: prime_factors(36) = [2, 2, 3, 3]
def prime_factors(num):
    validation(num, 2)
    factor = 2
    sqrt = math.sqrt(num)
    factors = []
    while factor <= sqrt:
        if num % factor == 0:
            factors.append(factor)
            num //= factor
            sqrt = math.sqrt(num)
        elif factor == 2:
            factor += 1
        else:
            factor += 2
    if num > 1:
        factors.append(num)
    return factors


# Returns a list of pairs corresponding to the prime factorization of an integer
# where each pair is the prime factor and the number of occurrences.
# Example: prime_factors2(36) = [(2, 2), (3, 2)]
def prime_factors2(num):
    validation(num, 2)
    primes = prime_factors(num)
    prev = primes.pop(0)
    new_primes = []
    total = 1
    for val in primes:
        if prev == val:
            total += 1
        else:
            new_primes.append((prev, total))
            prev = val
            total = 1
    new_primes.append((prev, total))
    return new_primes


# Returns the Euler phi function value of a specific integer. Or, the amount of positive integers
# an integer is relatively prime to.
# Example: phi(10) = 4
def phi(num):
    arr = prime_factors(num)
    prev = arr.pop(0)
    mult = prev
    div = mult
    sub_one = (mult - 1)
    for val in arr:
        mult *= val
        if prev != val:
            div *= val
            sub_one *= (val - 1)
        prev = val
    return mult * sub_one // div


# Returns the number of factors a particular integer has.
# Example: number_of_factors(10) = 4
def number_of_factors(num):
    validation(num)
    num_factors = 1
    if num == 1:
        return 1
    factors = prime_factors(num)
    prev = factors.pop(0)
    total = 2
    for val in factors:
        if val != prev:
            prev = val
            num_factors *= total
            total = 1
        total += 1
    num_factors *= total
    return num_factors

# Returns the gcd, (greatest common divisor), of a variable length list of integers.
# Example: gcd(2, 3, 5, 7, 12, 15) = 1
def gcd(*args):
    validation(len(args), 2)

    #Helper function that returns the gcd of 2 integers.
    def gcd_help(num1, num2):
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return max(-num1, num1)

    return reduce(gcd_help, args)


# Returns the lcm, (least common multiple), of a variable length list of integers.
#Example: lcm(2, 3, 5, 7) = 210
def lcm(*args):

    # Helper function that returns the lcm of two integers.
    def lcm_help(num1, num2):
        gcd_val = gcd(num1, num2)
        return 0 if gcd_val == 0 else num1 * num2 // gcd_val

    return reduce(lcm_help, args)


# Returns the sum of the divisors of an integer, optionally can raise the divisors to some power then sum them.
# Example: sum_of_divisors(10) = 18, (1 + 2 + 5 + 10 = 18)
# Example: sum_of_divisors(10, 2) = 130, (1^2 + 2^2 + 5^2 + 10^2 = 130)
def sum_of_divisors(num, power=1):
    validation(num, 1)
    validation(power, 1)
    if num == 1:
        return 1

    def helper(pair):
        (base, exp) = pair
        return (base ** (power * (exp + 1)) - 1) // (base ** power - 1)

    sum_of = 1
    for (base, exp) in prime_factors2(num):
        sum_of *= helper((base, exp))
    return sum_of


# Returns whether an integer is square free. As in, are all powers of primes equal to 1?
# If so, return false, otherwise return true.
# Example: is_square_free(36) = false, (2 * 2 * 3 * 3 = 36)
def is_square_free(num):
    validation(num, 1)
    sqr_free = True
    if num > 1:
        primes = prime_factors2(num)
        for (prime, exp) in primes:
            if exp > 1:
                sqr_free = False
    return sqr_free


# Returns whether the given positive integer is a palindrome or not.
# Example: is_palindrome(2442) = true
# Example: is_palindrome(2443) = false
def is_palindrome(num):
    validation(num, 0)
    temp = num
    is_pal = 0
    while num > 0:
        is_pal *= 10
        is_pal += num % 10
        num = num // 10
        int(num)
    return is_pal == temp


# Returns whether a given integer is prime.
# Example: is_prime(7) = true
# Example: is_prime(6) = false
def is_prime(num):
    validation(num, 2)
    temp = 2
    sqrt = math.sqrt(num)
    while temp <= sqrt:
        if num % temp == 0:
            return False
        temp += 1
    return True


# Returns the number of unique primes for the integer given as input.
# Example: unique_primes(36) = 2, (2 * 2 * 3 * 3 = 36)
def unique_primes(num):
    return len(prime_factors2(num))


# Returns the value of the Liouville function. Returns 1 if input integer is made up of even number of primes
# -1 if input is made up of odd number of primes.
# Example: liouville(4) = 1
# Example: liouville(8) = -1
def liouville(num):
    primes = prime_factors2(num)
    summ = 0
    for (prime, exp) in primes:
        summ += exp
    return 1 if summ % 2 == 0 else -1


# Returns the sum of the digits for the given integer as input.
# Example: sum_of_digits(12445) = 16, (1 + 2 + 4 + 4 + 5 = 16)
def sum_of_digits(num):
    validation(num, 0)
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    return summ


# Returns the nth triangle number when given an integer as input.
# Example: triangle_num(7) = 28
def triangle_num(n):
    validation(n, 1)
    return n * (n + 1) // 2


# Returns the nth pentagonal number when given an integer as input.
# Example: pentagonal_num(6) = 51
def pentagonal_num(num):
    validation(num, 1)
    return num * (3 * num - 1) // 2


# Returns the nth hexagonal number when given an integer as input.
# Example: hexagonal_num(4) = 28
def hexagonal_num(num):
    validation(num, 1)
    return num * (2 * num - 1)


# Returns whether input integer is a non-increasing number.
# Example: non_increasing_number(222111) = true
# Example: non_increasing_number(2222212) = false
def non_increasing_number(num):
    validation(num, 10)
    curr = num % 10
    num //= 10
    non_inc = True
    while num > 0 and non_inc:
        temp = num % 10
        num //= 10
        if curr > temp:
            non_inc = False
        else:
            curr = temp
    return non_inc


# Returns whether input integer is a non-decreasing number.
# Example: non_decreasing_number(111112) = true
# Example: non_decreasing_number(2222212) = false
def non_decreasing_number(num):
    validation(num, 10)
    curr = num % 10
    num //= 10
    non_dec = True
    while num > 0 and non_dec:
        temp = num % 10
        num //= 10
        if curr < temp:
            non_dec = False
        else:
            curr = temp
    return non_dec


# Returns the number required for input integer to reach 1 following the rules of the
# Collatz conjecture. (Includes initial value as first step).
# Example: collatz(12) = 10
# Example: collatz(4) = 3
def collatz(num):
    validation(num, 1)
    length = 1
    while num > 1:
        num = num // 2 if num % 2 == 0 else 3 * num + 1
        length += 1
    return length
