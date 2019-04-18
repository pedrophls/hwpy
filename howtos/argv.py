from sys import argv
parameters = [ f for f in argv]

print(f"The program was started with {len(parameters)} parameters", end="\n\n")

for i, x in enumerate(parameters):
    print(f"Parameter {i} has: {x} inside")

