SELECT_ALL = 'SELECT character_id, name FROM charactercreator_character;'  # end with ;


AVG_ITEM_WEIGHT_PER_CHAR = '''
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON cc_inv.item_id = ai.item_id
    GROUP BY cc_char.character_id'''
