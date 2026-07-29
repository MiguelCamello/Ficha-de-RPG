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
|  [4] Excluir ficha                   |
|  [5] Editar ficha                    |
|                                      |
|  [0] Fecha programa                  |
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
|   • Gênero                           |
|   • Classe                           |
|                                      |
========================================
""")
        # criando objeto
        nome = input("  Nome: ").strip().capitalize()
        raça = input("  Raça: ").strip()
        genero = input("  Gênero: ").strip()
        classe = input("  Classe: ").strip()
        ficha_ = Jogador(nome, raça, genero, classe)

        print("""
========================================
|       Deseja editar ficha ou         | 
|       randomizar os status?          |
========================================
|                                      |
|   [1] Editar Status                  |
|   [2] Randomizar status              |
|                                      |
========================================
""")
        
        editar = input("> ").strip()
        trocar_tela()

        if editar == "1":
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
|   [1] Nível       [5] Agilidade      |
|   [2] Mana        [6] Vitalidade     |
|   [3] Força       [7] Resistência    |
|   [4] Itens       [8] Inteligência   |
|                                      |
|   [0] Continuar                      |
|                                      |
========================================
""")
                
                edição_ficha = input("> ")
                # Nivel
                if edição_ficha == "1":
                    print("  Novo valor do Nível:")
                    ficha_.atualizar_status("nivel", int(input("> ")))
                    print("  Valor do Nível alterado com sucesso!")
                    time.sleep(1)
                # Mana
                elif edição_ficha == "2":
                    print("  Novo valor da Mana:")
                    ficha_.atualizar_status("mana", int(input("> ")))
                    print("  Valor da Mana alterada com sucesso!")
                    time.sleep(1)
                # Força
                elif edição_ficha == "3":
                    print("  Novo valor da Força:")
                    ficha_.atualizar_status("força", int(input("> ")))
                    print("  Valor da Força alterada com sucesso!")
                    time.sleep(1)
                # Itens
                elif edição_ficha == "4":
                    print("  Informe os itens separados por virgula e espaço (, ):")
                    novos_items = input("> ").split(", ")
                    ficha_.adicionar_itens(*novos_items)
                    print(f"  Itens adicionados com sucesso!")
                    time.sleep(2)
                # Agilidade
                elif edição_ficha == "5":
                    print("  Novo valor da Agilidade:")
                    ficha_.atualizar_status("agilidade", int(input("> ")))
                    print("  Valor da Agilidade alterada com sucesso!")
                    time.sleep(1)
                # Vitalidade
                elif edição_ficha == "6":
                    print("  Novo valor da Vitalidade:")
                    ficha_.atualizar_status("vitalidade", int(input("> ")))
                    print("  Valor da Vitalidade alterada com sucesso!")
                    time.sleep(1)
                # Resistencia
                elif edição_ficha == "7":
                    print("  Novo valor da Resistência:")
                    ficha_.atualizar_status("resistencia", int(input("> ")))
                    print("  Valor da Resistência alterada com sucesso!")
                    time.sleep(1)
                # Inteligencia
                elif edição_ficha == "8":
                    print("  Novo valor da Inteligência:")
                    ficha_.atualizar_status("inteligencia", int(input("> ")))
                    print("  Valor da Inteligência alterada com sucesso!")
                    time.sleep(1)
                # continuar
                elif edição_ficha == "0":
                    trocar_tela()
                    break

                else:
                    print("  Opção inválida, digite um numero de 0 a 6")
                    time.sleep(1)

        elif editar == "2":
            atributos = ["mana", "força", "agilidade", "vitalidade", "resistencia", "inteligencia"]
            for att in atributos:
                ficha_.randomizer(att)

        while True:
            ficha_.mostrar_ficha
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


    elif menu_principal == "4":
        cls()
        print("""
========================================
|            EXCLUIR FICHA             |
========================================
|                                      |
|      Insira o id da ficha que        |
|      deseja que seja excluida        |
|      tendo em mente que ira          |
|      ficar um espaço em branco       |
|                                      |
========================================
""")
        try:
            id_excluir = int(input("> ").strip())
            ficha_excluir = carregar_json(id_excluir)

            trocar_tela()
            ficha_excluir.mostrar_ficha
            print("""
========================================
|       DESEJA EXCLUIR FICHA?          |
========================================
|                                      |
|   [S] Excluir ficha                  |
|   [N] não excluir                    |
|                                      |
|   [0] não excluir fechar             |
|                                      |
========================================
            """)
            certeza = input("> ").strip().lower()

            if certeza == "s":
                deletar(id_excluir)
                print(" Ficha excluida com sucesso!")
                time.sleep(2)
            elif certeza == "n":
                print("  Ficha não foi excluida.")
                time.sleep(2)
            elif certeza == "0":
                print("  Fechando...")
                time.sleep(2)
                cls()
                sys.exit()
                

        except AttributeError:
            print("  Esse id não existe!!!")
            time.sleep(2)

        # opção 5 edição json
    elif menu_principal == "5":
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
|   [1] Nível       [5] Agilidade      |
|   [2] Mana        [6] Vitalidade     |
|   [3] Força       [7] Resistência    |
|   [4] Itens       [8] Inteligência   |
|                                      |
|   [0] Continuar                      |
|                                      |
========================================
                        """)
                                        
                        edição_ficha = input("> ")
                        # Nivel
                        if edição_ficha == "1":
                            print("  Novo valor do Nível:")
                            ficha_edit.atualizar_status("nivel", int(input("> ")))
                            print("  Valor do Nível alterado com sucesso!")
                            time.sleep(1)
                        # Mana
                        elif edição_ficha == "2":
                            print("  Novo valor da Mana:")
                            ficha_edit.atualizar_status("mana", int(input("> ")))
                            print("  Valor da Mana alterada com sucesso!")
                            time.sleep(1)
                        # Força
                        elif edição_ficha == "3":
                            print("  Novo valor da Força:")
                            ficha_edit.atualizar_status("força", int(input("> ")))
                            print("  Valor da Força alterada com sucesso!")
                            time.sleep(1)
                        # Itens
                        elif edição_ficha == "4":
                            print("  Informe os itens separados por virgula e espaço (, ):")
                            novos_items = input("> ").split(", ")
                            ficha_edit.adicionar_itens(*novos_items)
                            print(f"  Itens adicionados com sucesso!")
                            time.sleep(2)
                        # Agilidade
                        elif edição_ficha == "5":
                            print("  Novo valor da Agilidade:")
                            ficha_edit.atualizar_status("agilidade", int(input("> ")))
                            print("  Valor da Agilidade alterada com sucesso!")
                            time.sleep(1)
                        # Vitalidade
                        elif edição_ficha == "6":
                            print("  Novo valor da Vitalidade:")
                            ficha_edit.atualizar_status("vitalidade", int(input("> ")))
                            print("  Valor da Vitalidade alterada com sucesso!")
                            time.sleep(1)
                        # Resistencia
                        elif edição_ficha == "7":
                            print("  Novo valor da Resistência:")
                            ficha_edit.atualizar_status("resistencia", int(input("> ")))
                            print("  Valor da Resistência alterada com sucesso!")
                            time.sleep(1)
                        # Inteligencia
                        elif edição_ficha == "8":
                            print("  Novo valor da Inteligência:")
                            ficha_edit.atualizar_status("inteligencia", int(input("> ")))
                            print("  Valor da Inteligência alterada com sucesso!")
                            time.sleep(1)
        
                        elif edição_ficha == "0":
                            trocar_tela()
                            break
        
                        else:
                            print("  Opção inválida, digite um numero de 0 a 6")
                            time.sleep(1)

                    while True:
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
                        menu = False # gambiarrinha pra voltar pro menu

                        if atualiza == "s":
                            atualizar(ficha_edit)
                            print("  Ficha atualizada com sucesso!")
                            menu = True
                            time.sleep(2)
                            break

                        elif atualiza == "n":
                            print("  Ficha não salva.")
                            time.sleep(2)
                            menu = True
                            break


                        elif atualiza == "0":
                            print("  Fechando...")
                            time.sleep(2)
                            sys.exit()

                        else:
                            print("  Resposta inválida.")
                            time.sleep(2)
                    if menu: break



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
        print("  Fechando...")
        time.sleep(2)
        break

    else:
        print("  Insira uma resposta valida!!!")
        time.sleep(2)