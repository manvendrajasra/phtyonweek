if __name__ == '__main__':
    n = int(input())  # Read the number of elements
    integer_list = tuple(map(int, input().split()))  # Convert input to a tuple of integers
    result = hash(integer_list)  # Compute hash of the tuple
    print(result)  # Print the result
