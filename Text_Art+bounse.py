
# import module
from art import *
from colorama import Fore, Back, Style

phrase1=text2art("BELIEVE AND ACHEIVE",font='block',chr_ignore=True) 
print(phrase1)

phrase1=text2art

phrase2=text2art("Hello",font='sub-zero',chr_ignore=True)
print(phrase2)

#Bonus#

phrase3=text2art("I am Lenah",font='random',chr_ignore=True)
print(phrase3)

print(Fore.RED + "Hello")
print(Back.WHITE + "Python camp")
print(Style.DIM + "Lenah")