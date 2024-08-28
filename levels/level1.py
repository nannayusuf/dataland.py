import pygame
import sys

def run_level1(window):
    # Inicializa fonte e clock
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    # Banco de dados simulado
    database = {
        "characters": [
            {"name": "Alice", "level": 5, "class": "Warrior"},
            {"name": "Bob", "level": 3, "class": "Mage"},
            {"name": "Charlie", "level": 2, "class": "Archer"}
        ]
    }

    # Variáveis para entrada do usuário e feedback
    input_text = ''
    feedback = ''

    running = True
    while running:
        # Processamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Verifica a consulta SQL
                    if input_text.lower() == "select name from characters":
                        names = ', '.join([char['name'] for char in database['characters']])
                        feedback = f"Correct! Names: {names}"
                    else:
                        feedback = "Incorrect query. Try again."
                    input_text = ''  # Limpa a entrada após o Enter
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Remove o último caractere
                else:
                    input_text += event.unicode  # Adiciona o caractere digitado

        # Preenche a tela com branco
        window.fill((255, 255, 255))

        # Renderiza a instrução do nível
        instruction_text = font.render('Use SELECT to retrieve character names', True, (0, 0, 0))
        window.blit(instruction_text, (50, 50))

        # Renderiza o campo de entrada
        input_box = font.render(f"SQL: {input_text}", True, (0, 0, 0))
        window.blit(input_box, (50, 150))
        
        # Renderiza o feedback
        feedback_box = font.render(feedback, True, (0, 0, 0))
        window.blit(feedback_box, (50, 200))

        # Atualiza a tela
        pygame.display.flip()
        clock.tick(30)

