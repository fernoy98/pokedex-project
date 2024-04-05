"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import pokedex.styles.styles as styles
from pokedex.styles.styles import BASE_STYLE, STYLESHEETS
from pokedex.views.header import header
from pokedex.views.main import main

# class State(rx.State):
#    """The app state."""


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(),
            main(),
        ),
        width=styles.MAX_WIDTH,
        align_items="center",
        margin="0 auto"
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="tomato",
        radius="full",
        grayColor="gray"
    )
)

app.add_page(index)
