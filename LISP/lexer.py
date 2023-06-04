from enum import Enum
from dataclasses import dataclass
import pandas as pd
import re

# @dataclass

class Token_e(Enum):
    open = 1
    close = 2
    ID = 3
    string = 3
    number = 4

class Token:
    def __init__(self, string:str) -> None:

        self.type = Token_e
        self.val = string

        if self.val == '(':
            self.type = Token_e.open
        elif self.val == ')':
            self.type = Token_e.close
        elif self.val.isdigit() \
                or self.val.replace('.', '').isdigit() \
                or self.val.replace(',', '').isdigit():
            self.type = Token_e.number
        else:
            self.type = Token_e.ID

    def __str__(self) -> str:
        return str(self.val)

class lex_str:
    def __init__(self, string: str) -> None:

        self.expression = list()
        
        string = string.replace('(', '( ')
        string = string.replace(')', ' )')
        pattern =  r"\s(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"
        string = re.split(pattern, string.strip())
        for literal in string:
            if literal != '':
                token = Token(literal)
                self.expression.append(token)
    
    def __getitem__(self, index):
        return self.expression[index]
    

    def show(self):
        print("="*30, '\n')
        cute_output = {
            'type': [T.type for T in self.expression],
            'value': [T.val for T in self.expression]
        }
        print(pd.DataFrame(cute_output))

        
