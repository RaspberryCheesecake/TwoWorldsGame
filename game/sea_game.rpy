
label sea_game:

    init python:
        timeout = 10.0

        def show_countdown(st, at):
            if st > timeout:
                return Text("0.0"), None
            d = Text("{:.1f}".format(timeout - st))
            return d, 0.1

    image countdown = DynamicDisplayable(show_countdown)

    show countdown at truecenter

    "Zomg, here is a new thing"


