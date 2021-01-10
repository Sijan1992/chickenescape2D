import pygame
import random
import time
screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('back.png')
user = pygame.image.load('user.png')
chicken = pygame.image.load('chicken.png')
pygame.font.init()
score = 0
start = int(time.time())
print(start)

def display_score():
    global score
    font = pygame.font.SysFont('Comic Sans MS',30)
    score_text = 'Score:'+ str(score)
    text_image = font.render(score_text,True,(0,255,0))
    screen.blit(text_image,[0,0])


def random_ness():
  return -1 *random.randint(100,1200)

chicken_y = [random_ness(),random_ness(),random_ness()]

user_x = 150
user_y = 495


def crashed(idx):
    global score
    score = score -50
    print('Crashed with chicken',idx,score)
    chicken_y[idx]= random_ness()

def update_chicken(idx):
    global score
    if chicken_y[idx] >600:

        chicken_y[idx] = random_ness()
        score = score +5
        print('Score',score)
    else:
        chicken_y[idx]= chicken_y[idx]+5


clock = pygame.time.Clock()
def timing():
    global score
    if score < 15:
        clock.tick(50)
    if 16<score<30:
        clock.tick(51)
    if 31<score<50:
        clock.tick(52)
    
   

keep_alive = True

def game_loop():
    global user_x
    global user_y
    
    while keep_alive:
        

        
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and user_x < 320:
            user_x = user_x +10
        elif keys[pygame.K_LEFT]and user_x >-40:
            user_x = user_x -10
        elif keys[pygame.K_UP]and user_y > 20:
            user_y = user_y -10
        elif keys[pygame.K_DOWN]and user_y <520 :
            user_y = user_y +10


        update_chicken(0)
        update_chicken(1)
        update_chicken(2)
        screen.blit(background,[0,0])
        screen.blit(user,[user_x,user_y])
        screen.blit(chicken,[0,chicken_y[0]])
        screen.blit(chicken,[150,chicken_y[1]])
        screen.blit(chicken,[280,chicken_y[2]])

        if (chicken_y[0]-user_y) >= 10 and (chicken_y[0]-user_y) <=40 and user_x<70:
            crashed(0)
        if (chicken_y[1]-user_y) >= 10 and (chicken_y[1]-user_y) <=40 and user_x>80 and user_x<200:
            crashed(1)

        if (chicken_y[2]-user_y) >= 10 and (chicken_y[2]-user_y) <=40 and user_x >220:
            crashed(2)
        display_score()
        pygame.display.update()
        clock.tick(50)
        elapsed_time = (int(time.time())- start)
        if elapsed_time >=120:
            break
game_loop()
    
        