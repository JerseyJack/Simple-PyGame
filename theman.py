import pygame 

#Setting up the window
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("The Man")


walk_right = [pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansright1.png'), pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansright2.png'), pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansright3.png'), pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansright4.png')]
walk_left = [pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansleft1.png'), pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansleft2.png'), pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansleft3.png'), pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansleft4.png')]
idle = pygame.image.load('C:/Users/jerse/OneDrive/Documents/Coding/Python/Block Game/Sprites/sansidle.png')


fps = pygame.time.Clock()

#Setting up the player variable
screen_width = 600
x = 250
y = 500
width = 59
height = 75
v = 15
game_run = True
jumping = False
jump_count = 7
left = False
right = False
walk_count = 0

def game_window_draw():
    global walk_count

    #Window background fill
    window.fill((50, 50, 50))

    #Refreshing the window
    if walk_count + 1 >= 27:
        walk_count = 0

    if left:
        window.blit(walk_left[walk_count//3], (x, y))
        walk_count += 1
    elif right:
        window.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1
    else:
        window.blit(idle, (x, y))

    pygame.display.update()

#Main loop
while game_run:
    fps.tick(27)

    for event in pygame.event.get():

        #Exit program on quit
        if event.type == pygame.QUIT:
            game_run = False

    #Character movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= v
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 570:
        x += v
        right = True
        left = False
    else:
        right = False
        left = False
        walk_count = 0
    
    #Jumping
    if not (jumping):
        if keys[pygame.K_SPACE]:
            jumping = True
            right = False
            left = False
            walk_count = 0

    else:
        if jump_count >= -7:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else: 
            jumping = False
            jump_count = 7

    #Draw things
    game_window_draw()


        

pygame.quit()