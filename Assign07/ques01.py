import random

def fitness(x):
    return 2*x**2 + 1

def mutate(x, mutation_rate):
    if random.random() < mutation_rate:
        return random.randint(0, 6)
    else:
        return x

def crossover(x, y):
    return (x + y) / 2

def genetic_algorithm(population_size, mutation_rate, generations):
    population = [random.randint(0, 6) for _ in range(population_size)]

    for _ in range(generations):
        fitness_values = [fitness(x) for x in population]
        parents = random.choices(population, weights=fitness_values, k=2)
        child = crossover(*parents)
        child = mutate(child, mutation_rate)

        min_index = fitness_values.index(min(fitness_values))
        population[min_index] = child

    return max(population, key=fitness)

population_size = int(input("Enter population size: "))
mutation_rate = float(input("Enter mutation rate: "))
generations = int(input("Enter number of generations: "))
best_individual = genetic_algorithm(population_size, mutation_rate, generations)
print(f"Best individual: {best_individual}, Fitness: {fitness(best_individual)}")