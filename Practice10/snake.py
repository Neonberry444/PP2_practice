import pygame
import random
import time, sys

# Initializing Pygame
pygame.init()

# Colors
WHITE  = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK  = (0, 0, 0)
RED    = (213, 50, 80)
GREEN  = (0, 255, 0)
BLUE   = (50, 153, 213)

# Display Dimensions
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20 

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
score_font = pygame.font.SysFont("verdana", 20)

def display_ui(score, level, speed):
    """Displays Score, Level, and Speed in the top left."""
    # Showing the counter for score and level as requested
    value = score_font.render(f"Score: {score} | Level: {level} | Speed: {speed}", True, WHITE)
    dis.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    """Draws the snake segments."""
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], block_size, block_size])

def get_random_food_pos(snake_list):
    """Generates food position ensuring it's not on the snake body."""
    while True:
        foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
        foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
        if [foodx, foody] not in snake_list:
            return foodx, foody

def gameLoop():
    game_over = False
    
    # Snake starting position
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Leveling and Speed settings
    score = 0
    level = 1
    # SLOWER START: Reduced from 10 to 5 for a more relaxed beginning
    current_speed = 5 
    food_to_next_level = 3 

    foodx, foody = get_random_food_pos(snake_List)

    while not game_over:

        for event in pygame.event.get():
            # Standard Quit functionality
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Border/Wall Collision detection
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over = True # Exit the loop to quit

        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        
        # Drawing Food
        pygame.draw.rect(dis, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        # Snake Body Logic
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Self-collision detection
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        draw_snake(BLOCK_SIZE, snake_List)
        display_ui(score, level, current_speed)

        pygame.display.update()

        # Food Collection logic
        if x1 == foodx and y1 == foody:
            foodx, foody = get_random_food_pos(snake_List)
            Length_of_snake += 1
            score += 1
            
            # Leveling up logic: Increase speed every 3 foods
            if score % food_to_next_level == 0:
                level += 1
                current_speed += 2 # Incremental speed increase

        clock.tick(current_speed)

    # Automatically close window on game over
    pygame.quit()
    quit()

gameLoop()