def movesRight(snake):
    snake.x+=50
    if copies:
        for i in range(0, len(copies)):
            if copies[f"copy{i}"].top == snake.y:
                copies[f"copy{i}"].left += 50
            if copies[f"copy{i}"].top > snake.y:
                copies[f"copy{i}"].top -= 50
            elif copies[f"copy{i}"].top < snake.y:
                copies[f"copy{i}"].top += 50    