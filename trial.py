import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Rendering Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 24)

def render_multiline_text_with_border(text, max_width):
    lines = []
    words = text.split()
    current_line = ''
    for word in words:
        test_line = current_line + ' ' + word if current_line != '' else word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    
    # Render text
    text_surfaces = []
    for line in lines:
        text_surface = font.render(line, True, BLACK)
        text_surfaces.append(text_surface)

    # Calculate bounding rectangle
    max_text_width = max(surface.get_width() for surface in text_surfaces)
    total_text_height = sum(surface.get_height() for surface in text_surfaces)

    # Draw border around the text block
    border_rect = pygame.Rect(10 - 5, (HEIGHT - total_text_height) // 2 - 5, max_text_width + 10, total_text_height + 10)
    pygame.draw.rect(screen, BLACK, border_rect, 1)

    # Blit text onto the screen
    y_offset = (HEIGHT - total_text_height) // 2
    for surface in text_surfaces:
        screen.blit(surface, (10, y_offset))
        y_offset += surface.get_height()



# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill(WHITE)

    # Render and display multiline text
    max_width = 200
    text = "This is a long text that should be rendered on multiple lines because it exceeds the maximum width."
    render_multiline_text_with_border(text, max_width)


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
