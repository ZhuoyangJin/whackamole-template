import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_pos = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_image.get_rect(topleft=mole_pos).collidepoint(event.pos):
                        mole_pos = (random.randrange(0, 640, 32),random.randrange(0, 512, 32))

            screen.fill("pink")


            def draw_():
                for x in range(0,641,32):
                    pygame.draw.line(screen, "green", (x,0), (x,512))
                for y in range(0, 513, 32):
                    pygame.draw.line(screen, "green", (0,y), (640,y))

            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            draw_()
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
