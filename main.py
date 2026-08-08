from database import *
from ficha import *
from assents import *
import time
import sys

# frufru de inicialização
cls()
loading(0.05)
time.sleep(1)

while True:
    trocar_tela(False)
    menu_principal = opção(0,5, MENU)
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
        nome = input("  Nome: ").strip().title()
        raça = input("  Raça: ").strip()
        genero = input("  Gênero: ").strip()
        classe = input("  Classe: ").strip()
        ficha_ = Jogador(nome, raça, genero, classe)

        editar = opção(0,2, RANDOM)
        trocar_tela()

        if editar == "1":
            while True:
                trocar_tela(False)
                ficha_.mostrar_ficha                
                edição_ficha = opção(0,8, EDICAO)

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

        elif editar == "2":
            atributos = ["mana", "força", "agilidade", "vitalidade", "resistencia", "inteligencia"]
            for att in atributos:
                ficha_.randomizer(att)

        while True:
            ficha_.mostrar_ficha
            salvar = pergunta(SALVAR)

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
        busca = input("> ").strip().title()
        listar_fichas(busca)

        print("  Insira 0 para voltar")
        voltar = input("> ").strip()
        if voltar != "0":
            print(" Aperta 0 burro, esquece eu saio para vc")
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
            print(" Aperta 0 burro, esquece eu saio para vc")
            time.sleep(2)

    elif menu_principal == "4":
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
            certeza = pergunta(EXCLUIR)

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
                break
                
        except AttributeError:
            print("  Esse id não existe!!!")
            time.sleep(2)

        # opção 5 edição json
    elif menu_principal == "5":
        print("""
========================================
|  Insira um id existente para edição  |
========================================
    """)
        try:
            id_edição = int(input("> ").strip())
            ficha_edit = carregar_json(id_edição)

            ficha_edit.mostrar_ficha
            correta = pergunta("Essa é a correta? S/N, 0 para sair")

            if correta == "s":
                while True:
                    trocar_tela(False)
                    ficha_edit.mostrar_ficha                                    
                    edição_ficha = opção(0,8, EDICAO)

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

                while True:
                    ficha_edit.mostrar_ficha
                    atualiza = pergunta(ATUALIZAR)

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
                        cls()
                        sys.exit()
                    
            elif correta == "n":
                cls()
                continue

            elif correta == "0":
                cls()
                break
        
        except AttributeError:
            print("  Esse id não existe!!!")
            time.sleep(2)
        except ValueError:
            print("  Insira um id, não um digito!!!")
            time.sleep(2)

        # 5 opção sair
    elif menu_principal == "0":
        print("  Fechando...")
        time.sleep(2)
        break

    else:
        print("  Insira uma resposta valida!!!")
        time.sleep(2)