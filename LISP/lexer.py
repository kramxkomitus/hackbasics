from enum import Enum
from dataclasses import dataclass
import pandas as pd

class Token_t(Enum):
    open = 1
    close = 2
    ID = 3
    string = 3
    number = 4

@dataclass

class Token:
    type: Token_t
    val: str

def lex_str(line: str):
        import re
        expression = list()
        pattern =  r"\s(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"
        line = re.split(pattern, line.strip())
        print()
        print(line)
        print('-'*100)
        print()
        for literal in line:
            token = Token(False, literal)
            if literal == '':
                continue
            if literal == '(':
                token.type = Token_t.open
            elif literal == '(':
                token.type = Token_t.close
            elif literal.isdigit():
                token.type = Token_t.number
            else:
                token.type = Token_t.ID
            expression.append(token)
        show_str(expression)
        return expression

def show_str(exp):
    print()
    print(exp)
    print("="*30, '\n')
    exp = pd.DataFrame(exp)
    exp = exp[['val', 'type']]
    print(exp)
