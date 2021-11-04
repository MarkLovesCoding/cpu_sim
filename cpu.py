from cache import Cache
from memory_bus import Memory_Bus

CPU_COUNTER_INIT = 0
NUMBER_OF_REGISTERS = 9

ADD_INSTRUCTION  = "ADD"
ADD_I_INSTRUCTION = "ADDI"
JUMP_INSTRUCTION = "J"
CACHE_INSTRUCTION = "CACHE"
SUBTRACT_INSTRUCTION  = "SUB"

CACHE_OFF_VAL = 0
CACHE_ON_VAL = 1
CACHE_FLUSH_VAL = 2

# get second value from register value converted to integer
def convert_register_to_index(val):
    return int(val[1:])


class CPU:
    
    def __init__(self):
        self.cpu_counter = CPU_COUNTER_INIT
        self.registers = [0]* NUMBER_OF_REGISTERS
        self.cache_flag = False
        self.cache = Cache()
        self.memory_bus = Memory_Bus()

    # counter functions
    def reset_counter(self):
        self.cpu_counter = CPU_COUNTER_INIT
    
    def increment_counter(self):
        self.cpu_counter += 1
    
    def set_counter(self, value):
        self.cpu_counter = value
    
    def get_counter(self):
        return self.cpu_counter
    
    # push through cache and memory functions

    def flush_cache(self):
        self.cache.flush_cache()

    def search_in_cache(self,address):
        return self.cache.search_in_cache(address)
    
    def write_to_cache(self,address,value):
        self.cache.write_to_cache(address,value)
    
    def set_cache_flag(self,value):
        self.cache_flag = value
    
    def write_to_memory_bus(self,address,value):
        self.memory_bus.write_to_memory_bus(address,value)

    def search_in_memory_bus(self,address):
        return self.memory_bus.search_in_memory_bus(address)
    

    # instructions

    def jump_instruction(self, target):
        self.cpu_counter = int(target)

    def add_instruction(self, destination, source, target):
        self.registers[convert_register_to_index(destination)] = self.registers[convert_register_to_index(source)] + \
                                                                 self.registers[convert_register_to_index(target)]

    def add_i_instruction(self, destination, source, immediate):
        self.registers[convert_register_to_index(destination)] = self.registers[convert_register_to_index(source)] + \
                                                                 int(immediate)
    def cache_instruction(self, value):
        if value == CACHE_OFF_VAL:
            self.set_cache_flag(False)
        if value == CACHE_ON_VAL:
            self.set_cache_flag(True)
        if value == CACHE_FLUSH_VAL:
            self.flush_cache()

    def subtract_instruction(self, destination, source, target):
        self.registers[convert_register_to_index(destination)] = self.registers[convert_register_to_index(source)] - \
                                                                 self.registers[convert_register_to_index(target)]
    


    def parse_instruction(self, instruction):
        instruction_parsed = instruction.split(",")
        print("Reading instruction: " + instruction)
        self.increment_counter()
        if instruction_parsed[0] == ADD_INSTRUCTION:
            self.add_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == ADD_I_INSTRUCTION:
            self.add_i_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == JUMP_INSTRUCTION:
            self.jump_instruction(instruction_parsed[1])
        if instruction_parsed[0] == CACHE_INSTRUCTION:
            self.cache_instruction(instruction_parsed[1])
        if instruction_parsed[0] == SUBTRACT_INSTRUCTION:
            self.subtract_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
    def print_registers(self):
        print("---Registers---")
        for i in range(len(self.registers)):
            print("R{0}: {1}".format(i,self.registers[i]))
    
