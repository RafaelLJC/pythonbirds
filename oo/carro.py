# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:41:09 2020

@author: rafae
Exercício
Você deve criar uma classe carro que vai possuir dois atributos
compostos por outras duas classes:
1) motor;
2) Direção.
    
O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade;
2) Método acelerar, que deverá incrementar a velocidade de uma unidade;
3) Método frenar, que deverá decrementar a velocidade em duas unidades.
    
A direção terá a responsabilidade de controlar a direção. Ela oferece os
seguintes atributos:
1) Valor de direção com valores possóveis: Norte, Sul, Leste e Oeste;
2) Método girar a direita
2) Método girar a esquerda
    N
O       L
    S
    Exemplo:
        #testando motor
        >>> motor = Motor()
        >>> motor.velocidade
        0
        >>> motor.acelerar
        >>> motor.velocidade
        1
        >>> motor.acelerar
        >>> motor.velocidade
        2
        >>> motor.acelerar
        >>> motor.velocidade
        3
        >>> motor.frear
        >>> motor.velocidade
        1
        >>> motor.frear
        >>> motor.velocidade
        0
        #testando direção
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
         >>> direcao.girar_a_direita()
         >>> direcao.valor
         'Leste'
         >>> direcao.girar_a_direita()
         >>> direcao.valor
         'Sul'
         >>> direcao.girar_a_direita()
         >>> direcao.valor
         'Oeste'
         >>> direcao.girar_a_direita()
         >>> direcao.valor
         'Norte'
         >>> direcao.girar_a_esquerda()
         >>> direcao.valor
         'Oeste'
         >>> direcao.girar_a_esquerda()
         >>> direcao.valor
         'Sul'
         >>> direcao.girar_a_esquerda()
         >>> direcao.valor
         'Leste'
         >>> direcao.girar_a_esquerda()
         >>> direcao.valor
         'Norte'
         >>> carro = Carro(direcao, motor)
         >>> carro.caluclar_velocidade()
         0
         >>> carro.acelerar
         >>> carro.caluclar_velocidade()
         1
         >>> carro.acelerar
         >>> carro.caluclar_velocidade()
         2
         >>> carro.frear
         >>> carro.caluclar_velocidade()
         0        
         >>> carro.caluclar_direcao()
         'Norte'
         >>> carro.girar_a_direita()
         >>> carro.caluclar_direcao()
         'Leste'
         >>> carro.girar_a_esquerda()
         >>> carro.caluclar_direcao()
         'Norte'
         >>> carro.girar_a_esquerda()
         >>> carro.caluclar_direcao()
         'Oeste'
        
"""
class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar
    def frear(self):
        self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
    

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1     
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
        
motor = Motor()
motor.acelerar()

motor.acelerar()

motor.frear()

motor.frear()

motor.frear()

motor.acelerar()

motor.frear()
motor.acelerar()
motor.frear()



NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
            
    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = rotacao_a_esquerda_dct[self.valor]
        
rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
rotacao_a_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}
    
direcao = Direcao()

direcao.girar_a_direita()
direcao.girar_a_esquerda()
direcao.girar_a_esquerda()

carro = Carro(direcao, motor)


#print(direcao.valor)
#print(motor.velocidade)
print(carro.calcular_direcao())
print(carro.calcular_velocidade())
      
      
