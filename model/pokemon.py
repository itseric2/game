class Pokemon:

    def __init__(self, name, health, damage, skills_list, speed, types, level):
        self.__name = name
        self.__health = health
        self.__level = level
        self.__damage = damage
        self.__skills_list = skills_list
        self.__speed = speed
        self.__types = types
        self.__alive = True

    def __str__(self):
        return f"{self.__name}, {self.__health}, {self.__level}, {self.__damage}, {self.__skills_list}, {self.__speed}, {self.__types}, {self.__alive}"
        
    @property
    def name(self, name):
        return self.__name
    
    @property
    def health(self, health):
        return self.__health
    
    @health.setter
    def health(self, health):
        self.__health = self.__health if self.__validate_health(health) == None else health

    @property
    def damage(self, damage):
        return self.__damage
    
    @damage.setter
    def damage(self, damage):
        self.__damage = self.__damage if self.__validate_damage(damage) == None else damage

    @property
    def speed(self, speed):
        return self.__speed
    
    @property
    def level(self, level):
        return self.__level
    


    def __validate_health(self, health):
        if health < 0 or health > 8000:
            return None
        else:
            return health
        
    def __validate_damage(self, damage):
        if damage <= 0 or damage >= 1000:
            return None
        else:
            return damage
