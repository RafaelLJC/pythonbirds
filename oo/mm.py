# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:00:54 2020

@author: rafae
"""


class Pessoa:
    olhos = 2
    
    def __init__(self, *filhos, nome = None, idade = 26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'
    @staticmethod
    def metodo_static():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'
    
if __name__ == '__main__':
    
    Luciano = Pessoa(nome='Luciano')
    Clara = Pessoa(nome='Clara')
    Luiza = Pessoa(nome='Luiza')
    Rafael = Pessoa(Luciano, Luiza, Clara, nome='Rafael')
    print(Pessoa.cumprimentar(Rafael))
    print(id(Rafael))
    print(Rafael.cumprimentar())
    print(Rafael.nome)
    print(Rafael.idade)
    for filho in Rafael.filhos: 
        print(filho.nome)
        Rafael.sobrenome = 'Junqueira'
    del Rafael.filhos
    Rafael.olhos = 1
    Pessoa.olhos = 5j
    del Rafael.olhos
    print(Rafael.__dict__)
    print(Luiza.__dict__)
    print(Clara.__dict__)
    print(Pessoa.olhos)
    print(Rafael.olhos)
    print(Luiza.olhos)
    print(Clara.olhos)
    print(type(Pessoa.olhos))
    print(id(Pessoa.olhos), id(Rafael.olhos))
    print(Pessoa.metodo_static(), Rafael.metodo_static())
    print(Pessoa.nome_e_atributos_de_classe())