import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooters")

#BACKGROUND

BG = pygame.transform.scale2x(pygame.image.load("/Users/chumpawhumps/Desktop/coding practice/Python/PygameExample-SpaceShooters/image for game/StarFoxBackgroundForGame.jpg"))
    
PLAYER_HEIGHT = 60
PLAYER_WIDTH = 40
PLAYER_VELOCITY = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 3

PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("/Users/chumpawhumps/Desktop/coding practice/Python/PygameExample-SpaceShooters/image for game/space_ship.jpg"))
player_width, player_height = PLAYER_IMAGE.get_size()

player_x = (WIDTH - player_width)//2
player_y = (HEIGHT - player_height)//2

player = pygame.Rect(player.x, player.y, PLAYER_WIDTH, PLAYER_HEIGHT)

FONT = pygame.font.SysFont("Times New Roman", 20)

def draw(player, elapsed_time, stars):
    WIN.blit(BG,(0,0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s",1,"white")

    WIN.blit(time_text, (10, 10))

    WIN.blit(PLAYER_IMAGE, (player.x, player.y))

   # pygame.draw.rect(WIN, "green", player)

    for star in stars:
        pygame.draw.rect(WIN, "yellow", star)
        
    pygame.display.update() #applies the draws on the screen



#WHILE LOOP FOR MENU
def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)


    #clock object determines the speed to be the same no matter what computer it runs on

    clock = pygame.time.Clock()


    startTime = time.time() #gives the current time when game started
    elapsed_time = 0

    #stars-lil projectiles-started here
    star_add_increment = 2000

    star_count = 0 #when we should add next star

    #array
    stars = []
    hit = False
    
    
    while run:
        star_count += clock.tick(60) #this shapes the fps/frames per second/runs 60 times per second
        elapsed_time = time.time() - startTime#this would give the numnber of seconds since we started the game or the while loop

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
    #movement code
        keys = pygame.key.get_pressed()
        if  keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if  keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY  + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        if keys[pygame.K_UP]:
            if player.y + - PLAYER_VELOCITY >= 0:
                player.y -= PLAYER_VELOCITY
        if  keys[pygame.K_DOWN]:
            if player.y + PLAYER_VELOCITY + player.height <= HEIGHT:
                player.y += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("You got hit! YOU LOSE!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
            
        draw(player, elapsed_time, stars)
    pygame.quit()

if __name__ == "__main__":
    main() 
