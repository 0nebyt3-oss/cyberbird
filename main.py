
import pygame
import asyncio
from pygame.locals import *

async def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    clock = pygame.time.Clock()
    running = True
    y = 300
    vel = 0
    gravity = 0.5

    bird = pygame.Surface((40, 30))
    bird.fill((200, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    vel = -10

        vel += gravity
        y += vel
        if y > 570:
            y = 570
            vel = 0

        screen.fill((0, 0, 0))
        screen.blit(bird, (180, y))
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())
