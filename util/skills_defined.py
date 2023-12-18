from model.skills import Skill
import random

types = ["Planta", "Roca", "Agua", "Fuego", "Fantasma"]

def skills(type):
    skill_list = []
    if type == "Planta":
        skill_list.append(Skill('nj', 28, type))
        skill_list.append(Skill('ka', 14, type))
        skill_list.append(Skill('la', 42, type))
        skill_list.append(Skill('ñp', 37, type))
    elif type == "Roca":
        skill_list.append(Skill('r', 15, type))
        skill_list.append(Skill('t', 20, type))
        skill_list.append(Skill('u', 40, type))
        skill_list.append(Skill('h', 25, type))
    elif type == "Agua":
        skill_list.append(Skill('k', 25, type))
        skill_list.append(Skill('b', 32, type))
        skill_list.append(Skill('fa', 20, type))
        skill_list.append(Skill('j', 44, type))
    elif type == "Fuego":
        skill_list.append(Skill('l', 20, type))
        skill_list.append(Skill('al', 40, type))
        skill_list.append(Skill('el', 35, type))
        skill_list.append(Skill('rl', 18, type))
    elif type == "Fantasma":
        skill_list.append(Skill('Espectral touch', 15, type))
        skill_list.append(Skill('Ghostly attack', 20, type))
        skill_list.append(Skill('Ethereal journey', 40, type))
        skill_list.append(Skill('Ghostly attack', 25, type))
    return skill_list

random_type = random.choice(types)
random_type2 = random.choice(types)

while random_type == random_type2:
    random_type2 = random.choice(types)

def type_pokemon():
    random_type = random.choice(types)
    random_type2 = random.choice(types)

    while random_type == random_type2:
        random_type2 = random.choice(types)

pokemon_type = [skills(random_type), skills(random_type2)]

def pokemon_skills():
    return pokemon_type