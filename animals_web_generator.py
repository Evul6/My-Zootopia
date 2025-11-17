import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding='utf-8') as handle:
        return json.load(handle)

def print_animal_info():
    try:
        # Load the animals data using the load_data function
        animals = load_data('animals_data.json')
        
        # Iterate through each animal and print the requested information
        for animal in animals:
            print(f"Name: {animal.get('name')}")

            # Print diet if it exists
            characteristics = animal.get('characteristics', {})
            if 'diet' in characteristics:
                print(f"Diet: {characteristics['diet']}")

            # Print first location if it exists
            locations = animal.get('locations', [])
            if locations:
                print(f"First Location: {locations[0]}")

            # Print type if it exists (case-insensitive check)
            type_key = next((k for k in characteristics if k.lower() == 'type'), None)
            if type_key:
                print(f"Type: {characteristics[type_key]}")

            # Add a separator between animals
            print("-" * 40)

    except FileNotFoundError:
        print("Error: The file 'animals_data.json' was not found.")
    except json.JSONDecodeError:
        print("Error: The file 'animals_data.json' is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_animal_info()