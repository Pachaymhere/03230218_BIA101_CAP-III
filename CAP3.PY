################################
# Github Repo link
# PEMA ZANGMO
# BBI B
# 03230218
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score: <total sum>
################################

def extract_two_digit_numbers_from_line(line):
    """
    Extracts the first and last digits from a line to form a two-digit number.
    
    Args:
        line (str): A string representing a line from the input file.
        
    Returns:
        int: The extracted two-digit number.
    """
    # Remove non-digit characters and split the line into individual characters
    digits = ''.join(filter(str.isdigit, line))
    
    # Check if there are enough digits to form a two-digit number
    if len(digits) < 2:
        return 0
    
    # Form the two-digit number using the first and last digits
    return int(digits[0] + digits[-1])

def sum_two_digit_numbers_in_file(file_path):
    """
    Sums up all the two-digit numbers extracted from a file.
    
    Args:
        file_path (str): The path to the text file containing the input data.
        
    Returns:
        int: The total sum of the two-digit numbers.
    """
    total_sum = 0
    
    # Open and read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Extract the two-digit number from the current line
            two_digit_number = extract_two_digit_numbers_from_line(line)
            
            # Add the extracted number to the total sum
            total_sum += two_digit_number
    
    return total_sum

# Example usage
file_path = '218.txt'
total_sum = sum_two_digit_numbers_in_file(file_path)
print(f'The total sum of from the given input file 218.txt is: {total_sum}')

