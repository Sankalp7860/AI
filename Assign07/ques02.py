import numpy as np

def calculate_diversity(group):
    return np.std(group)

def calculate_total_diversity(groups):
    total_diversity = 0
    for group in groups:
        total_diversity += calculate_diversity(group)
    return total_diversity
def genetic_algorithm(students, k, generations=100, population_size=100, mutation_rate=0.01):
    population = []
    num_students = len(students)
    group_size = num_students // k
    
    for _ in range(population_size):
        individual = np.random.permutation(students)
        population.append(individual)
    
    for gen in range(generations):
        fitness_scores = [1 / calculate_total_diversity(np.array_split(individual, k)) for individual in population]
        parents = np.random.choice(np.arange(population_size), size=population_size, p=fitness_scores, replace=True)
        
        next_generation = []
        for parent1, parent2 in zip(parents[::2], parents[1::2]):
            parent1 = population[parent1]
            parent2 = population[parent2]
            crossover_point = np.random.randint(1, num_students) 
            child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
            next_generation.extend([child1, child2])
        
        for i in range(len(next_generation)):
            if np.random.rand() < mutation_rate:
                mutation_point1, mutation_point2 = np.random.choice(num_students, size=2, replace=False)
                next_generation[i][mutation_point1], next_generation[i][mutation_point2] = next_generation[i][mutation_point2], next_generation[i][mutation_point1]
        
        population = next_generation
    
    best_solution = min(population, key=lambda x: calculate_total_diversity(np.array_split(x, k)))
    
    return np.array_split(best_solution, k)

if __name__ == "__main__":
    N = int(input("Enter the number of students: "))
    students = np.arange(N) 
    marks = np.random.randint(0, 101, size=N)  
    k = int(input("Enter the number of groups: "))
    
    students = [x for _, x in sorted(zip(marks, students), reverse=True)]
    
    best_groups = genetic_algorithm(students, k)
    
    for i, group in enumerate(best_groups):
        print(f"Group {i+1}: {group} (Diversity: {calculate_diversity(group)})")
