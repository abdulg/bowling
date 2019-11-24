import pytest
from bowling.score import calculate_score

class TestBowling:
    def test_calculate_score(self):
        assert calculate_score('1111111111') == 10
