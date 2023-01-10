import cmath
import numpy as np


def retangular_to_polar(numero_retangular):  # Numero em formato de Lista
    "Converte um numero complexo da forma retangular para polar"
    valor_polar_rad = cmath.polar(numero_retangular)
    valor_polar = valor_polar_rad[0], np.rad2deg(valor_polar_rad[1])
    return valor_polar


def polar_to_retangular(numero_polar):  # Numero em formato de Lista
    "Converte um numero complexo da forma polar para retangular"
    valor_retangular = cmath.rect(numero_polar[0], np.deg2rad(numero_polar[1]))
    return valor_retangular


def neutro(ia, ib, ic):
    "Calcula corrente de neutro"
    ia_retangular = polar_to_retangular(ia)
    ib_retangular = polar_to_retangular(ib)
    ic_retangular = polar_to_retangular(ic)

    ineutro_retangular = ia_retangular + ib_retangular + ic_retangular
    ineutro_bruto = retangular_to_polar(ineutro_retangular)
    ineutro = (round(ineutro_bruto[0], 2), round(ineutro_bruto[1], 2))
    return ineutro
