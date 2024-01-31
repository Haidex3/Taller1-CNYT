import math
def suma(a, b):
    suma_real = a[0] + b[0]
    suma_complejo = a[1] + b[1]
    return (suma_real, suma_complejo)

def multiplicacion(a, b):
    multiplicacion_real = a[0] * b[0] - a[1] * b[1]
    multiplicacion_complejo = (a[0] * b[1]) + (a[1] * b[0])
    return (multiplicacion_real, multiplicacion_complejo)


def resta(a, b):
    resta_real = a[0] - b[0]
    resta_complejo = a[1] - b[1]
    return (resta_real, resta_complejo)

def division(a, b):
    if (b[0] ** 2 + b[1] ** 2)!=0:
        division_real = ((a[0] * b[0]) + (a[1] * b[1])) / (b[0] ** 2 + b[1] ** 2)
        division_complejo = ((a[1] * b[0]) - (a[0] * b[1])) / (b[0] ** 2 + b[1] ** 2)
        return (division_real, division_complejo)

def modulo(a):
    modulo_rc = (a[0] ** 2 + a[1] ** 2) ** 0.5
    return modulo_rc

def conjugado(a):
    conjugado_rc = a[0], a[1]
    if a[1] < 0 or a[1] > 0:
        return a[0], -a[1]
    else:
        return 0,0

def polar(a):
    z = (a[0] ** 2 + a[1] ** 2) ** 0.5
    angle = math.atan(a[1] / a[0])
    polar_real = z * math.cos(angle)
    polar_complejo = z * math.sin(angle)
    return (polar_real, polar_complejo)

def fase(c1):
    sa = c1[1] / c1[0]
    sb = math.atan(sa)
    return sb

