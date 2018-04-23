# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image start_background = "pink-start-screen.png"
image sea_choice = "sea_choice.png"
image land_choice = "land_choice.png"
image sea_backdrop = "the-sea-backdrop.png"
image land_backdrop = "the-land-backdrop.png"

# Declare characters used by this game.
define s = Character('Sea Witch', color="#c8ffc8")

# The game starts here.
label start:

    $ land_solved = False
    $ sea_solved = False

    stop music

    scene start_background

    "Welcome."

    "Which world would you like to start in?"

    show sea_choice at left with dissolve
    
    "Sea?"

    show land_choice at right with dissolve

    "or Land?"

    label sea_land_selection:
        stop music
        scene start_background

        menu:

            "Sea":
                jump sea_chosen

            "Land":
                jump land_chosen

    label sea_chosen:
        scene sea_backdrop
        with fade
        play music "Lee_Rosevere_-_13_-_Decompress.mp3" loop
        "You chose the sea!"
        jump sea_game

        return

    label land_chosen:
        scene land_backdrop
        with fade
        play music "Lee_Rosevere_-_10_-_Puzzle_Pieces.mp3" loop
        jump land_game

        return

    return
