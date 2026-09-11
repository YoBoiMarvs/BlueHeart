import math
import random
import pygame
WIDTH, HEIGHT = 2000, 1200
FPS = 60
SCALE = 20
WORDS = ["love you", "Love You", "LOVE YOU"]
CENTER_TEXT = " Love You "
COLORS = [(70, 130, 180),  (30, 144, 255),(0, 191, 255), (100, 149, 237),(65, 105, 225)]
class Particle:
     def __init__(self, x, y, order, kind):
 self.x = x
    self.y = y
 self.order = order
    self.kind = kind
self.word = random.choice(WORDS)
 self.color = random.choice(COLORS)
self.alpha = 0
self.flicker = random.uniform(0, math.pi * 2)
self.font = None
   self.delay = 0
self.size = random.uniform(0.85, 1.15)
def heart_xy(t):
     x = 16 * math.sin(t) ** 3
     y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        return x, -y
def to_screen(x, y):
     return x * SCALE + WIDTH / 2, y * SCALE + HEIGHT / 2
def create_particles():
        particles = []
      for i in range(300):
 t = random.uniform(0, math.pi * 2)
    r = random.uniform(0.15, 1.0)
x, y = heart_xy(t)
        x *= r
           y *= r
       sx, sy = to_screen(x, y)
        particles.append(Particle(sx, sy, i, "heart"))
  return particles
def draw_text(layer, particle, font):
     text = font.render(particle.word,True,particle.color)
    text.set_alpha(particle.alpha)
 rect = text.get_rect(center=(particle.x, particle.y))
layer.blit(text, rect)
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Love You <3")
clock = pygame.time.Clock()
 font = pygame.font.SysFont("arial",18,bold=True)
 center_font = pygame.font.SysFont("georgia",55,bold=True)
particles = create_particles()
running = True
    frame = 0
   while running:
     for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
                 if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_ESCAPE:
                          running = False
                          screen.fill((0, 0, 0))
                          frame += 1
                           layer = pygame.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)
         for p in particles:
 if frame > p.delay:
         p.alpha = min(255,p.alpha + 12)
if p.alpha > 0:
    draw_text(layer,p, font)
    screen.blit(layer, (0, 0))
if frame > 350:
       center = center_font.render(CENTER_TEXT,True,(255, 250, 245))
               center.set_alpha(255)
 rect = center.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(center, rect)
   pygame.display.flip()
   clock.tick(FPS)
  pygame.quit()
if __name__ == "__main__":
   main()
