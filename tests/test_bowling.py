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
    {
        'score': 'X121212121212121212',
        'expected': 40
    },
    {
        'score': '1212121212121212121/5',
        'expected': 42
    },
    {
        'score': '121212121212121212X45',
        'expected': 46
    },
    {
        'score': '121212121212121212XX5',
        'expected': 52
    },
    {
        'score': '121212121212121212XXX',
        'expected': 57
    },
    {
        'score': 'XXXXXXXXXXXX',
        'expected': 300
    },
    {
        'score': '9-9-9-9-9-9-9-9-9-9-',
        'expected': 90
    },
    {
        'score': '9/9/9/9/9/9/9/9/9/9/9',
        'expected': 190
    },
])
def scores_to_test(request):
    yield request.param


class TestBowling:
    def test_calculate_score(self, scores_to_test):
        assert calculate_score(scores_to_test['score']) == scores_to_test['expected']
