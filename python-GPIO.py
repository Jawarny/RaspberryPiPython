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

def augmenterLaLuminosite(led, valeur, utiliserValeur):
    if valeurMax(led):
        print("valeur plus petite que 1")
        if utiliserValeur:
            print("incremente")
            print("la valeur est :" + str(led.value))
            if led.value == 0.06:
                print("essai")
                led.value = 0.07
            if led.value == 0.57:
                print("essai")
                led.value = 0.581
            else:
                led.value += valeur
        else:
            print("met 1")
            led.value = valeur

def diminuerLaLuminosite(led, valeur, utiliserValeur):
    if valeurMin(led):
        print("valeur plus grande que 0")
        if utiliserValeur:
            print("decremente")
            led.value -= valeur
        else:
            print("met 1")
            led.value = valeur

def valeurMin(led):
    return (led.value > 0)

def valeurMax(led):
    return (led.value < 1)






while True:
    #input("1) Augmenter\n2) Allumer")
    if bouttonJaune.is_pressed:
        if ledJaune.value <= 0.99999 and ledRouge.value >= 0.99999 and ledVert.value >= 0.99999:
            augmenterLaLuminosite(ledJaune, 1, False)
            augmenterLaLuminosite(ledRouge, 1, False)
            augmenterLaLuminosite(ledVert, 1, False)  
            sleep(0.2) 
            print(str(ledJaune.value) + "\n" + str(ledRouge.value )+ "\n" + str(ledVert.value)) 
            print("valeur pas 1")    
        
            
       
    
    if bouttonRouge.is_pressed:
        diminuerLaLuminosite(ledJaune, 0.01, True)
        diminuerLaLuminosite(ledRouge, 0.01, True)
        diminuerLaLuminosite(ledVert, 0.01, True)
        sleep(0.2)
        print(str(ledJaune.value) + "\n" + str(ledRouge.value )+ "\n" + str(ledVert.value)) 
        
    if bouttonVert.is_pressed:
        augmenterLaLuminosite(ledJaune, 0.01, True)
        augmenterLaLuminosite(ledRouge, 0.01, True)
        augmenterLaLuminosite(ledVert, 0.01, True)
        sleep(0.2)
        print(str(ledJaune.value) + "\n" + str(ledRouge.value )+ "\n" + str(ledVert.value)) 
        
