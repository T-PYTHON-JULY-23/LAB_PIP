#labPip
from art import *
from colorama import Fore

textArt1 = text2art("BELIEVE AND ACHIEVE", font='block')
print(textArt1)

textArt2 = text2art("HELLO", font='sub-zero')
print(textArt2)


#bonus
textArt3 =Fore.BLUE + text2art("LIVE YOUR LIVE", font="cybermedum")
print(textArt3)
textArt4 =Fore.GREEN + text2art("YOU CAN DO IT", font="rnd-xlarge")
print(textArt4)
textArt5 =Fore.YELLOW + text2art("CODING MOOD ON", font="rnd-medium")
print(textArt5)