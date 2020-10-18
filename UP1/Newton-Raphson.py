import math

# Equação dada na questão
def Equation(x):
    e = 2.7182818284590452353602874
    y = pow(e, 0.3 * x) - 3 + (3 * x)
    return y


def DerivativeEquation(x):
    e = 2.7182818284590452353602874
    y = 0.3 * pow(e, 0.3 * x) + 3
    return y


x0 = 0
x1 = 0.7
i = 0  # Numero de iterações
print("i     x2                    ea\n")
while (1):
    i = i + 1
    x2 = x1 - Equation(x1) / DerivativeEquation(x1)
    ea = (x2 - x1) / x2
    print(i, x2, ea)
    x1 = x2
    if (abs(ea) < 0.002):
        break
