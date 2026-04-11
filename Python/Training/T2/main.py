def build_number_ladder(height):
    ladder = ""


    for row in range(1, height +1):
        for number in range(1, row + 1):
            ladder += str(number)
        if row < height :
            ladder += "\n"

    return ladder

