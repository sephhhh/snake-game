import pygame
import random




def main():
    global screen, copies
    pygame.init()

    x = 450
    y = 450
    l = 50
    w = 50
    screen = pygame.display.set_mode((900,900))
    clock = pygame.time.Clock()
    snake = pygame.Rect(x, y , 50, 50)
    point = pygame.Rect(randomWidth(snake), randomHeight(snake),w,l)
    right = False
    left = False
    up = False
    down = False
    frame_counter = 0
    copy_counter = 0
    copies = {}
    rect_visible = False
 

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
            rect_visible = True
            point.update(randomWidth(snake), randomHeight(snake), 50, 50)
            if right == True:
                createCopy(copy_counter, snake)
                if len(copies) > 1:
                    copies[f"copy{len(copies) - 1}"].left = copies[f"copy{len(copies) - 2}"].left - 50
                else:
                    copies[f"copy{len(copies) - 1}"].left -= 50
            if left == True:
                createCopy(copy_counter, snake)
                if len(copies) > 1:
                    copies[f"copy{len(copies) - 1}"].left = copies[f"copy{len(copies) - 2}"].left + 50
                else:
                    copies[f"copy{len(copies) - 1}"].left += 50
            if down == True:
                createCopy(copy_counter, snake)
                if len(copies) > 1:
                    copies[f"copy{len(copies) - 1}"].top = copies[f"copy{len(copies) - 2}"].top - 50
                else:
                    copies[f"copy{len(copies) - 1}"].top -= 50
            if up == True:
                createCopy(copy_counter, snake)
                if len(copies) > 1:
                    copies[f"copy{len(copies) - 1}"].top = copies[f"copy{len(copies) - 2}"].top + 50
                else:
                    copies[f"copy{len(copies) - 1}"].top += 50
            copy_counter+=1

        if rect_visible:
            for i in range(0, len(copies)):
                pygame.draw.rect(screen, "red", copies[f"copy{i}"])

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
                if copies:
                    for i in range(0, len(copies)):
                        if copies[f"copy{i}"].top == snake.y:
                            copies[f"copy{i}"].left += 50
                        if copies[f"copy{i}"].top > snake.y:
                            copies[f"copy{i}"].top -= 50
                        elif copies[f"copy{i}"].top < snake.y:
                            copies[f"copy{i}"].top += 50
    
            elif left == True and snake.x > 0:
                snake.x-=50
                if copies:
                    for i in range(0, len(copies)):
                        if copies[f"copy{i}"].top == snake.y:
                            copies[f"copy{i}"].left -= 50
                        if copies[f"copy{i}"].top > snake.y:
                            copies[f"copy{i}"].top -= 50
                        elif copies[f"copy{i}"].top < snake.y:
                            copies[f"copy{i}"].top += 50


            elif down == True and snake.y < 850:
                snake.y+=50
                if copies:
                    for i in range(0, len(copies)):
                        if copies[f"copy{i}"].left == snake.x:
                            copies[f"copy{i}"].top += 50
                        if copies[f"copy{i}"].left > snake.x:
                            copies[f"copy{i}"].left -= 50
                        elif copies[f"copy{i}"].left < snake.x:
                            copies[f"copy{i}"].left += 50

            elif up == True and snake.y > 0:
                snake.y-=50
                if copies:
                    for i in range(0, len(copies)):
                        if copies[f"copy{i}"].left == snake.x:
                            copies[f"copy{i}"].top -= 50
                        if copies[f"copy{i}"].left > snake.x:
                            copies[f"copy{i}"].left -= 50
                        elif copies[f"copy{i}"].left < snake.x:
                            copies[f"copy{i}"].left += 50
                
            frame_counter = 0
        else:
            frame_counter+=1
        


        pygame.display.flip()
        clock.tick(60)

def createCopy(copy_counter, snake):
    for i in range(0, copy_counter + 1):
            key = f"copy{i}"
            if key not in copies:
                copies[key] = snake.copy()

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
