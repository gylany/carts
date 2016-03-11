# You can place the script of your game in this file.
#
## Initialize per game config options
#


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg = "nullbg.png"
image bg cartsbg = "cartsbg.png"
image dcl scav =  "dcl_scav.png"
image dcl fight =  "cartheader.png"
image jack base = "Keitaro.png"
image dan base = "Jun.png"
image hacker base = "Kenji.png"
image sandy base = "Fumie.png"
image cop base = "Ai.png"
image black = "#000"
image white ="#fff"


# Declare characters used by this game.

define d=Character('Dead Cat Louie',color="ffcc")

define da=Character('Dan',color="ffff")
define j=Character('Free Boots Jack',color="ffff")
define dan=Character('Pushing Dan',color="ffff")
define ha=Character('Hacker Kid',color="ffff")
define sa=Character('Sandy',color="ffff")
define cop=Character('Old Bill',color="ffff")

# The game starts here.
label start:

    scene black
    show dcl scav at top
    d"What are you looking at?"
    scene white with dissolve
    show dcl fight at top
    d"AAAAIIIEEEEEEE"
    scene cartsbg 
    with dissolve
    j"Haven't seen Dead Cat Louie around for a while"
    da"No, haven't seen him or his cart lately"
    j"I wonder...."
    scene white with dissolve
    show jack base at left
    j"I'm Jack"
    j"My buddy Dead Cat Louie was just found dead and messed up in the alley"
    j"I'd better see what's going on"
    show dan base at right
    da"Hey Jack"
    j"Hey Dan. Didja hear about Louie?"
    da"Yeah, that's messed up"

menu:
    "Let's go see Sandy at the Mission":
         jump miss

    "Let's go talk to the cops":
         jump cops

label miss:
    show sandy base
    sa"Hey guys"
    jump maingame
     
label cops:
    show cop base
    cop"What's your problem?"
    jump maingame
     
label maingame:
    show hacker base at top
    ha"I'm Hacker Kid"
    show sandy base at top
    sa"I'm Sandy"
    show cop base at top
    cop"I'm Old Bill"

    return


