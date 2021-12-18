class Pessoa:
    # Método set
    def __init__(self, nome: str, telefone: int, email: str, matricula: int):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.matricula = matricula

        if self.validar_matricula():
            self.matricula = matricula
        else:
            print("Matricula invalida")
            exit()

    def validar_matricula(self):
        # Assumindo que a matricula é composta por 9 digitos
        if len(str(self.matricula)) == 9:
            return True
        else:
            return False

    # Método get
    def __str__(self):
        return f"{self.nome}, {self.telefone}, {self.email}, {self.matricula}"
