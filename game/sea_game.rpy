image front = "card-front-sea.png"
image back = "card-back-sea.png"

init:
    python:
        sea_flowers = ["card-front-sea-flower%d.png" % i for i in range(0, 7)]


screen sea_cards_screen(n_cards, n_rows):

    grid n_cards n_rows at truecenter:
        for card in sea_cards:

            button:
                background None

                if card.face_up:
                    add card.front  # Show front
                else:
                    add card.back  # Show back

                action If( (card.selected),  Return((False, card.number)), Return((True, card.number)) )



label sea_game:
    scene sea_backdrop

    python:
        if sea_solved == True:
            renpy.jump("solved_sea_game")

    "You chose the sea!"

    $ n_rows = 3
    $ n_cards_per_row = 4
    $ n_cards_tot = n_rows * n_cards_per_row
    $ sea_cards = [Card() for n in range(0, n_cards_tot)]

    python:
        n_pairs = n_cards_tot / 2
        pairs_list = range(0, n_pairs)

        for i in pairs_list:
            sea_cards[i].front = sea_flowers[i]
            sea_cards[-(i+1)].front = sea_flowers[i]

        renpy.random.shuffle(sea_cards)

        for i, card in enumerate(sea_cards):
            card.back = "card-back-sea.png"
            card.number = i  # Give each card a unique label
            card.coords = [i % n_cards_per_row, i // n_cards_per_row]

    show screen sea_cards_screen(n_cards_per_row, n_rows)

    label sea_game_loop:
        python:

            attempts = 0
            tries = 2
            fronts = []

            while attempts < tries:
            
                result, n = ui.interact()
                sea_cards[n].selected = result

                for card in sea_cards:
                    if card.selected:
                        card.face_up = True
                        fronts.append(card.front)

                attempts += 1
            
            # If the fronts of the cards selected match, they are paired OK

            if all(i == fronts[0] for i in fronts):
                for card in sea_cards:
                    if card.front ==  fronts[0]:
                        card.paired = True

            renpy.pause (1.0, hard = True)
            
            for card in sea_cards:
                 card.selected = False  # reset all selections
                 if not card.paired:
                     card.face_up = False  # Turn over any unpaired cards left

            if all(c.face_up for c in sea_cards):
                renpy.jump("solved_sea_game")

        jump sea_game_loop


label solved_sea_game:
    "You solved the sea puzzle!"
    hide screen sea_cards_screen
    $ sea_solved = True

    jump sea_land_selection
