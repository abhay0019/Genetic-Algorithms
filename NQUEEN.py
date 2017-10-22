from __future__ import division
import random
import time

N = 4
mut_prob = 0.01
pop_size = 100

def fitness(member):
	count = 0
	for i in range(0,len(member)):
		for j in range(i+1,len(member)):
			if(member[i]==member[j]):
				count+=1
			elif(abs(member[i]-member[j])==abs(j-i)):
				count+=1
	return count

def new_population():
	new_pop = []
	for no in range(0,pop_size):
		temp = []
		for i in range(0,N):
			temp.append(random.randint(0,N-1))
		new_pop.append(temp)
	return new_pop

def roulette_wheel(prob):
	r = random.uniform(0,1)
	for i in range(0,len(prob)):
		if(r<=prob[i]):
			return i
	return len(prob)-1

def crossover(par1,par2):
	child = []
	for i in range(0,len(par1)//2):
		child.append(par1[i])
	for i in range(len(par2)//2,len(par2)):
		child.append(par2[i])
		
	"""for i in range(0,len(par1)):
		if(i%2==0):
			child.append(par1[i])
		else:
			child.append(par2[i])"""
	return child

def mutate(member):
	for i in range(0,len(member)):
		r = random.uniform(0,1)
		if(r<=mut_prob):
			member[i] = random.randint(0,N-1)
	return member
			
def solve():
	new_pop = new_population()
	while(True):
		pop = new_pop
		new_pop = []
		fit = []
		prob = []
		prev = 0.0
		for i in range(0,len(pop)):
			fit.append(fitness(pop[i]))
		Sum = sum(fit)
		for i in range(0,len(fit)):
			prev+=(Sum - fit[i])/Sum
			prob.append(prev)
		for i in range(0,len(pop)):
			parent1 = roulette_wheel(prob)
			parent2 = roulette_wheel(prob)
			child = crossover(pop[parent1],pop[parent2])
			child = mutate(child)
			new_pop.append(child)
			print child,fitness(child)
			if(fitness(child)==0):
				return child

if __name__=='__main__':
	start = time.time()
	solution = solve()
	end = time.time()
	print solution,end-start

