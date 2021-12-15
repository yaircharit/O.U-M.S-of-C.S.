# Created By Yair Charit 207282955 #

class User:
    def __init__(self, name: str, occ: str):
        self._name = name
        self._occupation = occ
        
    def __str__(self):
        return f''   
    
class Engineer(User):
    def __init__(self):
        pass
    def __str__(self):
        return f''

class Technician(User):
    def __init__(self):
        pass
    def __str__(self):
        return f''

if __name__ == "__main__":
    pass