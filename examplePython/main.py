"""
Um jogador considerado fraco é um player que possui:
Vida: 20
Ataque: 500
Defesa: 5
Equipamento: 0

Quais parâmetros o monstro deve possuir para que um jogador fraco derrote ele com aproximadamente 6 golpes?

"""
import player
import population

ATAQUE_JOGADOR = 500

jogador = player.Player(20,ATAQUE_JOGADOR,5,0)
pop = population.Population(13,0.01,100,jogador)

cont = 0
while(pop.minFitness()[0] > 1):
    pop.calcFitness(jogador)
    pop.naturalSelection()
    pop.generate()
    print(pop.minFitness()[0], pop.minFitness()[1])



