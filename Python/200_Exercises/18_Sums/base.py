user_input_str = input("Please enter a number: ")

try:
   
    n = int(user_input_str)
    
    
    if n < 1:
        print("Please enter a positive integer.")
    else:
        
        total_sum = 0
        for i in range(1, n + 1):
            total_sum += i
            
        
        print(f"The sum of 1 to {n} is: {total_sum}")
        
except ValueError:
    
    print("Invalid input. Please enter a whole number.")