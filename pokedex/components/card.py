import reflex as rx

from pokedex.styles.colors import TypeColors
from pokedex.styles.styles import EmSize

# first, install requests and matplotlib (pip install requests matplotlib)
from urllib.request import urlopen
from PIL import Image
import matplotlib.pyplot as plt
import requests


def card_pokemon(image_url: str, index: int) -> rx.Component:
    # Convierte el índice en un número de tres dígitos (por ejemplo, 1 -> "001")
    pokemon_number = str(index).zfill(3)

    return rx.card(
        rx.vstack(
            rx.image(
                src=image_url,
                height="200px",
                width="200px",
                object_fit="contain"
            ),
            rx.badge(
                rx.text.strong(
                    f"#{pokemon_number}",
                    as_="span",
                    color="#000000",
                    font_size=EmSize.DEFAULT.value
                ),
                background_color="#C2C2C2"
            ),
            rx.text(
                "Bulbasur",
                font_size=EmSize.MEDIUM.value
            ),
            rx.image(
                src="/img/icon/grass.svg",
                background=TypeColors.PLANTA.value,
                width="40px",
                border_radius="50px",
                padding="10px",
                box_shadow="0px 2px 3px 0px rgba(0, 0, 0, 0.2)",
            ),
            align_items="center"
        )
    )


def detect_img():

    pokemon_cards = []
    for element in range(1, 20):
        api_url_pokemon = 'https://pokeapi.co/api/v2/pokemon/' + str(element)
        result = requests.get(api_url_pokemon)
        if result.status_code == 200:
            pokemon_data = result.json()

        url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
        pokemon_cards.append(card_pokemon(url_image, element))

    return pokemon_cards


cards = detect_img()
