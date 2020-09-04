def fucntionCalculator(ops):
    val = None
    error = 'No error'
    precedence = {'(':0,')':1,'^':2,'/':3,'*':4,'+':5,'-':6}
    if len(ops) == 0:
        error = 'Please enter an equation'
        return val,error
    operands = []
    operators = []
    for op,i in zip(ops,range(len(ops))):
        if len(operators) != 0:
            if isOperator(op):
                if precedence[op] < precedence[operators[-1]]:
                    operators.append(op)
                    continue
                operator = operators[-1]
                if operator == '^':
                    operation = operands[-2] ** operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '/':
                    operation = operands[-2] / operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '*':
                    operation = operands[-2] * operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '+':
                    operation = operands[-2] + operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '-':
                    operation = operands[-2] - operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                operators.append(op)

            else:
                operands.append(op)
                if i != len(ops) - 1 and isOperator(ops[i + 1]) and precedence[ops[i + 1]] < precedence[operators[-1]]:
                    continue
                operator = operators[-1]
                if operator == '^':
                    operation = operands[-2] ** operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '/':
                    operation = operands[-2] / operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '*':
                    operation = operands[-2] * operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '+':
                    operation = operands[-2] + operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)
                elif operator == '-':
                    operation = operands[-2] - operands[-1]
                    operators.pop()
                    operands.pop()
                    operands.pop()
                    operands.append(operation)

        else:
            if isOperator(op):
                operators.append(op)
            else:
                operands.append(op)

    if len(operators) != 0 and len(operands) != 1:
        error = 'Please check your equation, operands and operators are not matching'
        return val,error
    if len(operators) != 0:
        error = 'Please check your operators, There is unused operators'
        return val,error
    if len(operands) != 1:
        error = 'Please check your operands, There is unused operands'
        return val,error

    val = operands[0]
    operands.clear()
    operators.clear()
    return val, error

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
        if isOperator(ch):
            ops.append(ch)
        elif ch.isnumeric or ch == '.':
            number = ch
            for char in equation[i + 1:]:
                if char.isnumeric() or char == '.':
                    number += char
                    i += 1
                else:
                    break
            ops.append(float(number))
        i += 1
    return ops

name = 'x'
#equation = '(5.5*' + name + ' - 4)^2 + 3*' + name + ' - 2'
equation = '2 * ' + name +  '^2 -3.5*' + name + '-6'
print(equation)
equation = removeSpaces(equation)
print(equation)
print(getVariableName(equation))
print(checkVarName(equation,name))
equation = raplaceVar(equation,name,'4')
print(equation)
ops = trimTerms(equation)
print(ops)
print(fucntionCalculator(ops))
