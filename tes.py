
import pygame
import sys

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация Pygame
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Text Input")

clock = pygame.time.Clock()

# Настройка шрифта
font = pygame.font.Font(None, 36)

# Создание поля ввода текста
input_rect = pygame.Rect(50, 100, 200, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
text_surface = font.render(text, True, color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                text_surface = font.render(text, True, color)

    screen.fill(WHITE)
    width = max(200, text_surface.get_width()+10)
    input_rect.w = width
    pygame.draw.rect(screen, color, input_rect, 2)
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    pygame.display.flip()
    clock.tick(30)