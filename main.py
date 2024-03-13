import pygame
import random




def main():
    global screen
    pygame.init()

    x = 450
    y = 450
    screen = pygame.display.set_mode((900,900))
    clock = pygame.time.Clock()
    point = pygame.Rect(randomWidth(), randomHeight(),50,50)
    right = False
    left = False
    up = False
    down = False
    frame_counter = 0
 

    while True:
        screen.fill("black")
        drawGrid()
        snake = pygame.draw.rect(screen, "red", (x, y ,50, 50))
        apple = pygame.draw.rect(screen, "green", point)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RIGHT:
                    right = True
                    left = False
                    up = False
                    down = False
                elif event.key == pygame.K_LEFT:
                    right = False
                    left = True
                    up = False
                    down = False
                elif event.key == pygame.K_DOWN:
                    right = False
                    left = False
                    up = False
                    down = True
                elif event.key == pygame.K_UP:
                    right = False
                    left = False
                    up = True
                    down = False

        if snake.colliderect(apple):
            point.update(randomWidth(), randomHeight(), 50, 50)

        if x == 900:
            x = 850
        elif x == 0:
            x = 0
        if y == 900:
            y = 850
        elif y == 0:
            y = 0

        if frame_counter == 7:
            if right == True and x < 850:
                x+=50
            elif left == True and x > 0:
                x-=50
            elif down == True and y < 850:
                y+=50
            elif up == True and y > 0:
                y-=50
            
            frame_counter = 0
        else:
            frame_counter+=1

        pygame.display.flip()
        clock.tick(60)


def randomWidth():
    randomNum = random.randint(1,18)*50

    while randomNum == 450:
        randomNum = random.randint(1,18)*50
    return randomNum

def randomHeight():
    randomNum = random.randint(1,18)*50
    while randomNum == 450:
        randomNum = random.randint(1,18)*50
    return randomNum

def drawGrid():
    blockSize = 50
    for x in range(0, 900, blockSize):
        for y in range(0, 900, blockSize):
            rect = pygame.Rect(x,y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)

if __name__ == "__main__":
    main()
