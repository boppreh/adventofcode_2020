import re

instructions = [(ins, int(n)) for ins, n in re.findall(r'(nop|acc|jmp) ([-+]\d+)', open('8.txt').read())]

def execute(instructions):
    next_i = 0
    executed = {next_i}
    accumulator = 0
    while True:
        instruction, n = instructions[next_i]
        if instruction == 'nop':
            next_i += 1
        elif instruction == 'acc':
            accumulator += n
            next_i += 1
        elif instruction == 'jmp':
            next_i += n
        if next_i in executed:
            return 'looped', accumulator
        elif next_i == len(instructions):
            return 'terminated', accumulator
        executed.add(next_i)

print(execute(instructions))

for i, (instruction, n) in enumerate(instructions):
    if instruction == 'acc': continue
    replacement = {'jmp': 'nop', 'nop': 'jmp'}[instruction]
    result, accumulator = execute(instructions[:i] + [(replacement, n)] + instructions[i+1:])
    if result == 'terminated':
        print('Accumulator is', accumulator, 'after replacing instruction', i, 'which was', instruction)