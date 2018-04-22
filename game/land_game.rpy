image front = "card-front-land.png"
image back = "card-back-land.png"


init:
    python:
        class Card(object):
            def __init__(self):
                self.selected = False


screen land_cards_screen:

    grid 1 1:
        for card in card_list:

            button:
                background None

                if card.selected:
                    add "card-front-land.png"  # Display card front
                else:
                    add "card-back-land.png"  # Display card back

                action If( (card.selected ),  Return(False), Return(True))




label land_game:
    scene land_backdrop

    $ n_land_cards = 4
    $ card_list = [Card()]

    show screen land_cards_screen

    label land_game_loop:
        $ result = ui.interact()
        $ card_list[0].selected = result

        jump land_game_loop

    return
