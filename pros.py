# Created By Yair Charit 207282955 #
import re
class User:
    def __init__(self, name='John Doe'):
        self._name = name
        self._occupation = 'User'

    def __str__(self):
        return f'{self._name} is a {self._occupation}'


class Engineer(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self._occupation = 'Engineer'


class Technician(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self._occupation = 'Technician'


class Barber(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self._occupation = 'Barber'


class Politician(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self._occupation = 'Politician'


class ElectricalEngineer(Engineer):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self._occupation = 'Electrical Engineer'


class ComputerEngineer(Engineer):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self._occupation = 'Computer Engineer'


class MechanicalEngineer(Engineer):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self._occupation = 'Mechanical Engineer'

def main():
    # Some example code
    c = ComputerEngineer('Henry')
    print(c)
    
    to_continue = class_name = method_name = attr_name = ''
    dynamic_classes = dict()
    exit_strings = ['q', 'Q', 'exit', 'quit', 'n']
    while (to_continue not in exit_strings):
    # Get and validate input #
        # New Class Name
        class_name = input('Please enter the name of new class: ')
        # Check if new class doesn't exists
        while not re.search('^[A-Z][a-zA-Z0-9]*$',class_name)  or class_name in globals() or class_name in dynamic_classes:
            class_name = input('INVALID CLASS NAME!\nPlease enter the name of new class: ')
        # Base class
        base_class_name = input('Please enter name of base class (blank if none): ')
        # Check if baseclass exists
        while not re.search('^[A-Z][a-zA-Z0-9]*$|^$',base_class_name) or not (base_class_name in globals() or base_class_name in dynamic_classes):
            if not base_class_name:
                base_class = object
            base_class_name = input('INVALID BASE CLASS NAME!\nPlease enter name of base class (blank if none): ')
        if base_class_name:
            base_class = globals().get(base_class_name,dynamic_classes.get(base_class_name))
        # Method name
        method_name = input(f'Please enter name of new method for class {class_name}: ')
        while not re.search('^[A-Za-z][a-zA-Z0-9]*$',method_name) :
            method_name = input(f'INVALID METHOD NAME!\nPlease enter name of new method for class {class_name}: ')
        # Attribute name
        attr_name = input(f'Please enter name of new attribute for class {class_name}: ')
        while not re.search('^[A-Za-z][a-zA-Z0-9]*$',attr_name) :
            attr_name = input(f'NVALID ATTRIBUTE NAME!\nPlease enter name of new attribute for class {class_name}: ')
    
        # Create the class
        newclass = type(class_name, (base_class,), {method_name: lambda: print("HELLO"), attr_name: None})
        # Print the new class
        print(f'Class {class_name} created {f"with base class {base_class_name}" if base_class_name else ""}')
        print('Class __name__ is:', newclass.__name__)
        print('Class __dict__ is:', newclass.__dict__)
        dynamic_classes[class_name] = newclass
        to_continue = input('Do you wish to cotinue? (y/n): ')
        
    print('goodbye..\n')
    


if __name__ == "__main__":
    main()
