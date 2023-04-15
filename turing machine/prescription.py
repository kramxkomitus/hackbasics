prescription = dict()

def load(filename):
    global prescription
    try:
        file = open(filename, 'r', encoding="utf8")
        while True:
            line = file.readline()
            if not line:
                break
            A = list(map(lambda x: x.strip(), line.split(", ")))
            key = A[0] + A[1]
            val = (A[2], A[3], A[4])
            prescription[key] = val
    except:
        print("problem")
    file.close()
    print(prescription)
    return prescription

def get_action(register: str, memory: str):
    key = register + memory
    if key in prescription:
        return prescription[key]
    else:
        print("undefined behaviour")
        return None


load("./prog.txt")