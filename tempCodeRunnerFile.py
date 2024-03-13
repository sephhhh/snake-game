    if snake_draw.colliderect(apple):
                point.update(randomWidth(snake), randomHeight(snake), 50, 50)
                if right == True:
                    createCopy(copy_counter, snake)
                    copies[f"copy{len(copies) - 1}"].left -= 200
                    pygame.draw.rect(screen, "red", copies[f"copy{len(copies) - 1}"])
                copy_counter+=1