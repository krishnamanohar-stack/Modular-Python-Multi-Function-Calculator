def gcd(a, b):
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for 0 and 0")

    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def hcf(a, b):
    return gcd(a, b)

def lcm(a, b):
    gcd_result = gcd(a, b)

    return abs(a * b) // gcd_result

def is_prime(n):
    count =0
    i=1

    while i<=n:
        if n%i==0:
            count +=1
        i=i+1

    if count ==2:
        return True
    else:
        return False

    
def prime_factors(n):
    factors =[]
    i=2
    while i<=n:
        if n%i==0:
            factors.append(i)
            n=n//i
        else:
            i=i+1
    return factors

def fibonacci(n):
    n1=0
    n2=1
    if n == 0:
        return n1
    if n == 1 :
        return n2
    for next_number in range(2,n+1):
        next_number= n1 + n2
        n1 = n2
        n2 = next_number
    return n2

def fibonacci_series(n):
    n1=0
    n2=1
    if n == 0:
        return[]
    if n == 1:
        return [0]
    series = [0,1]
    for  next_number in range(2,n+1):
        next_number= n1+n2
        series.append(next_number)
        n1 =n2
        n2 = next_number
    return series

def perfect_number(n):

    total = 0
    i = 1

    while i<n:
        if  n%i ==0:
            total = total+i
        i = i+1
    if total == n:
        return True
    else :
        return False
    
def divisors(n):
    factors = []
    i = 1
    while i <= n:
        if n%i == 0:
            factors.append(i)
        i = i+1
    return factors

def sum_of_divisors(n):
    exisitig_divisors = divisors(n)
    total = 0
    for num in exisitig_divisors:
        total = total + num
    return total

def armstrong_numbers(n):

    original_number = n
    total = 0
    powers = len(str(n))
    while n > 0:
        remainder = n%10
        total = total + remainder**powers
        n = n//10

    if sum == original_number:
        return True
    else:
        return False



    