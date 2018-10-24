'''
Your goal is to find the material which when made into a tuning fork 107mm long
and 7.2 mm thick will produce the highest frequency.

The necessary data is in the dictionary materials which has been loaded for
you. The keys are the names of the materials and the values are a tuple of the
young's modulus in pascals and the density in kg/m^3.
'''

from math import sqrt  # you may want the sqrt function


def load_material_properties(filename):
    '''
    Load csv data of material names, young's modulus, and density into a Python
    dictionary.

    The keys of the materials dictionary are the names of materials and the
    value of each is a tuple of (Young's Modulus, Density).
    '''
    materials_dictionary = {}
    file = open(filename)
    data = file.readlines()
    file.close()

    for line in data:
        key, yModulus, density = line.strip('\n').split(',')
        materials_dictionary[key] = (float(yModulus), float(density))

    return materials_dictionary


materials = load_material_properties('materials-youngs modulus-densities.csv')

# Your code goes here.

# print the answer so you can see what material has the highest max frequency
# and what that frequency is.
