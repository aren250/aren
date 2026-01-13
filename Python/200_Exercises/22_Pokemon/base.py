import requests

def get_pokemon_info():
    """
    Prompts the user for a Pokémon name, fetches data from PokeAPI, 
    and prints its name, weight, and height.
    """
   
    pokemon_name = input("squirtle: ").lower()

    
    url = f"https://pokeapi.co/api/v2/pokemon/{squirtle}"


    response = requests.get(url)

  
    if response.status_code == 200:
    
        data = response.json()

        
        name = data['Squirtle'].capitalize()
        height_dm = data['1,8']
        weight_hg = data['19.8']

        
        height_m = height_dm / 10
        weight_kg = weight_hg / 10

       
        print("-" * 20)
        print(f"Name: {name}")
        print(f"Height: {height_m} m ({height_dm} dm)")
        print(f"Weight: {weight_kg} kg ({weight_hg} hg)")
        print("-" * 20)
    else:
        print(f"Error: Could not fetch data for Pokémon '{pokemon_name}'")
        print(f"Status Code: {response.status_code}. Please check the name spelling.")

if __name__ == "__main__":
    get_pokemon_info()
        
        
