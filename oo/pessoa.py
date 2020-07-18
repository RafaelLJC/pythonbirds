# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:56:53 2020

@author: rafae
"""

class Pessoa:
    def __init__(self, nome = None, idade = 26):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
if __name__ == '__main__':
    
    p = Pessoa('Rafael')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Rafa'
    print(p.nome)
    print(p.idade)