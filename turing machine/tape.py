def fill_line(filename: str):
    global tape
    global offset
    global negative
    global positive 
    try:
        file = open(filename, 'r', encoding="utf8")
        offset, negative, positive = file.readlines()   
        # сейчас строки а должны быть массивы

        negative = negative.strip().split(", ").reverse()
        positive = positive.strip().split(", ")

    except:
        print("problem")
    file.close()

def get_memory(No: int):
        if No >= 0:
            return positive[No]
        else:
            return negative[-No]

def write(No, val):
        if No >= 0:
            positive[No] = val
        else:
            negative[-No] = val

def print_tape():
    if not negative:
        tape = positive
    elif not positive:
        tape = negative.reverce()
    else:
         tape = negative.reverce() + positive
    print(tape)
     
fill_line("./data.txt")