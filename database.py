from pathlib import Path
from ficha import *
import textwrap
import json

BASE_DIR = Path(__file__).parent
ARQUIVO = BASE_DIR / "Json" / "personagens.json"
ID = BASE_DIR / "Json" / "config.json"

def lista_json(itens):
    inventario = ", ".join(itens)
    
    linhas = []
    
    for linha in textwrap.wrap(inventario, width=36):
        linhas.append(f"|  {linha:<36}|")
    
    return "\n".join(linhas)

def save(ficha):
    with ID.open("r", encoding="utf-8") as IDJson:
        id = json.load(IDJson)

    id[0]["ultimo_id"] += 1

        # criando var com novo id
    novo_id = id[0]["ultimo_id"]

    with ID.open("w", encoding="utf-8") as IDJson:
        json.dump(id, IDJson)


    with ARQUIVO.open("r", encoding="utf-8") as perJson:
        personagens = json.load(perJson)

    personagens.append(ficha.to_dict(novo_id))

    with ARQUIVO.open("w", encoding="utf-8") as perJson:
        json.dump(personagens, perJson, indent=4, ensure_ascii=False)


def listar_fichas(buscar=None):
    with ARQUIVO.open("r", encoding="utf-8") as perJson:
        personagens = json.load(perJson)

    for p in personagens:
        if buscar is not None and buscar != p["nome"]:
            continue
        print(f"""
                  
========================================
|       FICHA DE PERSONAGEM - {p["id"] if p["id"] is not None else '?':<9}|
========================================
|                                      |
|   Nome: {p["nome"]:<29}|
|   Raça: {p["raça"]:<29}|
|   Gênero: {p["genero"]:<27}|
|   Classe: {p["classe"]:<27}|
|                                      |
|   Estatisticas                       |
========================================
|                                      |
|   Nivel: {p["nivel"]:<28}|
|                                      |
|   Mana: {p["mana"]:<29}|
|   Força: {p["força"]:<28}|
|   Agilidade: {p["agilidade"]:<24}|
|   Vitalidade: {p["vitalidade"]:<23}|
|   Resistência: {p["resistencia"]:<22}|
|   Inteligência: {p["inteligencia"]:<21}|
|                                      |
|   Inventário                         |
========================================
|                                      |
{lista_json(p["itens"])}
|                                      |
========================================

""")
            
def carregar_json(id):
    with ARQUIVO.open("r", encoding="utf-8") as perJson:
        personagens = json.load(perJson)

    for p in personagens:
        if p["id"] == id:
            return Jogador.carregar(p)
        
    return None

def atualizar(ficha):
    with ARQUIVO.open("r", encoding="utf-8") as perJson:
        personagens = json.load(perJson)

    for i, p in enumerate(personagens):
        if p["id"] == ficha.id:
            personagens[i] = ficha.to_dict(ficha.id)
            break
    else:
        print("erro, essa ficha não existe nos arquivos")

    with ARQUIVO.open("w", encoding="utf-8") as perJson:
        json.dump(personagens, perJson, indent=4, ensure_ascii=False)

def deletar(id):
    with ARQUIVO.open("r", encoding="utf-8") as perJson:
        personagens = json.load(perJson)

    for i, p in enumerate(personagens):
            if p["id"] == id:
                del personagens[i]
                break

    with ARQUIVO.open("w", encoding="utf-8") as perJson:
        json.dump(personagens, perJson, indent=4, ensure_ascii=False)