from pygame import display, FULLSCREEN, font

MAP = {'Camp': True, 'svetovna': False, 'kovane': False, 'Pig Cave': False, 'Pig Cave.pestera': False, 'Market place': False, 'Westvield City': False}

SRIFT = 'data/srift/seguisym.ttf'

#DYLZINA = 1080
#VISOCINA = 720

# font.init()
FONT15 = font.Font(SRIFT, 15)
FONT18 = font.Font(SRIFT, 18)
FONT20 = font.Font(SRIFT, 20)
FONT22 = font.Font(SRIFT, 22)
FONT25 = font.Font(SRIFT, 25)
FONT28 = font.Font(SRIFT, 28)
FONT35 = font.Font(SRIFT, 35)
FONT40 = font.Font(SRIFT, 40)

poslednaZona = [{}, []]
nastojastaZona = ['Camp']

dvizenie = [0, 0]
EKRAN = display.set_mode((1080, 720))
display.set_caption("STICK-MAN Adventure")
# display.set_icon(image.load("icon.png"))
FPS = 240
