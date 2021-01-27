from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Rodrigues', idade=19)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Marciano').first()
    print(pessoa.idade)
    print(pessoas)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Padilha').first()
    pessoa.idade = 31 # pessoa.nome = 'Marcos'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Edson').first()


if __name__ == '__main__':
    insere_pessoas()
    #altera_pessoa()
    consulta_pessoas()
