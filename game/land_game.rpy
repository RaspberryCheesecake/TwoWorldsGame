image front = "card-front-land.png"
image back = "card-back-land.png"


init:
    python:
        class Card(object):
            def __init__(self):
                self.selected = False
                self.back = "card-back-land.png"
                self.front = "card-front-land.png"


screen land_cards_screen(n_cards):

    grid n_cards 1 at truecenter:
        for card in card_list:

            button:
                background None

                if card.selected:
                    add card.front  # Show front
                else:
                    add card.back  # Show back

                action If( (card.selected ),  Return(False), Return(True))




label land_game:
    scene land_backdrop

    $ n_land_cards = 4
    $ card_list = [Card() for n in range(0, n_land_cards)]

    show screen land_cards_screen(n_land_cards)

    label land_game_loop:
        $ result = ui.interact()
        $ card_list[0].selected = result
        python:
            if all(c.selected for c in card_list):
                renpy.jump("solved_land_game")


        jump land_game_loop


label solved_land_game:
    "You solved the land game!"
    jump sea_land_selection
