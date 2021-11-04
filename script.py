from cpu import CPU

DATA_FILE = "data_input.txt"
ASSEMBLY_FILE = "assembly_input.txt"

def fetch_data():
    data_file = open(DATA_FILE, 'r').readlines()
    data = map(lambda d:d.strip(), data_file)
    return list(data)

def fetch_assembly_instructions():
    assembly_file = open(ASSEMBLY_FILE, 'r').readlines()
    assembly = map(lambda a:a.strip(), assembly_file)
    return list(assembly)

def init_mem_bus(cpu):
    data = fetch_data()
    for d in data:
        parsed = d.split(",")
        cpu.write_to_memory_bus(parsed[0],parsed[1])

def send_to_cpu(cpu):
    assembly_instructions = fetch_assembly_instructions()
    for i in assembly_instructions:
        cpu.parse_instruction(i)    
        cpu.print_registers()

new_cpu = CPU()
print("---------------------------------------------------")
print("Welcome to the Python CPU Simulator!")
print("---------------------------------------------------")
print("Initializing Memory Bus from data input file...")
init_mem_bus(new_cpu)
print("Memory Bus successfully initialized")
print("---------------------------------------------------")
print("Sending instructions to CPU...")
send_to_cpu(new_cpu)
print("---------------------------------------------------")
print("Terminating CPU Processing...")

# def print_mem_bus(cpu):
#     data = fetch_data()
#     for d in data:
#         parsed = d.split(",")
#         # cpu.write_to_memory_bus(parsed[0],parsed[1])
#         print(parsed)
# print_mem_bus(new_cpu)
# new_cpu.print_registers()   