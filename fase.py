# -*- coding: utf-8 -*-
from itertools import chain
from atores import ATIVO


<<<<<<< HEAD
class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = x
        self.y = y
=======
VITORIA = 'VITORIA'
DERROTA = 'DERROTA'
EM_ANDAMENTO = 'EM_ANDAMENTO'


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

<<<<<<< HEAD
=======
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    def __init__(self, intervalo_de_colisao=1):
<<<<<<< HEAD
=======
        """
        Método que inicializa uma fase.

        :param intervalo_de_colisao:
        """
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
        self.intervalo_de_colisao = intervalo_de_colisao
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

<<<<<<< HEAD
    def _adicionar_ator(self, lista, *atores):
        lista.extend(atores)

    def adicionar_obstaculo(self, *obstaculos):
        self._adicionar_ator(self._obstaculos, *obstaculos)

    def adicionar_porco(self, *porcos):
        self._adicionar_ator(self._porcos, *porcos)

    def adicionar_passaro(self, *passaros):
        self._adicionar_ator(self._passaros, *passaros)

    def acabou(self, tempo):
        return not self._existe_porco_ativo(tempo) or not self._existe_passaro_ativo(tempo)

    def status(self, tempo):
        if not self._existe_porco_ativo(tempo):
            return 'Jogo em encerrado. Você ganhou!'
        if self._existe_passaro_ativo(tempo):
            return 'Jogo em andamento.'
        return 'Jogo em encerrado. Você perdeu!'

    def lancar(self, angulo, tempo):
        for passaro in self._passaros:
            if not passaro.foi_lancado():
                passaro.lancar(angulo, tempo)
                return

    def resetar(self):
        for ator in chain(self._passaros, self._obstaculos, self._porcos):
            ator.resetar()

    def calcular_pontos(self, tempo):
        pontos = [self._calcular_ponto_de_passaro(p, tempo) for p in self._passaros]
        obstaculos_e_porcos = chain(self._obstaculos, self._porcos)
        pontos.extend([self._transformar_em_ponto(ator, tempo) for ator in obstaculos_e_porcos])
        return pontos

    def _transformar_em_ponto(self, ator, tempo):
        return Ponto(ator.x, ator.y, ator.caracter(tempo))

    def _calcular_ponto_de_passaro(self, passaro, tempo, ):
        passaro.calcular_posicao(tempo)
        for ator in chain(self._obstaculos, self._porcos):
            if ATIVO == passaro.status(tempo):
                passaro.colidir(ator, tempo, self.intervalo_de_colisao)
                passaro.colidir_com_chao(tempo)
            else:
                break
        return self._transformar_em_ponto(passaro, tempo)

    def _existe_porco_ativo(self, tempo):
        return self._verificar_se_existe_ator_ativo(self._porcos, tempo)

    def _verificar_se_existe_ator_ativo(self, atores, tempo):
        for a in atores:
            if a.status(tempo) == ATIVO:
                return True
        return False

    def _existe_passaro_ativo(self, tempo):
        return self._verificar_se_existe_ator_ativo(self._passaros, tempo)
=======

    def adicionar_obstaculo(self, *obstaculos):
        """
        Adiciona obstáculos em uma fase

        :param obstaculos:
        """
        pass

    def adicionar_porco(self, *porcos):
        """
        Adiciona porcos em uma fase

        :param porcos:
        """
        pass

    def adicionar_passaro(self, *passaros):
        """
        Adiciona pássaros em uma fase

        :param passaros:
        """
        pass

    def status(self):
        """
        Método que indica com mensagem o status do jogo

        Se o jogo está em andamento (ainda tem porco ativo e pássaro ativo), retorna essa mensagem.

        Se o jogo acabou com derrota (ainda existe porco ativo), retorna essa mensagem

        Se o jogo acabou com vitória (não existe porco ativo), retorna essa mensagem

        :return:
        """
        return EM_ANDAMENTO

    def lancar(self, angulo, tempo):
        """
        Método que executa lógica de lançamento.

        Deve escolher o primeiro pássaro não lançado da lista e chamar seu método lançar

        Se não houver esse tipo de pássaro, não deve fazer nada

        :param angulo: ângulo de lançamento
        :param tempo: Tempo de lançamento
        """
        pass


    def calcular_pontos(self, tempo):
        """
        Lógica que retorna os pontos a serem exibidos na tela.

        Cada ator deve ser transformado em um Ponto.

        :param tempo: tempo para o qual devem ser calculados os pontos
        :return: objeto do tipo Ponto
        """
        pontos=[self._transformar_em_ponto(a) for a in self._passaros+self._obstaculos+self._porcos]

        return pontos

    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter())

>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
