from __future__ import division
import random
import time

mut_prob = 0.01
pop_size = 100

def fitness(member):
	a = member[0]
	b = member[1]
	c = member[2]
	d = member[3]
	return abs(60-abs(a+2*b+3*c+4*d));
	
def new_population():
	pop = []
	for no in range(0,pop_size):
		sub = []
		for i in range(0,4):
			sub.append(random.randint(0,60))
		pop.append(sub)
	return pop

def roulette_wheel(prob):
	r = random.uniform(0,1)
	for i in range(0,len(prob)):
		if(r<=prob[i]):
			return i
	return len(prob)-1
	
def crossover(par1,par2):
	child = []
	child.append(par1[0])
	child.append(par1[1])
	child.append(par2[2])
	child.append(par2[3])
	return child

def mutation(child):
	for i in range(0,4):
		r = random.uniform(0,1)
		if(r<=mut_prob):
			child[i] = random.randint(0,60)
	return child
		
def evaluate():
	new_pop = new_population()
	pop = []
	while(True):
		fit = []
		prob = []
		norm_prob = []
		pop = new_pop
		new_pop = []
		prev = 0.0
		for i in range(0,len(pop)):
			#print pop[i]
			fit.append(fitness(pop[i]))
		Sum = sum(fit)
		for i in range(0,len(fit)):
			prob.append((Sum-fit[i])/Sum)
		for i in range(0,len(prob)):
			prev += prob[i]
			norm_prob.append(prev)
		for i in range(0,len(pop)):
			parent1 = roulette_wheel(norm_prob)
			parent2 = roulette_wheel(norm_prob)
			child = crossover(pop[parent1],pop[parent2])
			child = mutation(child)
			#print child,fitness(child)
			new_pop.append(child)
			if(fitness(child)==0):
				return child
if __name__ == '__main__':
	start = time.time()
	ans = evaluate()
	end = time.time()
	print ans,str(end-start)+" secs"	
	
