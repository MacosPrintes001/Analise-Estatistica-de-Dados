import funcoes as fc
from sympy import *


# mylista = [22.8, 20.2, 23.5, 24.8, 25.0]  # Lista padrão
# meus_pesos = mylista

# print("A Média de {} é: {:.3f}".format(mylista, fc.media_simples(mylista)))

# print("A Média Ponderada de {} com peso {} é aproximadamente : {:.3f}".format(
#     mylista, meus_pesos, fc.media_ponderada(mylista, meus_pesos)))

# print("A Mediana de {} é: {:.3f}".format(mylista, fc.mediana(mylista)))

# print("A Moda de {} é: {}".format(mylista, fc.moda(mylista)))

# print("A Amplitude de {} é: {:.3f}".format(mylista, fc.amplitude(mylista)))

# print("A Variância de {} é: {:.3f}".format(mylista, fc.variancia(mylista)))

# print("O Desvio Padrão de {} é: {:.3f} ".format(mylista, fc.desvPadrao(mylista)))

# print("O Coeficiente de variação de {} é: {:.3f}%".format(
#     mylista, fc.coeficiente_variacao(mylista)))

# print("A Variação Média de {} é: {:.3f}".format(
#     mylista, fc.variacao_media(mylista)))

# print("O Erro Padrão de {} é: {:.3f}".format(mylista, fc.erro_padrao(mylista)))


# Exemplo de uso da função calcular_limite()
# Definindo a função f(x)
x = symbols('x')
f = (x**2 - 1)/(x - 1)

# Calculando o limite de f(x) quando x tende a 1
limite = fc.calcular_limite(f, 1)

# Imprimindo o resultado
print(limite)
