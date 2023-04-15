import prescription as prct
import tape

pointer = int(0)
register = 'START'
memory = tape.get_memory(pointer)
while True:
    if register == 'STOP':
        print('terminate')
        break
    else:
        memory = tape.get_memory(pointer)
        print(register, memory, end=' => ')
        register, val, direction = prct.get_action(register, memory)
        print(register, val, direction)
        tape.write(pointer, val)

        tape.print_tape()
        if direction == '>':
            pointer += 1
        elif direction == '<':
            pointer -= 1
        elif direction == '_':
            pass
        else:
            print("undefined behaviour")
            break