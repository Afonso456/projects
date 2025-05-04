import random

def pedra_papel_tesoura():
    print("Bem-vindo ao Jogo de Pedra, Papel, Tesoura!")
    
    opcoes = ["pedra", "papel", "tesoura"]
    
    while True:
        escolha_jogador = input("Escolha (pedra, papel, tesoura) ou 'sair' para terminar: ").lower()
        
        if escolha_jogador == 'sair':
            print("Obrigado por jogar! Até à próxima!")
            break
        
        if escolha_jogador not in opcoes:
            print("Escolha inválida! Tente novamente.")
            continue
        
        escolha_computador = random.choice(opcoes)
        print(f"O computador escolheu: {escolha_computador}")
        
        # Determinar o vencedor
        if escolha_jogador == escolha_computador:
            print("É um empate!")
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel"):
            print("Ganhaste!")
        else:
            print("Perdeste!")

# Iniciar o jogo
pedra_papel_tesoura()
