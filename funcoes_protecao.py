from funcoes_complexas import retangular_to_polar, polar_to_retangular


def neutro(ia, ib, ic):
    """Calcula corrente de neutro"""
    ia_retangular = polar_to_retangular(ia)
    ib_retangular = polar_to_retangular(ib)
    ic_retangular = polar_to_retangular(ic)

    ineutro_retangular = ia_retangular + ib_retangular + ic_retangular
    ineutro_bruto = retangular_to_polar(ineutro_retangular)
    ineutro = (round(ineutro_bruto[0], 2), round(ineutro_bruto[1], 2))
    return ineutro


def sobrecorrente_temporizada_iec(corrente_falta, pickup, curva, dial):
    m = corrente_falta/pickup
    if curva == "SI":
        tempo_disparo = dial*(0.14/((m**0.02)-1))
        return tempo_disparo
    elif curva == "VI":
        tempo_disparo = dial*(13.5/(m - 1))
        return tempo_disparo
    elif curva == "EI":
        tempo_disparo = dial*(80/((m**2)-1))
        return tempo_disparo


def sobrecorrente_temporizada_ansi(corrente_falta, pickup, curva, dial):
    pass
