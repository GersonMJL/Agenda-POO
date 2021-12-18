from models.agenda import Agenda
from models.pessoa import Pessoa


def main():

    agenda = Agenda()

    p1 = Pessoa("João", 99999999, "email1@email.com", 123456789)
    p2 = Pessoa("Maria", 99999999, "email2@email.com", 123456789)
    p3 = Pessoa("Pedro", 99999999, "email3@email.com", 123456789)

    agenda.inserir_pessoa(p1)
    agenda.inserir_pessoa(p2)
    agenda.inserir_pessoa(p3)

    agenda.imprimir_agenda()

    agenda.remover_pessoa("Pedro")

    agenda.imprimir_agenda()


main()
