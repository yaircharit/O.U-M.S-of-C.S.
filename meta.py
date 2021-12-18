from inspect import isclass, isfunction
import ast

# get input and validate
module = None
while True:
    try:
        if not module:
            py_file = input('Please enter a python module to load: ')
            module = __import__(py_file)

        py_func = input('Please enter a python command to inject: ')
        ast.parse(py_func)
        break
    except Exception as e:
        print(e)

# go over all attributes in module.__dict__
for mod_key in dir(module):
    cl = getattr(module, mod_key)
    if isclass(cl):
        # for all classes in module
        for class_key in dir(cl):
            func = getattr(cl, class_key)
            if isfunction(func):
                # for all functions in class:
                def func_factory(old_func):
                    # returns a new function that executes the input and then the old function
                    def new_func(*params):
                        eval(py_func)
                        return old_func(*params)
                    return new_func
                # replace class method
                setattr(cl, class_key, func_factory(func))

# execute main function if exists
if module.main:
    module.main()
