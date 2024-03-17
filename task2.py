def generate_number_pyramid(rows):
    for i in range(1, rows + 1):  # Loop through each row
        # Print spaces before the numbers to align the pyramid
        print(" " * (rows - i), end="")

        # Print numbers in increasing order for each row
        for j in range(1, i + 1):
            print(j, end=" ")

        print()  # Move to the next line after printing the row

# Test the function with a pyramid of 5 rows
print("Number Pyramid:")
generate_number_pyramid(5)
