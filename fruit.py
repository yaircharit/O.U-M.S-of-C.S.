# Created By Yair Charit 207282955 #

class AppleBasket:
    def __init__(self ,color: str, quantity: int):
        self.__apple_color = color
        self.__quantity = quantity      
    def increase(self):
        self.__quantity += 1
    def __str__(self):
        return f'A basket of {self.__quantity} {self.__apple_color} apples.'   

def main():
    a1 = AppleBasket('red', 4)
    a2 = AppleBasket('blue', 50)
    print(a1,a2,sep='\n')
    a2.increase()

if __name__ == "__main__":
    main()