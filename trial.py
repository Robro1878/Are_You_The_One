import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Messaging App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 24)

# Messages
messages = [
    "Hello!",
    "How are you?",
    "I'm good, thanks!",
    "What about you?",
    "I'm doing well too.",
    "That's great!",
    "We should catch up sometime.",
    "Definitely!",
    "Let's plan something soon."
]

# Scroll functionality
scroll_y = 0
scroll_speed = 30

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:  # Scroll up
                scroll_y += scroll_speed
            elif event.button == 4:  # Scroll down
                scroll_y -= scroll_speed

    # Fill the screen
    screen.fill(WHITE)

    # Calculate the visible messages based on the scroll position
    start_index = max(0, min(len(messages) - 1, len(messages) - (HEIGHT // 30)))
    visible_messages = messages[start_index:]

    # Display messages
    for i, message in enumerate(visible_messages):
        message_text = font.render(message, True, BLACK)
        text_rect = message_text.get_rect(topleft=(10, i * 30 - scroll_y))
        screen.blit(message_text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
