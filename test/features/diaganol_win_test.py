import pytest
import sys
import os

sys.path.insert(0, os.path.abspath("lib"))

import connect4 as c4

def test_diaganol_win_for_player1_from_bottom_left_corner():
    output = []
    input_values = [1,2,2,3,4,3,3,4,4,5,4]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    c4.input = mock_input
    c4.print = lambda s : output.append(s)

    game = c4.Connect4()
    game.start()

    assert output.count("Player 1 wins") == 1
