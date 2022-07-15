import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World") #similar to title in head in html
WHITE = (255, 255, 255)

FPS = 60

characterimage = pygame.image.load(
    os.path.join('assets', 'scrnunkly.png'))
character = pygame.transform.scale(characterimage, (200, 150))



def draw_window():
    WIN.fill(WHITE)
    WIN.blit(character, (300, 100))
    pygame.display.update()

def main():
    #everything bscly
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #checks the events that may happen
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
