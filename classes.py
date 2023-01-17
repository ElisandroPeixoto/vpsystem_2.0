from funcoes import neutro


class Disjuntor:
    def __init__(self, corrente_ia, corrente_ib, corrente_ic, estado=False):
        self.__corrente_ia = corrente_ia
        self.__corrente_ib = corrente_ib
        self.__corrente_ic = corrente_ic
        self.__corrente_in = neutro(corrente_ia, corrente_ib, corrente_ic)
        self.__estado = estado

    # Habilita acesso ao estado do disjuntor
    @property
    def estado(self):
        "Abertura e fechamento do disjuntor"
        return self.__estado

    def abrir(self):
        "Método de Abertura"
        self.__estado = False
        return self.__estado

    def fechar(self):
        "Método de Fechamento"
        self.__estado = True
        return self.__estado

    def rele50(self, pickup):
        "Relé 50 de Fase"
        if (self.__corrente_ia[0] or self.__corrente_ib[0] or self.__corrente_ic[0]) > 0:
            return True
        else:
            return False

    def rele50N(self, pickup):
        "Relé 50 de Neutro"
        if (self.__corrente_in[0]) > pickup:
            return True
        else:
            return False

    def rele51(self, pickup, curva, dial):
        pass

    def rele51N(self, pickup, curva, dial):
        pass
