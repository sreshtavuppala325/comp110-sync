"""Making art... in space!"""

from math import atan2, degrees, sqrt

from spacepaint import Ship, start_spacepaint

__author__: str = "730995916"


def main(aura: Ship) -> None:
    """Calls to the sqaure function and can repeat it in Space Paint"""
    aura.beam(on=True)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=5.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=4.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=3.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=2.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=1.0)
    return None


def angle_between(ship: Ship, x: float, y: float) -> float:
    """Compute the turn from the ship's heading toward an X/Y point."""
    return degrees(atan2(y - ship.y, x - ship.x)) - ship.heading_x_y


def distance_between(ship: Ship, x: float, y: float) -> float:
    """Compute the distance from the ship to an X/Y point."""
    return sqrt((x - ship.x) ** 2 + (y - ship.y) ** 2)


def move_to(ship: Ship, x: float, y: float) -> None:
    """Move the ship from its current position to an X/Y point."""
    ship.turn(degrees=angle_between(ship, x, y))
    ship.forward(units=distance_between(ship, x, y))


def square_at( ship: Ship, center_x: float, center_y: float, length: float ) -> None:
    """Paint a square centered at an X/Y point"""
    half_length: float = length/2
    ship.beam(on=False)
    move_to(ship=ship, x=center_x + half_length , y= center_y + half_length) # top right corner
    ship.beam(on=True)
    move_to(ship=ship, x=center_x - half_length , y=center_y + half_length ) #top left corner
    move_to(ship=ship, x=center_x - half_length , y=center_y - half_length) #bottom left corner
    move_to(ship=ship, x=center_x + half_length , y=center_y - half_length) #bottom right corner
    move_to(ship=ship, x=center_x + half_length , y=center_y + half_length) #top right corner
    return None


if __name__ == "__main__":
    start_spacepaint()
