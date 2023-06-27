accept = "><+-.,[]"
pc = 0
program = ""

data_p = 0
mem = [0]

def getchar():
    s = ''
    while True:
        if len(s) == 0:
            s = input() + '\n'
        yield ord(s[0])
        s = s[1:]
getchar = getchar()

def inc_p():
    global data_p
    data_p += 1
    if data_p >= len(mem):
        mem.extend(len(mem) * [0])
def dec_p():
    global data_p
    data_p -= 1
    if data_p < 0:
        mem.insert(0, 0)
        data_p = 0
def inc_d():
    mem[data_p] = (mem[data_p] + 1) % (2**8)
def dec_d():
    mem[data_p] = (mem[data_p] + 127) % (2 ** 8)
def out_d():
    print(chr(mem[data_p]), end='')
def inp_d():
    mem[data_p] = next(getchar)
def beqz():
    global pc
    if mem[data_p] != 0:
        return
    br_dep = 1
    while br_dep:
        pc += 1
        if pc >= len(program):
            raise SyntaxError("Brackets does not match")
        if program[pc] == "[":
            br_dep += 1
        if program[pc] == "]":
            br_dep -= 1
def bnez():
    global pc
    if mem[data_p] == 0:
        return
    br_dep = 1
    while br_dep:
        pc -= 1
        if pc < 0:
            raise SyntaxError("Brackets does not match")
        if program[pc] == "]":
            br_dep += 1
        if program[pc] == "[":
            br_dep -= 1
inst = {
    ">": inc_p,
    "<": dec_p,
    "+": inc_d,
    "-": dec_d,
    ".": out_d,
    ",": inp_d,
    "[": beqz,
    "]": bnez
}

program = ''.join([i if i in accept else "" for i in input()])
while pc < len(program):
    inst[program[pc]]()
    pc += 1

