'''
Game Defend Aniladlas
Alunos: Simei Thander e Rafael Crisostomos
IFRN - TADS 2018.2 - www.ifrn.edu.br
'''
#importa o pygame
import pygame
#inicia o Pygame
pygame.init()
#obtem o clock do Pygame
clock = pygame.time.Clock()
#Define o tamanho da tela do jogo
display_width = 640
display_height = 480
#seta na variavel win o display com largura e altura
win = pygame.display.set_mode((display_width, display_height))
#Seta o nome do game na barra superior de titulos
pygame.display.set_caption("Defend Aniladlas")
#Define algumas variáveis para altura, largura, coordenada X e Y, velocidade
x = 15
y = 398
width = 64
height = 55
hitbox = (x+11, y, 39, 55)
#Velocidade
vel = 8
#Define que o loop começará verdadeiro
run = True
#Define a condição do pulo
is_jump = False
max_jump = 8
#Define a contagem do pulo
jump_count = 8
#Define para onde está percorrendo o personagem:
left = False
right = False
#contagem de passos
walk_count = 0
#estado do botão left:
press_left = False
#Condição de inicialização do Game
start_game = False

#váriaveis globais para oslug
x_slug = 0
y_slug = 410
width_slug = 64
height_slug = 42
end_slug = 598
walk_count_slug = 0
vel_slug = 2
patch_slug = [x_slug, end_slug]
hitbox_slug = (x_slug+5, y_slug+4, 50, height_slug-1)

#Função para fechar o Game se precionado a de fechar
def close_game():
    global run, start_game
    #Define um laço para os eventos do jogo
    for event in pygame.event.get():
        #Se o tipo do evento for igual a QUIT, a variavel run receberá falso
        if event.type == pygame.QUIT:
            run = False
            start_game = True
    return run

#Desenha o cenário
def draw_scenario():
    win.blit(pygame.image.load("arquivos/bg.jpg"),(0,0))
    bloco = pygame.image.load("arquivos/bloco.jpg")
    house = pygame.image.load("arquivos/house.png")
    win.blit(house,(50,211))
    cont = 0
    for i in range(0,31):
        win.blit(bloco,(cont,453))
        cont += 32
#desenha o personagem
def draw_char():
    global x, y, width, height, walk_count, left, right, press_left, hitbox
    #obtem as teclas
    keys = pygame.key.get_pressed()
    #carrega os sprites do personagem
    walk_right = [
    pygame.image.load("arquivos/player/player-skip/p_left_1.png"),
    pygame.image.load("arquivos/player/player-skip/p_left_2.png"),
    pygame.image.load("arquivos/player/player-skip/p_left_3.png"),
    pygame.image.load("arquivos/player/player-skip/p_left_4.png"),
    pygame.image.load("arquivos/player/player-skip/p_left_5.png"),
    pygame.image.load("arquivos/player/player-skip/p_left_6.png"),
    pygame.image.load("arquivos/player/player-skip/p_left_7.png"),
    pygame.image.load("arquivos/player/player-skip/p_left_8.png")]
    walk_left = [
    pygame.image.load("arquivos/player/player-skip/p_right_1.png"),
    pygame.image.load("arquivos/player/player-skip/p_right_2.png"),
    pygame.image.load("arquivos/player/player-skip/p_right_3.png"),
    pygame.image.load("arquivos/player/player-skip/p_right_4.png"),
    pygame.image.load("arquivos/player/player-skip/p_right_5.png"),
    pygame.image.load("arquivos/player/player-skip/p_right_6.png"),
    pygame.image.load("arquivos/player/player-skip/p_right_7.png"),
    pygame.image.load("arquivos/player/player-skip/p_right_8.png")]
    #sprite IDEL (parado)
    char_right_idle = pygame.image.load("arquivos/player/player-idle/p_right_idle.png")
    char_left_idle = pygame.image.load("arquivos/player/player-idle/p_left_idle.png")
    #define a animação de movimento do personagem
    if walk_count + 1 >= 16:
        walk_count = 0
    if press_left:
        char_position = char_left_idle
        if left:
            char_position = walk_left[walk_count//3]
            walk_count +=1
            press = True
    else:
        char_position = char_right_idle
        if right:
            char_position = walk_right[walk_count//3]
            walk_count +=1
            press = True
    win.blit(char_position, (x,y))
    hitbox = (x+11, y, 39, 55)
    pygame.draw.rect(win, (255,0,0), hitbox, 2)
#Cria o inimigo Slug
def draw_enemy_slug():
    global x_slug, y_slug, width_slug, height_slud, end_slug, walk_count_slug, vel_slug, patch_slug
    walk_left = [
    pygame.image.load("arquivos/monsters/slug/slug-left-1.png"),
    pygame.image.load("arquivos/monsters/slug/slug-left-2.png"),
    pygame.image.load("arquivos/monsters/slug/slug-left-3.png"),
    pygame.image.load("arquivos/monsters/slug/slug-left-4.png"),]
    walk_right = [
    pygame.image.load("arquivos/monsters/slug/slug-right-1.png"),
    pygame.image.load("arquivos/monsters/slug/slug-right-2.png"),
    pygame.image.load("arquivos/monsters/slug/slug-right-3.png"),
    pygame.image.load("arquivos/monsters/slug/slug-right-4.png"),]

    #move o inimigo
    if vel_slug > 0:
        if x_slug + vel_slug < patch_slug[1]:
            x_slug += vel_slug
        else:
            vel_slug = vel_slug * -1
            walk_count_slug = 0
    else:
        if x_slug - vel_slug > patch_slug[0]:
            x_slug += vel_slug
        else:
            vel_slug = vel_slug * -1
            walk_count_slug = 0

    #desenha o inimigo
    if walk_count_slug + 1 >= 8:
        walk_count_slug = 0
    if vel_slug > 0:
        win.blit(walk_right[walk_count_slug // 3],(x_slug, y_slug))
        walk_count_slug += 1
    else:
        win.blit(walk_left[walk_count_slug // 3],(x_slug, y_slug))
        walk_count_slug += 1
    hitbox_slug = (x_slug+5, y_slug+4, 50, height_slug-1)
    pygame.draw.rect(win, (255,0,0), hitbox_slug, 2)

#Define a movimentação do personagem
def move_char():
    global x, y, width, height, win, is_jump, jump_count, max_jump, left, right,press_left
    #Armazena na variável key a tecla pressionada
    keys = pygame.key.get_pressed()
    #Altera as variáveis de acordo com a tecla pressionada
    #A condição após o AND limita o personagem para nao sair da tela
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        right = False
        left = True
        press_left = True
    elif keys[pygame.K_RIGHT] and x < display_width - width - vel:
        x += vel
        right = True
        left = False
        press_left = False
    else:
        right = False
        left = False
        walk_count = 0
    #Se for pressionado a tecla de pulo, será realizado a condição abaixo:
    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        #define a velocidade e altura do pulo
        if jump_count >= -max_jump:
            #variavel para não deixar o pulo negativo
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = max_jump
def hit():
    print('hit')
    
#Tela de Inicio
while not start_game:
    #Chama o background do jogo
    win.blit(pygame.image.load("arquivos/bg.jpg"),(0,0))
    #Mostra na tela as informações iniciais
    win.blit(pygame.image.load("arquivos/infos.png"), (152,130))
    #desenha a tecla enter
    win.blit(pygame.image.load("arquivos/enter.png"), (192,360))
    #desenha o logo da tela
    win.blit(pygame.image.load("arquivos/logo.png"), (0,10))
    #atualiza a tela
    pygame.display.update()
    #Verifica se o jogador clicou em Enter para iniciar o jogo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        start_game = True
    close_game()

def draw():
    draw_char()
    draw_enemy_slug()
    pygame.display.update()
    
#Define o loop principal
while run:
    #define os frames per seconds do jogo
    clock.tick(60)
    #desenha o cenario:
    draw_scenario()
    #chama a função que desenha os objetos animados
    draw()
    #chama a funcao de mover o personagem
    move_char()
    #função: fechar o game
    close_game()
#encerra o Pygame
pygame.quit()
