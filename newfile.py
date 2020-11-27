# Создаем класс "робот" - решение прошло!
print('Version 2.1')
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

# class Vector:
#
#     def __init__(self, *args):
#         self.values = []
#         for arg in args:
#             if isinstance(arg, int):
#                 self.values.append(arg)
#
#     def __str__(self):
#         if not self.values:
#             return f'Пустой вектор'
#         self.values.sort()
#         self.values = tuple(self.values)
#         return f'Вектор{self.values}'
