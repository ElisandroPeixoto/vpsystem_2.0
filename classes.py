from funcoes import neutro


class Rele50:
    def __init__(self, corrente_ia, corrente_ib, corrente_ic):
        self.__corrente_ia = corrente_ia
        self.__corrente_ib = corrente_ib
        self.__corrente_ic = corrente_ic
        self.__corrente_in = neutro(corrente_ia, corrente_ib, corrente_ic)


class Disjuntor(Rele50):
    def __init__(self, corrente_ia, corrente_ib, corrente_ic, estado=False):
        super().__init__(corrente_ia, corrente_ib, corrente_ic)
        self.__estado = estado

    # Habilita acesso ao estado do disjuntor
    @property
    def estado(self):
        return self.__estado

    def abrir(self):
        "Método de Abertura"
        self.__estado = False
        return self.__estado

    def fechar(self):
        "Método de Fechamento"
        self.__estado = True
        return self.__estado
