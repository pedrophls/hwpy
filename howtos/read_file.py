from sys import argv

if(len(argv) != 2):
    print("""
    The file must be passed as parameter!
    Example: ./read_file ~/Documents/name_file
    """)
    exit()

script_name, file_input = argv

f_open = open(file_input)