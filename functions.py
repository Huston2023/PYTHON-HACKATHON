def generate_fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence
    fibonacci_sequence = [0, 1]

    # Generate Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

def main():
    # Ask the user to input the value of n
    n = int(input("Enter the number of terms: "))

    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(n)

    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()
