import random

element_database = {
    1: {"name":"Hydrogen", "symbol":"H", "mass":1.008},
    2: {"name":"Helium" , "symbol":"He", "mass": 4.003},
    3: {"name":"Lithium" , "symbol":"Li", "mass":6.941},
    4: {"name":"Beryllium" , "symbol":"Be", "mass":9.012},
    5: {"name":"Boron" , "symbol":"B", "mass":10.81},
    6: {"name":"Carbon" , "symbol":"C", "mass":12.01},
    7: {"name":"Nitrogen" , "symbol":"N", "mass":14.01},
    8: {"name":"Oxygen" , "symbol":"O", "mass":16.00},
    9: {"name":"Fluorine" , "symbol":"F", "mass":19.00},
    10: {"name":"Neon" , "symbol":"Ne", "mass":20.18},
    11: {"name":"Sodium" , "symbol":"Na", "mass":22.99},
    12: {"name":"Magnesium" , "symbol":"Mg", "mass":24.31},
    13: {"name":"Aluminium", "symbol":"Al", "mass":26.98},
    14: {"name":"Silicon", "symbol":"Si", "mass":28.09},
    15: {"name":"Phosphorus", "symbol":"P", "mass":30.97},
    16: {"name":"Sulfur", "symbol":"S", "mass":32.07},
    17: {"name":"Chlorine", "symbol":"Cl", "mass":35.45},
    18: {"name":"Argon", "symbol":"Ar", "mass":39.95},
    19: {"name":"Potassium", "symbol":"K", "mass":39.10},
    20: {"name":"Calcium", "symbol":"Ca", "mass":40.08},
    21: {"name":"Scandium", "symbol":"Sc", "mass":44.96},
    22: {"name":"Titanium", "symbol":"Ti", "mass":47.88},
    23: {"name":"Vanadium", "symbol":"V", "mass":50.94},
    24: {"name":"Chromium", "symbol":"Cr", "mass":52.00},
    25: {"name":"Manganese", "symbol":"Mn", "mass":54.94},
    26: {"name":"Iron", "symbol":"Fe", "mass":55.85},
    27: {"name":"Cobalt", "symbol":"Co", "mass":58.93},
    28: {"name":"Nickel", "symbol":"Ni", "mass":58.69},
    29: {"name":"Copper", "symbol":"Cu", "mass":63.55},
    30: {"name":"Zinc", "symbol":"Zn", "mass":65.38}
}

def quiz_mass():
    random_atomic_number = random.choice(list(element_database.keys()))
    guess = input(f"What is the atomic mass for element that has atomic number of {random_atomic_number}? \nAnswer: ")
    random_mass = element_database[random_atomic_number]["mass"]
    is_correct = float(guess) == random_mass
    if is_correct:
        print(f"Correct!\nElement that has atomic number of {random_atomic_number} has {random_mass} atomic mass!")
    else:
        print(f"Incorrect. \nElement that has atomic number of {random_atomic_number} has {random_mass} atomic mass.")

def quiz_element():
    random_atomic_number = random.choice(list(element_database.keys()))
    random_element = element_database[random_atomic_number]["name"]
    guess = input(f"What is the name of the element that has atomic number {random_atomic_number}?\nAnswer: ")
    is_true = guess.lower() == random_element.lower()
    if is_true:
        print("Right!")
    else:
        print("Wrong")

def quiz_mass_to_name():
    random_atomic_number = random.choice(list(element_database.keys()))
    random_mass = element_database[random_atomic_number]["mass"]
    random_element = element_database[random_atomic_number]["name"]
    guess = input(f"Given an element has {random_mass} atomic mass. \nWhat is the element?\n")
    is_true = guess.lower() == random_element.lower()
    if is_true:
        print(f"Correct! \n{random_element} has atomic mass of {random_mass}!\n")
    else:
        print(f"Incorrect.\nThe element that has {random_mass} atomic mass is {random_element}.\n")

input_q_num = input("How many questions do you want to challenge right now?\n")
q_num = int(input_q_num)
input_type = input("What type of questions you want to do?\n" \
"From given atomic number:"\
"1) guess the atomic mass of element\n" \
"2) guess the element\n" \
"From given atomic mass:\n"\
"3) Guess the element\n"\
"----------------------------------------- Type 1 ~ 3 -----------------------------------------\n")
q_type = int(input_type)

for i in range(q_num):
    if q_type == 1:
        print(f"Question {i+1}:")
        quiz_mass()
    elif q_type == 2:
        print(f"Question {i+1}:")
        quiz_element()
    elif q_type == 3:
        print(f"Question {i+1}:")
        quiz_mass_to_name()