import pygame
import random

pygame.init()

# colours
white= (255, 255,255)
red= (255, 0,0)
black= (0, 0,0)


# Creating window
screen_width= 200
screen_height= 40
gamewindow=pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Hunny's Snake")
pygame.display.update()

# Game Variables
exit_game = False
game_over = False
snake_x= 5
snake_y= 5
velocity_x= 0
velocity_y= 0

food_x = random.randint(5, screen_width/2)
food_y = random.randint(5, screen_height/2)
score=0

init_velocity = 3
snake_size= 20
fps=20

clock = pygame.time.Clock()


# Game loop
while not exit_game:
  for event in pygame.event.get():
       if event.type == pygame.QUIT:
            exit_game = True
      
       if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
           velocity_x = init_velociy
           velocity_y = 0
           
         if event.key == pygame.K_LEFT:
           velocity_x = - init_velocity
           velocity_y = 0
           
         if event.key == pygame.K_UP:
           velocity_x = 0
           velocity_y = - init_velocity
           
         if event.key == pygame.K_DOWN:
           velocity_x = 0
           velocity_y = init_velocity
         
  snake_x = snake_x + velocity_x
  snake_y = snake_y + velocity_y
  
  if abs(snake_x-food_x)<2 and abs(snake_y-food_y)<2:
    score +=1
    print("score: ", score * 10)
    food_x = random.randint(5, screen_width/2)
    food_y = random.randint(5, screen_height/2)
  
gamewindow.fill(white)
pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
pygame.display.update()
clock.tick(fps)
  
pygame.quit()
quit()
