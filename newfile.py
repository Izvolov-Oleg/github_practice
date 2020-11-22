# Создаем класс "робот" - решение прошло!

class Robot(object):
    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @staticmethod
    def how_many():
        print(f'{Robot.population}, вот сколько нас еще осталось')