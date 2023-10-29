import pygame
from random import choice
from pygame.color import THECOLORS as col

pygame.init()
start = 0
screen = pygame.display.set_caption('GALLOWS')
screen = pygame.display.set_mode((800, 490))
font_1 = pygame.font.SysFont('italic', 40)
font_2 = pygame.font.SysFont('italic', 100)
font_3 = pygame.font.SysFont('italic', 30)
font_4 = pygame.font.SysFont('italic', 80)
input_box = pygame.Rect(80, 350, 100, 70)
button_rect = pygame.Rect(200, 350, 100, 70)
button_text = font_1.render('ОК', True, col['black'])
back_ground = pygame.image.load(f'image/image_0{start}.jpg')
user_text = ''
vocabulary = dict()
tries = 7
secret_word = None
message = 0
messages = [
    '',                             
    'Нужно ввести одну букву!',     
    'Осталось попыток: ',           
    'GAME OVER',                    
    'Ты уже угадал эту букву!',     
    'CONGRATULATIONS'               
]

with open('words.txt', 'r', encoding='utf-8') as file:
    for i in range(100):
        text = file.readline().split('-')
        vocabulary[text[0].strip().upper()] = text[1].strip()
while not secret_word:
    random_word = (choice(list(vocabulary.keys())))
    if len(random_word) <= 10:
        secret_word = random_word 
clue = vocabulary[secret_word]
word = ['_' for i in range(len(secret_word))]

def check(letter):
    if not(len(letter) == 1 and letter.isalpha()):
        return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if not check(user_text):
                    message = 1
                    user_text = ''
                    continue
                if user_text in word:
                    message = 4
                    user_text = ''
                    continue
                letter = [i for i, char in enumerate(secret_word.upper()) if char == user_text]
                if letter:
                    for num in letter:
                        word[num] = user_text
                        # user_text = ''
                    if '_' not in word:
                        message = 5
                    
                else:
                    start += 1
                    tries -= 1
                user_text = ''
                back_ground = pygame.image.load(f'image/image_0{start}.jpg')
            user_text = ''
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode.upper()

    screen.blit(back_ground, (0, 0))

    secret_text = font_4.render(' '.join(word), True, col['black'])
    secret_rect = secret_text.get_rect(center=((800 // 2, 150)))

    over_text = font_2.render(messages[3], True, col['red'])
    over_rect = over_text.get_rect(center=((800 // 2), (490 / 2)))

    win_text = font_2.render(messages[5], True, col['green'])
    win_rect = win_text.get_rect(center=((800 // 2), (490 / 2)))

    tries_text = font_3.render(f'{messages[2]} {tries}', True, col['black'])
    tries_rect = tries_text.get_rect(left=5, top=280)
    
    warning_text = font_3.render(messages[message], True, col['red'])
    warning_rect = warning_text.get_rect(left=5, top=300)

    text_clue = font_1.render(clue, True, col['black'])
    text_rect = text_clue.get_rect(left=20, top=30)

    pygame.draw.rect(screen, col['yellow'], button_rect)
    pygame.draw.rect(screen, col['blue'], button_rect, 4)
    text_rect_button = button_text.get_rect(center=(button_rect.center))



    text_surface = font_2.render(user_text, True, col['black'])
    pygame.draw.rect(screen, col['blue'], input_box, 4)

    if not tries:
        screen.blit(pygame.image.load(f'image/image_07.jpg'), (0, 0))   
        screen.blit(over_text, over_rect)
                                                                        
    elif message == 5:
        screen.blit(pygame.image.load(f'image/image_00.jpg'), (0, 0))   
        screen.blit(win_text, win_rect)
                                                                        
    else:                                                           
        screen.blit(tries_text, tries_rect)                             
        screen.blit(warning_text, warning_rect)                         
        screen.blit(text_surface, (input_box.x+30, input_box.y+5))      
        screen.blit(text_clue, text_rect)                               
        screen.blit(button_text, text_rect_button)                      
        screen.blit(secret_text, secret_rect)                           

    pygame.display.flip()

    

