from classes import Disjuntor

dj = Disjuntor([1000, 0], [300, -120], [2, 140])

x = dj.rele51('IEC', 100, 'SI', 0.05)
y = dj.rele51('IEC', 100, 'VI', 0.05)
z = dj.rele51('IEC', 100, 'EI', 0.05)
print(x)
print(y)
print(z)
