def fucntionCalculator(ops):
    val = None
    if len(ops) == 0:
        return val
    operands = []
    operators = []
    for op in ops:
        if op.isnumeric():
            operands.append(op)
    return val

def isOperator(char):
    if char != '+' and char != '-' and char != '*' and char != '/' and char != '^' and char != '(' and char != ')':
        return False
    else:
        return True

def getVariableName(equation):
    for op,i in zip(equation,range(1,len(equation))):
        varName = ''
        if not op.isnumeric() and not isOperator(op) and op != '.':
            varName += op
            for ch in equation[i:]:
                i += 1
                if not ch.isnumeric() and not isOperator(ch) and op != '.':
                    varName += ch
                else:
                    return varName, i
    return varName,-1

def checkVarName(equation,varName):
    index = 0
    for i in range(len(equation)):
        name,ind = getVariableName(equation[index:])
        if ind == -1:
            return True
        elif name != varName:
            return False
        index += ind - 1

def removeSpaces(equation):
    return equation.replace(' ','')

def raplaceVar(equation,varName,number):
    return equation.replace(varName,number)

def trimTerms(equation):
    ops = []
    i = 0
    while i < len(equation):
        ch = equation[i]
        i += 1
        if isOperator(ch):
            ops.append(ch)
        elif ch.isnumeric or ch == '.':
            number = ch
            for char in equation[i:]:
                if char.isnumeric() or char == '.':
                    number += char
                    i += 1
                else:
                    ops.append(number)
                    break
    return ops

name = 'x'
equation = '(5.5*' + name + ' - 4)^2 + 3*' + name + ' - 2'
print(equation)
equation = removeSpaces(equation)
print(equation)
print(getVariableName(equation))
print(checkVarName(equation,name))
equation = raplaceVar(equation,name,'123.5')
print(equation)
print(trimTerms(equation))