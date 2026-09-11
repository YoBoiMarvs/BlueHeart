import math
import random
import pygame
WIDTH, HEIGHT = 1600, 900
FPS = 60
SCALE = 18
BACKGROUND_COLOR = (3, 5, 12)
WORDS = [ "love you", "Love You", "LOVE YOU" ]
CENTER_TEXT = "Love You"
COLORS = [ (80, 150, 255), (40, 180, 255), (100, 190, 255), (90, 120, 255), (150, 170, 255)
          def heart_xy(t):
              x = 16 * math.sin(t) ** 3
              y = ( 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t) )
              return x, -y
              def to_screen(x, y):
                  return ( x * SCALE + WIDTH / 2, y * SCALE + HEIGHT / 2 )
                  class Particle:
                      __slots__ = ( "x", "y", "order", "kind", "word", "color", "alpha", "flicker", "font", "delay", "size_mult", "phase" )
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
                          self.size_mult = random.uniform(0.85, 1.15)
                          self.phase = random.uniform(0, math.pi * 2)
def build_outline_particles(amount, min_gap=28):
    particles = []
    placed = []
    for i in range(amount):
        t = (i / amount) * math.tau
        bx, by = heart_xy(t)
        sx, sy = to_screen(bx, by)
        if any( math.hypot(sx - px, sy - py) < min_gap for px, py in placed ):
            placed.append((sx, sy))
            particles.append( Particle( sx, sy, i, "outline" ) )
            def build_fill_particles(amount, min_gap=42):
                particles = []
                placed = []
                attempts = 0
        max_attempts = amount * 100
        while len(particles) < amount and attempts < max_attempts:
            attempts += 1
            t = random.uniform(0, math.tau)
            r = math.sqrt(random.uniform(0.05, 0.82))
            bx, by = heart_xy(t)
            px = bx * r
            py = by * r
            sx, sy = to_screen(px, py)
            if any( math.hypot(sx - qx, sy - qy) < min_gap for qx, qy in placed ):
            placed.append((sx, sy))
            particles.append( Particle( sx, sy, random.randint(0, 500), "fill" ) )
            def draw_glow_text(glow_layer, text_layer, font, word, color, x, y, alpha, size_mult=1.0 )
            screen.blit( glow_layer, (0, 0) )
            screen.blit( text_layer, (0, 0) )
            center_start = fill_start + 180
            if frame > center_start:
                progress = min( 1.0, (frame - center_start) / 70 )
                center_alpha = int( 255 * (1 - math.exp(-progress * 7)) )
                pulse = ( 1.0 + 0.035 * math.sin(frame * 0.045) )
                center_text = font_center.render( CENTER_TEXT, True, (245, 248, 255) )
                new_width = max( 1, int( center_text.get_width() * pulse ) )
                new_height = max( 1, int( center_text.get_height() * pulse ) )
                center_text = pygame.transform.smoothscale( center_text, ( new_width, new_height ) )
                center_text.set_alpha( center_alpha )
        center_pos = ( WIDTH // 2, HEIGHT // 2 )
        if center_alpha > 10:
            glow_center = pygame.transform.smoothscale( center_text, ( int( center_text.get_width() * 1.7 ),int( center_text.get_height() * 1.7 ) ) )
            glow_center.set_alpha( int(center_alpha * 0.12) )
            low_rect = glow_center.get_rect( center=center_pos )
            screen.blit( glow_center, glow_rect )
            text_rect = center_text.get_rect( center=center_pos )
            screen.blit( center_text, text_rect )
            pygame.display.flip()
            clock.tick(FPS)
            pygame.quit()
            if __name__ == "__main__":try: main()
                import traceback traceback.print_exc()
            

