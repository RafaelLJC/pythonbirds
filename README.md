Python Birds
===========

<<<<<<< HEAD
=======
Essa versão é a mais simples. Ela não contém replay nem reset, de forma que o jogo não pode retroceder.

Para versão mais complexa, acesse a branch [diversao](https://github.com/pythonprobr/pythonbirds/tree/diversao)

>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
Projeto para Ensino de Programação Orientadas a Objetos em Python.

A versão utilizada para desenvolvimento foi Python 3.4

Um vídeo fala mais que 1000 palavras: [Python Birds](https://www.youtube.com/watch?v=b899h0lNd7U&list=PLA05yVJtRWYTm0sIa6n56UpCjCsR5ekla)

<<<<<<< HEAD
=======
# Contribuidores

* [Giovane Liberato](https://github.com/giovaneliberato)
* [Guido Luz](https://github.com/GuidoBR)
* [Michel Amaral](https://github.com/michelamaral)
* [Renzo Nuccitelli](https://github.com/renzon)

>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
# Abordagem

Instalar [Python 3](https://www.python.org/download/).

<<<<<<< HEAD
Baixar a versão contendo apenas a [estrutura do projeto](https://github.com/pythonprobr/pythonbirds/archive/diversao.zip)

Os testes se encontram dentro do pacote "testes" e servem para definir a dinâmica das classes. Para rodar todos testes, execute

    python executor_de_testes.py
    
Explicação detalhada sobre classes e métodos se encontram em [Simplificação do Jogo](#simplifica%C3%A7%C3%A3o-do-jogo)
=======
Baixar o zip do projeto (botão Download Zip) 

Os testes se encontram dentro do pacote "testes" e servem para definir a dinâmica das classes. Para rodar todos testes, execute:

    python executor_de_testes.py
    
Explicação detalhada sobre classes e métodos se encontram nos scripts atores.py e fase.py.
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar

## Ordem de desenvolvimento

A ordem preferida é começar pelos atores, seguindo a ordem dos testes presentes no script atores_testes.py.
Depois passar para a fase_teste.py, onde é implementada uma fase.

<<<<<<< HEAD
Após o desenvolvimento é possível emular um jogo que termina em vitória rodando:
=======
É possível emular um jogo que termina em vitória rodando:
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar

    python fase_testes.py

É possível jogar a fase rodando:

    python placa_grafica_tkinter.py

Para jogar, utilize as setas para cima e para baixo. Para lançar, utilize a tecla enter ou espaço.
Demonstração nos vídeos:

[Python Birds](https://www.youtube.com/watch?v=b899h0lNd7U&list=PLA05yVJtRWYTm0sIa6n56UpCjCsR5ekla)

## script atores.py

Contém todos atores do projeto.

## script fase.py

Contém classes respectivas a fase e ponto do plano cartesiano

## script placa_grafica.py

Contém lógica para rodar jogo e exibir no console.

## script placa_grafica_tkinter.py

<<<<<<< HEAD
Contém lógica para rodar jogo e em uma janela.
=======
Contém lógica para rodar jogo em uma janela.
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar

# Simplificação do Jogo

1. Atores são pontos no plano cartesiano. 
<<<<<<< HEAD
2. A velocidade dos pontos e pequena, de tal forma que a cada passo os atores se movam apenas para pontos vizinhos.
=======
2. A velocidade dos pontos é pequena, de tal forma que a cada passo os atores se movam apenas para pontos vizinhos.
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
3. A colisão entre pontos ocorre quando eles estão em ponto vizinho, de acordo com valor de intervalo.

A seguir é apresentada a especificação detalhada do jogo.

## Classe Ator

Classe base para todos atores do jogo.

### Método calcular_posicao

Método que recebe o tempo (float) como parâmetro e retorna uma tupla com 2 elementos, posição horizontal (x) como 
primeiro elemento e posição vertical (y) como segundo.

<<<<<<< HEAD
### Método resetar

Método que ao ser executado, seta o valor de _tempo_de_colisão para None

### Método status

O ator possui os status Ativo ou Destruido. Além disso o status deve ser dependente do tempo. Ou seja, se o ator foi 
destruido no tempo 1, ele deve possuir status Ativo antes desse tempo, como 0.9, e Destruido após esse tempo, como em tempo 1.1.
 
### Método colidir

O método colidir executa a lógica de colisão. A colisão só ocorre com atores ativos e que estejam
em pontos vizinhos. 
O ator deve guardar o tempo de colisão para calcular corretamente seu status.
Além disso, um intervalo é recebido como parâmetro indicando qual a tolerância para considerar um ponto vizinho.
 Por padrão, seu valor é 1.

## Método caracter

O método caracter retorna 'A' quando o ator tem status Ativo e '+' caso contrário. Também é depende do tempo.


## Classe Obstaculo

Classe que representa obstáculos na fase e que podem ser destruidos por pássaros. Herda de ator. Seu caracter de 
representação é a letra "O" quando Ativo.
=======
### Método colidir

O método colidir executa a lógica de colisão. A colisão só ocorre com atores ativos e que estejam
em pontos vizinhos. Ao colidir, os atores envolvidos devem ter seus status alterado para DESTRUIDO

## Classe Obstaculo

Classe que representa obstáculos na fase e que podem ser destruídos por pássaros. Herda de ator. Seu caracter de 
representação é a letra "O", quando ATIVO.
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar

### Status

Um obstáculo ao ter seu status alterado para DESTRUIDO deve ter seu caracter de apresentação alterado para " " (vazio).
Assim ele vai "sumir" da tela.

## Classe Porco

<<<<<<< HEAD
Classe que representa porcos na fase e que podem ser destruidos por pássaros. Herda de ator. Seu caracter de 
representação é a o caracter "@".

=======
Classe que representa porcos na fase e que podem ser destruídos por pássaros. Herda de ator. Seu caracter de 
representação é a o caracter "@".

### Status

Um obstáculo ao ter seu status alterado para DESTRUIDO deve ter seu caracter de apresentação alterado para "+" (sinal de mais).
Assim sua imagem é alterada para a de porco morto.

>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
## Passaro

Classe base de todos os passáros. Cada tipo possui uma velocidade de lançamento (v). No lançamento o jogador escolhe o 
ângulo (teta), em graus, no qual o passáro deve ser lançado. O lançamento respeita as regras de lançamento oblíquo com 
<<<<<<< HEAD
gravidade (G) constante e igual a 10 m/s^2.

### Método lancar

O método lançar recebe o ângulo, em graus, que será feito o lançamento. Cada pássaro deve armazenar esse valor e o tempo
de lançamento para cálculo de sua posíção. Lembrar que o tempo das fórmulas é delta_t = T_final - T_inicial

### Método de resetar

O método resetar deve chamar o método resetar de Ator.
Além disso, deve setar como Nome os parầmetros de tempo de lançamento e ângulo de lançamento
=======
gravidade (GRAVIDADE) constante e igual a 10 m/s^2.

### Método lancar

O método lançar recebe o ângulo, em graus, que será feito o lançamento. Ele deve ser convertido para radianos.
Cada pássaro deve armazenar esse valor e o tempo
de lançamento para cálculo de sua posíção. Lembrar que o tempo das fórmulas é delta_t = T_final - T_inicial.
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar


### Método de colidir_com_chao

Todo pássaro que colidir com o chão (y<=0) deve ser destruído.

<<<<<<< HEAD
### Método foi lançado

Esse método deve retornar verdadadeiro se o pássaro foi lançado (tempo de lançamento é None).
Caso contrário deve retornar falso

### Lançamentomento

Se o pássaro ainda não foi lançado, ou se o tempo de jogo é menor que o tempo de lançamento,
O pássaro deve permanecer na posição inicial.
  
Calso tenha sido lançado e seu status esteja ativo, sua posição deve ser calculada de acordo com o lançamento oblíquo.
Nesse caso, delta_t vai ser igual ao tempo do jogo menos o tempo do lançamento.
  
Caso contrário, ele deve retornar a posição onde colidiu. Para isso, pasta
calcular o ponto em que o pássaro estava no tempo da colisão.

#### Método posicao_horizontal

Fórmula X=X0+v*cos(teta)*delta_t.

#### Método posicao_vertical

Fórmula Y=Y0+v*sen(teta)delta_t-(G*delta_t^2)/2.
=======
### Método foi_lançado

Esse método deve retornar verdadadeiro se o pássaro foi lançado (tempo de lançamento é None).
Caso contrário deve retornar falso.

### Lançamento

Se o pássaro ainda não foi lançado, o pássaro deve permanecer na posição inicial.
  
Caso tenha sido lançado e seu status esteja ATIVO, sua posição deve ser calculada de acordo com o lançamento oblíquo.
Nesse caso, delta_t vai ser igual ao tempo do jogo menos o tempo do lançamento.
  
Caso contrário, ele deve retornar a posição onde colidiu.

#### Método posicao_horizontal

Fórmula X=X0+v\*cos(teta)\*delta_t.

#### Método posicao_vertical

Fórmula Y=Y0+v\*sen(teta)delta_t-(G\*delta_t^2)/2.
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
    

## Classe Passaro Vermelho

<<<<<<< HEAD
Tipo de Pássaro que representa o pássaro vermelho. Possui velocidade de lançamento igual a 20 m/s. Seu caracter é "D".

## Classe Passaro Amarelo

Tipo de Pássaro que representa o pássaro amarelo. Possui velocidade de lançamento igual a 30 m/s. Seu caracter é ">".

## Classe Fase

Classe responsável por organizar atores e transformarem os dados em pontos a serem representados na tela.

### Método adicionar_obstaculo

Método que adiciona um ou mais obstáculos na fase

### Método adicionar_porco

Método que adiciona um ou mais porcos na fase

### Método adicionar_passaro

Método que adiciona um ou mais pássaros na fase

### Método acabou

Método que recebe o tempo do jogo e retorna verdadeiro (True) se o jogo acabou e (False) caso contrário.
O jogo pode acabar por duas razôes:

1. Todos porcos foram destruídos
2. Não há mais pássaros a serem lançados

### Método status

Recebe o tempo como parâmetro e retorna mensagem com status do jogo.

1. Se o jogo está em andamento, retorna mensagem "Jogo em andamento."
2. Se o jogo acabou e não existem porcos ativos, retorna a mensagem "Jogo em encerrado. Você ganhou!"
3. Se o jogo acabou e existem porcos ativos, retorna a mensagem "Jogo em encerrado. Você perdeu!"

### Método lancar

Recebe o ângulo e o tempo do lançamento. Deve delegar o lançamento ao primeiro pássaro ativo da lista de pássaros.
=======
Tipo de Pássaro que representa o pássaro vermelho. Possui velocidade de lançamento igual a 20 m/s. 
Seu caracter quanto ATIVO é "V". Quando DESTRUIDO é "v".

## Classe Passaro Amarelo

Tipo de Pássaro que representa o pássaro amarelo. Possui velocidade de lançamento igual a 30 m/s.
Seu caracter quanto DESTRUIDO é "a".

## Classe Fase

Classe responsável por organizar atores e transformar os dados em pontos a serem representados na tela.

### Método adicionar_obstaculo

Método que adiciona um ou mais obstáculos na fase.

### Método adicionar_porco

Método que adiciona um ou mais porcos na fase.

### Método adicionar_passaro

Método que adiciona um ou mais pássaros na fase.


### Método status

Recebe o tempo como parâmetro e retorna status do jogo.

1. Se o jogo está em andamento, retorna status "EM_ANDAMENTO";
2. Se o jogo acabou e não existem porcos ativos, retorna STATUS "VITORIA";
3. Se o jogo acabou e existem porcos ativos, retorna status "DERROTA".

### Método lancar

Recebe o ângulo e o tempo do lançamento. Deve delegar o lançamento ao primeiro pássaro ATIVO da lista de pássaros que 
ainda não foi lançado.
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar

### Método calcular_pontos

Método que executa a lógica do jogo a cada passo (tempo), retornando pontos a serem exibidos na tela.

Ele deve:

1. Calcular a posição de cada pássaro, verificando se ele colidiu com algum obstáculo, porco ou chão.
<<<<<<< HEAD
2. Retornar instâncias da classe Ponto, informando x,y e caracter respectivo a cada ator.

### Divirta-se!!!!

Powered by [Python Pro](http://adm.python.pro.br)
=======
2. Retornar instâncias da classe Ponto, informando x, y e caracter respectivo a cada ator.

### Divirta-se!!!!

Powered by [Python Pro](http://adm.python.pro.br)

# Observação Importante

Esse projeto usa somente o interpretador padrão do Python. Para fazer jogos com mais interatividade, existe a biblioteca Pygame. Ela não foi utilizada por motivos de simplicidade, para evitar que o aluno iniciante tenha dificuldades na hora de instalar o projeto.

Contudo o Estevão Fonseca fez um versão com essa biblioteca, confira o projeto:

<https://github.com/estevaofon/angry-birds-python>

Ele também colocou esse [vídeo no Youtube](https://www.youtube.com/watch?v=B7G5JtCFepE). 
>>>>>>> 261ea9f... Criado classe Pessoa e método cumprimentar
