def can_cast_spell(mana, spell_cost, level, required_level, is_silenced):
    return mana >= spell_cost and level >= required_level and not is_silenced 
