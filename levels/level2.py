import pygame
import sys

def run_level2(window):
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    characters = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]

    classes = [
        {"id": 1, "class_name": "Warrior"},
        {"id": 2, "class_name": "Mage"},
        {"id": 3, "class_name": "Archer"}
    ]

    running = True
    while running:
        window.fill((255, 255, 255))

        instruction_text = font.render('Use INNER JOIN to combine character and class data', True, (0, 0, 0))
        window.blit(instruction_text, (50, 50))

        for character in characters:
            class_name = next(cls["class_name"] for cls in classes if cls["id"] == character["id"])
            character_text = font.render(f"{character['name']} - {class_name}", True, (0, 0, 0))
            window.blit(character_text, (50, 100 + characters.index(character) * 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(30)
