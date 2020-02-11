from math import factorial

def simple_disposition (number_of_elements,number_of_groups):
    return factorial(number_of_elements)/factorial(number_of_elements-number_of_groups)

def repeted_disposition (number_of_elements,number_of_groups):
    return number_of_elements**number_of_groups
