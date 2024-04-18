class Animal:
    def comer(self):
        print('O animal está comendo')

    def andar(self):
        print('O animal está andando na jaula')


class Felino(Animal):
    def lamber(self):
        print('O felino está lambendo seu pelo')

    # Utilização incorreta
    # def comer(self):
    #     print('O felino come sua reção')


class Leao(Felino):
    def rugir(self):
        print('O leão está rugindo alto')


class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()


animal = Animal()
felino = Felino()
leao = Leao()
pessoa = Pessoa()
# animal.comer()
# felino.comer()
pessoa.observa(felino)
pessoa.observa(leao)
