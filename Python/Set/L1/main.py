
def remove_duplicates(spells):
    return list(set(spells))

def remove_duplicates(spells):
    track_spell = set()
    unique_spell = []
    for spell in spells:
        track_spell.add(spell)
        
    for spell in track_spell:
        unique_spell.append(spell)

    return unique_spell