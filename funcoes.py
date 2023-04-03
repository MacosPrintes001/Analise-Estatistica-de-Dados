import numpy as np
from collections import Counter


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


mylista = [22.8, 20.2, 23.5, 24.8, 25.0]  # Lista padrão
meus_pesos = mylista


print("A Média de {} é: {:.3f}".format(mylista, media_simples(mylista)))

print("A Média Ponderada de {} com peso {} é aproximadamente : {:.3f}".format(
    mylista, meus_pesos, media_ponderada(mylista, meus_pesos)))

print("A Mediana de {} é: {:.3f}".format(mylista, mediana(mylista)))

print("A Moda de {} é: {}".format(mylista, moda(mylista)))

print("A Amplitude de {} é: {:.3f}".format(mylista, amplitude(mylista)))

print("A Variância de {} é: {:.3f}".format(mylista, variancia(mylista)))

print("O Desvio Padrão de {} é: {:.3f} ".format(mylista, desvPadrao(mylista)))

print("O Coeficiente de variação de {} é: {:.3f}%".format(
    mylista, coeficiente_variacao(mylista)))

print("A Variação Média de {} é: {:.3f}".format(
    mylista, variacao_media(mylista)))

print("O Erro Padrão de {} é: {:.3f}".format(mylista, erro_padrao(mylista)))
