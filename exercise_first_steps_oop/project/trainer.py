from typing import List

from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        pokemon_data = '\n'.join(f'- {x.pokemon_details()}' for x in self.pokemons)

        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemons)}\n" + \
               f"{pokemon_data}"

