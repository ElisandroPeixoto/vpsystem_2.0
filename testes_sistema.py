from classes import Disjuntor

# Sequencia de Ações
dj = Disjuntor([100, 0], [0, 0], [0, 0], estado=True)  # Instanciando um disjuntor


def execucao(tempo):
    x = 0
    while x < tempo:
        # Sequencia de Parametrizacoes
        disp1 = dj.rele51(90, 'EI', 0.05, x)
        disp2 = dj.rele50(900)

        disparo = [disp1, disp2]  # Armazena as funcoes de protecao

        if any(disparo):
            dj.abrir()
            print(f'Tempo decorrido: {x}s')
            print(dj.estado)
            break

        x += 0.05  # Incremento de tempo

        if x >= tempo:
            print(f'Tempo decorrido: {x}s')
            print(dj.estado)


print('Fim da simulação')
execucao(20)
