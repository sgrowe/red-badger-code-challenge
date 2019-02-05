

class Robot:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def perform_instruction(self, instruction):
        if instruction == 'L':
            self.orientation = rotate_left(self.orientation)
        if instruction == 'R':
            self.orientation = rotate_right(self.orientation)
        if instruction == 'F':
            (xDiff, yDiff) = move_forwards(self.orientation)
            self.x += xDiff
            self.y += yDiff


def rotate_left(orientation):
    next_orientation = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N',
    }
    return next_orientation[orientation]


def rotate_right(orientation):
    next_orientation = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N',
    }
    return next_orientation[orientation]


def move_forwards(orientation):
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }
    return moves[orientation]
