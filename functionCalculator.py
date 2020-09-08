# algorithm to evaluate a list of operands and operators in order
# it work basicly with 2 stacks one for operands and another for operators
# iterate of the input list ans check the high precedence
# check some errors in the operands, operators or parentheses
def functionCalculator(ops):
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

    if len(operators) != 0 and operators[-1] == '(':
        error = 'Please check your parentheses'
        return val,error
    if len(operators) != 0 and len(operands) != 1:
        error = 'Please check your equation, operands and operators are not matching'
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

# arithmetic operations and it could be expanded for more operations
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

# check if the char is an operator or not
def isOperator(char):
    if char != '+' and char != '-' and char != '*' and char != '/' and char != '^':
        return False
    else:
        return True

# algorithm to extract the first variable name in the equation
def getVariableName(equation):
    i = 1
    varName = ''
    for op in equation:
        if i > len(equation):
            if varName == '':
                return varName,-1
            else:
                return varName,i
        if not op.isnumeric() and not isOperator(op) and op != '.' and op != '(' and op != ')':
            varName += op
            for ch in equation[i:]:
                i += 1
                if not ch.isnumeric() and not isOperator(ch) and ch != '.' and ch != '(' and ch != ')':
                    varName += ch
                else:
                    return varName, i
        i += 1
    if varName == '':
        return varName,-1
    else:
        return varName,i

# check if the equation has multiple names or no operators before the variable
def checkVarName(equation,varName):
    index = 0
    error = None
    for i in range(len(equation)):
        name,ind = getVariableName(equation[index:])
        index += ind - 1
        if ind != -1 and len(name) != ind - 1 and not isOperator(equation[index - len(name) - 1]) and equation[index - len(name) - 1] != '(':
            error = 'Please put operands before variable name'
            return False,error
        if ind == -1:
            return True,error
        if name != varName:
            error = 'There is multiple variable names'
            return False, error
        if index >= len(equation):
            return True,error

# remove spaces from the equation to be independent of it
def removeSpaces(equation):
    return equation.replace(' ','')

# replace variable name with a specific number
def replaceVar(ops,varName,number):
    replaced_ops = []
    for op in ops:
        if op == varName:
            replaced_ops.append(float(number))
        else:
            replaced_ops.append(op)
    return replaced_ops

# crop the operands and operators of the equation in order
def trimTerms(equation,varName):
    ops = []
    i = 0
    while i < len(equation):
        ch = equation[i]
        if isOperator(ch) or ch == '(' or ch == ')':
            ops.append(ch)
        elif ch.isnumeric() or ch == '.':
            number = ch
            for char in equation[i + 1:]:
                if char.isnumeric() or char == '.':
                    number += char
                    i += 1
                else:
                    break
            ops.append(float(number))
        else:
            ops.append(varName)
            i += len(varName) - 1
        i += 1
    return ops

# test cases for the logic

# name = 'x'
# equation = '10*x'
# #equation = '(5.5*' + name + ' - 4*(5 + 6))^2 + 3*(' + name + ') - 2*x'
# #equation = '(2 * ' + name +  '^2) -3.5*' + name + '-6'
# print(equation)
# equation = removeSpaces(equation)
# print(equation)
# varName,_ = getVariableName(equation)
# print(varName)
# print(checkVarName(equation,varName))
# ops = trimTerms(equation,varName)
# print(ops)
# ops = replaceVar(ops,varName,'-4')
# print(ops)
# print(functionCalculator(ops))
