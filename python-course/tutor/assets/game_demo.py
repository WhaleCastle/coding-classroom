"""
Minimal pygame demo: move the comic hero around with the arrow keys.

Run:
    pip install pygame
    python game_demo.py

Expects 'hero_sprite.png' in the same folder.
"""

import pygame

pygame.init()
SCREEN_W, SCREEN_H = 800, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Comic Hero Demo")
clock = pygame.time.Clock()

# Load the transparent PNG sprite (convert_alpha keeps the transparency).
hero = pygame.image.load("hero_sprite.png").convert_alpha()
# Scale to a sensible in-game size (original is 512x640).
hero = pygame.transform.smoothscale(hero, (160, 200))
hero_rect = hero.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2))

SPEED = 5
facing_left = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * SPEED
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * SPEED
    hero_rect.x += dx
    hero_rect.y += dy
    hero_rect.clamp_ip(screen.get_rect())

    # Flip the sprite to face the movement direction.
    if dx < 0:
        facing_left = True
    elif dx > 0:
        facing_left = False
    frame = pygame.transform.flip(hero, True, False) if facing_left else hero

    screen.fill((124, 180, 120))            # grassy background
    screen.blit(frame, hero_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()