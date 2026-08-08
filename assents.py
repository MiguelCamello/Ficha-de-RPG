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
EDICAO = """
========================================
|           EDIÇÃO DA FICHA            |
========================================
|                                      |
|   O que deseja editar?               |
|                                      |
|   [1] Nível       [5] Agilidade      |
|   [2] Mana        [6] Vitalidade     |
|   [3] Força       [7] Resistência    |
|   [4] Itens       [8] Inteligência   |
|                                      |
|   [0] Continuar                      |
|                                      |
========================================
"""
MENU = """
========================================
|            MENU PRINCIPAL            |
========================================
|                                      |
|  O que deseja fazer?                 |
|                                      |
|  [1] Criar ficha de RPG              |
|  [2] Consultar ficha                 |
|  [3] Listar todas as fichas          |
|  [4] Excluir ficha                   |
|  [5] Editar ficha                    |
|                                      |
|  [0] Fecha programa                  |
|                                      |
========================================
"""
RANDOM = """
========================================
|       Deseja editar ficha ou         |
|       randomizar os status?          |
========================================
|                                      |
|   [1] Editar Status                  |
|   [2] Randomizar status              |
|                                      |
|   [0] Ficha em branco                |
|                                      |
========================================
"""
SALVAR = """
========================================
|           DESEJA SALVAR?             |
========================================
|                                      |
|   [S] Salvar ficha                   |
|   [N] Não salvar                     |
|                                      |
|   [0] Fechar programa                |
|                                      |
========================================
"""
EXCLUIR = """
========================================
|       DESEJA EXCLUIR FICHA?          |
========================================
|                                      |
|   [S] Excluir ficha                  |
|   [N] Não excluir                    |
|                                      |
|   [0] Fechar programa                |
|                                      |
========================================
"""
ATUALIZAR = """
========================================
|       DESEJA ATUALIZAR FICHA?        |
========================================
|                                      |
|   [S] Atualizar ficha                |
|   [N] Não atualizar                  |
|                                      |
|   [0] Fechar programa                |
|                                      |
========================================
"""

def cls():
    os.system("cls")

def trocar_tela(load=True):
    if load:
        loading(0.01)
    cls()
    print(RPG)

def loading(delay=0.1):
    por = 0
    for _ in range(10):
        for _ in range(10):
            barra = por // 10
            print(f"  Carregando[{'▉'*barra:<10}]{por}%", end="\r")
            por += 1
            time.sleep(delay)
    print(f"  Carregado[{'▉'*10}]100%")

def pergunta(mensagem=""):
    while True:
        print(mensagem)
        resposta = input("> ").strip().lower()

        if resposta in ("s", "n", "0"):
            return resposta
        print("  Opção inválida!")

def opção(num0, num, mensagem=""):
    while True:
        print(mensagem)
        try:
            op = int(input("> ").strip())

            if op in range(num0, num+1):
                return str(op)
            print(f"  Opção inválida! digite um numero entre {num0} e {num}")
        except:
            print(f"  Digito inválido! digite um numero")