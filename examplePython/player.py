import random

class Player():
    def __init__(self, vida, ataque, defesa, equipamento):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.equipamento = equipamento

    def calcBatalha(self, monster):
        ##Se a Defesa do monstro/2 for maior que o ataque do jogador os turnos serão negativos
        ##Se a defesa do monstro/2 for igual ao ataque do jogador a divisão será por 0
        ##Logo a defesa do monstro deve ser 2 vezes o ataque do jogador -1
        "Eu quero saber na minha batalha, quantos turnos e também qual a vida que o jogador sai"
        dano = 4*monster.dna[1] - 2*self.defesa
        turnos = monster.dna[0] / ( 4 * (self.ataque - (monster.dna[2]/2)))
        return int(turnos), dano*turnos

class Monster():
    def __init__(self, vida, ataque, defesa):
        #self.vida = vida
        #self.ataque = ataque
        #self.defesa = defesa
        self.dna = [vida, ataque, defesa]
        self.fitness = 0

    def resultFitness(self, target, numAtqs):
        newFitness = abs(target-numAtqs)
        self.fitness = newFitness
        return newFitness

    def crossover(self, partener):
        child = []
        for a in range(0,len(self.dna)):
            child.append(0)
        midPoint = random.randint(0,len(self.dna))
        for a in range(0, len(self.dna)):
            if a > midPoint:
                child[a] = self.dna[a]
            else:
                child[a] = partener.dna[a]
        return child

    def mutate(self, mutationRate):
        for a in range(0,len(self.dna)):
            if random.random() < mutationRate:
                self.dna[a] = random.randint(0,20)