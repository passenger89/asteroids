import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""
    Screen width: {SCREEN_WIDTH} 
    Screen height: {SCREEN_HEIGHT}
    """)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    font = pygame.font.SysFont("monospace", 35)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    player_score = 0
    print(f"score: {player_score}")
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if (asteroid.collides_with(shot) == True):
                    log_event("asteroid_shot")
                    player_score += 1
                    print(f"score: {player_score}")
                    shot.kill()
                    asteroid.split()
            if (asteroid.collides_with(player) == True):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        
        for each in drawable:
            each.draw(screen)
        
        # Render the text into an 'image'
        # The arguments are: (string, anti-aliasing, color)
        score_surface = font.render(f"Score: {player_score}", True, (255, 255, 255))

        # Draw (blit) it to the screen at coordinates (x, y)
        screen.blit(score_surface, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
