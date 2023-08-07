from art import *
from colorama import Fore
art_text1 = text2art ("BELIEVE AND ACHEIVE", font = "block")
print(art_text1)
art_text2 = text2art ("HELLO" , font ="sub-zero")
print(art_text2)
art_text3 = text2art ("FOFO" , font = "random")
print(art_text3+Fore.BLUE)
