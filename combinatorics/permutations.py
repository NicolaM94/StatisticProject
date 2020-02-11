from math import factorial


def simple_permutation (number_of_elements):
    return factorial(number_of_elements)


def repeted_permutation (number_of_elements,*subsets):
    denomin = 1
    for el in subsets:
        denomin = denomin * factorial(el)
    return factorial(number_of_elements)/denomin


def ciclic_permutation (number_of_elements):
    return factorial(number_of_elements-1)