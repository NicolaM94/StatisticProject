from math import factorial

def simple_combination (number_of_elements,number_of_groups):
    return factorial(number_of_elements)/(factorial(number_of_groups)*factorial(number_of_elements-number_of_groups))

def repeted_combination (number_of_elements,number_of_groups):
    return factorial(number_of_elements+number_of_groups-1)/(factorial(number_of_groups)*factorial(number_of_elements-number_of_groups))