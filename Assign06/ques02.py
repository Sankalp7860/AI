import math
import random

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def tour_length(tour):
    return sum(distance(tour[i], tour[i - 1]) for i in range(len(tour)))

def simulated_annealing(cities, temp, cooling_rate, max_iterations):
    current_tour = random.sample(cities, len(cities))
    current_length = tour_length(current_tour)

    for i in range(max_iterations):
        new_tour = current_tour[:]
        i, j = random.sample(range(len(new_tour)), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_length = tour_length(new_tour)

        scaled_diff = (current_length - new_length) / temp

        if scaled_diff < 0 or math.exp(-scaled_diff) > random.random():
            current_tour, current_length = new_tour, new_length

        temp *= cooling_rate

    return current_tour, current_length

cities = [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(20)]
temp = float(input("Enter the initial temperature: "))
cooling_rate = float(input("Enter the cooling rate (between 0 and 1): "))
max_iterations = int(input("Enter the maximum number of iterations: "))

best_tour, best_length = simulated_annealing(cities, temp, cooling_rate, max_iterations)

print(f"The shortest tour has length {best_length} and visits the cities in this order:")
for city in best_tour:
    print(city)
