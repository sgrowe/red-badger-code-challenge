import sys


class Map:
    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax
        self.scents = {}

    def add_scent(self, x, y):
        self.scents[(x, y)] = True

    def has_scent_at(self, x, y):
        return self.scents.get((x, y), False)

    def position_out_of_bounds(self, x, y):
        xOutOfBounds = x < 0 or x > self.xMax
        yOutOfBounds = y < 0 or y > self.yMax

        return xOutOfBounds or yOutOfBounds


class Robot:
    def __init__(self, x, y, orientation, map):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.map = map
        self.is_lost = False

    def perform_instruction(self, instruction):
        if instruction == 'L':
            self.orientation = rotate_left(self.orientation)
        if instruction == 'R':
            self.orientation = rotate_right(self.orientation)
        if instruction == 'F':
            self.move_forwards()

    def move_forwards(self):
        (xDiff, yDiff) = step_forwards(self.orientation)
        newX = self.x + xDiff
        newY = self.y + yDiff

        if self.map.position_out_of_bounds(newX, newY):
            if self.map.has_scent_at(self.x, self.y):
                # ignore instruction
                return
            else:
                self.map.add_scent(self.x, self.y)
                self.is_lost = True

        self.x = newX
        self.y = newY

    def format_status(self):
        status = f'{self.x} {self.y} {self.orientation}'
        if self.is_lost:
            status += ' LOST'
        return status


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


def step_forwards(orientation):
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }
    return moves[orientation]


def parse_robots_and_instructions(input):
    lines = input.strip().splitlines()
    map = parse_map(lines[0])

    robots_and_instructions = []

    i = 1
    while i < len(lines):
        # skip any blank lines
        if not lines[i]:
            i += 1
            continue

        robot = parse_robot(lines[i], map)
        instructions = lines[i + 1]
        robots_and_instructions.append((robot, instructions))
        i += 2

    return robots_and_instructions


def parse_map(line):
    xMax, yMax = line.split()
    return Map(int(xMax), int(yMax))


def parse_robot(line, map):
    xMax, yMax, orientation = line.split()
    return Robot(int(xMax), int(yMax), orientation, map)


def run_robots(input):
    output_lines = []
    for robot, instructions in parse_robots_and_instructions(input):
        for instruction in instructions:
            robot.perform_instruction(instruction)
        output_lines.append(robot.format_status())

    output_lines.append('')  # Add a trailing new line
    return '\n'.join(output_lines)


if __name__ == '__main__':
    input_filename = sys.argv[1]
    with open(input_filename) as f:
        output = run_robots(f.read())
    print(output, end='')
