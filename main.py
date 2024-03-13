import pygame
import random




def main():
    global screen
    pygame.init()

    x = 450
    y = 450
    screen = pygame.display.set_mode((900,900))
    clock = pygame.time.Clock()
    snake = pygame.Rect(x, y , 50, 50)
    point = pygame.Rect(randomWidth(snake), randomHeight(snake),50,50)
    right = False
    left = False
    up = False
    down = False
    frame_counter = 0
 

    while True:
        screen.fill("black")
        drawGrid()
        snake_draw = pygame.draw.rect(screen, "red", snake)
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

        if snake_draw.colliderect(apple):
            point.update(randomWidth(snake), randomHeight(snake), 50, 50)


        if snake.x == 900:
            snake.x = 850
        elif snake.x == 0:
            snake.x = 0
        if snake.y == 900:
            snake.y = 850
        elif snake.y == 0:
            snake.y = 0

        if frame_counter == 7:
            if right == True and snake.x < 850:
                snake.x+=50
            elif left == True and snake.x > 0:
                snake.x-=50
            elif down == True and snake.y < 850:
                snake.y+=50
            elif up == True and snake.y > 0:
                snake.y-=50
            
            frame_counter = 0
        else:
            frame_counter+=1

        pygame.display.flip()
        clock.tick(60)


def randomWidth(snake):
    randomNum = random.randint(1,17)*50
    while randomNum == snake.x:
        randomNum = random.randint(1,17)*50
    return randomNum

def randomHeight(snake):
    randomNum = random.randint(1,17)*50
    while randomNum == snake.y:
        randomNum = random.randint(1,17)*50
    return randomNum

def drawGrid():
    blockSize = 50
    for x in range(0, 900, blockSize):
        for y in range(0, 900, blockSize):
            rect = pygame.Rect(x,y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)

if __name__ == "__main__":
    main()
