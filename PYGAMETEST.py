import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Square properties
square_size = 50
square_x = SCREEN_WIDTH // 2 - square_size // 2
square_y = SCREEN_HEIGHT // 2 - square_size // 2
square_speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    
    # Move the square based on key presses
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed
    
    # Keep the square within the screen boundaries
    square_x = max(0, min(square_x, SCREEN_WIDTH - square_size))
    square_y = max(0, min(square_y, SCREEN_HEIGHT - square_size))
    
    # Fill the screen with white
    screen.fill(WHITE)
    
    # Draw the red square
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
