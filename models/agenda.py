class Agenda:
    def __init__(self):
        self.pessoas = []

    def inserir_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def remover_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                self.pessoas.remove(pessoa)

    def imprimir_agenda(self):
        for pessoa in self.pessoas:
            print(pessoa.nome, pessoa.telefone)

    def __str__(self):
        return str(self.pessoas)
