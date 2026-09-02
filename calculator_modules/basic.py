def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        raise ValueError(" cannot be divide with 0")
    return a/b

def modulus(a,b):
    if b==0:
        raise ValueError("cannot be divide with zero")
    return a % b


