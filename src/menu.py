import pygame, sys
from button import Button
from pygame import mixer

pygame.init()

#screen setup
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#load bg image
BG = pygame.image.load("assets/Background (1).png")

#fonts & colour
FONT = pygame.font.Font(None, 50)
BASE_COLOR = (255, 255, 255)  # White
HOVERING_COLOR = (255, 0, 0)  # Red

#initialisng mixer
pygame.init()
pygame.mixer.init()

#load and play bg music
pygame.mixer.music.load("assets/background_music.ogg") 
pygame.mixer.music.set_volume(1)  #volume
pygame.mixer.music.play(-1)  #loop music


def get_font(size):
    """Return a pygame font object."""
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))  #draw bg

        #mouse pos
        mouse_pos = pygame.mouse.get_pos()

        #title bg
        pygame.draw.rect(SCREEN, "#b68f40", (100, 50, 1070, 120))  # Mustard-yellow rectangle

        #title text
        title_font = get_font(65)  # Adjust font size for the title
        title_text = title_font.render("Snakes & Ladders", True, "Black")  # Black text
        title_rect = title_text.get_rect(center=(640, 110))  # Centered position
        SCREEN.blit(title_text, title_rect)

        #button creation 
        new_game_button = Button(
            image=None, pos=(640, 250), 
            text_input="New Game", font=get_font(50), base_color="#d7fcd4", hovering_color="Red"
        )
        load_game_button = Button(
            image=None, pos=(640, 350), 
            text_input="Load Game", font=get_font(50), base_color="#d7fcd4", hovering_color="Red"
        )
        save_game_button = Button(
            image=None, pos=(645, 450), 
            text_input="Save Game", font=get_font(50), base_color="#d7fcd4", hovering_color="Red"
        )
        quit_button = Button(
            image=None, pos=(640, 550), 
            text_input="Quit", font=get_font(50), base_color="#d7fcd4", hovering_color="Red"
        )

        # update button
        for button in [new_game_button, load_game_button, save_game_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)

        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.checkForInput(mouse_pos):
                    new_game()
                if load_game_button.checkForInput(mouse_pos):
                    load_game()
                if save_game_button.checkForInput(mouse_pos):
                    save_game()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def new_game():
    print("Starting a new game")
   

def load_game():
    print("Loading game")


def save_game():
    print("Saving game")


if __name__ == "__main__":
    main_menu()
