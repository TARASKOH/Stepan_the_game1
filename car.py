class Car():
    def __init__(self, name, kms):
        self.name = name
        self.kms = kms

    def full_name(self):
        print(self.name, self.kms)


class Electro(Car):
    def __init__(self, name, kms):
        super().__init__(name, kms)
    def full_name(self):
        print('Hi')


my_tesla = Electro('Model S', 200)
my_tesla.full_name()