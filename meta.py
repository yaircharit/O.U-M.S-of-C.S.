from inspect import isclass, isfunction, getsource, getblock
import ast

if __name__ == '__main__':
    module = None
    while not module:
        try:
            py_file = input('Please enter a python module to load: ')
            module = __import__(py_file)
        except:
            print('ERROR: no such module was found')
    
    while True:
        py_func = input('Please enter a python command to inject: ')
        try:
            ast.parse(py_func)
            break
        except Exception as e:
            print(e)

    for mod_key in dir(module):
        cl = getattr(module, mod_key)
        if isclass(cl):
            for class_key in dir(cl):
                func = getattr(cl, class_key)
                if isfunction(func):
                    def func_factory(old_func):
                        def new_func(*params):
                            eval(py_func)
                            return old_func(*params)
                        return new_func

                    setattr(cl, class_key, func_factory(func))

            setattr(module, mod_key, cl)
    module.main()
