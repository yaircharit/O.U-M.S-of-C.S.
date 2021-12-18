# Created By Yair Charit 207282955 #

class BankAccount:
    def __init__(self ,name: str, amount: int):
        self.name = name
        self.amt = amount      
    def __str__(self):
        return f'Your account, {self.name}, has {self.amt} dollars.'   
    
if __name__ == "__main__":
    t1 = BankAccount('Bob', '100')
    print(t1)