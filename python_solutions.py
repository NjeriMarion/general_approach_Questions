class Ankara:
    def __init__(self, mood, temp) :
        self.mood = mood
        self.temp = temp
        self.fabric = " "
    
    def fabric_check(self, daily_mood, moment_temp):
        if daily_mood == self.mood:
            if moment_temp == self.temp:
                self.fabric += "Dotted"
            elif moment_temp > self.temp:
                self.fabric += "Stripped"
            else:
                self.fabric += "Floral"

        elif daily_mood > self.mood:
            if moment_temp == self.temp:
                self.fabric += "Dotted"
            elif moment_temp > self.temp:
                self.fabric += "Stripped"
            else:
                self.fabric += "Floral"

        elif daily_mood < self.mood:
            if moment_temp == self.temp:
                self.fabric += "Dotted"
            elif moment_temp > self.temp:
                self.fabric += "Stripped"
            else:
                self.fabric += "Floral"
        else:
            print("Please enter a mood")
        
        return f'Your fabric pattern will be {self.fabric}'
    
print("******************************************************")
ankaraOne = Ankara(5, 20.5)
print(ankaraOne.fabric_check(7, 22.0))



class Movement:
    def __init__(self, river_levels, predator_locations, weather):
        self.river_levels = river_levels
        self. predator_locations = predator_locations
        self.weather = weather
        self.movement = True
    def migration(self, herd, river, present_location, weather):

        if river == self.river_levels and present_location == self.predator_locations and weather == self.weather:
            self.movement = True
            return f'{herd} are moving from {present_location}'
        else :
            self.movement = False
            return f'{herd} are not moving from {present_location}'
           
print("******************************************************")
animals = Movement("12ft", "North", "Hot and Dry")
print(animals.migration("Zebras", "13ft", "South", "Hot and Dry"))
print(animals.migration("Zebras","12ft", "North", "Hot and Dry"))


class Movies:
    def __init__(self, movie_name, schedule, budget):
        self.movie_name = movie_name
        self.schedule = schedule
        self.budget = budget
        self.cast_members = {}
    def add_cast(self, cast_member, role):
        if cast_member in self.cast_members:
            return f'{cast_member} is already on the list of cast members for {self.movie_name}'
        else:
            self.cast_members[cast_member] = role
            return self.cast_members
    def remove_cast(self, cast_member):
        if cast_member in self.cast_members:
            self.cast_members.pop(cast_member)
            return self.cast_members
        else :
            return f'{cast_member} is not on the list of cast members for {self.movie_name}'
    def check_budget(self, final_budget):
        if final_budget <= self.budget:
            return f'{final_budget} has been confirmed to be in line with the {self.budget}'
        else:
             return f'{final_budget} is higher than {self.budget}'

print("******************************************************")
movie = Movies("Jumanji","Morning", "1 Million")
print(movie.add_cast("Loice", "Star"))
print(movie.add_cast("Mary", "other"))
print(movie.add_cast("Mwangi", "co-star"))
print(movie.add_cast("Mwangi", "co-star"))
print(movie.remove_cast("Loice"))

class Baobab:
    def __init__(self):
        self.leaf_presence = True
        self.powers = {}
    def fruits(self, leaf_color, stem_thickness):
        if self.leaf_presence:
            fruit = ""
            if leaf_color == "green":
                if stem_thickness in range(1,20):
                    fruit = "Mango"
                    self.powers[fruit] = "Super Strength"
                    return f"Next season you will have {self.powers}"
                else:
                    fruit = "Orange"
                    self.powers[fruit] = "Super Speed"
                    return f"Next season you will have {self.powers}"
            elif leaf_color == "yellow":
                if stem_thickness in range(21,30):
                    fruit = "PineApple"
                    self.powers[fruit] = "Invisibility"
                    return f"Next season you will have {self.powers}"
                else:
                    fruit = "Banana"
                    self.powers[fruit] = "Immortality"
                    return f"Next season you will have {self.powers}"
        else:
            return f'The tree has no fruit at the said period'


                
tree = Baobab()
# print(tree.fruits("green", 15))
print(tree.fruits("yellow", 25))
print(tree.fruits("yellow", 35))


class Drums:
    def __init__(self , material, size):
        self.material = material
        self.size = size
    def predict_sound(self):
        print(f"{self.__class__.__name__}, {self.sound}")
    

class Djembe(Drums):
    sound = "Produces a base sound"

class TalkingDrum(Drums):
    sound = "Produces a soft sound"

class Bougarabou(Drums):
    sound = "Produces a light sound"


drum_one= Djembe("Leather", "small")
drum_one.predict_sound()
print(drum_one.size)
print("***********************************************************")

drum_two= Bougarabou("Leather", "small")
drum_two.predict_sound()

print("***********************************************************")
drum_three= TalkingDrum("Leather", "small")
drum_three.predict_sound()