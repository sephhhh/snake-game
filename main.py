import pygame
import random




def main():
    global screen
    pygame.init()

    screen = pygame.display.set_mode((900,900))
    clock = pygame.time.Clock()
    snake = pygame.Rect(450, 450, 50, 50)
    point = pygame.Rect(randomWidth(), randomHeight(),50,50)

    while True:
        screen.fill("black")
        drawGrid()
        pygame.draw.rect(screen, "red", snake)
        pygame.draw.rect(screen, "green", point)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RIGHT:
                    snake = snake.move(50,0)
                elif event.key == pygame.K_LEFT:
                    snake = snake.move(-50,0)
                elif event.key == pygame.K_DOWN:
                    snake = snake.move(0,50)
                elif event.key == pygame.K_UP:
                    snake = snake.move(0,-50)
        pygame.display.flip()
        clock.tick(60)

def randomWidth():
    randomNum = random.randint(0,18)*50
    while randomNum == 450:
        randomNum = random.randint(0,18)*50
    return randomNum

def randomHeight():
    randomNum = random.randint(0,18)*50
    while randomNum == 450:
        randomNum = random.randint(0,18)*50
    return randomNum

def drawGrid():
    blockSize = 50
    for x in range(0, 900, blockSize):
        for y in range(0, 900, blockSize):
            rect = pygame.Rect(x,y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)

if __name__ == "__main__":
    main()
