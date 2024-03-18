def f(x):
    return x**2

def hill_climbing(start, step, max_iterations):
    current_x = start
    for _ in range(max_iterations):
        next_x = current_x + step
        if f(next_x) <= f(current_x):
            return current_x
        current_x = next_x
    return current_x

start = float(input("Enter the starting value: "))
step = float(input("Enter the step size: "))
max_iterations = int(input("Enter the maximum number of iterations: "))
max_value = hill_climbing(start, step, max_iterations)
print(f"The maximum value of f(x) within the specified range is at x = {max_value}")