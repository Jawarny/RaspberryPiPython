from gpiozero import LEDBoard, LED, PWMLED, Button, RGBLED, Buzzer, TonalBuzzer
from gpiozero.tones import Tone

from colorzero import color

from time import sleep
from signal import pause

#ledRGB = RGBLED(red = GIPO#, green = GIPO#, blue = GIPO#, active_high=True #ground)

bouttonJaune = Button(23)
bouttonRouge = Button(24)
bouttonVert = Button(25)

ledJaune = PWMLED(13)
ledRouge = PWMLED(19)
ledVert = PWMLED(26)

def augmenterLaLuminosite(led):
    if (led.value <= 0.9):
        led.value += 0.1
    else:
        led.value = 1

def diminuerLaLuminosite(led):
    if (led.value >= 0.1):
        led.value -= 0.1
    else:
        led.value = 0




while True:
    if bouttonJaune.is_pressed:
        augmenterLaLuminosite(ledJaune)
        sleep(0.2)
    
    if bouttonRouge.is_pressed:
        diminuerLaLuminosite(ledJaune)
        sleep(0.2)
        
    if bouttonVert.is_pressed:
        print("boutton vert est pressed")
        sleep(0.2)
        
