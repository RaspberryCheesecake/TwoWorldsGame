image front = "card-front-land.png"
image back = "card-back-land.png"

init:
    python:

        flowers = ["card-front-land-flower%d.png" % i for i in range(1, 3)]

        class Card(object):
            def __init__(self):
                self.face_up = False
                self.number = 0
                self.coords = [0, 0]
                self.back = "card-back-land.png"
                self.front = flowers[0]

            @property
            def coord_text(self):
                return "{}, {}".format(self.coords[0], self.coords[1])


screen land_cards_screen(n_cards, n_rows):

    grid n_cards n_rows at truecenter:
        for card in card_list:

            button:
                background None

                if card.face_up:
                    add card.front  # Show front
                else:
                    text card.coord_text
                    # add card.back  # Show back

                action If( (card.face_up ),  Return((False, card.number)), Return((True, card.number)) )




label land_game:
    scene land_backdrop

    python:
        if land_solved == True:
            renpy.jump("solved_land_game")

    "You chose the land!"

    $ n_rows = 3
    $ n_cards_per_row = 4
    $ card_list = [Card() for n in range(0, n_cards_per_row * n_rows)]

    python:
        for i, card in enumerate(card_list):
            card.number = i  # Give each card a unique label
            card.coords = [i % n_cards_per_row, i // n_cards_per_row]

    show screen land_cards_screen(n_cards_per_row, n_rows)

    label land_game_loop:
        $ result, n = ui.interact()
        $ card_list[n].face_up = result
        python:

            if all(c.face_up for c in card_list):
                renpy.jump("solved_land_game")

        jump land_game_loop


label solved_land_game:
    "You solved the land puzzle!"
    hide screen land_cards_screen
    $ land_solved = True

    jump sea_land_selection
