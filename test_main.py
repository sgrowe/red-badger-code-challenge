import pytest
from main import Robot, Map, parse_robots_and_instructions, run_robots


@pytest.fixture
def default_map():
    return Map(10, 10)


def test_robot_obeys_turn_left_instruction(default_map):
    robot = Robot(1, 2, 'E', default_map)

    robot.perform_instruction('L')
    assert robot.orientation == 'N'

    robot.perform_instruction('L')
    assert robot.orientation == 'W'


def test_robot_obeys_turn_right_instruction(default_map):
    robot = Robot(1, 2, 'W', default_map)

    robot.perform_instruction('R')
    assert robot.orientation == 'N'

    robot.perform_instruction('R')
    assert robot.orientation == 'E'


def test_robot_obeys_forward_intruction(default_map):
    robot = Robot(1, 2, 'N', default_map)
    robot.perform_instruction('F')
    assert robot.x == 1
    assert robot.y == 3

    robot = Robot(1, 2, 'E', default_map)
    robot.perform_instruction('F')
    assert robot.x == 2
    assert robot.y == 2

    robot = Robot(1, 2, 'S', default_map)
    robot.perform_instruction('F')
    assert robot.x == 1
    assert robot.y == 1

    robot = Robot(1, 2, 'W', default_map)
    robot.perform_instruction('F')
    assert robot.x == 0
    assert robot.y == 2


def test_robot_is_lost_if_it_moves_beyond_top_of_map(default_map):
    robot = Robot(10, 10, 'N', default_map)

    assert not robot.is_lost

    robot.perform_instruction('F')
    assert robot.x == 10
    assert robot.y == 11
    assert robot.is_lost


def test_robot_is_lost_if_it_moves_beyond_bottom_of_map(default_map):
    robot = Robot(0, 0, 'S', default_map)

    assert not robot.is_lost

    robot.perform_instruction('F')
    assert robot.x == 0
    assert robot.y == -1
    assert robot.is_lost


def test_robot_does_not_moves_out_of_bounds_if_there_is_a_scent_at_its_location():
    map = Map(10, 10)
    map.add_scent(10, 10)

    robot = Robot(10, 10, 'N', map)

    robot.perform_instruction('F')
    assert robot.x == 10
    assert robot.y == 10
    assert not robot.is_lost


def test_parse_robots_and_instructions_allows_whitespace_between_robots_data():
    input = '''5 3
1 1 E
RFRFRFRF

3 2 N
FRRFLLFFRRFLL

0 3 W
LLFFFLFLFL
'''
    robots_and_instructions = parse_robots_and_instructions(input)

    assert len(robots_and_instructions) == 3

    (robot, instructions) = robots_and_instructions[2]
    assert robot.x == 0
    assert robot.y == 3
    assert robot.orientation == 'W'
    assert instructions == 'LLFFFLFLFL'


def test_parse_robots_and_instructions_returns_correct_data():
    input = '''5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
'''
    robots_and_instructions = parse_robots_and_instructions(input)

    assert len(robots_and_instructions) == 3

    (robot, instructions) = robots_and_instructions[0]
    assert robot.map.xMax == 5
    assert robot.map.yMax == 3

    assert robot.x == 1
    assert robot.y == 1
    assert robot.orientation == 'E'
    assert instructions == 'RFRFRFRF'

    (robot, instructions) = robots_and_instructions[1]
    assert robot.x == 3
    assert robot.y == 2
    assert robot.orientation == 'N'
    assert instructions == 'FRRFLLFFRRFLL'

    (robot, instructions) = robots_and_instructions[2]
    assert robot.x == 0
    assert robot.y == 3
    assert robot.orientation == 'W'
    assert instructions == 'LLFFFLFLFL'


def test_format_status_outputs_robots_position(default_map):
    robot = Robot(2, 3, 'S', default_map)
    assert robot.format_status() == '2 3 S'


def test_format_status_indicates_if_robot_is_lost(default_map):
    robot = Robot(10, 3, 'E', default_map)
    robot.perform_instruction('F')
    assert robot.format_status() == '11 3 E LOST'


def test_run_program_produces_expected_output():
    input = '''5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
'''
    output = run_robots(input)
    assert output == '''1 1 E
3 3 N LOST
2 3 S
'''
