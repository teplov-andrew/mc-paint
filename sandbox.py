class Animal:
    def __init__(self):
        self.type = 'Animal'

    def voice(self):
        return 'Rrrr'


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.subtype = 'Cat'

    def voice(self):
        return 'Meow'

    def eat(self, food):
        if food == 'meat' and self.subtype == 'Tiger':
            return True
        elif food == 'milk' and self.subtype == 'Cat':
            return True
        else:
            return False


cat = Cat()
cat2 = Cat()
cat2.subtype = 'Tiger'
print(cat.type, cat.subtype)
print(cat2.type, cat2.subtype)
print('Greeting:', cat.voice())
print('Cat eating meat:', cat.eat('meat'))
print('Cat eating milk:', cat.eat('milk'))
print('Tiger eating meat:', cat2.eat('meat'))
print('Tiger eating milk:', cat2.eat('milk'))
