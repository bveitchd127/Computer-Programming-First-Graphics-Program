import pygame

pygame.init()

screen = pygame.display.set_mode( (1280,720) )
clock = pygame.time.Clock()
running = True

playerx = 640
playery = 360

# 300 px / s
playerSpeed = 5
playerImage = pygame.image.load("pacman.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (64,64))

while running:
    dt = clock.tick(60) # waits for 17ms

    # for i in range(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     # if event.key == pygame.K_UP:
        #     #     playery = playery - 20
        #     # if event.key == pygame.K_DOWN:
        #     #     playery = playery + 20
            
        #     if event.key == pygame.K_LEFT:
        #         playerx = playerx - 20
        #     if event.key == pygame.K_RIGHT:
        #         playerx = playerx + 20

    # Computation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playery = playery - playerSpeed
    
    if keys[pygame.K_DOWN]:
        playery = playery + playerSpeed
    
    if keys[pygame.K_LEFT]:
        playerx = playerx - playerSpeed
    
    if keys[pygame.K_RIGHT]:
        playerx = playerx + playerSpeed
                
    
    # Render
    screen.fill("purple")
    #pygame.draw.circle(screen, "red", (playerx, playery), 50)
    screen.blit(playerImage, (playerx, playery))
    pygame.display.update()

pygame.quit()