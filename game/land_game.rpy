
screen land_cards_screen(n_cards, n_rows):

    grid n_cards n_rows at truecenter:
        for card in card_list:

            button:
                background None

                if card.face_up:
                    add card.front  # Show front
                else:
                    # text card.coord_text  # for debugging
                    add card.back  # Show back

                action If( (card.selected),  Return((False, card.number)), Return((True, card.number)) )



label land_game:
    scene land_backdrop

    python:
        if land_solved == True:
            renpy.jump("solved_land_game")

    "You chose the land!"

    $ n_rows = 4
    $ n_cards_per_row = 4
    $ card_list = [Card() for n in range(0, n_cards_per_row * n_rows)]

    python:
        for i, card in enumerate(card_list):
            card.number = i  # Give each card a unique label
            card.coords = [i % n_cards_per_row, i // n_cards_per_row]

    show screen land_cards_screen(n_cards_per_row, n_rows)

    label land_game_loop:
        python:

            result, n = ui.interact()

            card_list[n].selected = result

            x_selected, y_selected = card_list[n].coords
            
            for card in card_list:
                if abs(card.coords[0] - x_selected) == 1 and card.coords[1] == y_selected:
                    card.face_up = not card.face_up
                if card.coords[0] == x_selected and abs(card.coords[1] - y_selected) == 1:
                    card.face_up = not card.face_up
                if card.coords[0] == x_selected and card.coords[1] == y_selected:
                    card.face_up = not result

            if all(c.face_up for c in card_list):
                renpy.jump("solved_land_game")

        jump land_game_loop


label solved_land_game:
    "You solved the land puzzle!"
    hide screen land_cards_screen
    $ land_solved = True

    jump sea_land_selection
