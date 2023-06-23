from colorama import Style, Fore, Back
import numpy
import os
import msvcrt
import random

#Diseño

def pr(texto: str):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def pv(texto: str):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def pa(texto: str):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def lp():
    pa("<<Press any key to continue>>")
    msvcrt.getch()
    os.system('cls')

#Operaciones

def vc(cod):
    pass

def guardar(cod,ti,au,pre):
    pass

def bu(cod):
    pass

def c_criticas(cod):
    pass

def c_detalles(cod):
    pass
