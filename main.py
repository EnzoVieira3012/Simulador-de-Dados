import random


def roll_dice():
    """Simula o lançamento de um dado de seis faces e retorna o resultado."""
    return random.randint(1, 6)


def main():
    print("Bem-vindo ao simulador de lançamento de dados!")

    while True:
        input("Pressione Enter para lançar o dado (ou 'sair' para encerrar): ")
        result = roll_dice()
        print(f"O resultado do lançamento é: {result}")

        # Verificar se o usuário deseja continuar ou sair
        quit_choice = input("Deseja lançar o dado novamente? (sair para encerrar): ").strip().lower()
        if quit_choice == 'sair':
            print("Saindo...")
            break


if __name__ == "__main__":
    main()
