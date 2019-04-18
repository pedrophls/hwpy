from sys import argv
from os.path import exists

if(len(argv) != 3):
    print("""
    The file must be passed as parameter!
    Example: ./write_file ~/Documents/name_file1 ~/Documents/name_file2
    """)
    exit()

script, from_file, to_file = argv

if(exists(from_file)):
    in_file = open(from_file)
    text = in_file.read()
    print(f"Len of file: {len(text)}")

    out_file = open(to_file, 'w')
    out_file.write(text)
    print("Copy done!")

out_file.close()
in_file.close()