import reflex as rx
from pokedex.components.card import get_pokemon


def header() -> rx.Component:

    return rx.center(
        rx.image(
            src="/img/logo.png",
            margin_bottom="30px"
        ),
        align_items="centet",
        margin="0 auto",
    )
