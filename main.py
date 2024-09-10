import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Most Popular Games")

img = pygame.image.load("MPG1.jfif")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))

while(True):
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Fortnite", True, (0,0,0))
    display_surface.fill((255,0,0))
    display_surface.blit(image, (0,0))
    display_surface.blit(text,(210,180))
    pygame.display.update()
    time.sleep(2)

    img2 = pygame.image.load("MPG2.jfif")
    font2 = pygame.font.SysFont("Arial",36)
    text2 = font2.render("Minecraft",True,(0,0,0))
    display_surface.fill((255,0,0))
    display_surface.blit(img2,(0,0))
    display_surface.blit(text2,(30,30))
    pygame.display.update()
    time.sleep(2)

    img3 = pygame.image.load("MPG3.jfif")
    font3 = pygame.font.SysFont("Times New Roman", 36)
    text3 = font3.render("Roblox",True,(255,0,0))
    display_surface.fill((255,0,0))
    display_surface.blit(img3,(0,0))
    display_surface.blit(text3,(30,30))
    pygame.display.update()
    time.sleep(2)