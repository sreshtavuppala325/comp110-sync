"""Making art... in space!"""

from math import atan2, degrees, sqrt

from spacepaint import Ship, start_spacepaint

__author__: str = "730995916"


def main(aura: Ship) -> None:
    """arrange the creeper head scene"""
    count: int = 0
    block: float = -3.0
    while count < 3:
        draw_block(ship=aura, x=block, y=-2.0, length=2.0)
        block = block + 2.0
        count = count + 1

    draw_head(ship=aura, x=-2.0, y=0.0)
    return None



def draw_block(ship: Ship, x: float, y: float, length: float) -> None:
    """Component 1: Draw a square ground block at (x, y) using `length`."""
    ship.beam(on=False)
    move_to(ship, x=x, y=y)

    ship.beam_color(value="green")
    ship.beam_width(width=0.08)
    ship.fill(on=True, opacity=0.7)
    ship.beam(on=True)

    move_to(ship, x=x + length, y=y)
    move_to(ship, x=x + length, y=y + length)
    move_to(ship, x=x, y=y + length)
    move_to(ship, x=x, y=y)

    ship.fill(on=False)
    ship.beam(on=False)


def draw_eye(ship: Ship, x: float, y: float) -> None:
    """Component 2: Draw a solid black eye square at (x, y)."""
    ship.beam(on=False)
    move_to(ship, x=x, y=y)

    ship.beam_color(value="purple")
    ship.beam_width(width=0.05)
    ship.fill(on=True, opacity=1.0)
    ship.beam(on=True)

    move_to(ship, x=x + 1.0, y=y)
    move_to(ship, x=x + 1.0, y=y + 1.0)
    move_to(ship, x=x, y=y + 1.0)
    move_to(ship, x=x, y=y)

    ship.fill(on=False)
    ship.beam(on=False)


def draw_mouth(ship: Ship, x: float, y: float) -> None:
    """Component 3: Draw the black Creeper mouth shape at (x, y)."""
    ship.beam(on=False)
    move_to(ship, x=x, y=y)

    ship.beam_color(value="purple")
    ship.beam_width(width=0.05)
    ship.fill(on=True, opacity=1.0)
    ship.beam(on=True)

    # Traces upside-down U mouth shape
    move_to(ship, x=x + 1.5, y=y)
    move_to(ship, x=x + 1.5, y=y + 0.5)
    move_to(ship, x=x + 1.0, y=y + 0.5)
    move_to(ship, x=x + 1.0, y=y + 1.5)
    move_to(ship, x=x + 0.5, y=y + 1.5)
    move_to(ship, x=x + 0.5, y=y + 0.5)
    move_to(ship, x=x, y=y + 0.5)
    move_to(ship, x=x, y=y)

    ship.fill(on=False)
    ship.beam(on=False)


def draw_head(ship: Ship, x: float, y: float) -> None:
    """Component 4: Draw the green head box, eyes, mouth."""
    ship.beam(on=False)
    move_to(ship, x=x, y=y)

    ship.beam_color(value="green")
    ship.beam_width(width=0.1)
    ship.fill(on=True, opacity=0.8)
    ship.beam(on=True)

    # Outer 4x4 head box
    move_to(ship, x=x + 4.0, y=y)
    move_to(ship, x=x + 4.0, y=y + 4.0)
    move_to(ship, x=x, y=y + 4.0)
    move_to(ship, x=x, y=y)

    ship.fill(on=False)
    ship.beam(on=False)

    draw_eye(ship=ship, x=x + 0.5, y=y + 2.5)
    draw_eye(ship=ship, x=x + 2.5, y=y + 2.5)
    draw_mouth(ship=ship, x=x + 1.25, y=y + 0.5)


def angle_between(ship: Ship, x: float, y: float) -> float:
    """Return the shortest signed turn toward an X/Y waypoint"""
    if ship.x == x and ship.y == y:
        return 0.0

    target_heading: float = degrees(atan2(y - ship.y, x - ship.x))
    difference: float = target_heading - ship.heading_x_y

    if difference > 180.0:
        difference = difference - 360.0
    else:
        if difference < -180.0:
            difference = difference + 360.0
    return difference


def distance_between(ship: Ship, x: float, y: float) -> float:
    """Compute the distance from the ship to an X/Y point."""
    return sqrt((x - ship.x) ** 2 + (y - ship.y) ** 2)


def move_to(ship: Ship, x: float, y: float) -> None:
    """Move ship directly to (x,y) using the shortest turn."""
    ship.turn(degrees=angle_between(ship, x, y))
    ship.forward(units=distance_between(ship, x, y))


if __name__ == "__main__":
    start_spacepaint()
