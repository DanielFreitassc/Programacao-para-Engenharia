#Adicionar musica com o pygame!
import pygame
pygame.init()
pygame.mixer.music.load("banido_FzWil58.mp3")
pygame.mixer.music.play()
pygame.event.wait()
