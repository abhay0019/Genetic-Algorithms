from __future__ import division
import random
character_population = []
pop_size = 100
mutation_prob = 0.01
target = " profile is abhay "

def generate_character_pop():			
	character_population.append(' ')
	for i in range(97,123):
		character_population.append(chr(i))

def fitness(child):
	match = 0
	for i in range(0,len(child)):
		if(child[i]==target[i]):
			match = match + 1
			
	return match
	
def randomchar():
	return character_population[random.randint(0,len(character_population)-1)]
	
def new_population():
	population = []
	for no in range(0,pop_size):
		member = ""
		for i in range(0,len(target)):
			member = member + randomchar()
		population.append(member)
	return population

def pop_fitness_prob(pop_fitness):
	prob = []
	Sum = sum(pop_fitness)
	for i in range(0,len(pop_fitness)):
		prob.append(pop_fitness[i]/Sum)
	return prob

def Normalize(prob):
	prev = 0.0
	norm = []
	for i in range(0,len(prob)):
		prev += prob[i]
		norm.append(prev)
	return norm

def roulette_wheel(normalized_prob):
	r = random.uniform(0,1)	
	for i in range(0,len(normalized_prob)):
		if( r <= normalized_prob[i] ):
			return i
	return len(normalized_prob)-1

def mutate(child):
	newchild = ""
	for i in range(0,len(child)):
		r = random.uniform(0,1)
		if(mutation_prob>=r):
			newchild += randomchar()
		else:
			newchild += child[i]
	return newchild

def check(pop):
	for i in range(0,len(pop)):
		if(fitness(pop[i])==len(target)):
			return i
	return -1

def guess():
	generate_character_pop()
			
	new_pop = new_population()
	iteration = 0

	while(check(new_pop)==-1):
		iteration += 1
		population = new_pop
		pop_fitness = []
		selection_prob = []
		for i in range(0,len(population)):
			pop_fitness.append(fitness(population[i]))
		selection_prob = pop_fitness_prob(pop_fitness)
		normalized_prob = Normalize(selection_prob)
		new_pop = []
		for i in range(0,len(population)):	
			parent1 = roulette_wheel(normalized_prob)
			parent2 = roulette_wheel(normalized_prob)
			new_child = population[parent1][:len(population[parent1])//2] + population[parent2][len(population[parent2])//2:]
			new_child = mutate(new_child)
			new_pop.append(new_child)
			print new_child
	print "Iteration ",iteration+1
	return (check(new_pop),new_pop)
	
if __name__ == '__main__':
	i,population = guess()
	print population[i]	
	
	
	
	
