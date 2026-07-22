from database import *
from ficha import *
from assents import *
import time
import sys


cls()
# frufru de inicialização
iniciando()
time.sleep(1)
cls()
print("inicialização completa")
time.sleep(1)

while True:
    cls()
    print(RPG)

    print("""
========================================
|            MENU PRINCIPAL            |
========================================
|                                      |
|  O que deseja fazer?                 |
|                                      |
|  [1] Criar ficha de RPG              |
|  [2] Consultar ficha                 |
|  [3] Listar todas as fichas          |
|  [4] Editar ficha                    |
|                                      |
|  [0] Sair                            |
|                                      |
========================================
""")

    menu_principal = input("> ")
    trocar_tela()

    # 1 opção criar
    if menu_principal == "1":
        print("""
========================================
|       CRIAÇÃO DA FICHA DO RPG        |
========================================
|                                      |
|   Insira as seguintes informações:   |
|                                      |
|   • Nome                             |
|   • Raça                             |
|   • Classe                           |
|                                      |
========================================
""")
        # criando objeto
        nome = input("Nome: ").strip().capitalize()
        raça = input("Raça: ").strip()
        classe = input("Classe: ").strip()
        ficha_ = Jogador(nome, raça, classe)

        print("\n  Deseja editar os dados? S/N")
        editar = input("> ").strip().lower()
        trocar_tela()

        if editar == "s":
            while True:
                trocar_tela()
                ficha_.mostrar_ficha
                print("""
========================================
|           EDIÇÃO DA FICHA            |
========================================
|                                      |
|   O que deseja alterar?              |
|                                      |
|   [1] Nível       [4] Defesa         |
|   [2] Força       [5] Inteligência   |
|   [3] Saúde       [6] Itens          |
|                                      |
|   [0] Sair                           |
|                                      |
========================================
""")
                
                edição_ficha = input("> ")

                if edição_ficha == "1":
                    print("  Novo valor do nível:")
                    ficha_.atualizar_status("nivel", int(input("> ")))
                    print("  Valor do nivel alterado com sucesso!")
                    time.sleep(1)

                elif edição_ficha == "2":
                    print("  Novo valor da força:")
                    ficha_.atualizar_status("força", int(input("> ")))
                    print("  Valor da força alterada com sucesso!")
                    time.sleep(1)

                elif edição_ficha == "3":
                    print("  Novo valor da saúde:")
                    ficha_.atualizar_status("saude", int(input("> ")))
                    print("  Valor da saúde alterada com sucesso!")
                    time.sleep(1)

                elif edição_ficha == "4":
                    print("  Novo valor da defesa:")
                    ficha_.atualizar_status("defesa", int(input("> ")))
                    print("  Valor da defesa alterada com sucesso!")
                    time.sleep(1)

                elif edição_ficha == "5":
                    print("  Novo valor da inteligência:")
                    ficha_.atualizar_status("inteligencia", int(input("> ")))
                    print("  Valor da inteligência alterada com sucesso!")
                    time.sleep(1)

                elif edição_ficha == "6":
                    print("  Informe os itens separados por virgula e espaço (, ):")
                    novos_items = input("> ").split(", ")
                    ficha_.adicionar_itens(*novos_items)
                    print(f"  Itens adicionados com sucesso!")
                    time.sleep(2)

                elif edição_ficha == "0":
                    cls()
                    break

                else:
                    print("  Opção inválida, digite um numero de 0 a 6")
                    time.sleep(1)

        print("""
========================================
|           DESEJA SALVAR?             |
========================================
|                                      |
|   [S] salvar ficha                   |
|   [N] não salvar                     |
|                                      |
|   [0] não salvar e fecha o programa  |
|                                      |
========================================
""")    
        while True:
            salvar = input("> ").strip().lower()
            if salvar == "s":
                save(ficha_)
                print("  Ficha salva com sucesso!")
                time.sleep(1)
                break
            elif salvar == "n":
                print("  Ficha não salva.")
                time.sleep(1)
                break
            elif salvar == "0":
                print("  Programa encerrando...")
                time.sleep(1)
                cls()
                sys.exit()           
            else:
                print(f"  Opção inválida, digite S, N ou 0.")

        # 2 opção buscar
    elif menu_principal == "2":
        print("""
========================================
|           BUSCA DE FICHA             |
========================================
|                                      |
|   Insira o nome salvo na ficha e     |
|   a busca mostra os semelhantes      |
|                                      |
========================================
""")
        busca = input("> ").strip().capitalize()
        listar_fichas(busca)

        print("  Insira 0 para voltar")
        voltar = input("> ").strip()
        if voltar != "0":
            print(" Aperta 0 burro, vou deixar passar dessa vez")
            time.sleep(2)

        # 3 opção lista
    elif menu_principal == "3":
        print("""
========================================
|          LISTA DE FICHAS             |
========================================

        """)
        listar_fichas()

        print("  Insira 0 para voltar")
        voltar = input("> ").strip()
        if voltar != "0":
            print(" Aperta 0 burro, vou deixar passar dessa vez")
            time.sleep(2)

        # opção 4 edição json
    elif menu_principal == "4":
        while True:
            cls()
            print("""
========================================
|  Insira um id existente para edição  |
========================================
""")
            try:
            
                id_edição = int(input("> ").strip())
                ficha_edit = carregar_json(id_edição)

                ficha_edit.mostrar_ficha
                print("  Essa é a correta? S/N")
                correta = input("> ").strip().lower()

                if correta == "s":
                    while True:
                        trocar_tela()
                        ficha_edit.mostrar_ficha
                        print("""
========================================
|           EDIÇÃO DA FICHA            |
========================================
|                                      |
|   O que deseja alterar?              |
|                                      |
|   [1] Nível       [4] Defesa         |
|   [2] Força       [5] Inteligência   |
|   [3] Saúde       [6] Itens          |
|                                      |
|   [0] Sair                           |
|                                      |
========================================
                        """)
                                        
                        edição_ficha = input("> ")
        
                        if edição_ficha == "1":
                            print("  Novo valor do nível:")
                            ficha_edit.atualizar_status("nivel", int(input("> ")))
                            print("  Valor do nivel alterado com sucesso!")
                            time.sleep(1)
        
                        elif edição_ficha == "2":
                            print("  Novo valor da força:")
                            ficha_edit.atualizar_status("força", int(input("> ")))
                            print("  Valor da força alterada com sucesso!")
                            time.sleep(1)
        
                        elif edição_ficha == "3":
                            print("  Novo valor da saúde:")
                            ficha_edit.atualizar_status("saude", int(input("> ")))
                            print("  Valor da saúde alterada com sucesso!")
                            time.sleep(1)
        
                        elif edição_ficha == "4":
                            print("  Novo valor da defesa:")
                            ficha_edit.atualizar_status("defesa", int(input("> ")))
                            print("  Valor da defesa alterada com sucesso!")
                            time.sleep(1)
        
                        elif edição_ficha == "5":
                            print("  Novo valor da inteligência:")
                            ficha_edit.atualizar_status("inteligencia", int(input("> ")))
                            print("  Valor da inteligência alterada com sucesso!")
                            time.sleep(1)
        
                        elif edição_ficha == "6":
                            print("  Informe os itens separados por virgula e espaço (, ):")
                            novos_items = input("> ").split(", ")
                            ficha_edit.adicionar_itens(*novos_items)
                            print(f"  Itens adicionados com sucesso!")
                            time.sleep(2)
        
                        elif edição_ficha == "0":
                            cls()
                            break
        
                        else:
                            print("  Opção inválida, digite um numero de 0 a 6")
                            time.sleep(1)

                    while True:
                        trocar_tela()
                        ficha_edit.mostrar_ficha
                        print("""
========================================
|       DESEJA ATUALIZAR FICHA?        |
========================================
|                                      |
|   [S] atualizar ficha                |
|   [N] não atualizar                  |
|                                      |
|   [0] não atualizar e fecha          |
|                                      |
========================================
                        """)
                        atualiza = input("> ").strip().lower()
                        if atualiza == "s":
                            atualizar(ficha_edit)
                            print("  Ficha atualizada com sucesso!")
                            time.sleep(2)
                            break

                        elif atualiza == "n":
                            print("  Ficha não salva.")
                            time.sleep(2)
                            break


                        elif atualiza == "0":
                            print("  Fechando...")
                            time.sleep(2)
                            sys.exit()

                        else:
                            print("  Resposta inválida.")
                            time.sleep(2)



                elif correta == "n":
                    cls()
                    continue

                else:
                    print("  Resposta inválida")
                    time.sleep(2)
            
            except AttributeError:
                print("  Esse id não existe!!!")
                time.sleep(2)
            except ValueError:
                print(" Insira um id, não um digito!!!")
                time.sleep(2)

        # 5 opção sair
    elif menu_principal == "0":
        break