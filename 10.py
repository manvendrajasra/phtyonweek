def print_formatted(number):
    # Determine the width needed based on the binary representation of `number`
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        # Generate and format each representation
        decimal = str(i)
        octal = format(i, 'o')
        hexadecimal = format(i, 'X')
        binary = format(i, 'b')
        
        # Print all representations space-padded to the width
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

if __name__ == '__main__':...