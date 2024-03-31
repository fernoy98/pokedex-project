"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from pokedex.views.main import main

# class State(rx.State):
#    """The app state."""


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        main()
    )


app = rx.App(
    # stylesheets=STYLESHEETS,
    # style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="tomato",
        radius="full",
        grayColor="gray"
    )
)

app.add_page(index)
