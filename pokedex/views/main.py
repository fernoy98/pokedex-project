import reflex as rx
from pokedex.components.card import detect_img


def main() -> rx.Component:
    # Obtener las imágenes de los Pokémon
    pokemon_cards = detect_img()

    return rx.center(
        rx.grid(
            *pokemon_cards,
            grid_template_columns="repeat(4, 1fr)",
            grid_template_rows="repeat(4, 1fr)",
            grid_column_gap="30px",
            grid_row_gap="30px",
        )
    )
