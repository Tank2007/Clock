
import pygame
import time


pygame.init()

width, height = 400, 100
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Clock")

font = pygame.font.Font(None, 48)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.strftime("%H:%M:%S")

    screen.fill((0, 0, 0))

    time_text = font.render(current_time, True, (0, 0, 255))

    screen.blit(time_text, (width // 2 - time_text.get_width() // 2, height // 2 - time_text.get_height() // 2))

    pygame.display.flip()

    clock.tick(1)

pygame.quit()
