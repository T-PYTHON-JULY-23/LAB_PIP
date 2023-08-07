from art import *
from colorama import Fore

tprint("BELIEVE \nAND \nACHEIVE", font='block')
tprint("HELLO", font='sub-zero')


txt = text2art("WELCON",font="random")
print(Fore.RED + txt)


txt1 = text2art("PLAY THE GAME",font="kgames_i")
print(Fore.BLUE + txt1)


txt2 = decor("barcode")
print(Fore.YELLOW + txt2)

