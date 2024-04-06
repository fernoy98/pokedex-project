import reflex as rx

from pokedex.styles.colors import TypeColors
from pokedex.styles.styles import EmSize

# first, install requests and matplotlib (pip install requests matplotlib)
from urllib.request import urlopen
from PIL import Image
import matplotlib.pyplot as plt
import requests


def card_pokemon(image_url: str, name_pokemon: str, types_pokemon: list, index: int) -> rx.Component:
    # Convierte el índice en un número de tres dígitos (por ejemplo, 1 -> "001")
    pokemon_number = str(index).zfill(3)
    pokemon_name = str(name_pokemon)
    # Lista para almacenar las imágenes de los tipos
    type_images = [rx.image(
        src=get_type_image_url(type_pokemon),
        width="40px",
        border_radius="50px",
        padding="10px",
        box_shadow="0px 2px 3px 0px rgba(0, 0, 0, 0.2)",
        background_color=get_type_background_color(type_pokemon)
    ) for type_pokemon in types_pokemon]

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
                f"{pokemon_name}",
                font_size=EmSize.MEDIUM.value,
                text_transform="uppercase"
            ),
            rx.hstack(
                *type_images,
            ),
            align_items="center"
        ),
        background_color="rgba(255, 255, 255, 0.01)",
        box_shadow="inset 0 22px 56px -36px rgba(255, 255, 255, .5), inset 0 4px 5px -4px rgba(255, 255, 255, 1), inset 0 -31px 34px -32px rgba(96, 68, 144, .3), inset 0 39px 50px -34px rgba(202, 172, 255, .3), inset 0 2px 9px rgba(154, 146, 210, .3), inset 0 1px 10px rgba(227, 222, 255, .2)",
        color="#ffffff",
        backdrop_filter="blur(100px)",
        border_radius="3rem",
        padding="3.5rem 1.5rem 2rem",
        transition=".3s",
        _hover={
            "box-shadow": "inset 0 19px 28px -18px rgba(255, 255, 255, .5), inset 0 4px 6px -3px rgba(255, 255, 255, 1), inset 0 -51px 44px -42px rgba(96, 68, 144, .3), inset 0 59px 60px -32px rgba(202, 172, 255, .3), inset 0 4px 16px rgba(154, 146, 210, .3), inset 0 2px 25px rgba(227, 222, 255, .23)"
        },
        variant="ghost"
    )


offset = 1
limit = 29


def get_pokemon():

    global offset, limit
    pokemon_cards = []

    for element in range(offset, limit):
        api_url_pokemon = 'https://pokeapi.co/api/v2/pokemon/' + str(element)
        result = requests.get(api_url_pokemon)
        if result.status_code == 200:
            pokemon_data = result.json()

        url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
        name_pokemon = pokemon_data['name']
        # Obtener los tipos de Pokémon
        types = [type_info['type']['name']
                 for type_info in pokemon_data['types']]
        pokemon_cards.append(card_pokemon(
            url_image, name_pokemon, types, element))

    offset += limit
    print(offset)
    print(limit)

    return pokemon_cards


def get_type_image_url(pokemon_type: str) -> str:
    type_image_urls = {
        "normal": "/img/icon/normal.svg",
        "fighting": "/img/icon/fighting.svg",
        "flying": "/img/icon/flying.svg",
        "poison": "/img/icon/poison.svg",
        "ground": "/img/icon/ground.svg",
        "rock": "/img/icon/rock.svg",
        "bug": "/img/icon/bug.svg",
        "ghost": "/img/icon/ghost.svg",
        "steel": "/img/icon/steel.svg",
        "fire": "/img/icon/fire.svg",
        "water": "/img/icon/water.svg",
        "grass": "/img/icon/grass.svg",
        "electric": "/img/icon/electric.svg",
        "psychic": "/img/icon/psychic.svg",
        "ice": "/img/icon/ice.svg",
        "dragon": "/img/icon/dragon.svg",
        "dark": "/img/icon/dark.svg",
        "fairy": "/img/icon/fairy.svg",
    }
    # Si el tipo no está en la lista, devuelve una imagen predeterminada
    return type_image_urls.get(pokemon_type, "/img/icon/unknown.svg")


def get_type_background_color(pokemon_type: str) -> str:
    type_background_colors = {
        "normal": TypeColors.NORMAL.value,
        "fighting": TypeColors.FIGHTING.value,
        "flying": TypeColors.FLYING.value,
        "poison": TypeColors.POISON.value,
        "ground": TypeColors.GROUND.value,
        "rock": TypeColors.ROCK.value,
        "bug": TypeColors.BUG.value,
        "ghost": TypeColors.GHOST.value,
        "steel": TypeColors.STEEL.value,
        "fire": TypeColors.FIRE.value,
        "water": TypeColors.WATER.value,
        "grass": TypeColors.GRASS.value,
        "electric": TypeColors.ELECTRIC.value,
        "psychic": TypeColors.PSYCHIC.value,
        "ice": TypeColors.ICE.value,
        "dragon": TypeColors.DRAGON.value,
        "dark": TypeColors.DARK.value,
        "fairy": TypeColors.FAIRY.value,
    }
    # Si el tipo no está en la lista, devuelve un color de fondo predeterminado
    return type_background_colors.get(pokemon_type, "#C2C2C2")
