def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for _ in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Adjust the value of 'n' to control the length of the Fibonacci sequence
n = 10
result = generate_fibonacci(n)
print(f"Fibonacci sequence of length {n}: {result}")
