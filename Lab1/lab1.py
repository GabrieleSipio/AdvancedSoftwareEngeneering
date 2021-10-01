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