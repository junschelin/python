import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

image = pygame.image.load('./chap12/ship.bmp')

image_rect = image.get_rect()

image_rect.midbottom = screen.get_rect().midbottom

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            image_rect.left -= 20
        if event.key == pygame.K_RIGHT:
            image_rect.left += 20
        if event.key == pygame.K_SPACE:
            bullets.append(create_bullet(image_rect))
    

    # Do logical updates here.
    # 비행기를 왼쪽 오른쪽으로 움직이는 이벤트 구현
    for bullet in bullets:
        bullet.top -= 10
    
    # screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    screen.blit(image, image_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)