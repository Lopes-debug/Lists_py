
# lista = ['Roland', 'ALfred', 'Goiania' 'Iphone', 'Macbook', 'notebook', 'PC','Radio', 'pac']
# lista.sort()
# print(lista)

# # aplicar parâmetro no .sort
# lista.sort(key=str.casefold)
# print(lista)

# converter lista em dicionario
# def convert(list):
#     keys = list[::2]  
#     values = list[1::2] 
#     dict = {keys[i]: values[i] for i in range(len(keys))}
#     return dict
# list = ['a', 1, 'b', 2, 'c', 3]
# print(convert(list))  # {'a': 1, 'b': 2, 'c': 3}

# converter lista em tupla
# tupla = tuple(lista)
# ou
# tupla = tuple(i for i in lista)

# converter listas em lista de tupla
# lista_tuplas = zip(lista1, lista2)

# converter lista de tuplas em dicionario
# dicionario = dict(lista_tuplas)

# EXERCICIO 1

# meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
# vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
# vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

# vendas_1sem.extend(vendas_2sem)

# maximo = max(vendas_1sem)
# minimo = min(vendas_1sem)
# i_max = vendas_1sem.index(maximo)
# i_min = vendas_2sem.index(minimo)
# print('O mês com maior qnt de vendas foi {} e o pior foi {}'.format(meses[i_max],meses[i_min]))
    