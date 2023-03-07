from classes import Disjuntor

dj = Disjuntor([100, 0], [0, 0], [0, 0], estado=True)

x = dj.rele51(90, 'SI', 0.05, )
print(x)
