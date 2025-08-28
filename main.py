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

# # 3- Podemos criar vetores, matrizes e tensores
# rng = numpy.random.default_rng()  # numpy tem sua métodos random inclusos
# vetor = rng.random(4)
# print(f'Array de 1 Dimensão (VETOR) randômico:\n{vetor}\n')
# matriz = rng.random([4, 4])
# print(f'Array de 2 Dimensões (MATRIZ) randômico:\n{matriz}\n')
# tensor = rng.random([4, 4, 4])
# print(f'Array de 3  Dimensões (TENSOR) randômico:\n{tensor}\n')

# # 4- Posso ordenar esses vetores
# rng = numpy.random.default_rng()
# matriz = rng.random([4, 4])
# m_coluna = numpy.sort(matriz, axis=0)
# m_linha = numpy.sort(matriz, axis=1)
# m_col_lin = numpy.sort(m_linha, axis=1)
# print(f'Ordenação dentro coluna:\n{m_coluna}')
# print(f'Ordenação dentro linha :\n{m_linha}')
# print(f'Ordenação dentro coluna e linha :\n{m_col_lin}')

# # 5 - Agora vamos preparar alguns ndarrays para serem representados por gráficos:
# a = 3 / 4
# b = 2 / 4
# c = 1 / 4
# vetor_a = numpy.linspace(10, 1000, 100)
# vetor_b = numpy.linspace(10, 3000, 100)
# vetor_c = numpy.linspace(10, 8000, 100)
#
# print(vetor_a)
# print(vetor_b)
# print(vetor_c)
#
# # Numpy já tem métodos bem diretos de como salvar um arquivo no formato .txt
# numpy.savetxt('vetor_a.txt', vetor_a, fmt='%f', delimiter=';')
# numpy.savetxt('vetor_b.txt', vetor_b, fmt='%f', delimiter=';')
# numpy.savetxt('vetor_c.txt', vetor_c, fmt='%f', delimiter=';')
#
# # 6 - Agora podemos utilizar uma das várias bibliotecas para plotar gráficos, eu escolhi a plotly
# import plotly.express
#
# array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
# array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
# array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')
# print(array_a)
#
# array_abc = numpy.vstack([array_a, array_b, array_c])
# print(array_abc)
# array_abc = array_abc.transpose()
# print(array_abc)
# fig = plotly.express.line(array_abc)
# fig.show()

print("Hello world")