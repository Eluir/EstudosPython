import math


def bhaskara(a, b, c):
    delta = calcular_delta(a, b, c)
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    return {
        'x1': x1,
        'x2': x2
    }


def calcular_delta(a, b, c):
    resultado = b ** 2 - 4 * a * c
    return resultado

