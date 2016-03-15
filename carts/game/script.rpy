#
## Carts! by Rob Sutherland - Released under Creative Commons 
#

#
## Initialize per game config options
#


# Declare images below this line, using the image statement.

#
## Backgrounds
#
image black = "#000"
image white ="#fff"
image bg = "nullbg.png"
image bg cartsbg = "cartsbg.png"
image catstreet = "catstreet.png"
image meeting = "meeting.png"
image homelessguyalley = "homelessguyalley.png"
image sadwoman = "sad-woman.png"
image shopping-cart-bg = "shopping-cart-bg.png"
#
## NPC
#
image shopping-cart-attack = "shopping-cart-attack.png"
image dcl scav =  "dcl_scav.png"
image dcl fight =  "cartheader.png"
#
## Characters
#
image jack base = "Keitaro.png"
image dan base = "Jun.png"
image hacker base = "hacker.png"
image sandy base = "Fumie.png"
image cop base = "Ai.png"
image cartmaster base = "cartmaster.png"



# Declare characters used by this game.

define d=Character('Dead Cat Louie',color="ffcc")

define j=Character('Free Boots Jack',color="ffff")
define da=Character('Pushing Dan',color="ffff")
define ha=Character('Hacker Kid',color="ffff")
define sa=Character('Sandy',color="ffff")
define cop=Character('Old Bill',color="ffff")
define cm=Character('Cartmaster',color="fff")
#
## Start
#

label start:
#debug
menu:
    "Jump to current":
         jump current

    "Jump intro":
         jump intro

#
## Intro
#

label intro:

    scene black
    show dcl scav at top
    d"What are you looking at?"
    scene white with dissolve
    show dcl fight at top
    d"AAAAIIIEEEEEEE"
#
## Jack & Dan 
#
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
#
## Cops / Sandy Menu
#
menu:
    "Let's go see Sandy at the Mission":
         jump miss

    "Let's go talk to the cops":
         jump cops
#
## Mission Intro
#
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
#
## Hacker Intro
#    
label hackersandy:
    scene white with dissolve
    show sandy base at right
    show hacker base at left
    sa"Something strange is killing the homeless"
    ha"Ok, strange is my thing"
    jump hackercart
#
## Hacker Cart Fight
#    
label hackercart:
    scene white with dissolve
    show hacker base at left
    
    ha"My magic plot device shows a weird disturbance in the farce"
    ha"I'd better check it out"
#
## City Tour
#
    scene catstreet with dissolve
    show hacker base at left 
    ha"Not you pussycat"
    
    
    scene homelessguyalley with dissolve
    show hacker base at left
    ha"Just the usual misery.."

    
    scene sadwoman with dissolve
    show hacker base at left
    ha"Have to tell Sandy about her.."
#
## Fight
#   
    scene shopping-cart-bg with dissolve
    show hacker base at left
    ha"Something is registering, I must be very close..."
    show shopping-cart-attack at right
    ha"What the fuck!!"
    scene white with dissolve
    show dcl fight at top
    ha"Whoa! If I hadn't zapped that shopping cart with my MPD it would have killed me. I better talk to Sandy"
    jump council
#
## Cop Intro
#    
label cops:
    show cop base
    cop"What's your problem?"
    da"Someone killed Dead Cat Louie. What's up with that?"
    j"Yeah!"
    cop"I know about that. What have you heard?"
    da"Nuthin'. That's what's strange"
    cop"Come back when you know something."
    jump copcart
#
## City Tour
#   
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
#
## Fight
#
    show shopping-cart-attack at right
    cop"What the hell!"
    scene white with dissolve
    show dcl fight at top
    cop"I can't believe it. If I hadn't fought that shopping cart off it would have killed me. I better talk to Sandy"
    show cop base at left   
    jump council
#
## Council of War
#
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
    scene meeting with dissolve
    show sandy base at left
    sa"What can we do? Organize and fight!"
    show hacker base at right
    ha"The bad carts have a mysterious plot device attached that's controlled from somewhere in the swamp"
    scene meeting
    show sandy base at left
    show cop base at right
    cop"We can go there and capture the source when we locate it."
    sa"Can you mobilize the police?"
    cop"No. The ones that don't think I'm crazy think it's a good thing they're killing the homeless. We're on our own."
    scene meeting
    show sandy base at left
    show dan base at right
    da"So what's new. Let's go kick some cart!"
    scene meeting
    show sandy base at left
    show jack base at right
    j"Yeah!"
    scene meeting
    show sandy base at left
    show hacker base at right
    sa"Can you help, Hacker?"
    
    ha"I can make a few magic plot devices to give us some warning. But we still have to fight"
    scene meeting
    show sandy base at left
    show dan base at right
    da"I know where to find a few tools."
    scene meeting
    show sandy base at left
    show jack base at right
    j"We can let people know."
    scene meeting
    show sandy base at left
    show cop base at right
    cop"Just where are you *finding* these tools...ah screw it. Meet me at the park later and we'll start hunting"
    sa"OK"
#
## Cart Master Intro
#    
    scene meeting
    show sandy base at left
    sa"And so the defense began. We fought them in the alleys!. We fought them in the parking lots! We never surrendered!"
    sa"But it was hard. New hostile carts appeared as the Hacker searched for the source. People kept dying and the authorities kept ignoring it."
    sa"Then the the Hacker discovered....the Cartmaster"
    scene black
    show sandy base at left
    show cartmaster base at right
    sa"Doesn't look that scary does she?"
    sa"But behind that innocent face lurks the soul of a genocidal war criminal...."
    sa"And so we prepare for our final conflict"
    return


