import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding='utf-8') as handle:
        return json.load(handle)

def generate_animal_cards(animals):
    """Generate HTML cards for each animal"""
    cards_html = []
    
    for animal in animals:
        characteristics = animal.get('characteristics', {})
        locations = animal.get('locations', [])
        type_key = next((k for k in characteristics if k.lower() == 'type'), None)
        
        # Create card HTML
        card = f'''
        <li class="cards__item">
            <h2 class="card__title">{animal.get('name', 'Unnamed Animal')}</h2>
            <div class="card__text">
                <p><strong>Name:</strong> {animal.get('name', 'N/A')}</p>
        '''
        
        # Add diet if available
        if 'diet' in characteristics:
            card += f'<p><strong>Diet:</strong> {characteristics["diet"]}</p>\n'
            
        # Add first location if available
        if locations:
            card += f'<p><strong>Location:</strong> {locations[0]}</p>\n'
        # Add type if available
        if type_key and characteristics[type_key]:
            card += f'<p><strong>Type:</strong> {characteristics[type_key]}</p>\n'
        card += '''            </div>
        </li>'''
        
        cards_html.append(card)
    
    return '\n'.join(cards_html)

def generate_html():
    try:
        # Load data
        animals = load_data('animals_data.json')
        
        # Generate animal cards HTML
        animals_html = generate_animal_cards(animals)
        
        # Read template
        with open('animals_template.html', 'r', encoding='utf-8') as file:
            template = file.read()
        
        # Replace placeholder with generated HTML
        output_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_html)
        
        # Write to output file
        with open('animals_template.html', 'w', encoding='utf-8') as file:
            file.write(output_html)
        
        print("Successfully generated animals.html")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in animals_data.json")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_html()