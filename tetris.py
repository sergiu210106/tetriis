import pygame
import sys
from game import Game
from colors import Colors
pygame.init()

titleFont = pygame.font.Font(None, 40)
scoreSurface = titleFont.render("Score :", True, Colors.white)
nextSurface = titleFont.render("Next", True, Colors.white)
gameOverSurface = titleFont.render("Game Over!", True, Colors.white)

scoreRect = pygame.Rect(320, 55, 170, 60)
nextRect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Python Tetris")

music = pygame.mixer.Sound("tetrisMusic.mp3")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if game.gameOver == True:
                game.gameOver = False
                game.reset()
            
            if event.key == pygame.K_LEFT and game.gameOver == False:
                game.moveLeft()
            if event.key == pygame.K_RIGHT and game.gameOver == False:
                game.moveRight()
            if event.key == pygame.K_DOWN and game.gameOver == False:
                game.moveDown()
                game.updateScore(0, 1)
            if event.key == pygame.K_UP and game.gameOver == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.gameOver == False:
            game.moveDown()
    scoreValueSurface = titleFont.render(str(game.score), True, Colors.white)
    
    screen.fill(Colors.darkBlue)
    
    screen.blit(scoreSurface, (365, 20, 20, 50))
    screen.blit(nextSurface, (375, 180, 50, 50))
    if game.gameOver == True:
        screen.blit(gameOverSurface, (320, 450, 50, 50))
        
    pygame.draw.rect(screen, Colors.lightBlue, scoreRect, 0, 10)
    screen.blit(scoreValueSurface, scoreValueSurface.get_rect(centerx = scoreRect.centerx, 
                                                              centery = scoreRect.centery))
    pygame.draw.rect(screen, Colors.lightBlue, nextRect, 0, 10)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)