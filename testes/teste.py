import pygame
from pygame.locals import *

pygame.init()
print('Inicializando game...')

# Definindo as configurações de FPS
hertz = 60  # Taxa de atualização da tela em ciclos por segundo
fps_clock = pygame.time.Clock()

# Definindo as configurações da janela
window_size = (640, 480)
main_surface = pygame.display.set_mode(window_size)
pygame.display.set_caption('Academia Hacker')

# Definindo as cores RGB
fg_color = (0, 0, 0)
bg_color = (255, 255, 255)
greetings_surface = pygame.Surface(window_size)
greetings_surface.fill(bg_color)

# Preparando o primeiro texto
font_size = 25
font_obj = pygame.font.Font('freesansbold.ttf', font_size)
text_surface = font_obj.render('Preparando para salvar o mundo', True, fg_color, bg_color)
text_rect = text_surface.get_rect()
text_rect.center = greetings_surface.get_rect().center

# Preparando o segundo texto
dots = ''
dots_surface = font_obj.render(dots, True, fg_color, bg_color)
dots_rect = dots_surface.get_rect()
dots_rect.centerx = text_rect.left + text_rect.width
dots_rect.centery = text_rect.centery

# Setando o temporizador
pygame.time.set_timer(USEREVENT, 1000) # Cria um temporizador de 1 segundo

print('Nosso game começou!')
is_running = True

while is_running:  # Loop principal
    ######################
    # Entrada de usuário #
    ######################
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        elif event.type == USEREVENT:
            dots = dots+'.'
            if len(dots) > 3:
                dots='.'

    ############################
    # Atualização de Variáveis #
    ############################
    dots_surface = font_obj.render(dots, True, fg_color, bg_color) 
    # Limpe a tela e escreva os textos
    greetings_surface.fill(bg_color)
    greetings_surface.blit(text_surface, text_rect)
    greetings_surface.blit(dots_surface, dots_rect)
    

    ##########################
    # Atualização do Monitor #
    ##########################    
    main_surface.blit(greetings_surface, (0,0))
    pygame.display.update() 
    fps_clock.tick(hertz)
    
print('Fim de game.')
pygame.quit()