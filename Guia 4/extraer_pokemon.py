import pandas as pd
import requests
import pandas as pd

import requests
import pandas as pd

pokemon_data = []
errores = []

for i in range(1, 151):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        height = data['height']
        weight = data['weight']
        types = [t['type']['name'] for t in data['types']]
        pokemon_data.append({
            'name': name,
            'height': height,
            'weight': weight,
            'type': ', '.join(types)
        })
    else:
        errores.append(i)

# Mostrar errores si los hay
if errores:
    print(f"IDs con error: {errores}")
else:
    print("Todos los Pokémon fueron extraídos correctamente.")

# Guardar CSV
df = pd.DataFrame(pokemon_data)
df.to_csv('pokemones.csv', index=False)




