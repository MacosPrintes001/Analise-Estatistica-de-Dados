# Análise Estatística de Dados

Este repositório contém um arquivo em Python com funções para análise estatística de dados.

## Funcionalidades

- Cálculo da média simples de um conjunto de dados
- Cálculo da média ponderada de um conjunto de dados
- Cálculo da mediana de um conjunto de dados
- Cálculo da moda de um conjunto de dados
- Cálculo da variância de um conjunto de dados
- Cálculo da amplitude de um conjunto de dados
- Cálculo do desvio padrão de um conjunto de dados
- Cálculo do coeficiente e variação de um conjunto de dados
- Cálculo da variação média de um conjunto de dados
- Cálculo do erro padrão de um conjunto de dados


## Como utilizar

Para utilizar as funções deste arquivo em seu projeto, basta importar o arquivo "estatistica.py" e chamar as funções necessárias. Veja um exemplo:

```python
import funções as fc 

mylista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista padrão
meus_pesos = mylista #substitua pelo peso para calculo de media ponderada

media = fc.media_simples(mylista)
media_ponderada = fc.media_ponderada(mylista, meus_pesos)

print("A Média de {} é: {:.3f}".format(mylista, media))
print("A Média Ponderada de {} com peso {} é aproximadamente : {:.3f}".format(mylista, meus_pesos, ))
```

Este exemplo calculará a média, média ponderada, (podem ser chamadas as outras funções descritas antes) do conjunto de dados [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e imprimirá os resultados na tela.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma "issue" ou enviar um "pull request" para melhorar este arquivo.

## Licença

Este projeto está licenciado sob a licença [Nome da Licença]. Para mais informações, consulte o arquivo [LICENSE.md](LICENSE.md).
