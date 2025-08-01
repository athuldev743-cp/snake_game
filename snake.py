import pygame
import time
import random

pygame.init()

# Window size
window_x = 750
window_y = 450

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Set up display
pygame.display.set_caption("Snake Game - Graphical Version")
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Load images
snake_head_img = pygame.image.load('snake.jpg').convert_alpha()
snake_body_img = pygame.image.load('snake_body.png').convert_alpha()
fruit_img = pygame.image.load('apple.jpeg').convert_alpha()
background_img = pygame.image.load('snbg.jpg')  # Optional

# Resize images
snake_head_img = pygame.transform.scale(snake_head_img, (10, 10))
snake_body_img = pygame.transform.scale(snake_body_img, (10, 10))
fruit_img = pygame.transform.scale(fruit_img, (10, 10))
background_img = pygame.transform.scale(background_img, (window_x, window_y))

# Snake & fruit
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction
score = 0

# Score display
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.topleft = (10, 10)
    else:
        score_rect.center = (window_x / 2, window_y / 1.25)
    game_window.blit(score_surface, score_rect)

# Game over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Update snake body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    # Draw background
    game_window.blit(background_img, (0, 0))

    # Draw snake
    for i, pos in enumerate(snake_body):
        if i == 0:
            game_window.blit(snake_head_img, pygame.Rect(pos[0], pos[1], 10, 10))
        else:
            game_window.blit(snake_body_img, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw fruit
    game_window.blit(fruit_img, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(15)





    



