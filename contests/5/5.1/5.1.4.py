classes = {
    'Junior' : 10,
    'Middle' : 15,
    'Senior' : 20,
}


class Programmer:

    def __init__(self,name, position):
        self.name = name
        self.position = position
        self.time = 0
        self.salary = 0


    def work(self, time):
        self.time += time
        self.salary += classes[self.position] * time

    def rise(self):
        current = self.position
        if current == 'Junior':
            self.position = 'Middle'
        elif current == 'Middle':
            self.position = 'Senior'
        elif current == 'Senior':
            classes['Senior'] += 1

    def info(self):
        return f'{self.name} {self.time}ч. {self.salary}тгр.'

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())