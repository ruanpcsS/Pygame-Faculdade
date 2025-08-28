# #o que é numpy: é uma biblioteca que oferece estrutura de dados não nativas do python com suporte
# #numpy oferece maior desempenho e ferramentas superiores se comparada com a padrão
# #numpy trabalha com a ideia de vetores (arrays), conhecido como ndarrays
# #Com a diferença que ndarrays só trabalham com dados do mesmo tipo que lembram muito as listas do python
# #Outra vantagem: por trabalhar com um só tipo de dado o ndarray tem um desempenho muito melhor se comparado com listas
# import numpy as np
#
#
# print(np.__version__)
#
# #Exemplo de criação:
# ndarray1 = np.zeros(10000)
# print(f"1 - conteúdo da lista: {ndarray1}, o tamanho {len(ndarray1)}")
# ndarray1 = np.ones(10000)
# print(f"2 - conteúdo da lista: {ndarray1}, o tamanho {len(ndarray1)}")
# ndarray1 = np.linspace(10, 1000, 10000)
#
# print(f"3 - conteúdo da lista: {ndarray1}, o tamanho {len(ndarray1)}")


# import time
# #comparar desempenho:
# start_time = time.time()
# lista = [0] * 100000000
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"A criação da lista de 100 milhões de elementos levou {elapsed_time} segundo(s)")
#
# start_time = time.time()
# ndarray = np.zeros(100000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"A criação da lista de 100 milhões de elementos em numpy levou {elapsed_time} segundo(s)")

# # 3- Dá para fazer ainda melhor se definirmo o tipo de dado, exemplo: dado tipo int8 (para valores de 0 - 255)
# start_time = time.time()
# ndarray_uint8 = numpy.zeros(1000000000, dtype='uint8')
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de um ndarray de 1 bilhão de elementos em int de 8 não sinalizado levou: {elapsed_time}')

