# You can place the script of your game in this file.
#
## Initialize per game config options
#


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg = "nullbg.png"
image bg cartsbg = "cartsbg.png"
image catstreet = "catstreet.png"
image meeting = "meeting.png"
image homelessguyalley = "homelessguyalley.png"
image sad-woman = "sad-woman.png"
image shopping-cart-bg = "shopping-cart-bg.png"
image shopping-cart-attack = "shopping-cart-attack.png"
image dcl scav =  "dcl_scav.png"
image dcl fight =  "cartheader.png"
image jack base = "Keitaro.png"
image dan base = "Jun.png"
image hacker base = "hacker.png"
image sandy base = "Fumie.png"
image cop base = "Ai.png"
image black = "#000"
image white ="#fff"


# Declare characters used by this game.

define d=Character('Dead Cat Louie',color="ffcc")

define j=Character('Free Boots Jack',color="ffff")
define da=Character('Pushing Dan',color="ffff")
define ha=Character('Hacker Kid',color="ffff")
define sa=Character('Sandy',color="ffff")
define cop=Character('Old Bill',color="ffff")

# The game starts here.
label start:
menu:
    "Jump to current":
         jump current

    "Jump intro":
         jump intro
         
label intro:

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
    scene white with dissolve
    show jack base at left
    show dan base at right
    show sandy base at center
    sa"Hey guys"
    j"Did you hear about Louie?"
    da"Someone killed him when he was scavenging!"
    sa"Yes, I heard. I'm so sorry."
    j"We think something weird is going on"
    sa"Hmmm....come and talk to me over here"
    scene white with dissolve
    show sandy base at center
    sa"I think I better talk to the hacker"
    jump hackersandy
    
label hackersandy:
    scene white with dissolve
    show sandy base at right
    show hacker base at left
    sa"Something strange is killing the homeless"
    ha"Ok, strange is my thing"
    jump hackercart
    
label hackercart:
    scene white with dissolve
    show hacker base at left
    
    ha"My magic plot device shows a weird disturbance in the farce"
    ha"I'd better check it out"
    scene catstreet with dissolve
    show hacker base at left 
    ha"Not you pussycat"
    
    
    scene homelessguyalley with dissolve
    show hacker base at left
    ha"Just the usual misery.."

    
    scene sad-woman with dissolve
    show hacker base at left
    ha"Have to tell Sandy about her.."
    
    scene shopping-cart-bg with dissolve
    show hacker base at left
    ha"Something is registering, I must be very close..."
    show shopping-cart-attack at right
    ha"What the fuck!!"
    scene white with dissolve
    show dcl fight at top
    ha"Whoa! If I hadn't zapped that shopping cart with my MPD it would have killed me. I better talk to Sandy"
    jump council
    
label cops:
    show cop base
    cop"What's your problem?"
    da"Someone killed Dead Cat Louie. What's up with that?"
    j"Yeah!"
    cop"I know about that. What have you heard?"
    da"Nuthin'. That's what's strange"
    cop"Come back when you know something."
    jump copcart
    
label copcart:

    scene white with dissolve
    show cop base at left
    cop"I don't like what's going on here...let's go see"
    
    scene catstreet with dissolve
    show cop base at left 
    cop"Looks quiet.."
    
    
    scene homelessguyalley with dissolve
    show cop base at left
    cop"Just the usual misery.."

    
    scene sad-woman with dissolve
    show cop base at left
    cop"Have to tell Sandy about her.."
    
    scene shopping-cart-bg with dissolve
    show cop base at left
    cop"Nothing. Well, I'm going to get some more people on this. Nothing's going to kill people on my watch.."
    show shopping-cart-attack at right
    cop"What the hell!"
    scene white with dissolve
    show dcl fight at top
    cop"I can't believe it. If I hadn't fought that shopping cart off it would have killed me. I better talk to Sandy"
    show cop base at left   
    jump council
label council:
label current:
    scene meeting with dissolve
 
    show sandy base at left
    sa"What did you find out?"
    show hacker base at right
    ha"Shopping carts attacked me and I barely escaped with my life"
    scene meeting
    show sandy base at left
    show cop base at right
    cop"Shopping carts attacked me and I barely escaped with my life"
    scene cartsbg with dissolve
    show sandy base at left
    show jack base at right
    j"Those fuckin' carts nearly killed me last night"
    scene cartsbg
    show sandy base at left
    show dan base at right
    da"Me too!"
    return


