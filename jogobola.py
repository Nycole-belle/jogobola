import random


class Bola:
    def __init__(self, valor):
        self.valor = valor


class Urna:
    def __init__(self):
        self.bolas = [Bola(valor) for valor in range(1, 21)]


    def sortear_bola(self):
        return random.choice(self.bolas)


class JogoBola:
    def __init__(self):
        self.urna = Urna()
        self.alvo = 0
        self.palpite = 0
        self.jogando = True


    def iniciar_jogo(self):
        while self.jogando:
            self.sortear_alvo()
            self.palpite = int(input("Adivinhe o número alvo: "))
            self.verificar_palpite()


    def sortear_alvo(self):
        bola_sorteada = self.urna.sortear_bola()
        self.alvo += bola_sorteada.valor


    def verificar_palpite(self):
        print(f"O alvo é: {self.alvo}")
        print(f"Seu palpite: {self.palpite}")


        if self.palpite == self.alvo:
            print("Você acertou o alvo!")
            self.jogando = False
        elif self.alvo > 100:
            print("Game over! O computador venceu!")
            self.jogando = False
        else:
            print("Você errou! Tente novamente.")


if __name__ == "__main__":
    jogo = JogoBola()
    jogo.iniciar_jogo()



