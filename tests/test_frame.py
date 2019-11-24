import pytest

from bowling.score import Frame


class TestFrame:
    def test_frame(self):
        frame = Frame()
        frame.calculate_frame('11')
        assert frame.score == 2
