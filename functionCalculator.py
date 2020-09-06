def fucntionCalculator(ops):
    val = None
    error = None
    # low number high precedence
    precedence = {'(':6,'^':5,'/':4,'*':3,'+':2,'-':1}
    if len(ops) == 0:
        error = 'Please enter an equation'
        return val,error
    operands = []
    operators = []
    for op in ops:
        # check if the element is a number
        if not isOperator(op) and op != '(' and op != ')':
            # add to the operands list
            operands.append(op)
        # check if the element is an operator or left parentheses
        elif isOperator(op) or op == '(':
            # check if there's no operators in the list or the precedence of the op is higher than the last one in the list
            if len(operators) == 0 or precedence[op] > precedence[operators[-1]]:
                # add to operators list
                operators.append(op)
            else:
                # evaluate all in the list until the operators list became empty
                while len(operators) > 0 and precedence[op] <= precedence[operators[-1]] and isOperator(operators[-1]):
                    # check if there's enough operands
                    if len(operands) < 2:
                        error = 'Please check your operators'
                        return val, error
                    else:
                        # evaluate the operation
                        operation = evaluate(operators[-1],operands[-2],operands[-1])
                        # remove the last 2 operands and last operator then add the value of the operation
                        operands.pop()
                        operands.pop()
                        operators.pop()
                        operands.append(operation)
                operators.append(op)

        # elif op == '(':
        #     operators.append(op)
        elif op == ')':
            # check if the operators list isn't empty and the last element is operator not parentheses
            while len(operators) > 0 and isOperator(operators[-1]):
                # check if there's enough operands
                if len(operands) < 2:
                    error = 'Please check your operators'
                    return val, error
                else:
                    # evaluate the operation
                    operation = evaluate(operators[-1], operands[-2], operands[-1])
                    # remove the last 2 operands and last operator then add the value of the operation
                    operands.pop()
                    operands.pop()
                    operators.pop()
                    operands.append(operation)
            if len(operators) > 0 and operators[-1] == '(':
                operators.pop()
            else:
                error = 'Please check your parentheses'
                return val, error
    while len(operators) > 0 and isOperator(operators[-1]):
        # check if there's enough operands
        if len(operands) < 2:
            error = 'Please check your operators'
            return val, error
        else:
            # evaluate the operation
            operation = evaluate(operators[-1], operands[-2], operands[-1])
            # remove the last 2 operands and last operator then add the value of the operation
            operands.pop()
            operands.pop()
            operators.pop()
            operands.append(operation)

    if len(operators) != 0 and len(operands) != 1:
        error = 'Please check your equation, operands and operators are not matching'
        return val,error
    if len(operators) == 1 and operators[0] == '(':
        error = 'Please check your parentheses'
        return val,error
    if len(operators) != 0:
        error = 'Please check your operators'
        return val,error
    if len(operands) != 1:
        error = 'Please check your operands'
        return val,error

    val = operands[0]
    operands.clear()
    return val, error

def evaluate(operator,op1,op2):
    operation = None
    if operator == '^':
        operation = op1 ** op2
    elif operator == '/':
        operation = op1 / op2
    elif operator == '*':
        operation = op1 * op2
    elif operator == '+':
        operation = op1 + op2
    elif operator == '-':
        operation = op1 - op2

    return operation


def isOperator(char):
    if char != '+' and char != '-' and char != '*' and char != '/' and char != '^':
        return False
    else:
        return True

def getVariableName(equation):
    for op,i in zip(equation,range(1,len(equation))):
        varName = ''
        if not op.isnumeric() and not isOperator(op) and op != '.' and op != '(' and op != ')':
            varName += op
            for ch in equation[i:]:
                i += 1
                if not ch.isnumeric() and not isOperator(ch) and ch != '.' and ch != '(' and ch != ')':
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
        if isOperator(ch) or ch == '(' or ch == ')':
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
#equation = '34'
equation = '(5.5*' + name + ' - 4*(5 + 6))^2 + 3*' + name + ' - 2'
#equation = '(2 * ' + name +  '^2) -3.5*' + name + '-6'
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
