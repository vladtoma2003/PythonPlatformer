import pygame, sys
from screen import *
from level import Level
from game_data import level_0
from player import *
from ui import *

class Game:
    def __init__(self):
        self.max_health = 100
        self.curren_health = 100
        self.coins = 0
        self.ui = UI(screen)
        self.level = Level(level_0, screen, self.change_coins)
        self.font = self.ui.font

    def change_coins(self, amount):
        self.coins += amount

    def check_game_over(self):
        if game.curren_health <= 0:
            screen.fill((0, 0, 0))

            screen.blit(self.font.render("GAME OVER", 1, (200, 200, 200)), (500, 300))

    def run(self):
        self.level.run()
        self.ui.show_health(self.curren_health, self.max_health)
        self.ui.show_coins(self.coins)
        self.ui.show_objective()
        # game.curren_health = game.curren_health - 1
        if self.level.alive == False:
            self.curren_health = 0
        if self.level.win == True:
            if self.coins == 18:
                screen.fill((0, 0, 0))
                screen.blit(self.font.render("YOU WON", 1, (200, 200, 200)), (500, 300))
                screen.blit(self.font.render("CONGRATS FOR COLLECTING ALL THE COINS!", 1, (200, 200, 200)), (175, 400))
            else:
                screen.fill((0, 0, 0))
                screen.blit(self.font.render("YOU WON", 1, (200, 200, 200)), (500, 300))
        if self.level.hurt == True:
            self.curren_health -= 0.5
            self.level.hurt = False
        self.check_game_over()


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)
