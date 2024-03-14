from gpiozero import LED
from time import sleep
from tkinter import *

principal = Tk()
principal.title("interface- GPIO")
principal.geometry("300x100")

def bouton_rouge_clicked():
    if rougeLED.is_lit:
        rougeLED.off()
        lbl_LED = Label(principal, text="Éteint", fg="red")
        lbl_LED.grid(row=0, column=1)
    else:
        rougeLED.on()
        lbl_LED = Label(principal, text="Allumé", fg="green")
        lbl_LED.grid(row=1, column=1)
        
boutton_rouge.grid(row=0, column=0)

boutton_rouge = Button(principal, text = "GPIO 19", bg = "red", command = "boutton_rouge_clicked")