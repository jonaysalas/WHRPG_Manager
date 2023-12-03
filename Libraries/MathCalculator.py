#In this file you can find the functions used for math calculation

def Calculate(text):
    '''
    Given a operation in String, it resolves it. Only supports integers and
    +, -, * & /
    :param text: An string with the operation. For example "3 + (6/2)"
    :return int: The result of the operation. Always an integer
    '''

    res = 0
    operands = ["+", "-", "*", "/"]

    #First, convert the operation in a list of numbers, operands and parentesis
    text = text.replace(" ","") #to remove spaces

    pile = []
    val = ""
    for i in text:
        if not i.isdigit():
            if val != "":
                pile.append(int(val))
                val = ""

            if i in operands:
                pile.append(i)
            elif i in ['(', ')']:
                pile.append(i)
            else:
                val += i
        else:
            val += i
    if val != "":
        pile.append(int(val))

    #Resolve the operations inside the parentesis. Starting from the deeper parentesis
    while "(" in pile:
        start = len(pile) -1 - pile[::-1].index('(') #it returns the index of the last(
        end = pile.index(')', start)

        while pile.index(')', start) - start > 2:
            if '*' in pile[start:end]:
                op_ind = pile[start:end].index('*')+start
            elif '/' in pile[start:end]:
                op_ind = pile[start:end].index('/')+star
            elif '-' in pile[start:end]:
                op_ind = pile[start:end].index('-')+start
            elif '+' in pile[start:end]:
                op_ind = pile[start:end].index('+')+start

            else:
                raise (Exception("NO SUPPORTED OPERAND FOUND IN: {}".format(text)))

            v1 = pile.pop(op_ind-1) #the first value is previous to the operand
            op = pile.pop(op_ind-1)
            v2 = pile.pop(op_ind-1)

            if op == '*':
                pile.insert(op_ind-1, v1*v2)
            elif op == '/':
                pile.insert(op_ind - 1, int(v1//v2))
            elif op == '+':
                pile.insert(op_ind - 1, v1+v2)
            elif op == '-':
                pile.insert(op_ind - 1, v1-v2)
        pile.pop(start)
        pile.pop(start+1)

    #Resolve all other operations until there is only one number
    while len(pile) > 1:
        if '*' in pile:
            op_ind = pile.index('*')
        elif '/' in pile:
            op_ind = pile.index('/')
        elif '-' in pile:
            op_ind = pile.index('-')
        elif '+' in pile:
            op_ind = pile.index('+')

        else:
            raise (Exception("NO SUPPORTED OPERAND FOUND IN: {}".format(text)))

        v1 = pile.pop(op_ind - 1)  # the first value is previous to the operand
        op = pile.pop(op_ind - 1)
        v2 = pile.pop(op_ind - 1)

        if op == '*':
            pile.insert(op_ind - 1, v1 * v2)
        elif op == '/':
            pile.insert(op_ind - 1, int(v1//v2))
        elif op == '+':
            pile.insert(op_ind - 1, v1 + v2)
        elif op == '-':
            pile.insert(op_ind - 1, v1 - v2)

    return pile.pop()