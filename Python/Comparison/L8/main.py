def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if high_scoring_player_name == player_name:
        return "high"
    elif low_scoring_player_name == player_name:
        return "low"
    else :
        return "neither"
