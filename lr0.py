# open table File 
f = open("table.txt", "r")
if f.mode == 'r':
    string = f.read()
string = string.replace(" ", "")
string = string.replace(']', '').replace('[', '')
string = string.replace("'", '').split(",")
string = string[::2]
string.reverse()
"""
DFA STATE Number :{
    "terminal or non terminal": [action, number]
}
action s => shift
action r => reduce
action g =>non-terminals production goto
"""
lr_table = {
    0: {
        "if": ['s', 2],
        "while": ['s', 3],
        "var": ['s', 4],
        "S": ['g', 1]
    },
    1: {
        "$": ['a', 1]
    },
    2: {
        ">": ['s', 5],
        "var": ['s', 6],
        "num": ['s', 7],
        "X": ['g', 8, 'X'],
        'E': ['g', 5, 'E']
    },
    3: {
        "var": ['s', 6],
        'num': ['s', 7],
        'X': ['g', 9, 'X'],
        'E': ['g', 5, 'E']
    },
    4: {
        '=': ['s', 10]
    },
    5: {
        "<": ['s', 13],
        ">": ['s', 12],
        'COP': ['g', 11, 'COP']
    },
    6: {
        '*': ['r', 8],
        '+': ['r', 8],
        '<': ['r', 8],
        '>': ['r', 8],
        'if': ['r', 8],
        'else': ['r', 8],
        'then': ['r', 8],
        'while': ['r', 8],
        'var': ['r', 8],
        'epsilon': ['r', 8],
        '$': ['r', 8],
    },
    7: {
        '*': ['r', 9],
        '+': ['r', 9],
        '<': ['r', 9],
        '>': ['r', 9],
        'if': ['r', 9],
        'else': ['r', 9],
        'then': ['r', 9],
        'while': ['r', 9],
        'var': ['r', 9],
        'epsilon': ['r', 9],
        '$': ['r', 9],
    },
    8: {
        "then": ['s', 14]
    },
    9: {
        'if': ['s', 2],
        'while': ['s', 3],
        'var': ['s', 4],
        'S': ['g', 15, 'S']
    },
    10: {
        'var': ['s', 6],
        'num': ['s', 7],
        'E': ['g', 16, 'E']
    },
    11: {
        'var': ['s', 6],
        'num': ['s', 7],
        'E': ['g', 17, 'E']
    },
    12: {
        'var': ['r', 12],
        'num': ['r', 12]
    },
    13: {
        'var': ['r', 13],
        'num': ['r', 13]
    },
    14: {
        'if': ['s', 2],
        'while': ['s', 3],
        'var': ['s', 4],
        'S': ['g', 18, 'S']
    },
    15: {
        'else': ['r', 3],
        'epsilon': ['r', 3],
        '$': ['r', 3]
    },
    16: {
        '*': ['s', 20],
        '+': ['s', 21],
        'AOP': ['g', 19, 'AOP']
    },
    17: {
        'if': ['r', 7],
        'then': ['r', 7],
        'while': ['r', 7],
        'var': ['r', 7]
    },
    18: {
        'else': ['s', 23],
        'epsilon': ['s', 24],
        'A': ['g', 22, 'A']
    },
    19: {
        'var': ['s', 6],
        'num': ['s', 7],
        'E': ['g', 25, 'E']
    },
    20: {
        'var': ['r', 10],
        'num': ['r', 10]
    },
    21: {
        'var': ['r', 11],
        'num': ['r', 11]
    },
    22: {
        'else': ['r', 2],
        'epsilon': ['r', 2],
        '$': ['r', 2]
    },
    23: {
        'if': ['s', 2],
        'while': ['s', 3],
        'var': ['s', 4],
        'S': ['g', 26, 'S']
    },
    24: {
        '<': ['r', 6],
        '>': ['r', 6],
        'else': ['r', 6],
        'epsilon': ['r', 6],
        '$': ['r', 6]
    },
    25: {
        'else': ['r', 4],
        'epsilon': ['r', 4],
        '$': ['r', 4]
    },
    26: {
        '<': ['r', 5],
        '>': ['r', 5],
        'else': ['r', 5],
        'epsilon': ['r', 5],
        '$': ['r', 5]
    }
}
"""
production number: [pop time number, non terminal, production string]
"""
prod_table = {
    1: [2, 'SPRIM', 'S->Sprim'],
    2: [10, 'S', 'S->if X then S A'],
    3: [6, 'S', 'S->while X S'],
    4: [10, 'S', 'S->var = E AOP E'],
    5: [4, 'A', 'A->else S'],
    6: [2, 'A', 'A->epsilon'],
    7: [6, 'X', 'X->E COP E'],
    8: [2, 'E', 'E->var'],
    9: [2, 'E', 'E->num'],
    10: [2, 'AOP', 'AOP->*'],
    11: [2, 'AOP', 'AOP->+'],
    12: [2, 'COP', 'COP->>'],
    13: [2, 'COP', "COP-><"]
}


def actionfunc(stack, action, inp, string,tree):
    print("action:",action)
    if action is None:
        action = lr_table.get(stack[-1]).get('epsilon')
        if action is None:
            print("ERORR!!!")
            return False
    if action[0] == 's':
        stack.append(inp)
        stack.append(action[1])
        print('shift\n')
        return True
    elif action[0] == 'r':
        string.append(inp)
        reduce = prod_table[action[1]]
        for i in range(reduce[0]):
            if len(stack) <= 1:
                flag = False
                print("ERORR!!!")
                return False
            stack.pop()
        temptree = []
        temptree.append(stack[1::2])
        tempstring = list(string)
        tempstring.reverse()
        temptree.append(tempstring)
        tree.append(temptree)
        print(stack)
        print('Reduce ' + reduce[2] + '\n')
        newaction = lr_table.get(stack[-1]).get(reduce[1])
        return actionfunc(stack, newaction, reduce[1], string,tree)
    elif action[0] == 'g':
        stack.append(inp)
        stack.append(action[1])
        return True
    elif action[0] == 'a':
        print("accept")
        return False


def parser(string):
    # initialize the stack
    stack = [0]
    flag = True
    tree = []
    temp = []
    temp = list(string)
    temp.reverse()
    tree.append(temp)
    while flag:
        print("stack:",stack)
        print("string:",string)
        if not string:
            inp = '$'
        else:
            inp = string.pop()
        action = lr_table.get(stack[-1]).get(inp)
        print("input:",inp)
        if not actionfunc(stack, action, inp, string,tree):
            break
        print("--------------------------------")
    for i in tree:
            print(i)

parser(string)
