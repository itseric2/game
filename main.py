from model.pokemon import Pokemon
from model.skills import Skill
from model.player import Player
from model.potion import Potion
from util.skills_defined import *

if __name__ == "__main__":
    
    level = 1
    xp_counter = 0
    xp_neccesary = 200
    types = ["Planta", "Roca", "Agua", "Fuego", "Fantasma"]
    precision = random.randint(1,11)
    falla = None

    if xp_counter == xp_neccesary:
        level += 1
        xp_counter = 0
        xp_neccesary += 400

    if precision <= 4:
        falla = True

    else:
        falla = False

    def create_pokemon():
        syllable_list = ["ba","be","bi","bo","bu","ca","ce","ci","co","cu","da","de","di","do","du","fa","fe","fi","fo","fu","ga","ge","gi","go","gu","ha","he","hi","ho","hu","ja","je","ji","jo","ju","ka","ke","ki","ko","ku","la","le","li","lo","lu","na","ne","ni","no","nu","ña","ñe","ñi","ño","ñu","ma","me","mi","mo","mu","pa","pe","pi","po","pu","qa","qe","qi","qo","qu","ra","re","ri","ro","ru","sa","se","si","so","su","ta","te","ti","to","tu","va","ve","vi","vo","vu","wa","we","wi","wo","wu","xa","xe","xi","xo","xu","ya","ye","yi","yo","yu","za","ze","zi","zo","zu"]
        syllable1 = random.choice(syllable_list)
        syllable2 = random.choice(syllable_list)
        syllable3 = random.choice(syllable_list)
        nombre = syllable1 + syllable2 + syllable3 + syllable1
        vida = random.randint(12, 30)
        dano = random.randint(20,40)
        velocidad = random.randint(5,35)

        pokemon = Pokemon(nombre, vida, dano, pokemon_skills(), velocidad, type_pokemon(), level)
        print(pokemon)
    create_pokemon()