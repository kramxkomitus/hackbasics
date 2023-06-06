import lexer
import LISP_parser as parser



def eval(s_exp: parser.S_exp_c):
    import functions
    function = getattr(functions, s_exp.command)
    print(function.__name__)
    # getattr gets attributes of LISP.functions, so functions can be attributes too
    result = function(s_exp.args)
    # * - asterisk or unpacking operator, unpacks elements from the sequence into 
    # args of function
    print(result)
    return result



file = open('LISP/input.txt', 'r', encoding="utf8")
try:
    for line in file.readlines():
        print(line)
        lexed = lexer.lex_str(line)
        lexed.show()
        result = parser.parse(lexed)[0]
        print(result)
        eval(result)


except:
    print("problem")

file.close()
