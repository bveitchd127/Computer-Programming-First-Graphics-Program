import pygame

pygame.init()

screen = pygame.display.set_mode( (1280,720) )
clock = pygame.time.Clock()
running = True

playerx = 640
playery = 360

while running:
    dt = clock.tick(60) # waits for 17ms

    # for i in range(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playery = playery - 20
            if event.key == pygame.K_DOWN:
                playery = playery + 20

    screen.fill("purple")

    pygame.draw.circle(screen, "red", (playerx, playery), 50)

    pygame.display.update()

pygame.quit()