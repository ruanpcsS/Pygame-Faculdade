import pygame

print("começando")
# inicia o pygame
pygame.init()

print("Abrindo tela")
# faz uma tela
screen = pygame.display.set_mode(size=(600,480))

print("rodando")
# faz a tela permanecer ativa
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #fechar a janela
            quit() #encerra o pygame
