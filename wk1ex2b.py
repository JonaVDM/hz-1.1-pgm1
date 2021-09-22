import time


def adventure():
    """Runs one session of interactive fiction

    Well, it"s "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # zet deze waarde op 0.0 om te testen of snel te spelen,
    # ..of hoger voor meer dramatisch effect!
    delay = 1.0

    username = input("Hoe mogen we je noemen? ")

    intro = _intro(username, delay)
    ghost = False

    # This took me longer than I like to admit to make, so no comments (can't
    # be bothered). All required conditional statements are here though!

    if intro == "tafel":
        table = _goToTable(username, delay)
        if table == "quit":
            return
        elif table == "strawberry":
            ghost = True
        _goUpstairs(ghost)

    elif intro == "deur":
        door = _goThroughDoor(username, delay)
        if door == "quit":
            return
        elif door == "strawberry":
            ghost = True
        _goUpstairs(ghost)

    elif intro == "trap":
        _goUpstairs(ghost)

    else:
        _hallway()
        _goUpstairs(ghost)


def _goToTable(name, delay):
    table = _table()

    if table == "deur":
        return _goThroughDoor(name, delay)
    elif table == "trap":
        return ""
    else:
        _leaveTable(name)
        return "quit"


def _goThroughDoor(name, delay):
    door = _door(name, delay)

    if door == "aardbei":
        _strawberry()
        return "strawberry"
    else:
        _noStrawberry(door)
        return "quit"


def _goUpstairs(ghost):
    direction = _staircase(ghost)

    if direction == "links":
        _left()
    elif direction == "rechts":
        _right()


def _intro(name, delay):
    print(f"""

    Welkom terug {name}, na de laatste keer verslagen te zijn achter de deur
    besluit je terug te gaan. De heerlijke taarten in het complex zijn te
    verleidend om niet te gaan. Maar wanneer je binnenkomt merk je, het is
    anders! Naast dat de hal waardoor je heenliep laatste keer er anders
    uitziet lijken er nieuwe kamers en zij gangen te zijn, maar er zijn ook
    een aantal kamers weg.

    """)

    time.sleep(delay)

    print("""

    Na een tijdje kom je de kamer weer tegen met de tafel en de deur. Ook al
    lijkt de tafel wat leger te zijn het ziet eruit alsof er nog steeds iets
    oplicht. Je kan er alleen niet uitkomen wat het is, is het taart? De deur
    lijkt nu wat wijder openstaan. Je bent nieuwsgierig maar herinnerd ook een
    trap in de gang, misschien ligt daar nu de taart. De gang was nog niet aan
    het einde, je kan ook doorlopen. Misschien is er nog wat verderop.

    """)

    return input("Waar ge je heen? [tafel/deur/trap/gang] ")


def _table():
    print("""

    Je komt bij de tafel aan. Maar je er bent zie je dat er helemaal geen taart
    ligt, het is het tafelkleed en een slapende rat! Je staat nu alweer voor een
    keuze, ga je naar de keuken of toch naar de trap. Na even er over nagedacht
    te denken hoor je de rat wakker worden en komt er een gedachte op. Wat als
    de ratten alle taart al hebben opgegeten? En zit nu te twijfelen om met lege
    handen terug naar de ingang te gaan.

    """)

    return input("[deur/trap/uitgang] ")


def _leaveTable(name):
    print(f"""

    Spijtig om je al te zien gaan, maar die rat zag er inderdaad eng uit. Tot
    de volgende keer {name}.

    """)


def _door(name, delay):
    print("""

    Je doet de deur langzaam open en loopt naar binn_goThroughDooren, maar wanneer je
    binnenkomt is er… niets! Geen wijze dames en heren, geen dozen en zover je
    kan zien ook geen kruimels van de taart. Je denkt bij jezelf dat je beter
    terug kan naar de trap, maar zodra je begint te lopen naar de deur slaat
    die dicht! Je loopt er wat sneller naar toe maar je merkt dat hij dicht zit.

    """)

    time.sleep(delay)

    print(f"""

    Opeens hoor je een stem. “Welkom {name}, om de taart te kunnen bemachtigen
    moet je eerst een vraag goed beantwoorden: Wat is mijn favoriete smaak
    taart?” Je schrikt je bijna dood! Waar kwam deze stem vandaan? Van wie is
    deze stem? Misschien waren de geruchten waar en is er inderdaad een spook
    in het complex. Maar wat zal zijn favoriete smaak zijn, en hoe kan hij dat
    eten. Je denkt terug naar de gang en kan je vaag herinneren dat er een
    figuur op elke deur zat. Maar wat was dat ook al weer. Je denkt hard en
    komt erop dat het een ijshoorntje met een kroontje was. Maar wat heb je
    daar nou aan.

    """)

    return input("De stem klinkt opnieuw: “Wat is mijn favoriete smaak taart” ")


def _strawberry():
    print("""

    De stem knikt opnieuw: “Aardbei is inderdaad mijn favoriete smaak, Je kan
    de taarten vinden bij de trap omhoog”. En de deur gaat open, je loopt er
    snel doorheen naar de trap toe.

    """)


def _noStrawberry(cake):
    print(f"""

    Je hoort de stem “helaas {cake} is niet mijn favoriete”. De kamer word donker
    totdat je niets kunt zien. Zodra het licht weer zichtbaar is voel je de
    wind, je staat buiten voor de deur. Het avontuur was voor vandaag weer
    over, zonder taart.

    """)


def _hallway():
    print("""

    Je loopt de gang door en ziet opnieuw een trap, het lijkt precies op de
    vorige. Na nog even doorgelopen kwam je bij de dezelfde kamer uit met de
    tafel en de deur. Je besluit door te lopen weer naar de trap toe om daar
    omhoog te gaan.

    """)


def _staircase(ghost):
    extra = ""

    if ghost:
        extra = "Je merkt nu dat het inderdaad aardbeien zijn op de deuren."

    print(f"""

    Je loopt de trap op. Boven op de trap zie je twee deuren, aan de rechter en
    aan de linker kant. {extra}

    """)

    return input("Maar je moet nu een keuze maken. welke deur [rechts/links]? ")


def _right():
    print("""
    Je loopt door de deur heen en word begroet met alle taarten die je maar
    kunt bedenken. Je eet en eet maar door. Het avontuur was een succes.
    """)


def _left():
    print("""
    Je loopt de kamer in maar ziet geen taarten meer, alleen maar lege dozen en
    een groep raten. Je loopt nog snel naar de rechter deur maar die is nu op
    slot. Teleurstellend loop je terug naar de ingang zonder taart.
    """)
