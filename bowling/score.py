def calculate_score(score_string):
    score = 0
    frames = []
    while len(score_string) > 0:
        frame = Frame()
        score_string = frame.calculate_frame(score_string)
        frames.append(frame)

    score = 0
    for frame in frames:
        score += frame.score
    return score


class Frame():
    def __init__(self):
        self.pins1 = 0
        self.pins2 = 0

    @property
    def score(self):
        return self.pins1 + self.pins2

    def calculate_frame(self, score_string):
        self.pins1 = self.convert_pins(score_string)
        self.pins2 = self.convert_pins(score_string[1:])
        return score_string[2:]

    def convert_pins(self, score_string):
        if score_string[0].isdigit():
            return int(score_string[0])

        if score_string[0] == '-':
            return 0

        if score_string[0] == '/':
            partial = 10 - self.pins1
            if score_string[1].isdigit():
                return partial + int(score_string[1])

            if score_string[1] == '-':
                return partial
