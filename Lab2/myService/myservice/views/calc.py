from flakon import JsonBlueprint
from flask import Flask, request, jsonify

calc = JsonBlueprint("calc", __name__)

@calc.route("/calc/sum", methods=["GET"])
def sum():

    m = int(request.args.get("m"))
    n = int(request.args.get("n"))

    if type(n) is int :
        for i in range(abs(n)):
            if n > 0 : 
                m += 1
            else :
                m -= 1
        return jsonify(({"result":str(m)}))
    raise ValueError("It works only in Z")

@calc.route("/calc/diff", methods=["GET"])
def diff():
    m = int(request.args.get("m"))
    n = int(request.args.get("n"))
    if type(n) is int:
        result = m 
        for i in range(abs(n)):
            if (m > 0 and n > 0) or (m < 0 and n > 0):
                result -= 1
            else:
                result +=1
        return jsonify(({"result":str(result)}))
    raise ValueError("It works only in Z")

@calc.route("/calc/mult", methods=["GET"])
def mult():
    m = int(request.args.get("m"))
    n = int(request.args.get("n"))
    if type(n) is int :
        result=0
        for i in range(abs(n)):
            result += abs(m)
        if m > 0 and n < 0 or m < 0 and n > 0:
            return jsonify(({"result":str(-result)}))
        return jsonify(({"result":str(result)}))
    raise ValueError("It works only in Z")

@calc.route("/calc/div",methods=["GET"])
def div():
    m = int(request.args.get("m"))
    n = int(request.args.get("n"))
    absM = abs(m)
    absN = abs(n)
    i = 0
    if type(n) is int and n != 0 :
        while absM >= absN:
                absM -= absN
                i +=1  
        if (n > 0 and m > 0) or (n < 0 and m < 0):
            return jsonify(({"result":str(i)}))
        else :
            return jsonify(({"result":str(-i)}))
    raise ZeroDivisionError("It only works with positives != 0")
