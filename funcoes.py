import numpy as np
from collections import Counter
from sympy import *


def calcular_limite(funcao, a):
    # Definindo a variável simbólica x
    x = symbols('x')

    # Calculando o limite da função quando x tende a a
    limite = limit(funcao, x, a)

    # Retornando o resultado
    return limite


def media_ponderada(valores, pesos):
    return np.average(valores, weights=pesos)


def media_simples(lista):
    return np.mean(lista)


def mediana(lista):
    return np.median(lista)


def moda(lista):
    freq_dict = Counter(lista)
    modas = [k for k, v in freq_dict.items(
    ) if v == max(list(freq_dict.values()))]
    return modas if len(modas) != len(lista) else np.nan


def amplitude(lista):
    return np.max(lista) - np.min(lista)


def variancia(lista):
    return np.var(lista)


def desvPadrao(lista):
    return np.std(lista)


def coeficiente_variacao(lista):
    return np.std(lista) / np.mean(lista) * 100


def variacao_media(lista):
    # Calcula a média dos valores
    media = np.mean(lista)

    # Calcula a variação média
    variacao_media = np.mean(np.abs(lista - media))

    # Retorna a variação média
    return variacao_media


def desvio_padrao(lista):
    return np.std(lista)


def erro_padrao(lista):
    # Calcula a média dos valores
    media = np.mean(lista)

    # Calcula o desvio padrão dos valores
    desvio_padrao = np.std(lista, ddof=1)

    # Calcula o tamanho da amostra
    n = len(lista)

    # Calcula o erro padrão da média
    erro_padrao = desvio_padrao / np.sqrt(n)

    # Retorna o erro padrão da média
    return erro_padrao


# Definindo a variável simbólica x
x = symbols('x')

# Definindo a função f(x)
f = (x**2 - 1)/(x - 1)

# Calculando o limite de f(x) quando x tende a 1
limite = limit(f, x, 1)

print(limite)
