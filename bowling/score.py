def calculate_score(score_string):
    score = 0
    for pins in score_string:
        score += convert_pins(pins)
    return score


def convert_pins(pins):
    if pins.isdigit():
        return int(pins)

    if pins == '-':
        return 0;
