# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:36:21 2020

@author: rafae
"""


from unittest import TestCase
from oo.carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)