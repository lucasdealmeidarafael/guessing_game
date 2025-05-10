import random

minimum_number = int(input('Qual o número minimo do intervalo?\n'))
maximum_number = int(input('Qual o número máximo do intervalo?\n'))

attempts = int(input('Quantas tentativas para acertar?\n'))

drawn_number = random.randint(minimum_number, maximum_number)

while True:
    attempt = int(input(f'Digite um número entre {minimum_number} e {maximum_number}.\n'))

    if attempt == drawn_number:
        print('Parabéns você acertou!!')
        break
    else:
        attempts -= 1 # Tentativas = Tentativas -1
        if attempts == 0:
            print(f'Você não acertou o número, e não tem mais tentativas. O número era {drawn_number}')
            break
        else:
            print(f'Número errado. Tente novamente. Você ainda tem {attempts} tentativas.')