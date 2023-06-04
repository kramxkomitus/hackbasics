import lexer

class S_exp_c:
    def __init__(self, car:lexer.Token, rest:list[lexer.Token] ) -> None:
        if car.type == lexer.Token_e.ID:
            self.command = car.val
        else:
            print("wrong token")
        self.args = rest
    
    def __str__(self) -> str:
        
        output = f"{self.command}(" 
        for item in self.args:
            output += f" {item}"
        output += " )"
        return output
    
        
def parse(token_list : lexer.lex_str):

    if isinstance(token_list, lexer.lex_str):
        token_list = token_list.expression
        
    if token_list[0].type == lexer.Token_e.open:
        if token_list[1].type == lexer.Token_e.ID:
            car = token_list[1]
            rest = list()
        else:
            print("wrong expression")
            return
        i = 2
        while i <= len(token_list[2:]) + 1:
            item = token_list[i]
            if item.type == lexer.Token_e.open:
                # No = token_list.index(item)
                result = parse(token_list[i:])
                s_exp = result[0]
                i = i + result[1]
                rest.append(s_exp)
            elif item.type == lexer.Token_e.close:
                res = S_exp_c(car, rest)
                print(res)
                return res, i
            else:
                rest.append(item)
            i += 1


file = open('LISP/input.txt', 'r', encoding="utf8")
try:
    for line in file.readlines():
        print(line)
        lexed = lexer.lex_str(line)
        lexed.show()
        result = parse(lexed)[0]
        print(result)


except:
    print("problem")

file.close()
