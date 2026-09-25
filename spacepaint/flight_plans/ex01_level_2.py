"""Making art... in space!"""

from spacepaint import Ship, start_spacepaint

__author__: str = "730995916"


def square(ship: Ship, length: float) -> None:
    """Aura draws a square in Space Paint"""
    ship.beam(on=True)
    ship.forward(units=length)
    ship.turn(degrees=90.0)
    ship.forward(units=length)
    ship.turn(degrees=90.0)
    ship.forward(units=length)
    ship.turn(degrees=90.0)
    ship.forward(units=length)
    return None


def main(aura: Ship) -> None:
    """Calls to the sqaure function and can repeat it in Space Paint"""
    aura.beam(on=True)
    square(ship=aura, length=4.0)
    square(ship=aura, length=3.0)
    square(ship=aura, length=2.0)
    square(ship=aura, length=1.0)
    return None


if __name__ == "__main__":
    start_spacepaint()
