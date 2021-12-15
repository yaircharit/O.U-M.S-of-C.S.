

class BaseClass(object):
    def __init__(self, classtype):
        self._type = classtype


def class_factory(name, argnames, base_class=BaseClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # here, the argnames variable is the one passed to the
            # ClassFactory call
            if key not in argnames:
                raise TypeError("Argument %s not valid for %s" % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("Class")])
    newclass = type(name, (BaseClass,),{"__init__": __init__})
    return newclass


SpecialClass = class_factory("SpecialClass", "a b c".split())
NewSpecialClass = class_factory("NewSpecialClass", "t", base_class=SpecialClass)


def name_of_func(self, x):
    return x**2


# I created a new method, with the name given, I just created that it takes an integer and give out it power 2 - it wasn't define in the question.
setattr(NewSpecialClass, "name_of_func", lambda self, x: x ** 2)
setattr(NewSpecialClass, "name_of_func2", name_of_func)

s = SpecialClass(a=2)
r = NewSpecialClass(t=500)

print(s.a)
print(r.name_of_func(3), NewSpecialClass.__name__)
print(NewSpecialClass.name_of_func(r, 3))


class Apple:

    mnot_moshe = 3

    def moshe(self, x, y, p=50):
        pass

    def yossi(self, t):
        pass

    def haim(self):
        pass

    @staticmethod
    def naknik():
        pass


new_method = 'print("hello")'

for methodname in dir(Apple):
    orig_method = getattr(Apple, methodname)
    # this checks if this parameter is a function
    if hasattr(orig_method, '__code__'):

        # new_function_header = 'def {:}({:}): {:}'.format(orig_method.__name__,
        #                                                  ",".join(orig_method.__code__.co_varnames), new_method)
        #
        # f_code = compile(new_function_header, "", "exec")
        # f_func = FunctionType(f_code.co_consts[0], globals(), "gfg")
        #
        #
        # setattr(Apple, methodname, f_func)

        new_function_header = 'lambda {:}: {:}'.format(",".join(orig_method.__code__.co_varnames), new_method)
        setattr(Apple, methodname, eval(new_function_header))




t = Apple()
t.moshe(5, 3, 1)
