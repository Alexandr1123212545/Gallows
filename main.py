import pygame
from generate import *
import sys

pygame.init()
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 490
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

start = 0
screen = pygame.display.set_caption('HangMan')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font_1 = pygame.font.SysFont('italic', 40)
font_2 = pygame.font.SysFont('italic', 100)
font_3 = pygame.font.SysFont('italic', 80)

back_ground = pygame.image.load(f'image/image_0{start}.jpg')

input_box = pygame.Rect(10, 200, 100, 40)

btn_ok = pygame.Rect(10, 250, 100, 70)
btn_ok_text = font_1.render('ОК', True, BLACK)

btn_game = pygame.Rect(300, 320, 200, 70)
btn_game_text = font_3.render('Грати', True, BLACK)

game = True
user_input = ''
tries = 7
secret_word = None
message = 0
entered_let = []
messages = [
    ' ',                             
    'Потррібно ввести одну літеру або слово цілком!',                 
    'Залишилось спроб: ',           
    'GAME OVER',                    
    'Ця літера вже була',     
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
            if btn_game.collidepoint(event.pos) and not game:
                game = True
                tries = 7
                start, message = 0, 0
                clue, word, secret_word = generate_word()
                entered_let = []
                back_ground = pygame.image.load(f'image/image_0{start}.jpg')
            if btn_ok.collidepoint(event.pos) and game:
                message = 0
                if user_input in word or user_input in entered_let:
                    message = 4
                    user_input = ''
                    continue
                if not check(user_input):
                    message = 1
                    user_input = ''
                    continue
                if user_input not in entered_let:
                    entered_let.append(user_input)
                if len(user_input) == 1:
                    letter = [i for i, char in enumerate(secret_word.upper()) if char == user_input]
                    if letter:
                        for num in letter:
                            word[num] = user_input
                        if '_' not in word:
                            game = False
                            start, message = 0, 5
                    else:
                        start += 1; tries -= 1
                else:
                    if user_input == secret_word:
                        game = False
                        start, message = 0, 5
                    start += 1; tries -= 1
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
    

    clock.tick(20)
    screen.blit(back_ground, (0, 0))

    entered_text = font_1.render('*'.join(entered_let), True, BLUE)
    entered_rect = entered_text.get_rect(left=10, top=40) 

    secret_text = font_3.render(' '.join(word), True, BLACK)
    secret_rect = secret_text.get_rect(center=((WIDTH // 2, 150)))

    over_text = font_2.render(messages[3], True, RED)
    over_rect = over_text.get_rect(center=((WIDTH // 2), (HEIGHT // 2)))

    win_text = font_2.render(messages[5], True, GREEN)
    win_rect = win_text.get_rect(center=((WIDTH // 2), (HEIGHT // 2)))

    try_text = font_1.render(f'{messages[2]} {tries}', True, BLACK)
    try_rect = try_text.get_rect(left=10, top=400)
  
    warning_text = font_1.render(messages[message], True, RED)
    warning_rect = warning_text.get_rect(center=(WIDTH // 2, 80))

    clue_text = font_1.render(clue, True, BLACK)
    clue_rect = clue_text.get_rect(center=(WIDTH // 2, 20))
       
    pygame.draw.rect(screen, YELLOW, btn_ok)
    pygame.draw.rect(screen, BLUE, btn_ok, 4)
    text_in_btn_ok = btn_ok_text.get_rect(center=(btn_ok.center))

    input_text = font_1.render(user_input, True, BLACK)
    width = max(100, input_text.get_width()+10)
    input_box.w = min(width, 300)
    pygame.draw.rect(screen, BLUE, input_box, 4)
    
    if not game:
        screen.blit(pygame.image.load(f'image/image_0{start}.jpg'), (0, 0)) 
        pygame.draw.rect(screen, GREEN, btn_game)
        pygame.draw.rect(screen, BLACK, btn_game, 4)
        text_in_btn_game = btn_game_text.get_rect(center=(btn_game.center))

        screen.blit(over_text if not tries else win_text, over_rect if not tries else win_rect)
        screen.blit(btn_game_text, text_in_btn_game)                                                       
    else:                                                           
        screen.blit(entered_text, entered_rect)
        screen.blit(try_text, try_rect)                             
        screen.blit(warning_text, warning_rect)                         
        screen.blit(input_text, (input_box.x+5, input_box.y+5))      
        screen.blit(clue_text, clue_rect)                               
        screen.blit(btn_ok_text, text_in_btn_ok)                      
        screen.blit(secret_text, secret_rect)                           
    pygame.display.flip()

    

