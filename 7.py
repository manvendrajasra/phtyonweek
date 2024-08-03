from itertools import combinations

def probability_of_letter_a(length, letters, k):
    # Find indices where the letter 'a' appears
    a_indices = [i for i, letter in enumerate(letters) if letter == 'a']
    
    # Total number of combinations
    total_combinations = list(combinations(range(length), k))
    total_count = len(total_combinations)
    
    # Count valid combinations
    valid_count = 0
    for combo in total_combinations:
        if any(index in a_indices for index in combo):
            valid_count += 1
    
    # Calculate probability
    probability = valid_count / total_count
    
    # Print probability rounded to 4 decimal places
    print(f"{probability:.4f}")

if __name__ == '__main__':
    n = int(input().strip())  # Length of the list
    letters = input().strip().split()  # List of letters
    k = int(input().strip())  # Number of indices to select
    
    probability_of_letter_a(n, letters, k)
