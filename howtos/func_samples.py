def func_variable_number_args(*args):
    for x in args:
        print(x)

def func_keyword_args(**kwargs):
    name = kwargs.get('name')
    age = kwargs.get('age')
    print(str(name) + " - " + str(age))

ls = [2**x for x in range(40)]
func_variable_number_args(ls)

func_keyword_args(name="pedro", age="22")
