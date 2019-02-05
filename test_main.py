from main import Robot


def test_robot_obeys_turn_left_instruction():
    robot = Robot(1, 2, 'E')

    robot.perform_instruction('L')
    assert robot.orientation == 'N'

    robot.perform_instruction('L')
    assert robot.orientation == 'W'


def test_robot_obeys_turn_right_instruction():
    robot = Robot(1, 2, 'W')

    robot.perform_instruction('R')
    assert robot.orientation == 'N'

    robot.perform_instruction('R')
    assert robot.orientation == 'E'


def test_robot_obeys_forward_intruction():
    robot = Robot(1, 2, 'N')
    robot.perform_instruction('F')
    assert robot.x == 1
    assert robot.y == 3

    robot = Robot(1, 2, 'E')
    robot.perform_instruction('F')
    assert robot.x == 2
    assert robot.y == 2

    robot = Robot(1, 2, 'S')
    robot.perform_instruction('F')
    assert robot.x == 1
    assert robot.y == 1

    robot = Robot(1, 2, 'W')
    robot.perform_instruction('F')
    assert robot.x == 0
    assert robot.y == 2
