from funcoes_protecao import neutro, sobrecorrente_temporizada_iec


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
        """Relé 50 de Fase"""
        if (self.__corrente_ia[0] or self.__corrente_ib[0] or self.__corrente_ic[0]) > pickup:
            return True
        else:
            return False

    def rele50n(self, pickup):
        """Relé 50 de Neutro"""
        if (self.__corrente_in[0]) > pickup:
            return True
        else:
            return False

    def rele51(self, pickup, curva, dial, tempo_simulacao):
        """Relé 51 de Fase"""
        if (self.__corrente_ia[0] or self.__corrente_ib[0] or self.__corrente_ic[0]) > pickup:
            icc = max(self.__corrente_ia[0], self.__corrente_ib[0], self.__corrente_ic[0])
            tempo_disparo = sobrecorrente_temporizada_iec(icc, pickup, curva, dial)

            if tempo_simulacao >= tempo_disparo:  # Compara tempo de atuação com o tempo da simulação
                return True
        else:
            return False

    def rele51n(self, pickup, curva, dial, tempo_simulacao):
        """Relé 51 de Neutro"""
        icc = self.__corrente_in[0]
        tempo_disparo = sobrecorrente_temporizada_iec(icc, pickup, curva, dial)

        if tempo_simulacao >= tempo_disparo:
            return True
        else:
            return False


class Disjuntor(ReleProtecao):
    def __init__(self, corrente_ia, corrente_ib, corrente_ic, estado=False):
        ReleProtecao.__init__(self, corrente_ia, corrente_ib, corrente_ic)
        self.__estado = estado

    @property  # Habilita acesso ao estado do disjuntor
    def estado(self):
        """Abertura e fechamento do disjuntor"""
        if self.__estado:
            return "Fechado"
        else:
            return "Aberto"

    def abrir(self):
        """Método de Abertura"""
        self.__estado = False
        return self.__estado

    def fechar(self):
        """Método de Fechamento"""
        self.__estado = True
        return self.__estado
