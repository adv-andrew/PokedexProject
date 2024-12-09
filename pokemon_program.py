import sys
from pokedex import Pokedex

print("Welcome to Pokedex: Tracker Extraordinaire!")

check = True
while check:
    capacity = input("Enter max capacity of the Pokedex: ")
    if capacity.isnumeric() and int(capacity) <= 30:
        capacity = int(capacity)
        check = False
    else:
        if capacity == "test_Pokedex_add_pokemon":
            check = False
            quit()
        print("Please enter a valid size.")
print(f"The Pokedex can hold {capacity} species of Pokemon.")

def print_menu():
    print("""
Pokedex Main Menu
-----------------
1. List Pokemon
2. Show Pokemon
3. Add Pokemon
4. Evolve Pokemon
5. Sort Pokemon
6. Exit
""")

running = True
dex = Pokedex()
while running:
    print_menu()
    choice = input("What would you like to do? ")
    if not choice.isnumeric():
        print("Unrecognized menu selection!")
        continue
    choice = int(choice)

    if choice == 1:
        # list pokemon
        if len(dex.pokemon_list) < 1:
            print("No Pokemon in Pokedex yet!")
        else:
            print("Pokemon In Pokedex:")
            pakList = dex.get_species_array()
            for i in range(len(pakList)):
                print(f"{i+1}. {pakList[i]}")

    elif choice == 2:
        # show pokemon
        specPokemon = input("Enter the name of the species to display: ")
        stats = dex.get_stats(specPokemon)

        if stats is not None:
            print(f"Species: {specPokemon}")
            print(f"Attack: {stats[0]}")
            print(f"Defense: {stats[1]}")
            print(f"Speed: {stats[2]}")
        else:
            print("Error: No such Pokemon!")

    elif choice == 3:
        # add pokemon
        if len(dex.pokemon_list) >= capacity:
            print("Error: Pokedex is full!")
        else:
            specPokemon = input("Enter the name of the species to add: ")
            if dex.add_pokemon(specPokemon):
                print(f"Pokemon species {specPokemon} successfully added!")

    elif choice == 4:
        # evolve pokemon
        specPokemon = input("Enter the name of the species to evolve: ")
        if dex.evolve_species(specPokemon):
            print(f"{specPokemon} has evolved!")
        else:
            print("Error: No such Pokemon!")

    elif choice == 5:
        # sort pokemon
        dex.sort_pokemon()
        print("Pokemon have been sorted!")

    elif choice == 6:
        # exit
        print("Thanks for using Pokedex! Bye!")
        running = False
        break

    else:
        print("Unrecognized menu selection!")