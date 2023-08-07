
from art import *
from colorama import *
  
print(text2art("BELIEVE AND ACHEIVE","black"))
print(text2art("HELLO","sub-zero"))
print(text2art("Python","starwars"))
print(text2art("Hassan","drpepper"))

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')