def high_and_low(numbers):
    
    num_list = list(map(int, numbers.split()))
    
    max_number = max(num_list)
    min_number = min(num_list)
    
    return f"{max_number} {min_number}"