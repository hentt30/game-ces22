import os
import constants as const
import pygame

class Screen:
    
    game_interface = pygame
        
    assets_directory = os.path.join(os.path.dirname(__file__), 'assets')
    
    ## Sounds
    paddle_hit = game_interface.mixer.Sound(os.path.join(assets_directory, 'hit.wav'))
    goal_whistle = game_interface.mixer.Sound(os.path.join(assets_directory, 'goal.wav'))

        
    clock = game_interface.time.Clock()

    width = const.WIDTH
    height = const.HEIGHT

    screen =  game_interface.display.set_mode((self.width, self.height))

    @staticmethod
    def init_game():
        game_interface.mixer.pre_init(44100, -16, 2, 2048)
        game_interface.mixer.init()
        game_interface.init()
    
    @staticmethod
    def events():
        """
        Retorna os eventos que ocorreram
        """
        return game_interface.event.get()
    
    @staticmethod
    def key_pressed():
        """
        Retorna as teclas pressionadas
        """
        return game_interface.key.get_pressed()
    
    @staticmethod
    def play_goal_sound():
        """"
        Toca o som do gol
        """"
        return game_interface.mixer.Sound.play(goal_whistle)
    
    @staticmethod
    def play_hit_sound():
        """
        Toca o som quando há uma colisão
        """
        return game_interface.mixer.Sound.play(paddle_hit)  
    
    @staticmethod
    def quit():
        """
        Sai do jogo
        """
        return game_interface.quit()  

    @staticmethod
    def set_audio():
        """
         Inicia o aúdio antes do jogo começar
        """
        game_interface.mixer.music.load(os.path.join(assets_directory, 'back.mp3'))  # background music
        game_interface.mixer.music.play(-1)
        game_interface.mixer.music.set_volume(.2)
        
        