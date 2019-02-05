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
