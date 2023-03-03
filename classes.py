from funcoes_protecao import neutro, sobrecorrente_temporizada_IEC


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
        self.__corrente_in = neutro(
            self.__corrente_ia, self.__corrente_ib, self.__corrente_ic)

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

    def rele51(self, pickup, curva, dial):
        if (self.__corrente_ia[0] or self.__corrente_ib[0] or self.__corrente_ic[0]) > pickup:
            icc = max(self.__corrente_ia[0],
                      self.__corrente_ib[0], self.__corrente_ic[0])
        else:
            icc = 0
        return sobrecorrente_temporizada_IEC(icc, pickup, curva, dial)

    def rele51N(self, pickup, curva, dial):
        icc = self.__corrente_in[0]
        return sobrecorrente_temporizada_IEC(icc, pickup, curva, dial)


class Disjuntor(ReleProtecao):
    def __init__(self, corrente_ia, corrente_ib, corrente_ic, estado=False):
        ReleProtecao.__init__(self, corrente_ia, corrente_ib, corrente_ic)
        self.__estado = estado

    @property  # Habilita acesso ao estado do disjuntor
    def estado(self):
        "Abertura e fechamento do disjuntor"
        if self.__estado:
            return "Fechado"
        else:
            return "Aberto"

    def abrir(self):
        "Método de Abertura"
        self.__estado = False
        return self.__estado

    def fechar(self):
        "Método de Fechamento"
        self.__estado = True
        return self.__estado
