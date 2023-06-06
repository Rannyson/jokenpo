
#### JOGO JOKENPO ####
from random import randint
from time import sleep
nome = str(input('Qual seu nome? '))
itens = ('Pedra','Papel','Tesoura')
computador = randint (0, 2)
print('''Suas Opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador jogou '.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('{} VENCEU!'.format(nome)) 
    elif jogador == 2:
        print('COMPUTADOR VENCEU.TURURUUU!')
    else:
        print('Jogada INVALIDA!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU.CHOLA MAIS!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador ==2:
        print('{} VENCEU!'.format(nome))
    else:
        print('Jogada INVALIDA!')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('{} VENCEU!'.format(nome))
    elif jogador == 1:
        print('COMPUTADOR VENCE.HAHAHA PERDEU HUMANO!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada INVALIDA')
