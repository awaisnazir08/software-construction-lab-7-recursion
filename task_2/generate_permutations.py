from itertools import permutations as itertools_permutations

def generate_permutations_recursive(s):
    """
    Recursively generates all permutations of the input string.

    Args:
        s (str): The input string.

    Returns:
        list: A list of all permutations.
    """
    if len(s) == 1:  # Base case: single character
        return [s]

    perms = []  # List to store permutations
    for i, char in enumerate(s):
        # Exclude current character and get permutations of the remaining part
        remaining = s[:i] + s[i+1:]
        # Recursive call for remaining characters
        for perm in generate_permutations_recursive(remaining):
            perms.append(char + perm)
    return perms


def generate_unique_permutations(s):
    """
    Generates only unique permutations by using a set to filter duplicates.

    Args:
        s (str): The input string.

    Returns:
        list: A list of unique permutations.
    """
    return list(set(generate_permutations_recursive(s)))


def generate_permutations_non_recursive(s):
    """
    Generates all permutations of the input string using a non-recursive method.

    Args:
        s (str): The input string.

    Returns:
        list: A list of all permutations.
    """
    return [''.join(p) for p in itertools_permutations(s)]


def main():
    print("Welcome to the String Permutations Generator!")
    input_string = input("Enter a string: ")

    if not input_string:
        print("Error: Input string cannot be empty.")
        return

    include_duplicates = input("Include duplicate permutations? (yes/no): ").strip().lower() == 'yes'

    # Recursive solution
    if include_duplicates:
        recursive_result = generate_permutations_recursive(input_string)
    else:
        recursive_result = generate_unique_permutations(input_string)

    print("\nRecursive Permutations:")
    print(recursive_result)

    # Non-recursive solution
    non_recursive_result = generate_permutations_non_recursive(input_string)
    print("\nNon-Recursive Permutations:")
    print(non_recursive_result)

    # Performance comparison setup (optional, for larger strings)
    if len(input_string) <= 7:
        print("\nNote: Performance comparisons are not meaningful for small strings.")
    else:
        import time
        print("\nPerformance Comparison:")
        
        start = time.time()
        generate_permutations_recursive(input_string)
        print(f"Recursive solution time: {time.time() - start:.5f} seconds")

        start = time.time()
        generate_permutations_non_recursive(input_string)
        print(f"Non-recursive solution time: {time.time() - start:.5f} seconds")


if __name__ == "__main__":
    main()
