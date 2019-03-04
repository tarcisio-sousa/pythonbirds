"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de  controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de  dado velocidade
2) Método acelerar que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

    N
O       L
    S


     Exemplo:
     >>> # Testando o Motor
     >>> motor = Motor()
     >>> motor.velocidade
     1
     >>> motor.acelerar()
     >>> motor.velocidade
     2
     >>> motor.acelerar()
     >>> motor.velocidade
     3
     >>> motor.frear()
     >>> motor.velocidade
     1
     >>> motor.acelerar()
     >>> motor.velocidade
     0
     >>> # Testando Direcao
     >>> direcao = Direcao()
     >>> direcao.valor
     'Norte'
     >>> direcao.girando_a_direita()
     >>> direcao.valor
     'Leste'
     >>> direcao.girando_a_direita()
     >>> direcao.valor
     'Sul'
     >>> direcao.girando_a_direita()
     >>> direcao.valor
     'Oeste'
     >>> direcao.girando_a_esquerda()
     >>> direcao.valor
     'Sul'
     >>> direcao.girando_a_esquerda()
     >>> direcao.valor
     'Leste'
     >>> direcao.girando_a_esquerda()
     >>> direcao.valor
     'Norte'
     >>> carro = Carro(direcao, motor)
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     >>> carro.calculcar_velociade()
     1
     >>> carro.acelerar()
     >>> carro.calculcar_velociade()
     2
     >>> carro.frear()
     >>> carro.calculcar_velociade()
     0
     >>> carro.calcular_direcao()
     >>> 'Norte'
     >>> carro.girar_a_direita()
     >>> carro.calcular_direcao()
     >>> 'Leste'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
     >>> 'Norte'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
     >>> 'Oeste'

"""
#Constantes PEP
# NORTE = 'Norte'
# SUL = 'Sul'
# LESTE = 'Leste'
# OESTE = 'Oeste'

class Motor:
    velocidade = 0

    def __init__(self):
        # self.velocidade = 0
        pass

    def acelerar(self):
        self.velocidade = self.velocidade + 1
        # self.velocidade += 1

    def frear(self):
        self.velocidade = self.velocidade - 2
        # self.velocidade -= 2

        if self.velocidade < 0:
            self.velocidade = 0
        # self.velocidade = max(0, self.velocidade)

class Direcao:
    # rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    # rotacao_a_direita_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.valor = 'Norte'
        # self.valor = NORTE

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        else:
            self.valor = 'Norte'

        # self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        else:
            self.valor = 'Norte'

        # self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Carro:
    def __init__(self, direcao=Direcao(), motor=Motor()):
        self.direcao = direcao
        self.motor = motor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def calculca_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        return motor.acelerar()

    def frear(self):
        return motor.frear()

    def calcula_velocidade(self):
        return self.motor.velocidade


if __name__ == '__main__':
    # carro = Carro()
    # print(carro)
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    carro = Carro(direcao, motor)
    print(carro.calcula_velocidade())
    carro.acelerar()
    print(carro.calcula_velocidade())
    carro.acelerar()
    print(carro.calcula_velocidade())
    carro.frear()
    print(carro.calcula_velocidade())