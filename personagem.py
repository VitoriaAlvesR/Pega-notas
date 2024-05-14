import pygame

class Personagem:

    def __init__(self,arquivo_imagem,largura_imagem, altura_imagem,x_inicial,y_inicial):
        #Carregar a imagem do personagem.
        self.imagem = pygame.image.load(arquivo_imagem)
        #Estrutura da largura e altura da imagem.
        self.lergura = largura_imagem
        self.altura = altura_imagem
        #Criação de como vai aparecer a imagem personagem.
        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))
        #Posição x inicial e y inicial.
        self.pos_x = x_inicial
        self.pos_y = y_inicial
        #Criação da máscara
        self.mascara = pygame.mask.from_surface(self.imagem)
        #Pontuação do personagem.
        self.pontuacao = 0

    def mota_via_controle(self,direita,esquerda):
        #Controle de teclas
        teclas = pygame.key.get_pressed()
        #Coordenadas da tecla esquerda
        if teclas[esquerda]:
            if self.pos_x > 0:
                self.pos_x = self.pos_x - 5
        
        if teclas[direita]:
            if self.pos_x < 800 - self.largura:
                self.pos_x = self.pos_x + 5

