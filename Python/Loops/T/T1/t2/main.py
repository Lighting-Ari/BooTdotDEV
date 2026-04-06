def get_final_score(player_name, base_score, bonus_score=0):
    score = base_score + bonus_score
    return score , f"{player_name} scored {score} points"
