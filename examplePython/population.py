import player
import random

class Population():
    def __init__(self, target, mutation, pop, p1):
        self.target = target
        self.mutationRate = mutation
        self.generations = 0
        self.population = []
        self.matingPool = []
        for a in range(0,pop):
            self.population.append(player.Monster(random.randint(0,(p1.ataque*2)-1), random.randint(0,10), random.randint(0,(p1.ataque*2)-1)))
        self.calcFitness(p1)

    def calcFitness(self, p1):
        for a in range(0,len(self.population)):
            self.population[a].resultFitness(self.target, p1.calcBatalha(self.population[a])[0])
            

    def maxFitness(self):
        maxFitness = 0
        for a in range(0,len(self.population)):
            if self.population[a].fitness > maxFitness:
                maxFitness = self.population[a].fitness
        return maxFitness

    def minFitness(self):
        minFitness = 1000000
        dna = []
        for a in range(0,len(self.population)):
            if self.population[a].fitness < minFitness:
                minFitness = self.population[a].fitness
                dna = self.population[a].dna
        return minFitness, dna

    def naturalSelection(self):
        maxFitness = self.maxFitness()
        for a in range(0,len(self.population)):
            n =  (1 - self.population[a].fitness/maxFitness) * 100
            n = int(n)
            for b in range(0,n):
                self.matingPool.append(self.population[a])
    
    def generate(self):
        for a in range(0, len(self.population)):
            ga = random.randint(1,len(self.matingPool))
            gb = random.randint(1,len(self.matingPool))
            partnerA = self.matingPool[ga-1]
            partnerB = self.matingPool[gb-1]
            child = partnerA.crossover(partnerB)
            self.population[a].dna = child
            self.population[a].mutate(self.mutationRate)

    



    