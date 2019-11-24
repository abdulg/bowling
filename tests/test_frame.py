import pytest

from bowling.score import Frame

@pytest.fixture(params=[
    {
        'frame': '11',
        'expected': 2
    },
    {
        'frame': '12',
        'expected': 3
    },
    {
        'frame': '1/3',
        'expected': 13
    },
    {
        'frame': 'X13',
        'expected': 14
    },
])
def frames(request):
    yield request.param


class TestFrame:
    def test_frame(self, frames):
        frame = Frame()
        frame.calculate_frame(frames['frame'])
        assert frame.score == frames['expected']
