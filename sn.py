# The title of the game
title = "My Snake Game"

# Importing required modules
import pygame, sys, time, random

# Setting the difficulty of the game
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 10

# Setting the size of the game window
frame_size_x = 720
frame_size_y = 480

# Initializing pygame
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# The second number in the tuple gives the number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Setting the title of the game window
pygame.display.set_caption(title)
# Creating the game window
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors for the game (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
orange = pygame.Color(255, 165, 0)
yellow = pygame.Color(255, 255, 0)
purple = pygame.Color(148, 0, 211)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Initial position of the snake
snake_pos = [100, 50]
# Initial body of the snake
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

# Initial position of the food
food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
# Flag to check if food has spawned
apple = True

# Initial direction of the snake
direction = 'RIGHT'
# Variable to store the direction the snake should move in next
diff_direction = direction

# Initial score
score = 0

# Function to display the 'Game Over' message
def game_over():
    # Font and size for the 'Game Over' message
    my_font = pygame.font.SysFont('times new roman', 90)
    # Rendering the 'Game Over' message
    game_over_surface = my_font.render('Game Over', True, purple)
    # Getting the rectangle surrounding the 'Game Over' message
    game_over_rect = game_over_surface.get_rect()
    # Positioning the 'Game Over' message at the top center of the screen
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    # Filling the screen with black color
    game_window.fill(black)
    # Blitting the 'Game Over' message on the screen
    game_window.blit(game_over_surface, game_over_rect)
    # Displaying the score in purple color at the bottom center of the screen
    show_score(0, purple, 'times', 20)
    # Updating the game screen
    pygame.display.flip()
    # Pausing the game for 3 seconds
    time.sleep(3)
    # Quitting pygame
    pygame.quit()
    # Exiting the program
    sys.exit()
    


# Score
# Function to display the score
def show_score(choice, color, font, size):
    # Font and size for the score
    score_font = pygame.font.SysFont(font, size)
    # Rendering the score
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # Getting the rectangle surrounding the score
    score_rect = score_surface.get_rect()
    # Positioning the score at the top left or bottom center of the screen
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    # Blitting the score on the screen
    game_window.blit(score_surface, score_rect)


# Main logic
# Main game loop
while True:
    # Iterating through the events (inputs) in the game
    for event in pygame.event.get():
        # If the event is to quit the game
        if event.type == pygame.QUIT:
            # Quitting pygame
            pygame.quit()
            # Exiting the program
            sys.exit()
        # If a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            # If the key pressed is 'w' or the up arrow key
            if event.key == pygame.K_UP or event.key == ord('w'):
                # Change the direction the snake should move in next to 'UP'
                diff_direction = 'UP'
            # If the key pressed is 's' or the down arrow key
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                # Change the direction the snake should move in next to 'DOWN'
                diff_direction = 'DOWN'
            # If the key pressed is 'a' or the left arrow key
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                # Change the direction the snake should move in next to 'LEFT'
                diff_direction = 'LEFT'
            # If the key pressed is 'd' or the right arrow key
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                # Change the direction the snake should move in next to 'RIGHT'
                diff_direction = 'RIGHT'
            # If the key pressed is 'Esc'
            if event.key == pygame.K_ESCAPE:
                # Posting an event to quit the game
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantly
    if diff_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if diff_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if diff_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if diff_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    # If the snake has not eaten the food
    if snake_pos[0] != food_pos[0] or snake_pos[1] != food_pos[1]:
        snake_body.pop()
    # If the snake has eaten the food
    else:
        # Increasing the score
        score += 1
        # Setting the flag to False to respawn the food
        apple = False

    # If the food has not spawned
    if not apple:
        # Randomly spawning the food within the game window
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    # Setting the flag to True
    apple = True
    
    # Filling the game window with black color
    game_window.fill(black)
    
    # Drawing the snake on the game window
    for pos in snake_body:
        pygame.draw.rect(game_window, orange, pygame.Rect(pos[0], pos[1], 10, 10))
        
    # Drawing the food on the game window
    pygame.draw.rect(game_window, yellow, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Game Over conditions
    # If the snake touches the edges of the game window
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    
    # If the snake touches its own body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    # Displaying the score at
            

    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
     # Frame per second controller
    fps_controller.tick(difficulty)