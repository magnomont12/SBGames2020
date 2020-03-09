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

jogador = player.Player(20,500,5,0)
pop = population.Population(13,0.1,10,jogador)

cont = 0
while(pop.minFitness()[0] > 1):
    pop.calcFitness(jogador)
    pop.naturalSelection()
    pop.generate()
    print("Entrei no laço")
    print(pop.minFitness()[0])
    print(pop.minFitness()[1])
    cont+=1
    for a in pop.population:
        print(a.fitness, a.dna, jogador.calcBatalha(a)[0])
    if cont > 3:
        break



