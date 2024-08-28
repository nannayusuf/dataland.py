import pygame
import sys

def run_level3(window):
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    characters = [
        {"name": "Alice", "level": 5},
        {"name": "Bob", "level": 3},
        {"name": "Charlie", "level": 2}
    ]

    running = True
    while running:
        window.fill((255, 255, 255))

        instruction_text = font.render('Use COUNT to calculate the number of characters', True, (0, 0, 0))
        window.blit(instruction_text, (50, 50))

        count_text = font.render(f"Number of characters: {len(characters)}", True, (0, 0, 0))
        window.blit(count_text, (50, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(30)
