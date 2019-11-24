from bowling.score import calculate_score
import pytest

@pytest.fixture(params= [
    {
        'score': '1111111111',
        'expected': 10
    },
])
def scores_to_test(request):
    yield request.param


class TestBowling:
    def test_calculate_score(self, scores_to_test):
        assert calculate_score(scores_to_test['score']) == scores_to_test['expected']
