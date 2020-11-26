print('Hello world')

from My_project import newfile as nf

R1 = nf.Robot('A234')
R1.say_hello()
print(R1.name)
V1 = nf.Vector(1, 2, 3)
print(V1.values)
