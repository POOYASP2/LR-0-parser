<h1>LR Parser :</h1>

<h3>first we get table token from phase 1 </h3>

<b><p>and clean the input from file </p></b>


```python
f = open("table.txt", "r")
if f.mode == 'r':
    string = f.read()
string = string.replace(" ", "")
string = string.replace(']', '').replace('[', '')
string = string.replace("'", '').split(",")
string = string[::2]
print(string)
```

    ['if', 'var', '>', 'var', 'then', 'while', 'var', '>', 'var', 'var', '=', 'var', '+', 'num', '$']


<p>string is our input to parser:</p>
<h3> Input Example :</h3>
<h4>['if', 'var', '+', 'num', 'then', 'var', '=', 'var', '+', 'num', '$']</h4>

<h3>Output Example:</h3>
<code>
['if', 'var', '<', 'var', 'then', 'var', '=', 'var', '+', 'num', '$']
[['if'], ['<', 'var', 'then', 'var', '=', 'var', '+', 'num', '$']]
[['if', 'E'], ['var', 'then', 'var', '=', 'var', '+', 'num', '$']]
[['if', 'E', 'COP'], ['then', 'var', '=', 'var', '+', 'num', '$']]
[['if'], ['then', 'var', '=', 'var', '+', 'num', '$']]
[['if', 'X', 'then', 'var', '='], ['+', 'num', '$']]
[['if', 'X', 'then', 'var', '=', 'E'], ['num', '$']]
[['if', 'X', 'then', 'var', '=', 'E', 'AOP'], ['$']]
[['if', 'X', 'then'], ['$']]
[['if', 'X', 'then', 'S'], ['$']]
[[], ['$']]</code>

<h2>Define table(lr(0) table) and gramer:</h2> 


```python
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

```

<h2>Define action function(for Shift , Reduce , accept , and not accept)</h2>


```python
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
```

<h2>Define function parser and print Tree ...</h2>


```python
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

```

<h2>and run function output </h2>


```python
parser(string)
```

    stack: [0]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then', 'var', '>', 'var', 'if']
    input: if
    action: ['s', 2]
    shift
    
    --------------------------------
    stack: [0, 'if', 2]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then', 'var', '>', 'var']
    input: var
    action: ['s', 6]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'var', 6]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then', 'var', '>']
    input: >
    action: ['r', 8]
    [0, 'if', 2]
    Reduce E->var
    
    action: ['g', 5, 'E']
    --------------------------------
    stack: [0, 'if', 2, 'E', 5]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then', 'var', '>']
    input: >
    action: ['s', 12]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'E', 5, '>', 12]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then', 'var']
    input: var
    action: ['r', 12]
    [0, 'if', 2, 'E', 5]
    Reduce COP->>
    
    action: ['g', 11, 'COP']
    --------------------------------
    stack: [0, 'if', 2, 'E', 5, 'COP', 11]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then', 'var']
    input: var
    action: ['s', 6]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'E', 5, 'COP', 11, 'var', 6]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then']
    input: then
    action: ['r', 8]
    [0, 'if', 2, 'E', 5, 'COP', 11]
    Reduce E->var
    
    action: ['g', 17, 'E']
    --------------------------------
    stack: [0, 'if', 2, 'E', 5, 'COP', 11, 'E', 17]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then']
    input: then
    action: ['r', 7]
    [0, 'if', 2]
    Reduce X->E COP E
    
    action: ['g', 8, 'X']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while', 'then']
    input: then
    action: ['s', 14]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var', 'while']
    input: while
    action: ['s', 3]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>', 'var']
    input: var
    action: ['s', 6]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'var', 6]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>']
    input: >
    action: ['r', 8]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3]
    Reduce E->var
    
    action: ['g', 5, 'E']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'E', 5]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var', '>']
    input: >
    action: ['s', 12]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'E', 5, '>', 12]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var']
    input: var
    action: ['r', 12]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'E', 5]
    Reduce COP->>
    
    action: ['g', 11, 'COP']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'E', 5, 'COP', 11]
    string: ['$', 'num', '+', 'var', '=', 'var', 'var']
    input: var
    action: ['s', 6]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'E', 5, 'COP', 11, 'var', 6]
    string: ['$', 'num', '+', 'var', '=', 'var']
    input: var
    action: ['r', 8]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'E', 5, 'COP', 11]
    Reduce E->var
    
    action: ['g', 17, 'E']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'E', 5, 'COP', 11, 'E', 17]
    string: ['$', 'num', '+', 'var', '=', 'var']
    input: var
    action: ['r', 7]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3]
    Reduce X->E COP E
    
    action: ['g', 9, 'X']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9]
    string: ['$', 'num', '+', 'var', '=', 'var']
    input: var
    action: ['s', 4]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4]
    string: ['$', 'num', '+', 'var', '=']
    input: =
    action: ['s', 10]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10]
    string: ['$', 'num', '+', 'var']
    input: var
    action: ['s', 6]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'var', 6]
    string: ['$', 'num', '+']
    input: +
    action: ['r', 8]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10]
    Reduce E->var
    
    action: ['g', 16, 'E']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'E', 16]
    string: ['$', 'num', '+']
    input: +
    action: ['s', 21]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'E', 16, '+', 21]
    string: ['$', 'num']
    input: num
    action: ['r', 11]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'E', 16]
    Reduce AOP->+
    
    action: ['g', 19, 'AOP']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'E', 16, 'AOP', 19]
    string: ['$', 'num']
    input: num
    action: ['s', 7]
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'E', 16, 'AOP', 19, 'num', 7]
    string: ['$']
    input: $
    action: ['r', 9]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'E', 16, 'AOP', 19]
    Reduce E->num
    
    action: ['g', 25, 'E']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'var', 4, '=', 10, 'E', 16, 'AOP', 19, 'E', 25]
    string: ['$']
    input: $
    action: ['r', 4]
    [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9]
    Reduce S->var = E AOP E
    
    action: ['g', 15, 'S']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'while', 3, 'X', 9, 'S', 15]
    string: ['$']
    input: $
    action: ['r', 3]
    [0, 'if', 2, 'X', 8, 'then', 14]
    Reduce S->while X S
    
    action: ['g', 18, 'S']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'S', 18]
    string: ['$']
    input: $
    action: None
    shift
    
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'S', 18, '$', 24]
    string: []
    input: $
    action: ['r', 6]
    [0, 'if', 2, 'X', 8, 'then', 14, 'S', 18]
    Reduce A->epsilon
    
    action: ['g', 22, 'A']
    --------------------------------
    stack: [0, 'if', 2, 'X', 8, 'then', 14, 'S', 18, 'A', 22]
    string: ['$']
    input: $
    action: ['r', 2]
    [0]
    Reduce S->if X then S A
    
    action: ['g', 1]
    --------------------------------
    stack: [0, 'S', 1]
    string: ['$']
    input: $
    action: ['a', 1]
    accept
    ['if', 'var', '>', 'var', 'then', 'while', 'var', '>', 'var', 'var', '=', 'var', '+', 'num', '$']
    [['if'], ['>', 'var', 'then', 'while', 'var', '>', 'var', 'var', '=', 'var', '+', 'num', '$']]
    [['if', 'E'], ['var', 'then', 'while', 'var', '>', 'var', 'var', '=', 'var', '+', 'num', '$']]
    [['if', 'E', 'COP'], ['then', 'while', 'var', '>', 'var', 'var', '=', 'var', '+', 'num', '$']]
    [['if'], ['then', 'while', 'var', '>', 'var', 'var', '=', 'var', '+', 'num', '$']]
    [['if', 'X', 'then', 'while'], ['>', 'var', 'var', '=', 'var', '+', 'num', '$']]
    [['if', 'X', 'then', 'while', 'E'], ['var', 'var', '=', 'var', '+', 'num', '$']]
    [['if', 'X', 'then', 'while', 'E', 'COP'], ['var', '=', 'var', '+', 'num', '$']]
    [['if', 'X', 'then', 'while'], ['var', '=', 'var', '+', 'num', '$']]
    [['if', 'X', 'then', 'while', 'X', 'var', '='], ['+', 'num', '$']]
    [['if', 'X', 'then', 'while', 'X', 'var', '=', 'E'], ['num', '$']]
    [['if', 'X', 'then', 'while', 'X', 'var', '=', 'E', 'AOP'], ['$']]
    [['if', 'X', 'then', 'while', 'X'], ['$']]
    [['if', 'X', 'then'], ['$']]
    [['if', 'X', 'then', 'S'], ['$']]
    [[], ['$']]
