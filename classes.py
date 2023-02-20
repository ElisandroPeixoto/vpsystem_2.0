from funcoes import neutro


class TransformadorCorrente:
    def __init__(self, corrente_ia, corrente_ib, corrente_ic):
        self.__corrente_ia = corrente_ia
        self.__corrente_ib = corrente_ib
        self.__corrente_ic = corrente_ic


class ReleProtecao(TransformadorCorrente):
    def __init__(self, corrente_ia, corrente_ib, corrente_ic):
        super().__init__(corrente_ia, corrente_ib, corrente_ic)
        self.__corrente_ia = corrente_ia
        self.__corrente_ib = corrente_ib
        self.__corrente_ic = corrente_ic
        self.__corrente_in = neutro(self.__corrente_ia, self.__corrente_ib, self.__corrente_ic)

    def rele50(self, pickup):
        "Relé 50 de Fase"
        if (self.__corrente_ia[0] or self.__corrente_ib[0] or self.__corrente_ic[0]) > pickup:
            return True
        else:
            return False

    def rele50N(self, pickup):
        "Relé 50 de Neutro"
        if (self.__corrente_in[0]) > pickup:
            return True
        else:
            return False

    def rele51(self, norma, pickup, curva, dial):
        if (self.__corrente_ia[0] or self.__corrente_ib[0] or self.__corrente_ic[0]) > pickup:
            icc = max(self.__corrente_ia[0],
                      self.__corrente_ib[0], self.__corrente_ic[0])
        else:
            icc = 0

        if norma == "IEC":
            M = icc/pickup
            if curva == "SI":
                tempo_disparo = dial*(0.14/((M**0.02)-1))
                return tempo_disparo
            elif curva == "VI":
                tempo_disparo = dial*(13.5/(M - 1))
                return tempo_disparo
            elif curva == "EI":
                tempo_disparo = dial*(80/((M**2)-1))
                return tempo_disparo

    def rele51N(self, norma, pickup, curva, dial):
        pass


class Disjuntor(ReleProtecao):
    def __init__(self, corrente_ia, corrente_ib, corrente_ic, estado=False):
        ReleProtecao.__init__(self, corrente_ia, corrente_ib, corrente_ic)
        self.__estado = estado

    @property  # Habilita acesso ao estado do disjuntor
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
