from art import *
import colorama
from colorama import Fore, Style

# Print the phrase "BELIEVE AND ACHIEVE" with the "block" font
block_art = text2art("BELIEVE\nAND\nACHIEVE", font="block")
print(block_art)

my_name=text2art("Basma", font="random")
print(my_name)

# Print the phrase "HELLO" with the "sub-zero" font in red color
sub_zero_art = text2art("HELLO", font="sub-zero")
print(colorama.Fore.RED + sub_zero_art)
