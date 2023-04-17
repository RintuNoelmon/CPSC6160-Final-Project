import pygame
import sys
import textwrap

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXT_WIDTH = 180

def draw_text(surface, text, font, color, x, y, outline=0, outline_color=BLACK):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(x=x, y=y + i * font.get_height())
        if outline > 0:
            outline_text = font.render(line, True, outline_color)
            for dx in range(-outline, outline + 1):
                for dy in range(-outline, outline + 1):
                    if dx != 0 or dy != 0:
                        surface.blit(outline_text, (text_rect.x + dx, text_rect.y + dy))
        surface.blit(text_surface, text_rect)

def wrap_text(text, width):
    return "\n".join(textwrap.wrap(text, width))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dialogue Example")

running = True
font = pygame.font.Font(None, 20)
bold_font = pygame.font.Font(None, 20)
bold_font.set_bold(True)

dialogue = [
    ("Azura", "Welcome to Eldoria Akio. I understand that you should be very confused right now."),
    ("Akio", "Yes. Could you please tell me whats going on?"),
    ("Azura", "I was the one who summoned you as a hero to defeat the demon lord, Leviathan, who threatens to destroy the world."),
    ("Akio", "I am just a normal student. How can I defeat a demon lord?"),
    ("Azura", "I will provide you with a sword called Totsuka. It's a medium-sized sword with a red stone as the pommel."),
    ("Akio", "Thank you for this powerful weapon."),
    ("Azura", "I will also bless you, so any damage dealt by weak mobs will be negated. This should help you in your journey."),
    ("Akio", "Thank you, Azura. I'll do my best to protect Eldoria."),
    ("Azura", "You first trial it to wield Totsuka to defeats the enemies nearby."),
    ("Akio", "I'm ready for the trial."),
]

for i, (char, text) in enumerate(dialogue):
    dialogue[i] = (char, wrap_text(text, TEXT_WIDTH))

while running:
    screen.fill(BG_COLOR)
    y = 10
    for character, text in dialogue:
        draw_text(screen, character + ":", bold_font, WHITE, 10, y, 1, BLACK)
        y += bold_font.get_height()
        draw_text(screen, text, font, WHITE, 10, y, 1, BLACK)
        y += len(text.splitlines()) * font.get_height() + 20
    draw_text(screen, "Click to continue...", bold_font, WHITE, 10, y, 1, BLACK)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False

pygame.quit()
