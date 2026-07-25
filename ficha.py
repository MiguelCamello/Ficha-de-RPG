import textwrap

class Jogador:
    def __init__(self, nome, raça, genero, classe):
        self.nome = nome
        self.raça = raça
        self.genero = genero
        self.classe = classe

        self.nivel = 1
        self.mana = 0
        self.força = 0
        self.agilidade = 0
        self.vitalidade = 0
        self.resistencia = 0
        self.inteligencia = 0
        self.itens = []
        self.id = None

    @classmethod
    def carregar(cls, save):
        persona = cls(
            save["nome"],
            save["raça"],
            save["genero"],
            save["classe"]
        )
        persona.nivel = save["nivel"]
        persona.mana = save["mana"]
        persona.força = save["força"]
        persona.agilidade = save["agilidade"]
        persona.vitalidade = save["vitalidade"]
        persona.resistencia = save["resistencia"]
        persona.inteligencia = save["inteligencia"]
        persona.itens = save["itens"]
        persona.id = save["id"]

        return persona

    def editar(self, atributo, novo):
        if atributo not in self.__dict__:
            print("atributo invalido")
            return
        setattr(self, atributo, getattr(self, novo))

    def atualizar_status(self, status, num=1):
        if status not in self.__dict__:
            print("atributo invalido")
            return
        setattr(self, status, num)

    def adicionar_itens(self, *itens):
        self.itens.extend(itens)

    def listar_itens(self):
        inventario = ", ".join(self.itens)

        linhas = []

        for linha in textwrap.wrap(inventario, width=36):
            linhas.append(f"|  {linha:<36}|")

        return "\n".join(linhas)

    def to_dict(self, id=None):
        return {
            "nome": self.nome,
            "raça": self.raça,
            "genero": self.genero,
            "classe": self.classe,
            "nivel": self.nivel,
            "mana": self.mana,
            "força": self.força,
            "agilidade": self.agilidade,
            "vitalidade": self.vitalidade,
            "resistencia": self.resistencia,
            "inteligencia": self.inteligencia,
            "itens": self.itens,
            "id": id

        }

    @property
    def mostrar_ficha(self):
        print(f"""
========================================
|       FICHA DE PERSONAGEM - {self.id if self.id is not None else '?':<9}|
========================================
|                                      |
|   Nome: {self.nome:<29}|
|   Raça: {self.raça:<29}|
|   Gênero: {self.genero:<27}|
|   Classe: {self.classe:<27}|
|                                      |
|   Estatisticas                       |
========================================
|                                      |
|   Nivel: {self.nivel:<28}|
|                                      |
|   Mana: {self.mana:<29}|
|   Força: {self.força:<28}|
|   Agilidade: {self.agilidade:<24}|
|   Vitalidade: {self.vitalidade:<23}|
|   Resistência: {self.resistencia:<22}|
|   Inteligência: {self.inteligencia:<21}|
|                                      |
|   Inventário                         |
========================================
|                                      |
{self.listar_itens()}
|                                      |
========================================
""")