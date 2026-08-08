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
    loading(0.01)
    cls()
    print(RPG)


def loading(delay=0.1):
    por = 0
    for _ in range(10):
        for _ in range(10):
            barra = por // 10
            print(f"Loading[{'▉'*barra:<10}]{por}%", end="\r")
            por += 1
            time.sleep(delay)
    print(f"Loading[{'▉'*10}]100%")