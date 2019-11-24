def calculate_score(score_string):
    score = 0
    for pins in score_string:
        score += int(pins)
    return score
