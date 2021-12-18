# Created By Yair Charit 207282955 #

class User:
    def __init__(self, name='John Doe'):
        self.__name = name
        self.__occupation = 'User'
        
    def __str__(self):
        return f'{self.__name} is {self.__occupation}'   
    
class Engineer(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self.__occupation = 'Engineer'
class Technician(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self.__occupation = 'Technician'
class Barber(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self.__occupation = 'Barber'
class Politician(User):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self.__occupation = 'Politician'

class ElectricalEngineer(Engineer):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self.__occupation = 'Electrical Engineer'

class ComputerEngineer(Engineer):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self.__occupation = 'Computer Engineer'
        
class MechanicalEngineer(Engineer):
    def __init__(self, name='John Doe'):
        super().__init__(name)
        self.__occupation = 'Mechanical Engineer'


exit_strings = ['q','Q','exit','quit', 'n']
if __name__ == "__main__":
    to_continue = ''
    dynamic_classes = dict()
    while (to_continue not in exit_strings):
        class_name = input('Please enter the name of new class: ')
        class_name = class_name[0].capitalize()+class_name[1:]
        base_class_name = input('Please enter name of base class (blank if none): ')
        method_name = input(f'Please enter name of new method for class {class_name}: ')
        attr_name = input(f'Please enter name of new attribute for class {class_name}: ')
        
        # Check if base class already exists either in globals or previously dynamically created classes or None, -1 if its not
        base_class = object if not base_class_name else globals()[base_class_name] if base_class_name in globals() else dynamic_classes.get(base_class_name,-1)
        if base_class != -1 and class_name not in globals() and class_name not in dynamic_classes:
            newclass = type(class_name, (base_class,),{method_name: lambda x:x, attr_name: None})
            print(f'Class {class_name} created {f"with base class: {base_class_name}" if base_class_name else ""}')
            print('Class __name__ is:', newclass.__name__)
            print('Class __dict__ is:', newclass.__dict__)
            dynamic_classes[class_name] = newclass
        else:
            if base_class != -1:
                print(f'ERROR: {base_class_name} is not a valid base class!')
            else:
                print(f'ERROR: {class_name} is not a valid NEW class!')
        
        to_continue = input('Do you wish to cotinue? (y/n): ')
    print('\ngoodbye..')
    
    