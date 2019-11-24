import pytest

from bowling.score import Frame

@pytest.fixture(params=[
    {
        'frame': '11',
        'expected': 2
    },
])
def frames(request):
    yield request.param


class TestFrame:
    def test_frame(self, frames):
        frame = Frame()
        frame.calculate_frame(frames['frame'])
        assert frame.score == frames['expected']
