import pygame
import random
<<<<<<< HEAD
from collections import deque
=======
import threading
>>>>>>> snake-2




def main():
    global screen, copies
    pygame.init()

    input_queue = deque()

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
                    input_queue.append('RIGHT')
                    right = True
                    left = False
                    up = False
                    down = False
                elif event.key == pygame.K_LEFT:
                    input_queue.append('LEFT')
                    right = False
                    left = True
                    up = False
                    down = False
                elif event.key == pygame.K_DOWN:
                    input_queue.append('DOWN')
                    right = False
                    left = False
                    up = False
                    down = True
                elif event.key == pygame.K_UP:
                    input_queue.append('UP')
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
<<<<<<< HEAD
            if input_queue:
                print(input_queue)
                direction = input_queue[0]
                #if right == True and snake.x < 850:
                if direction == "RIGHT" and snake.x < 900:
                    snake.x+=50
                    print(f"snake: {snake}")
                    if copies:
                        for i in range(0, len(copies)):
                            key = f'copy{i}'
                            value = copies[key]
                            print(f"{key}: {value}")
                            if copies[f"copy{i}"].top == snake.y:
                                copies[f"copy{i}"].left += 50
                            if copies[f"copy{i}"].top > snake.y:
                                copies[f"copy{i}"].top -= 50
                            elif copies[f"copy{i}"].top < snake.y:
                                copies[f"copy{i}"].top += 50
                    if right != True:
                        print('this runs')
                        input_queue.popleft()
                    print('-------')
        
                #elif left == True and snake.x > 0:
                elif direction == "LEFT" and snake.x > 0:
                    snake.x-=50
                    print('left runs')
                    print(f"snake: {snake}")
                    if copies:
                        for i in range(0, len(copies)):
                            key = f'copy{i}'
                            value = copies[key]
                            print(f"{key}: {value}")

                            if copies[f"copy{i}"].top == snake.y:
                                copies[f"copy{i}"].left -= 50
                            if copies[f"copy{i}"].top > snake.y:
                                copies[f"copy{i}"].top -= 50
                            elif copies[f"copy{i}"].top < snake.y:
                                copies[f"copy{i}"].top += 50
                    if left != True:
                        input_queue.popleft()
                    print('-------')

                #elif down == True and snake.y < 850:
                elif direction == "DOWN" and snake.y < 850:
                    snake.y+=50
                    print(f"snake: {snake}")
                    if copies:
                        for i in range(0, len(copies)):
                            key = f'copy{i}'
                            value = copies[key]
                            print(f"{key}: {value}")
                            if copies[f"copy{i}"].left == snake.x:
                                copies[f"copy{i}"].top += 50
                            if copies[f"copy{i}"].left > snake.x:
                                copies[f"copy{i}"].left -= 50
                            elif copies[f"copy{i}"].left < snake.x:
                                copies[f"copy{i}"].left += 50
                    if down != True:
                        input_queue.popleft()

                    print('-------')

                #elif up == True and snake.y > 0:
                elif direction == "UP" and snake.y > 0:
                    snake.y-=50
                    print('up runs')
                    print(f"snake: {snake}")
                    if copies:
                        for i in range(0, len(copies)):
                            key = f'copy{i}'
                            value = copies[key]
                            print(f"{key}: {value}")
                            count = len(copies)
                            if copies[f"copy{i}"].left == snake.x:
                                copies[f"copy{i}"].top -= 50
                                print(f'snakes moves up #{i}')
                                if count == 0:
                                    input_queue.popleft()
                            if copies[f"copy{i}"].left > snake.x:
                                print("this runs")
                                copies[f"copy{i}"].left -= 50
                            elif copies[f"copy{i}"].left < snake.x:
                                print("this runs")
                                copies[f"copy{i}"].left += 50
                        count -= 1
                    if up == False:
                        print('this runs')
                        input_queue.popleft()

                            
                    print('-------')

=======
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
                    
>>>>>>> snake-2
                
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
