class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    tarcisio = Pessoa(nome='Tarcísio')
    edilson = Pessoa(tarcisio, nome='Edilson', idade=57)
    print(Pessoa.cumprimentar(edilson))
    print(id(edilson))
    print(edilson.cumprimentar())
    print(edilson.nome)
    print(edilson.idade)
    for filho in edilson.filhos:
        print(filho.nome)

    edilson.sobrenome = 'Sousa'
    del edilson.filhos
    edilson.olhos = 1
    del edilson.olhos
    print(edilson.__dict__)
    print(tarcisio.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(edilson.olhos)
    print(tarcisio.olhos)
    print(id(Pessoa.olhos),id(edilson.olhos),id(tarcisio.olhos))
    print(Pessoa.metodo_estatico(), edilson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), edilson.nome_e_atributos_de_classe())

