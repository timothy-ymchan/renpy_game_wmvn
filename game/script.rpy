# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default player_name = "Player"

define player = Character("[player_name]")

# The game starts here.

label start:
    $script_load = ScriptLoader()

    label script_runner:
        $e = script_load.get_next_event()
        if e != '':
            $renpy.call(e)
            $renpy.block_rollback()
        else:
            $next_day = script_load.get_next_day()
            if(next_day == ''):
                jump end_runner
            $script_load.load_date(next_day)
        jump script_runner
    label end_runner:
    scene bg black with dissolve
    show text TITLE("END OF DAY 1") at center
    return
