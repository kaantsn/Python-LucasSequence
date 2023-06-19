def lucas_sequence(n):
    sequence = [2, 1]  # Initialize the starting values as a list
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]  # Calculate the sum of the last two numbers
        sequence.append(next_number)  # Add the calculated number to the sequence
    return sequence

# Ask the user for a number
number = int(input("Enter the position of the Lucas number you want to calculate: "))

# Calculate the Lucas series
lucas_seq = lucas_sequence(number)

# Print the result to the screen
print("Lucas series:")
for num in lucas_seq:
    print(num, end=" ")
