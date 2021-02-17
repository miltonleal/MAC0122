import re


def BuscaUnarios(exp):
    if exp[0] == "-":
        exp[0] = "@"
    elif exp[0] == "+":
        del exp[0]

    for j in range(2, len(exp) - 1):
        if exp[j] == "+":
            if exp[j - 1] == "(" or exp[j - 1] == ")" or exp[j - 1] == "*" or exp[j - 1] == "/" \
                    or exp[j - 1] == "%" or exp[j - 1] == "//" or exp[j - 1] == "**":
                del exp[j]

    for j in range(2, len(exp) - 1):
        if exp[j] == "-":
            if exp[j - 1] == "(" or exp[j - 1] == ")" or exp[j - 1] == "+" or exp[j - 1] == "*" or \
                    exp[j - 1] == "/" or exp[j - 1] == "%" or exp[j - 1] == "//" or exp[j - 1] == "**":
                exp[j] = "@"

    return exp


def Transforma_Int_Float(exp):
    for j in range(len(exp)):
        if '.' in exp[j]:
            exp[j] = float(exp[j])
        elif '0' in exp[j] or '1' in exp[j] or '2' in exp[j] or '3' in exp[j] or \
                '4' in exp[j] or '5' in exp[j] or '6' in exp[j] or '7' in exp[j] or \
                '8' in exp[j] or '9' in exp[j]:
            exp[j] = int(exp[j])
    return exp


while True:
    exp = input(">>> ")
    r = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/\%][\*\*]?[\/\/]?)", exp)

    print(Transforma_Int_Float(BuscaUnarios(r)))
