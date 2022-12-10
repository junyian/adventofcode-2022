
class CPU:
    def __init__(self):
        self.reg_X = 1
        self.V = 0
        self.cycle = 0
        self.queue = [(None,None)]
        self.score = 0

    def next_cycle(self):
        instruction = self.queue.pop(0)
        if instruction[0]=='addx':
            self.reg_X += instruction[1]
        else:
            pass
        self.cycle += 1
        self.check_cycle()
    
    def check_cycle(self):
        if (self.cycle - 20) % 40 == 0:
            self.print_cycle()
            self.score += self.cycle * self.reg_X

    def queue_instruction(self, instruction, arg=0):
        if instruction=='noop':
            self.queue.append(('noop',None))
        elif instruction=='addx':
            self.queue.append((None, None))
            self.queue.append(('addx', arg))

    def print_cycle(self):
        print(f"Cycle {self.cycle}: X={self.reg_X} SS={self.cycle * self.reg_X}")

cpu = CPU()

# cpu.queue_instruction('noop')
# cpu.queue_instruction('addx', 3)
# cpu.queue_instruction('addx', -5)

for l in open("input1.txt").readlines():
    if l.startswith('noop'):
        cpu.queue_instruction('noop')
    elif l.startswith('addx'):
        cpu.queue_instruction('addx', int(l.strip()[l.find(' '):]))

# print(cpu.queue)

while True:
    if len(cpu.queue) == 0:
        break
    else:
        cpu.next_cycle()
        cpu.print_cycle()
print(cpu.score)