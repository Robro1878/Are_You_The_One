import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input Field")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.SysFont(None, 24)

# Text input field
text = ""
input_rect = pygame.Rect(100, 100, 200, 30)
active = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Fill the screen
    screen.fill(WHITE)

    # Draw text input field
    pygame.draw.rect(screen, GRAY, input_rect)
    pygame.draw.rect(screen, BLACK, input_rect, 2)
    input_text = font.render(text, True, BLACK)
    screen.blit(input_text, input_rect.move(5, 5))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
