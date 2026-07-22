class Jogador:
    def __init__(self, nome, raça, classe):
        self.nome = nome
        self.raça = raça
        self.classe = classe

        self.nivel = 1
        self.força = 0
        self.saude = 0
        self.defesa = 0
        self.inteligencia = 0
        self.itens = []
        self.id = None

    @classmethod
    def carregar(cls, save):
        persona = cls(
            save["nome"],
            save["raça"],
            save["classe"]
        )
        persona.nivel = save["nivel"]
        persona.força = save["força"]
        persona.saude = save["saude"]
        persona.defesa = save["defesa"]
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

    def to_dict(self, id=None):
        return {
            "nome": self.nome,
            "raça": self.raça,
            "classe": self.classe,
            "nivel": self.nivel,
            "força": self.força,
            "saude": self.saude,
            "defesa": self.defesa,
            "inteligencia": self.inteligencia,
            "itens": self.itens,
            "id": id

        }

    @property
    def mostrar_ficha(self):
        print(f"""
========================================
|       FICHA DE PERSONAGEM - {self.id}
========================================
|                                      |
|   Nome: {self.nome}
|   Raça: {self.raça}
|   Classe: {self.classe}
|   Nivel: {self.nivel}
|                                      |
|   Estatisticas                       |
========================================
|                                      |
|   Força: {self.força}
|   Saúde: {self.saude}
|   Defesa: {self.defesa}
|   Inteligencia: {self.inteligencia}
|                                      |
|   Inventário                         |
========================================
|                                      |
|   {", ".join(self.itens)}
|                                      |
========================================
""")