from bowling.score import calculate_score
import pytest

@pytest.fixture(params= [
    {
        'score': '11111111111111111111',
        'expected': 20
    },
    {
        'score': '12121212121212121212',
        'expected': 30
    },
    {
        'score': '1-121212121212121212',
        'expected': 28
    },
    {
        'score': '1/121212121212121212',
        'expected': 38
    },
])
def scores_to_test(request):
    yield request.param


class TestBowling:
    def test_calculate_score(self, scores_to_test):
        assert calculate_score(scores_to_test['score']) == scores_to_test['expected']
