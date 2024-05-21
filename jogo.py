import pygame
from personagem import Personagem
from obstaculo import Obstaculo
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
#Notas musicais caindo pontuação
nota_semibreve = Obstaculo("Imagens/Semibreve nota musical.png",50,80,250,200)
nota_minima = Obstaculo("Imagens/Mínima nota músical.png",50,80,250,200)
nota_semifusa = Obstaculo("Imagens/Semifusa nota musical.png",50,80,250,200)
#Configuração da fonte
fonte = pygame.font.SysFont("Castellar",14)
#Criando um relógio para contrar o FPS
clock = pygame.time.Clock()
pontuacao = 0
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
    
    #Configurando o primeiro obstáculo para ter pontuação
    nota_semibreve.movimenta()
    nota_semibreve.desenhar(tela)
    if jogador1.mascara.overlap(nota_semibreve.mascara,(nota_semibreve.pos_x - jogador1.pos_x , nota_semibreve.pos_y - jogador1.pos_y )):
        pontuacao = pontuacao + 1
        nota_semibreve.pos_x = 1000
        nota_semibreve.pos_y = nota_semibreve.pos_y
    # Configurando o segundo obstáculo para ter pontuação
    nota_minima.movimenta()
    nota_minima.desenhar(tela)
    if jogador1.mascara.overlap(nota_minima.mascara,(nota_minima.pos_x - jogador1.pos_x , nota_minima.pos_y - jogador1.pos_y )):
        pontuacao = pontuacao + 1
    # Configurando o terceiro obstácupo para ter pontuação
    nota_semifusa.movimenta()
    nota_semifusa.desenhar(tela)
    if jogador1.mascara.overlap(nota_semifusa.mascara,(nota_semifusa.pos_x - jogador1.pos_x , nota_semifusa.pos_y - jogador1.pos_y )):
        pontuacao = pontuacao + 1
    #Pontuação maestro
    texto_pontuacao_maestro = fonte.render(f"Pontuação do Maestro: {pontuacao}",True,(255,0,0))
    tela.blit(texto_pontuacao_maestro,(0,10))
    pygame.display.update()

    clock.tick(60)
