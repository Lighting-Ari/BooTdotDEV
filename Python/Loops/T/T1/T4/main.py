guild_name = "Night Owls"


def get_badge_level(points):
    badge = "None"
    if points < 100 :
        badge = "Bronze"
    elif points < 500 :
        badge = "Silver"
    else :
        badge = "Gold"
    return badge

def build_member_card(name, points):
    return f"{guild_name} | {name} | {get_badge_level(points)}"


def build_trial_card(name, points):
    return f"Trial Guild | {name} | {get_badge_level(points)}"
