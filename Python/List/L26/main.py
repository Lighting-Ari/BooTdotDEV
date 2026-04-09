def check_ingredient_match(recipe, inventory):
    required_ingredients_percent = 0
    missing_ingredients_name = []
    total_recipe = len(recipe)
    missing_count = 0
    character_have = 0
    for i in range(0,total_recipe):
        if recipe[i] not in inventory:
            missing_count += 1
            missing_ingredients_name.append(recipe[i])
        else :
            character_have += 1

    required_ingredients_percent = (character_have/total_recipe)*100

    return required_ingredients_percent, missing_ingredients_name
        
        
