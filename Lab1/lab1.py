#calculator.py

def sum(m,n):
    if type(n) is int :
        for i in range(abs(n)):
            if n > 0 : 
                m += 1
            else :
                m -= 1
        return m
    raise ValueError("It works only in Z")

def divide(m,n):
    absM = abs(m)
    absN = abs(n)
    i = 0
    if type(n) is int and n != 0 :
        while absM >= absN:
                absM -= absN
                i +=1  
        if (n > 0 and m > 0) or (n < 0 and m < 0):
            return i
        else :
            return -i
    raise ZeroDivisionError("It only works with positives != 0")

def subtract (m,n):
    if type(n) is int:
        for i in range(abs(n)):
            if (m > 0 and n > 0) or (m < 0 and n < 0):
                m -= 1
            else:
                m +=1
        return m
    raise ValueError("It works only in Z")

def multiply(m,n):
    if type(n) is int :
        result=0
        for i in range(abs(n)):
            result += abs(m)
        if m > 0 and n < 0 or m < 0 and n > 0:
            return - result
        return result
    raise ValueError("It works only in Z")

def gcd(a, b):
    if type(a) is int and type(b) is int:
        if a == 0 :
            return b
        return gcd(b%a, a)