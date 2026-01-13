def print_stars(n):
    """
    Prints a specified number of stars.
    
    Args:
        n (int): The number of stars to print.
    """
    if n > 0:
        print("*" * n)
    else:
        print("Please provide a positive integer.")

# Example usage:
print_stars(5)
print_stars(10)
