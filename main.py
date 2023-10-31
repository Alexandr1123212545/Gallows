import pygame
from random import choice
from pygame.color import THECOLORS as col
from generate import *
import sys

pygame.init()
clock = pygame.time.Clock()
start = 0
screen = pygame.display.set_caption('GALLOWS')
screen = pygame.display.set_mode((800, 490))
font_1 = pygame.font.SysFont('italic', 40)
font_2 = pygame.font.SysFont('italic', 100)
font_3 = pygame.font.SysFont('italic', 30)
font_4 = pygame.font.SysFont('italic', 80)

back_ground = pygame.image.load(f'image/image_0{start}.jpg')

input_box = pygame.Rect(10, 200, 100, 40)

button_OK_rect = pygame.Rect(10, 250, 100, 70)
button_OK_text = font_1.render('ОК', True, col['black'])

button_GAME_rect = pygame.Rect(300, 320, 200, 70)
button_GAME_text = font_4.render('Играть', True, col['black'])

game = True
user_input = ''
tries = 7
secret_word = None
message = 0
break_out = False
entered_let = []
messages = [
    ' ',                             
    'Нужно ввести букву или слово!',                 
    'Осталось попыток: ',           
    'GAME OVER',                    
    'Ты уже угадал эту букву!',     
    'CONGRATULATIONS',
]
def check(letter):
    if not letter.isalpha():
        return False
    return True
clue, word, secret_word = generate_word()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_GAME_rect.collidepoint(event.pos) and not game:
                game = True
                tries = 7
                start, message = 0, 0
                clue, word, secret_word = generate_word()
                entered_let = []
                screen.blit(back_ground, (0, 0))
            if button_OK_rect.collidepoint(event.pos):
                print(start)
                message = 0
                if user_input in word:
                    message = 4
                    user_input = ''
                    continue
                if not check(user_input):
                    message = 1
                    user_input = ''
                    continue
                if len(user_input) == 1:
                    letter = [i for i, char in enumerate(secret_word.upper()) if char == user_input]
                    if letter:
                        for num in letter:
                            word[num] = user_input
                        if '_' not in word:
                            message = 5
                            game = False
                            start, message = 0, 5
                    else:
                        start += 1; tries -= 1
                        # tries -= 1

                else:
                    if user_input == secret_word:
                        message = 5
                        game = False
                        start, message = 0, 5
                    start += 1; tries -= 1
                    # tries -= 1
                if not tries:
                    game = False
                    start = 7
                back_ground = pygame.image.load(f'image/image_0{start}.jpg')
            user_input = ''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE or len(user_input) >= 12:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode.upper()
                if user_input not in entered_let:
                    entered_let.append(user_input)

    clock.tick(20)
    screen.blit(back_ground, (0, 0))

    entered_letters = font_3.render(' '.join(entered_let), True, col['blue'])
    entered_rect = entered_letters.get_rect(left=10, top=5) 

    secret_text = font_4.render(' '.join(word), True, col['black'])
    secret_rect = secret_text.get_rect(center=((800 // 2, 150)))

    over_text = font_2.render(messages[3], True, col['red'])
    over_rect = over_text.get_rect(center=((800 // 2), (490 / 2)))

    win_text = font_2.render(messages[5], True, col['green'])
    win_rect = win_text.get_rect(center=((800 // 2), (490 / 2)))

    tries_text = font_3.render(f'{messages[2]} {tries}', True, col['black'])
    tries_rect = tries_text.get_rect(left=10, top=400)
  
    warning_text = font_3.render(messages[message], True, col['red'])
    warning_rect = warning_text.get_rect(left=5, top=350)

    text_clue = font_1.render(clue, True, col['black'])
    text_rect = text_clue.get_rect(left=20, top=30)
       
    pygame.draw.rect(screen, col['yellow'], button_OK_rect)
    pygame.draw.rect(screen, col['blue'], button_OK_rect, 4)
    text_button_OK = button_OK_text.get_rect(center=(button_OK_rect.center))

    text_surface = font_1.render(user_input, True, col['black'])
    width = max(100, text_surface.get_width()+10)
    input_box.w = min(width, 300)
    pygame.draw.rect(screen, col['blue'], input_box, 4)
    
    if not game:
        screen.blit(pygame.image.load(f'image/image_0{start}.jpg'), (0, 0)) 
        pygame.draw.rect(screen, col['green'], button_GAME_rect)
        pygame.draw.rect(screen, col['black'], button_GAME_rect, 4)
        text_button_GAME = button_GAME_text.get_rect(center=(button_GAME_rect.center))

        screen.blit(over_text if not tries else win_text, over_rect if not tries else win_rect)
        screen.blit(button_GAME_text, text_button_GAME)                                                                  
    else:                                                           
        screen.blit(entered_letters, entered_rect)
        screen.blit(tries_text, tries_rect)                             
        screen.blit(warning_text, warning_rect)                         
        screen.blit(text_surface, (input_box.x+5, input_box.y+5))      
        screen.blit(text_clue, text_rect)                               
        screen.blit(button_OK_text, text_button_OK)                      
        screen.blit(secret_text, secret_rect)                           
    pygame.display.flip()

    

