from sys import argv

if(len(argv) != 2):
    print("""
    The file must be passed as parameter!
    Example: ./read_file ~/Documents/name_file
    """)
    exit()

script_name, file_output = argv

f_open = open(file_output, 'w')
option = input("""
    What would you like to do?
    w - for write
    t - for truncate
""")
if(option == "t"):
    f_open.truncate()
elif(option == "w"):
    partial = ""
    print("Remember, q to quit...:")
    while(partial != "q"):
        partial = input()
        if(partial == "q"):
            break
        f_open.write(partial + "\n")
f_open.close()