# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[name]", kind=nvl)
define narrator = nvl_narrator
define menu = nvl_menu

screen simple_stats_screen:

    frame:
        xalign 0.75 yalign 0.05
        vbox:
            text "Свободное время" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value time_hp
                    range time_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[time_hp] / [time_max_hp]" size 16

    frame:
        xalign 0.23 yalign 0.05
        vbox:
            text "Семья" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value family_hp
                    range family_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[family_hp] / [family_max_hp]" size 16


    frame:
        xalign 0.48 yalign 0.05
        vbox:
            text "Карьера и деньги" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value work_hp
                    range work_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[work_hp] / [work_max_hp]" size 16




 


# The game starts here.

label start:

$ time_max_hp = 10
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

scene solid

show yana white black green:
        xalign 0.0
        yalign 0.5



    # These display lines of dialogue.

nvl_narrator "Привет! Я героиня этой истории, и тебе решать, какой я буду."
nvl clear

python:
    name = renpy.input("Как меня зовут?", length=32)
    name = name.strip()

    if not name:
         name = "Яна"

nvl_narrator "Итак, меня зовут [name]. И я..." ##выяснить, что это за фигня

menu:

    "Белокожая":

        nvl clear

        jump white

    "Чернокожая":

        nvl clear

        jump black

label white:
show yana white black green:
        xalign 0.0
        yalign 0.5

menu:

    nvl_narrator "Мои волосы..."

    "Светлые":

        nvl clear

        jump white_blonde

    "Темные":

        nvl clear

        jump white_black

    "Рыжие":

        nvl clear

        jump white_red  



label black:
nvl clear
show yana black black brown:
        xalign 0.0
        yalign 0.5

nvl_narrator "Ну, вроде так."
jump game


label white_blonde:
nvl clear
show yana white blonde green:
        xalign 0.0
        yalign 0.5

nvl_narrator "Ну, вроде так."
jump game


label white_black:
nvl clear
show yana white black green:
        xalign 0.0
        yalign 0.5

nvl_narrator "Ну, вроде так."
jump game

label white_red:
nvl clear
show yana white red green:
        xalign 0.0
        yalign 0.5

nvl_narrator "Ну, вроде так."
jump game

label game:
nvl clear
nvl_narrator "За свои 32 я успела много интересного: нашла работу, вышла замуж, родила ребенка. Муж у меня зайка."

nvl clear
nvl_narrator "Мне приходится многое совмещать: карьеру, семью, поддерживать отношения с людьми вокруг. Как все успеть?"

$ work_max_hp = 10
$ family_max_hp = 10
$ time_max_hp = 10
$ work_hp = 5
$ family_hp = 5
$ time_hp = 5



show screen simple_stats_screen

menu:

    nvl_narrator "Вот ребенок заболел. Что делать?"

    "Вызвать няню":
        nvl clear
        $ family_hp = max(0, family_hp-1)
        $ work_hp = min(work_max_hp, work_hp+1)
        "Няня закрутила роман с моим мужем. Зато на работе все хорошо!"

    "Отпроситься с работы":
        nvl clear
        $ family_hp = min(family_max_hp, family_hp+1)
        $ work_hp = max(0, work_hp-1)
        $ time_hp = max(0, time_hp-1)
        "Шеф отпустил, закатив глаза. Придется потом переработать, а то уволит..."


    "Попросить мужа приглядеть":
        nvl clear
        $ family_hp = min(family_max_hp, family_hp-1)
        $ work_hp = max(0, work_hp-1)
        $ time_hp = max(0, time_hp-1)
        "Муж не согласился. Пришлось сидеть с ним самой." 

nvl clear

menu:

    nvl_narrator "Знаешь, я когда-то мечтала быть художником. Родители настояли, чтобы пошла на юриста, а потом замужество, ребенок... В общем, не сложилось. Но сейчас думаю, а может, сменить работу? Хоть и потеряю в деньгах."

    "Бросить работу":
        nvl clear
        $ work_hp = max(0, work_hp-1)
        $ family_hp = max(0, family_hp-1)
        "Ушла с работы. Муж обрадовался и попросил готовить ему не только ужин, а еще и обед. Я сказала, что буду фрилансить. Обиделся."

    "Остаться на своей. Не до этого.":
        nvl clear
        $ work_hp = min(work_max_hp, work_hp+1)
        "Лучше буду усердно работать на своей работе."


    "Совмещать 2 работы, пока не начну зарабатывать на новой":
        nvl clear
        $ family_hp = max(0, family_hp-1)
        $ work_hp = min(work_max_hp, work_hp+1)
        $ time_hp = max(0, time_hp-2)
        "Сплю по 3 часа в сутки, муж с сыном меня не видят. Зато деньги в семью приношу!" 



    # This ends the game.

return

