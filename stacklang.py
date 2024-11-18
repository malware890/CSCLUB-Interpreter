import sys

# GET FILE PATH
filepath = sys.argv[1]

# GET EACH LINE OF THE PROGRAM
lines = []
with open(filepath) as program_file:
    lines = [line.strip() for line in program_file.readlines()]
    
program = [] # INITIALIZES LIST TO HOLD ALL OF OUR INSTRUCTIONS AND INSTRUCTION PARAMETERS

# PARSE AND TOKENIZE FILE
for line in lines:
    parts = line.split(" ")
    opcode = parts[0]
    
    program.append(opcode)
    
    if opcode == "PUSH":
        operand = int(parts[1])
        program.append(operand)
    elif opcode == "PRINT":
        message = ' '.join(parts[1:])
        program.append(message)


# STACK MEMORY SYSTEM
class Stack:
    def __init__(self, size):
        self.buffer = [0 for _ in range(size)] # ENTIRE STACK MEMORY, ALL SPOTS IN MEMORY INITIALIZED TO 0
        self.sp = -1 # STACK POINTER TO KEEP TRACK OF THE TOP OF MEMORY
        
    def push(self, number):
        self.sp += 1 # MOVES STACK POINTER UP BY ONE
        self.buffer[self.sp] = number # PUTS NUMBER AT NEW TOP LOCATION
    
    def pop(self):
        number = self.buffer[self.sp] # TAKES TOP NUMBER
        self.sp -= 1 # MOVES STACK POINTER DOWN BY ONE
        return number

    def __str__(self):
        for i in self.buffer:
            if isinstance(i, int):
                print(i)
    

ip = 0 # instruction pointer, keeps track of current instruction to be executed
stack = Stack(256) # Our program's actual stack

while program[ip] != "END":  # WHILE CURRENT INSTRUCTION IS NOT END
    opcode = program[ip] # GET
    ip += 1
    
    if opcode == "PUSH":
        stack.push(program[ip])
        ip += 1
    elif opcode == "POP":
        stack.pop()
    elif opcode == "ADD":
        a, b = stack.pop(), stack.pop()
        stack.push(a + b)
    elif opcode == "SUB":
        a, b = stack.pop(), stack.pop()
        stack.push(b - a)
    elif opcode == "PRINT":
        print(program[ip])
        ip += 1
    elif opcode == "READ":
        number = int(input())
        stack.push(number)


# push: Push number ontop of stack
# pop: pop number from stack (and return)
# add: pops 2 numbers from the stack and pushes sum
# sub: add except subtract the numbers
# print: takes in a string and prints it to terminal
# read: reads number from terminal and pushes
# end: program ends
