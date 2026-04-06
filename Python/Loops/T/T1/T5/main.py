def build_reward_summary(wins, quests, bonus_points):
    win_points = wins * 5
    quest_points = quests * 2
    # bonus_points = win_points + quest_points + bonus_points
    
    total_points = win_points + quest_points + bonus_points
    return f"Win points: {win_points}\nQuest points: {quest_points}\nBonus points: {bonus_points}\nTotal points: {total_points}"