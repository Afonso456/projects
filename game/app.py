import pygame
import random

pygame.init() #iniciar o pygame

#desenhar a janela
largura= 800
altura= 600
tamanho=(largura,altura)
titulo= "Primeiro jogo"
frames= 60

#criar a janela
janela= pygame.display.set_mode(tamanho)
pygame.display.set_caption(titulo)
fundo= (36,36,36)

#Assets
#player
player_file= "game\imagens\\aviao.png"
player_speed_x = 0
player_speed_y = 0
player_img= pygame.image.load(player_file)
player_rect= player_img.get_rect()
player_rect.topleft = (360,400)

#npc
npc_file= "game\imagens\\npc.png"
npc_speed_x = 1
npc_speed_y = 1
npc_img= pygame.image.load(npc_file)
npc_rect= player_img.get_rect()
npc_rect.topleft = (400,50)


#texto game over
font= pygame.font.SysFont("serif",40)
texto= font.render("Game Over", True,(255,255,255))

relogio = pygame.time.Clock()
relogio.tick(60) #frames per second

run=True
player_stats= True #player vivo
#Game Loop
while run:
    if player_stats == False:
        player_speed_x= 0
        player_speed_y= 0

    #atualizar as posições 
    player_rect= player_rect.move(player_speed_x,player_speed_y)
    #atualizar o npc
    if player_rect.left > npc_rect.left:
        npc_speed_x = 1
    else:
        npc_speed_x = -1
    if npc_rect.bottom > altura:
        npc_rect.top= 0
        npc_rect.left=  random.randint(10,790-npc_rect.width)

    npc_rect = npc_rect.move(npc_speed_x,npc_speed_y)


    #limpar a janela com a cor de fundo
    janela.fill(fundo)

    #desenhar o player e os npcs
    janela.blit(player_img,player_rect)
    janela.blit(npc_img,npc_rect)
    #testar limites janela
    if player_rect.left <  0 or player_rect.top < 0 or player_rect.right > largura or player_rect.bottom > altura:
        janela.blit(texto,(300,100))
        player_stats = False

    if player_stats == False:
        janela.blit(texto,(50,50))
    #atualizar a janela
    pygame.display.flip()

    #verificar ass colisões
    if player_rect.colliderect(npc_rect):
        player_stats= False

    #verificar se o jogador morreu

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.QUIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.KEYUP or event.key == pygame.K_RIGHT:
                player_speed_x= 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed_y= 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.QUIT
                run = False
            #mover para a esquerda
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_speed_x = -1
            #mover para a direita
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_speed_x = 1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed_y = -1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed_y = 1