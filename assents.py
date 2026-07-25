import time
import os

RPG = """
        ██████╗ ██████╗  ██████╗
        ██╔══██╗██╔══██╗██╔════╝
        ██████╔╝██████╔╝██║  ███╗
        ██╔══██╗██╔═══╝ ██║   ██║
        ██║  ██║██║     ╚██████╔╝
        ╚═╝  ╚═╝╚═╝      ╚═════╝
"""

def cls():
    os.system("cls")

def trocar_tela():
    cls()
    print(RPG)

def iniciando():
    print("iniciando", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)