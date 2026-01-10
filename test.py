import pygame

def test_pygame():
    # Initialize all pygame modules
    pygame.init()

    # Create a simple window
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Pygame-CE Test")

    # Set a background color (Light Blue)
    screen.fill((173, 216, 230))
    
    # Draw a simple circle to prove graphics are working
    pygame.draw.circle(screen, (255, 0, 0), (200, 150), 50)

    # Refresh the display to show the changes
    pygame.display.flip()

    print("Pygame window opened! Close the window to continue.")

    # Simple loop to keep window open until you click 'X'
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # Cleanly shut down
    pygame.quit()
    print("Pygame shut down successfully.")

# Run the function
test_pygame()