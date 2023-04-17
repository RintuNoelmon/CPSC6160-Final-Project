import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Functions
def draw_text(surface, text, font, color, x, y, outline=0, outline_color=BLACK):
    lines = text.splitlines()
    total_height = len(lines) * font.get_height()
    y -= total_height // 2
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y + i * font.get_height()))
        if outline > 0:
            outline_text = font.render(line, True, outline_color)
            for dx in range(-outline, outline + 1):
                for dy in range(-outline, outline + 1):
                    if dx != 0 or dy != 0:
                        surface.blit(outline_text, (text_rect.x + dx, text_rect.y + dy))
        surface.blit(text_surface, text_rect)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Display")

running = True

font = pygame.font.Font(None, 32)
bold_font = pygame.font.Font(None, 32)
bold_font.set_bold(True)

text = """Our main character Akio, was an
ordinary Japanese high school student,
until he/she was mysteriously transported
to a magical world of Eldoria.
Eldoria is filled with monsters, magic,
and adventures. Akio finds his/herself
in a strange world and does not remember
how he/she got there after his/her death."""

while running:
    screen.fill(BG_COLOR)
    draw_text(screen, text, bold_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, 1, BLACK)
    draw_text(screen, "Click to continue...", bold_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150, 1, BLACK)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False

# Display Level 1 and Task
running = True
while running:
    screen.fill(BG_COLOR)
    draw_text(screen, "Level 1", bold_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, 1, BLACK)
    draw_text(screen, "Task: Explore the mysterious land to reach the end", bold_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, 1, BLACK)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

pygame.quit()
