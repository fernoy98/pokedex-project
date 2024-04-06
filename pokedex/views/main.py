import reflex as rx
from pokedex.components.card import get_pokemon


def main() -> rx.Component:
    # Obtener las imágenes de los Pokémon
    pokemon_cards = get_pokemon()

    return rx.center(
        rx.vstack(
            rx.grid(
                *pokemon_cards,
                grid_template_columns="repeat(4, minmax(310px, 1fr))",
                row_gap="3.5rem",
                column_gap="2.5rem"
            ),
            rx.button(
                "Ver más",
                margin="3.5rem 0",
                id="load_more_pokemon"),
            align_items="center"
        )
    )
