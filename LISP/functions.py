import LISP_parser
import lexer
import eval

args_dict = {

}


def add(args: list):
    sum = 0
    for arg in args:
        if isinstance(arg, LISP_parser.S_exp_c):
            arg = eval.eval(arg)
            print(f"eval s_exp {arg}")
        if arg.type == lexer.Token_e.number:
           sum += float(arg.val)
    return lexer.Token(str(sum))