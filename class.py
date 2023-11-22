class Human:
    def __init__(self, n, a, h):
        print('Создан объект класса Human')
        self.name=n
        self.age=a
        self.height=h
    
    def print(self):
        print(f'Имя:{self.name}')
        print(f'Возраст:{self.age}')
        print(f'Рост:{self.height}')
     
    @property
    def name(self):
        return self.__name.upper()
        
    @name.setter    
    def name(self, n):
        self.__name=n.capitalize()
        
    
person1=Human("Андрей", 18, 175)
person1.print()

person1.setName('МаКс')
person1.print()
