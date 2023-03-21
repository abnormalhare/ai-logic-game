from main import *

# FULL ADDER EXAMPLE
print(add_gate("OR", "Input 1", "Input 2", 0)) # OR 1
print(add_gate("AND", "Input 0", "OR Gate 1", 0)) # AND 1
print(add_gate("NOT", "Input 0", None, 0)) # NOT 1
print(add_gate("AND", "Input 1", "Input 2", 0)) # AND 2
print(add_gate("AND", "NOT Gate 1", "AND Gate 2", 0)) # AND 3
print(add_gate("OR", "AND Gate 1", "AND Gate 3", 1)) # OR 2
print(add_gate("XOR", "Input 1", "Input 2", 0)) # XOR 1
print(add_gate("AND", "NOT Gate 1", "XOR Gate 1", 0)) # AND 4
print(add_gate("NOT", "XOR Gate 1", None, 0)) # NOT 2
print(add_gate("AND", "Input 0", "NOT Gate 2", 0)) # AND 5
print(add_gate("OR", "AND Gate 4", "AND Gate 5", 1)) # OR 3
print(run_game(1, 0, 1))
