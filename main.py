import sys
import pygame
from screen import Screen

def init_pygame():
    """
    Inicia o jogo
    """
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()




def game_loop(game_object,game_screen):

    Screen.set_audio()

    while(True):
        for event in Screen.events():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            ## Pega as teclas que foram apertadas    
            key_presses = Screen.key_pressed()
            ## Atualiza os estados do paddle e do puckle    
            game_object.update(key_presses)
            ## Atualiza o estado do jogo e manda um dicionário de volta
            ## Esse state deve ter:
            ## Score da direita
            ## Score da esqueda
            ## Posições já atualizadas
            ## Se o jogo terminou ou não
            state = game_object.current_state()

            if(state['goal_left'] or state['goal_right']):
                Screen.play_goal_sound()
    
            if(state['collision']):
                Screen.play_hit_sound()

            if(state['finish']):
                Screen.quit()
                sys.exit()

            Screen.render_state(state)

if __name__ == "__main__":
   
   Screen.init_game()
   game_object = Game(pygame)
    while(True):
        game_loop(game_object)

    
        