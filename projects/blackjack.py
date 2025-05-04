import random
 
categorias_cartas = ['Copas', 'Ouros', 'Paus', 'Espadas']
cartas_lista = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
baralho = [(carta, categoria) for categoria in categorias_cartas for carta in cartas_lista]
 
def valor_carta(carta):
    if carta[0] in ['Valete', 'Dama', 'Rei']:
        return 10
    elif carta[0] == 'Ás':
        escolhaAS = int(input("tirou um Ás qual o valor que deseja que ele fique: "))
        if escolhaAS == 11:
            return 11
        else:
            return 1
    else:
        return int(carta[0])
 
random.shuffle(baralho)
cartas_jogador = [baralho.pop(), baralho.pop()]
cartas_dealer = [baralho.pop(), baralho.pop()]
 
while True:
    pontuacao_jogador = sum(valor_carta(carta) for carta in cartas_jogador)
    pontuacao_dealer = sum(valor_carta(carta) for carta in cartas_dealer)
    print("Cartas do Jogador:", cartas_jogador)
    print("Pontuação do Jogador:", pontuacao_jogador)
    print("\n")
    escolha = input('O que quer fazer? "bater" para pedir outra carta, "parar" para parar: ').lower()
    if escolha == "bater":
        nova_carta = baralho.pop()
        cartas_jogador.append(nova_carta)
   
    elif escolha == "parar":
        break
    else:
        print("Escolha inválida. Tente novamente.")
        continue
 
    if pontuacao_jogador > 21:
        print("Cartas do Dealer:", cartas_dealer)
        print("Pontuação do Dealer:", pontuacao_dealer)
        print("Cartas do Jogador:", cartas_jogador)
        print("Pontuação do Jogador:", pontuacao_jogador)
        print("Dealer ganha Jogador perde porque a pontuação do jogador ultrapassou 21")
        break
 
while pontuacao_dealer < 17:
    nova_carta = baralho.pop()
    cartas_dealer.append(nova_carta)
    pontuacao_dealer += valor_carta(nova_carta)
 
print("Cartas do Dealer:", cartas_dealer)
print("Pontuação do Dealer:", pontuacao_dealer)
print("\n")
 
if pontuacao_dealer > 21:
    print("Cartas do Dealer:", cartas_dealer)
    print("Pontuação do Dealer:", pontuacao_dealer)
    print("Cartas do Jogador:", cartas_jogador)
    print("Pontuação do Jogador:", pontuacao_jogador)
    print("Jogador ganha (Dealer perde porque a pontuação do dealer ultrapassou 21)")
elif pontuacao_jogador > pontuacao_dealer:
    print("Cartas do Dealer:", cartas_dealer)
    print("Pontuação do Dealer:", pontuacao_dealer)
    print("Cartas do Jogador:", cartas_jogador)
    print("Pontuação do Jogador:", pontuacao_jogador)
    print("Jogador ganha (Jogador tem pontuação maior que o Dealer)")
elif pontuacao_dealer > pontuacao_jogador:
    print("Cartas do Dealer:", cartas_dealer)
    print("Pontuação do Dealer:", pontuacao_dealer)
    print("Cartas do Jogador:", cartas_jogador)
    print("Pontuação do Jogador:", pontuacao_jogador)
    print("Dealer ganha (Dealer tem pontuação maior que o Jogador)")
else:
    print("Cartas do Dealer:", cartas_dealer)
    print("Pontuação do Dealer:", pontuacao_dealer)
    print("Cartas do Jogador:", cartas_jogador)
    print("Pontuação do Jogador:", pontuacao_jogador)
    print("Empate.")