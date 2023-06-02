from lexer import lex_str 


file = open('LISP/input.txt', 'r', encoding="utf8")
try:
    for line in file.readlines():
        lex_str(line)

except:
    print("problem")

file.close()


