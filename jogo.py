import pygame
from personagem import Personagem
pygame.init()
#Construção da tela:
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Notas explosivas")
tela.fill((80,120,200))
#contrução do fundo da tela
FUNDO = pygame.image.load("Imagens/Fundo branco.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))
#Criando mais personagens
jogador1 = Personagem("Imagens/Regente de orquestra.png",80,100,350,400)
#Configuração da fonte
fonte = pygame.font.SysFont("Castellar",14)
#Criando um relógio para contrar o FPS
clock = pygame.time.Clock()

rodando = True
while rodando:
    #Treatando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Vacê colidiu!")
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(FUNDO,(0,0))
    #Configurando jogador
    jogador1.mova_via_controle(pygame.K_d,pygame.K_a)
    jogador1.desenhar(tela)
    pygame.display.update()

