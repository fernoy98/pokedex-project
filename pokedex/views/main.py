import reflex as rx

# first, install requests and matplotlib (pip install requests matplotlib)
from urllib.request import urlopen
from PIL import Image
import matplotlib.pyplot as plt
import requests

api_url_pokemon = 'https://pokeapi.co/api/v2/pokemon/1'
result = requests.get(api_url_pokemon)
if result.status_code == 200:
    pokemon_data = result.json()

    url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
    im = Image.open(urlopen(url_image))
    plt.imshow(im)
    plt.show()


def main() -> rx.Component:
    return rx.center(
        rx.image(
            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"
        )
    )
