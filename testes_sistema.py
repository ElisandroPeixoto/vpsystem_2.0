from classes import Disjuntor


dj = Disjuntor([100, 0], [0, 0], [0, 0])


def execucao(tempo):
    x = 0
    while x < tempo:
        elemento1 = dj.rele51(90, "SI", 0.05)

        if elemento1 is not None:
            if x >= elemento1:
                print(f'Tempo: {x}s')
                break
            else:
                x += 0.1667  # Intervalo entre amostras


execucao(10)
