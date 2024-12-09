# contain all the pokemon that you encounter as Pokemon objects
from pokemon import Pokemon

class Pokedex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.pokemon_list = []

    def get_size(self):
        # count pokemon objects in pokemon list (pakudex)
        return len(self.pokemon_list)

    def get_capacity(self):
        # capacity
        return self.capacity

    def get_species_array(self):
        res = []
        if len(self.pokemon_list) == 0:
            return None
        for i in range(len(self.pokemon_list)):
            res.append(self.pokemon_list[i].get_species())
        return res

    def get_stats(self, species):
        for pokemon in self.pokemon_list:
            if species == pokemon.get_species():
                return [pokemon.get_attack(), pokemon.get_defense(), pokemon.get_speed()]
        return None

    def sort_pokemon(self):
        self.pokemon_list.sort(key=lambda pokemon: pokemon.get_species())

    def add_pokemon(self, species):
        if self.get_size() >= self.capacity:
            return False
        for pokemon in self.pokemon_list:
            if species == pokemon.get_species():
                return False
        self.pokemon_list.append(Pokemon(species))
        return True

    def evolve_species(self, species):
        for pokemon in self.pokemon_list:
            if species == pokemon.get_species():
                pokemon.evolve()
                return True
        return False