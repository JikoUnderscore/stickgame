from math import atan2, pi
from pygame import draw
from ENGINE import Predmet, Obekt, ObektDrug

class CircularArc:
    __slots__ = ('color', 'x', 'y', 'rect', 'radius', 'start_angle', 'stop_angle', 'width')

    def __init__(self, color, center, radius, start_angle, stop_angle, width=1):
        self.color = color
        self.x = center[0]  # center x position
        self.y = center[1]  # center y position
        self.rect = [self.x - radius, self.y - radius, radius * 2, radius * 2]
        self.radius = radius
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = width

    def draw(self, canvas):
        draw.arc(canvas, self.color, self.rect, self.start_angle, self.stop_angle, self.width)

    def contains(self, x, y):

        dx = x - self.x  # x distance
        dy = y - self.y  # y distance

        greater_than_outside_radius = dx * dx + dy * dy >= self.radius * self.radius

        less_than_inside_radius = dx * dx + dy * dy <= (self.radius - self.width) * (self.radius - self.width)

        # Quickly check if the distance is within the right range
        if greater_than_outside_radius or less_than_inside_radius:
            return False

        rads = atan2(-dy, dx)  # Grab the angle

        # convert the angle to match up with pygame format. Negative angles don't work with pygame.draw.arc
        if rads < 0:
            rads = 2 * pi + rads

        # Check if the angle is within the arc start and stop angles
        return self.start_angle <= rads <= self.stop_angle


def obekt_syzdatel():
    #import pympler.asizeof as razmer
    karta1PesteraVhod = Predmet('data/karta1/pestera.png', 910, 0, syobstenie='Press E to ENTER the cave',)

    lyc = CircularArc((0, 0, 0), [650, 500], 500, 0, 3.14159265 / 2, 100)

    vrag1 = Obekt('data/mobs/vrag1/vrag1.png', 800, 500)
    vrag1.HP, vrag1.HPnstojast = 200, 200;  vrag1.ime = 'The Red Pigg'
    vrag1.djasnaAtakaMAX = 8;               vrag1.djasnaAtaka = 11

    vragelit = Obekt('data/mobs/vrag1/vrag1Elit.png', 300, 100)
    vragelit.HP, vragelit.HPnstojast = 200, 200; vragelit.ime = 'ELIT PIGG'
    vragelit.djasnaAtakaMAX = 8;                 vragelit.djasnaAtaka = 11
    vragelit.ljavaAtakaMAX = 5;                  vragelit.ljavaAtaka = 19

    vragoficer = Obekt('data/mobs/vrag1/vrag1Oficer.png', 800, 100)
    vragoficer.HP, vragoficer.HPnstojast = 300, 300; vragoficer.ime = 'OFFICER PIGG'
    vragoficer.djasnaAtakaMAX = 5;                   vragoficer.djasnaAtaka = 5
    vragoficer.ljavaAtakaMAX = 6;                    vragoficer.ljavaAtaka = 6
    vragoficer.raznoCDMAX = 10;                      vragoficer.specialno = 15

    vragboss = Obekt('data/mobs/vrag1/vrag1Boss.png', 500, 500)
    vragboss.HP, vragboss.HPnstojast = 500, 500;    vragboss.ime = 'PIGG BOSS'
    vragboss.djasnaAtakaMAX = 10;                   vragboss.djasnaAtaka = 25
    vragboss.ljavaAtakaMAX = 3;                     vragboss.ljavaAtaka = 9
    vragboss.raznoCDMAX = 15;                       vragboss.specialno = 10

    prijatel1 = ObektDrug('data/mobs/NPC0/prijatel1.png', 500, 50, 'data/karta1/nepopVID1.json')

    kamyk = Predmet('data/karta1/kamynak.png', 300, 350, (50, 100), (20, 50))
    #print(razmer.asizesof(karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss))

    return karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss


