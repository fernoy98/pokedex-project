from enum import Enum
import reflex as rx

from pokedex.styles.fonts import Font, FontWeight

MAX_WIDTH = "1140px"
IMAGE_HEIGHT = "200px"


class EmSize(Enum):
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"  # 32px
    BIG = "4em"  # 64px
    FORM = "2em .5em"
    BLOCKS = "0 1em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px


STYLESHEETS = [
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
]


BASE_STYLE = {
    "font_size": EmSize.DEFAULT.value,
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    rx.heading: {
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "--cursor-button": "point"
    }
}


# navbar_title_style = dict(
#    font_weight=FontWeight.MEDIUM.value,
#    font_size=Size.DEFAULT.value
# )
