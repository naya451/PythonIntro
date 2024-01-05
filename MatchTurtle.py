'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from enum import Enum

class Direction(Enum):
    S = 1
    N = 2
    W = 3
    E = 4

x, y = 0, 0
last_move = None

while True:
    command = input()
    match bool(command):
        case False:
            break
    c = command.split()[0]

    match c:
        case "move" if len(command.split()) == 2:
            move_dir = command.split()[1]
            match move_dir:
                case "s":
                    y -= 1
                    last_move = Direction.S
                case "n":
                    y += 1
                    last_move = Direction.N
                case "w":
                    x -= 1
                    last_move = Direction.W
                case "e":
                    x += 1
                    last_move = Direction.E
                case _:
                    print(f"Cannot move to {move_dir}")
        case "move":
            match bool(last_move):
                case False:
                    continue
            match last_move:
                case Direction.S:
                    y -= 1
                case Direction.N:
                    y += 1
                case Direction.W:
                    x -= 1
                case Direction.E:
                    x += 1
        case "retreat":
            match bool(last_move):
                case False:
                    continue
            match last_move:
                case Direction.S:
                    y += 1
                case Direction.N:
                    y -= 1
                case Direction.W:
                    x += 1
                case Direction.E:
                    x -= 1
        case "info" if len(command.split()) == 2:
            info_type = command.split()[1]
            match info_type:
                case "x":
                    print(f"{x}")
                case "y":
                    print(f"{y}")
                case "xy":
                    print(f"{x} {y}")
                case _:
                    continue
        case "say":
            message = " ".join(command.split()[1:])
            print(message)
        case _:
            continue

print(f"{x} {y}")
