import math

# Equação dada na questão
def Equation(x):
    e = 2.7182818284590452353602874
    y = pow(e, 0.3 * x) - 3 + (3 * x)
    return y

# Derivada da equação dada na questão
def DerivativeEquation(x):
    e = 2.7182818284590452353602874
    y = 0.3 * pow(e, 0.3 * x) + 3
    return y


x0 = 0.7 # Estimativa inicial dada
i = 0  # Numero de iterações
print("i           x1                    ea\n")
while (1): # No loop de repetição aplica o algoritmo de Newton-Raphson
    i = i + 1 # Aumenta a iteração
    x1 = x0 - Equation(x0) / DerivativeEquation(x0)
    ea = (x1 - x0) / x1 # Calculo do erro
    print(f'{i}     {x1}      {ea}')
    x0 = x1
    if (abs(ea) < 0.002): # Condição de parada das iterações
        break
