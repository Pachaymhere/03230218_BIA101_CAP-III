################################
# https://github.com/Pachaymhere/03230218_BIA101_CAP-III
# PEMA ZANGMO
# BBI B
# 03230218
################################
# REFERENCES
# https://youtu.be/0EgSo7hsRWM?si=4nfsPuHSRZRClcId
# https://youtu.be/1Y-Zsdf66JU?si=bv3Aw_cU8nsrRIsL
################################
# SOLUTION
#The Solution Score: 483201
################################

def extract_two_digit_numbers_from_line(line): 
    #check the first and last digits from a line to form a two-digit number.
   
    # Remove non-digit characters and split the line into individual characters
    digits = ''.join(filter(str.isdigit, line))
    
    # Check if there are enough digits to form a two-digit number
    if len(digits) < 2:
        return 0
    
    # Form the two-digit number using the first and last digits
    return int(digits[0] + digits[-1])

def sum_two_digit_numbers_in_file(file_path):
    # Sums up all the two-digit numbers extracted from a file.
    
    total_sum = 0
    
    # Open and read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Extract the two-digit number from the current line
            two_digit_number = extract_two_digit_numbers_from_line(line)
            
            # Add the extracted number to the total sum
            total_sum += two_digit_number
    
    return total_sum


file_path = '218.txt'
total_sum = sum_two_digit_numbers_in_file(file_path)
print(f'The total sum of from the given input file 218.txt is: {total_sum}')

