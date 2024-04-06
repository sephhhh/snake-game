import pygame
import random
import threading




def main():
    global screen, copies
    pygame.init()

    x = 450
    y = 450
    l = 50
    w = 50
    screen = pygame.display.set_mode((900,900))
    clock = pygame.time.Clock()
    snake_segments = [pygame.Rect(x, y , 50, 50)]
    
    point = pygame.Rect(randX(snake_segments), randY(snake_segments),w,l)
    right = False
    left = False
    up = False
    down = False
    frame_counter = 0


    while True:
        screen.fill("black")
        drawGrid()
        for segment in snake_segments:
            pygame.draw.rect(screen,"red", segment)
        apple = pygame.draw.rect(screen, "green", point)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(snake_segments)
                    print(snake_segments[0].x)
                    pygame.quit()
                elif event.key == pygame.K_RIGHT:
                    if len(snake_segments) == 1 or left == False:
                        right = True
                        left = False
                        up = False
                        down = False
                elif event.key == pygame.K_LEFT:
                    if len(snake_segments) == 1 or right == False:
                        right = False
                        left = True
                        up = False
                        down = False
                elif event.key == pygame.K_DOWN:
                    if len(snake_segments) == 1 or up == False:
                        right = False
                        left = False
                        up = False
                        down = True
                elif event.key == pygame.K_UP:
                    if len(snake_segments) == 1 or down == False:
                        right = False
                        left = False
                        up = True
                        down = False
                    
        head = snake_segments[0].copy()
        
        if apple.colliderect(head):
            if right == True:
                snake_segments.append(pygame.Rect(head.x-50, head.y, 50, 50))
            elif left == True:
                snake_segments.append(pygame.Rect(head.x+50, head.y, 50, 50))
            elif down == True:
                snake_segments.append(pygame.Rect(head.x, head.y-50, 50, 50))
            elif up==True:
                snake_segments.append(pygame.Rect(head.x, head.y+50, 50, 50))

            point = pygame.Rect(randX(snake_segments), randY(snake_segments),w,l)

        if len(snake_segments) > 1:
            for segment in snake_segments[1:]:
                if head == segment:
                    pygame.quit()
                    raise SystemExit
                
        if frame_counter == 7:
            if right == True:
                if head.x < 850:                    
                    head.x+=50
                    snake_segments.insert(0, head)
                    snake_segments.pop()
                else:
                    pygame.quit()
                    raise SystemExit
            elif left == True:
                if head.x > 0:
                    head.x-=50
                    snake_segments.insert(0, head)
                    snake_segments.pop()
                else:
                    pygame.quit()
                    raise SystemExit
            elif down == True:
                if head.y < 850:
                    head.y+=50
                    snake_segments.insert(0, head)
                    snake_segments.pop()
                else:
                    pygame.quit()
                    raise SystemExit
            elif up == True:
                if head.y > 0:
                    head.y-=50
                    snake_segments.insert(0, head)
                    snake_segments.pop()
                else:
                    pygame.quit()
                    raise SystemExit
                    
                
            frame_counter = 0
        else:
            frame_counter+=1

        pygame.display.flip()
        clock.tick(60)


def randX(snake):
    numX = random.randint(0,17)*50
    for seg in snake:
        while numX == seg.x:
            numX = random.randint(0,17)*50
    return numX

def randY(snake):
    numY = random.randint(0,17)*50
    for seg in snake:
        while numY == seg.y:
            numY = random.randint(0,17)*50
    return numY


def drawGrid():
    blockSize = 50
    for x in range(0, 900, blockSize):
        for y in range(0, 900, blockSize):
            rect = pygame.Rect(x,y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)


if __name__ == "__main__":
    main()
