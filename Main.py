import sys, pygame
import pygame.locals

pygame.init()
WIDTH = 1500
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fred")
clock = pygame.time.Clock()

# Background Image
backgroundbase = pygame.image.load("base3.png")
backgroundbase = pygame.transform.scale(backgroundbase, (2400, 10))
backBx = -1000

background1 = pygame.image.load("platformer1.png")
background1 = pygame.transform.scale(background1, (300, 30))
back1x = 500

background2 = pygame.image.load("platformer1.png")
background2 = pygame.transform.scale(background2, (200, 30))
back2x = 300

background3 = pygame.image.load("platformer1.png")
background3 = pygame.transform.scale(background3, (200, 30))
back3x = 0

background4 = pygame.image.load("platformer1.png")
background4 = pygame.transform.scale(background4, (400, 30))
back4x = 580

background5 = pygame.image.load("platformer1.png")
background5 = pygame.transform.scale(background5, (200, 30))
back5x = 1200

background6 = pygame.image.load("platformer1.png")
background6 = pygame.transform.scale(background6, (200, 30))
back6x = 1600

background7 = pygame.image.load("platformer1.png")
background7 = pygame.transform.scale(background7, (40, 30))
back7x = 2020

background8 = pygame.image.load("platformer1.png")
background8 = pygame.transform.scale(background8, (200, 30))
back8x = 1870

background9 = pygame.image.load("platformer1.png")
background9 = pygame.transform.scale(background9, (200, 30))
back9x = 2360

background10 = pygame.image.load("platformer1.png")
background10 = pygame.transform.scale(background10, (40, 40))
back10x = 2520

background11 = pygame.image.load("platformer1.png")
background11 = pygame.transform.scale(background11, (200, 30))
back11x = 2680

background12 = pygame.image.load("platformer1.png")
background12 = pygame.transform.scale(background12, (200, 30))
back12x = 2520

background13 = pygame.image.load("platform2.png")
background13 = pygame.transform.scale(background13, (200, 30))
back13x = 3000

background14 = pygame.image.load("platform2.png")
background14 = pygame.transform.scale(background14, (30, 430))
back14x = 3200

background15 = pygame.image.load("platform2.png")
background15 = pygame.transform.scale(background15, (30, 290))
back15x = 3340

background16 = pygame.image.load("platformer1.png")
background16 = pygame.transform.scale(background16, (600, 30))
back16x = 3320

background17 = pygame.image.load("capture.png")
background17 = pygame.transform.scale(background17, (105, 170))
back17x = 3740

backxs = [backBx, back1x, back2x, back3x, back4x, back5x, back6x, back7x, back8x, back9x, back10x, back11x, back12x,
          back13x, back14x, back15x, back16x, back17x]
ogbackxs = [-1000, 500, 300, 0, 580, 1200, 1600, 2020, 1870, 2360, 2520, 2680, 2520, 3000, 3200, 3340, 3320, 3740]

# Start screen variables
Titlefont = pygame.font.Font("Font.ttf", 150)
gamefont = pygame.font.Font("Font.ttf", 30)

Title = Titlefont.render("F.R.E.D.", True, (255, 255, 255))
textquit = gamefont.render("QUIT", True, (255, 255, 255))
textstart = gamefont.render("START", True, (255, 255, 255))
textcredits = gamefont.render("CREDITS", True, (255, 255, 255))
infos = gamefont.render("i", True, (255, 255, 255))

# Player variables
playerx = 250
playery = 400
PLAYERW = 40
PLAYERH = 70
playerRect = pygame.Rect(playerx, playery, PLAYERW, PLAYERH)
# gravity = 0
jumping = True
xvelocity = 10
yvelocity = 10
gravity = 2

# Creating Villains (all have same H and W)
# Add movement
villain1x = 700
villain1y = 520
VILLAINW = 40
VILLAINH = 40
# villain1Rect = pygame.Rect(plat1Rect.left +200, plat1Rect.top-40, VILLAINW, VILLAINH)
villain1Rect = pygame.Rect(villain1x, villain1y, VILLAINW, VILLAINH)

villain2x = 700
villain2y = 220
villain2Rect = pygame.Rect(villain2x, villain2y, VILLAINW, VILLAINH)

villain3x = 1760
villain3y = 460
villain3Rect = pygame.Rect(villain3x, villain3y, VILLAINW, VILLAINH)

villain4x = 2030
villain4y = 230
villain4Rect = pygame.Rect(villain4x, villain4y, VILLAINW, VILLAINH)

bossx = 1000
bossy = -490
BOSSW = 100
BOSSH = 100
bossRect = pygame.Rect(bossx, bossy, BOSSW, BOSSH)

bossJump = True
vxvelocity = 10
vxvelocity2 = 10
vyvelocity = 20
direction = 1
direction2 = 1

villainxs = [villain1x, villain2x, villain3x, villain4x, bossx]
villainys = [villain1y, villain2y, villain3x, villain4x, bossy]
villainrects = [villain1Rect, villain2Rect, villain3Rect, villain4Rect, bossRect]

dist = playerx - villain1Rect.left
dist2 = playerx - villain3Rect.left
bossDist = playerx - bossRect.left

bulletrdy1 = False
bulletair1 = False
bullet = pygame.Rect(0, 0, 10, 10)
bulletair2 = False
bulletrdy2 = False
bullet2 = pygame.Rect(10, 10, 10, 10)

bossBulletrdy = False
bossBulletair = False
bossBullet = pygame.Rect(10, 10, 10, 10)

playerBulletrdy = False
playerBulletair = False
playerBullet = pygame.Rect(10, 10, 10, 10)

counter = 0

hlthx = 0
hlthbar = pygame.Rect(0, 0, 10, 10)

##################################################################

# Defining obstacles
# 0th platform (aka floor)
PLAT0W = 2400
PLAT0H = 100
plat0x = -500
plat0y = 590
plat0Rect = pygame.Rect(plat0x, plat0y, PLAT0W, PLAT0H)

# 1st Platform
PLAT1W = 300
PLAT1H = 30
plat1x = 500
plat1y = 560
plat1Rect = pygame.Rect(plat1x, plat1y, PLAT1W, PLAT1H)

# 2nd Platform
PLAT2W = 200
PLAT2H = 30
plat2x = 300
plat2y = 400
plat2Rect = pygame.Rect(plat2x, plat2y, PLAT2W, PLAT2H)

# 3rd Platform
PLAT3W = 200
PLAT3H = 30
plat3x = 0
plat3y = 560
plat3Rect = pygame.Rect(plat3x, plat3y, PLAT3W, PLAT3H)

# 4th Platform
PLAT4W = 400
PLAT4H = 30
plat4x = 580
plat4y = 260
plat4Rect = pygame.Rect(plat4x, plat4y, PLAT4W, PLAT4H)

# 5th Platform
PLAT5W = 200
PLAT5H = 30
plat5x = 1200
plat5y = 500
plat5Rect = pygame.Rect(plat5x, plat5y, PLAT5W, PLAT5H)

# 6th Platform
PLAT6W = 200
PLAT6H = 30
plat6x = 1600
plat6y = 500
plat6Rect = pygame.Rect(plat6x, plat6y, PLAT6W, PLAT6H)

# 7th Platform
PLAT7W = 40
PLAT7H = 30
plat7x = 2020
plat7y = 380
plat7Rect = pygame.Rect(plat7x, plat7y, PLAT7W, PLAT7H)

# 8th Platform
PLAT8W = 200
PLAT8H = 30
plat8x = 1870
plat8y = 270
plat8Rect = pygame.Rect(plat8x, plat8y, PLAT8W, PLAT8H)

# 9th Platform
PLAT9W = 200
PLAT9H = 30
plat9x = 2360
plat9y = 330
plat9Rect = pygame.Rect(plat9x, plat9y, PLAT9W, PLAT9H)

# 10th Platform (Box)
PLAT10W = 40
PLAT10H = 40
plat10x = 2520
plat10y = 290
plat10Rect = pygame.Rect(plat10x, plat10y, PLAT10W, PLAT10H)

# 11th Platform
PLAT11W = 200
PLAT11H = 30
plat11x = 2680
plat11y = 250
plat11Rect = pygame.Rect(plat11x, plat11y, PLAT11W, PLAT11H)

# 12th Platform
PLAT12W = 200
PLAT12H = 30
plat12x = 2520
plat12y = 40
plat12Rect = pygame.Rect(plat12x, plat12y, PLAT12W, PLAT12H)

# 13th Platform
PLAT13W = 200
PLAT13H = 30
plat13x = 3000
plat13y = 170
plat13Rect = pygame.Rect(plat13x, plat13y, PLAT13W, PLAT13H)

# 14th Platform (Pillar1)
PLAT14W = 30
PLAT14H = 430
plat14x = 3200
plat14y = 170
plat14Rect = pygame.Rect(plat14x, plat14y, PLAT14W, PLAT14H)

# 15th Platform (Pillar2)
PLAT15W = 30
PLAT15H = 290
plat15x = 3340
plat15y = 170
plat15Rect = pygame.Rect(plat15x, plat15y, PLAT15W, PLAT15H)

# 16th Platform
PLAT16W = 600
PLAT16H = 30
plat16x = 3320
plat16y = 580
plat16Rect = pygame.Rect(plat16x, plat16y, PLAT16W, PLAT16H)

# Boss Platforms ( other than ground cuz same for both phases )
BOSSPLAT1W = 500
BOSSPLAT1H = 30
bossPlat1x = -500
bossPlat1y = -258
bossPlat1Rect = pygame.Rect(bossPlat1x, bossPlat1y, BOSSPLAT1W, BOSSPLAT1H)

BOSSPLAT2W = 500
BOSSPLAT2H = 30
bossPlat2x = -10
bossPlat2y = -408
bossPlat2Rect = pygame.Rect(bossPlat2x, bossPlat2y, BOSSPLAT2W, BOSSPLAT2H)

BOSSPLAT3W = 500
BOSSPLAT3H = 30
bossPlat3x = -10
bossPlat3y = -150
bossPlat3Rect = pygame.Rect(bossPlat3x, bossPlat3y, BOSSPLAT3W, BOSSPLAT3H)

BOSSPLAT4W = 500
BOSSPLAT4H = 30
bossPlat4x = -990
bossPlat4y = -408
bossPlat4Rect = pygame.Rect(bossPlat4x, bossPlat4y, BOSSPLAT4W, BOSSPLAT4H)

BOSSPLAT5W = 500
BOSSPLAT5H = 30
bossPlat5x = -990
bossPlat5y = -150
bossPlat5Rect = pygame.Rect(bossPlat5x, bossPlat5y, BOSSPLAT5W, BOSSPLAT5H)

# Traps

# 1st Trap
TRAP1W = 60
TRAP1H = 30
trap1x = 2680
trap1y = 220
trap1Rect = pygame.Rect(trap1x, trap1y, TRAP1W, TRAP1H)

# 2nd Trap
TRAP2W = 30
TRAP2H = 30
trap2x = 3310
trap2y = 200
trap2Rect = pygame.Rect(trap2x, trap2y, TRAP2W, TRAP2H)

# 3rd Trap
TRAP3W = 30
TRAP3H = 30
trap3x = 3230
trap3y = 350
trap3Rect = pygame.Rect(trap3x, trap3y, TRAP3W, TRAP3H)

# Door
DOORW = 100
DOORH = 160
doorx = 3740
doory = 420
doorRect = pygame.Rect(doorx, doory, DOORW, DOORH)

# Keys
key1x = 1895
key1y = 245
radius = 15
key1Rect = pygame.Rect((key1x - radius), (key1y - radius), (radius * 2), (radius * 2))

key2x = 2730
key2y = 45
key2Rect = pygame.Rect((key2x - radius), (key2y - radius), (radius * 2), (radius * 2))

key3x = 3300
key3y = 360
key3Rect = pygame.Rect((key3x - radius), (key3y - radius), (radius * 2), (radius * 2))

keyCount = 0

# PowerUps
pwr1x = 1300
pwr1y = 500
pwr1Rect = pygame.Rect((pwr1x - radius), (pwr1y - radius), (radius * 2), (radius * 2))

pwr2x = 200
pwr2y = -500
pwr2Rect = pygame.Rect((pwr2x - radius), (pwr2y - radius), (radius * 2), (radius * 2))

pwrCount = 0
# pwr3x = 1100
# pwr3y = 130
# pwr3Rect = pygame.Rect((pwr3x - radius), (pwr3y - radius), (radius * 2), (radius * 2))

pwr = False
pwrup = pygame.Rect(10, 10, 10, 10)
jmppwr = False
movepwr = False
# shootpwr = False

# Platform lists

platxs = [plat0x, plat1x, plat2x, plat3x, plat4x, plat5x, plat6x, plat7x, plat8x, plat9x, plat10x, plat11x, plat12x,
          plat13x, plat14x, plat15x, plat16x, bossPlat1x, bossPlat2x, bossPlat3x, bossPlat4x, bossPlat5x]
platys = [plat0y, plat1y, plat2y, plat3y, plat4y, plat5y, plat6y, plat7y, plat8y, plat9y, plat10y, plat11y, plat12y,
          plat13y, plat14y, plat15y, plat16y, bossPlat1y, bossPlat2y, bossPlat3y, bossPlat4y, bossPlat5y]
platws = [PLAT0W, PLAT1W, PLAT2W, PLAT3W, PLAT4W, PLAT5W, PLAT6W, PLAT7W, PLAT8W, PLAT9W, PLAT10W, PLAT11W, PLAT12W,
          PLAT13W, PLAT14W, PLAT15W, PLAT16W, BOSSPLAT1W, BOSSPLAT2W, BOSSPLAT3W, BOSSPLAT4W, BOSSPLAT5W]
plaths = [PLAT0H, PLAT1H, PLAT2H, PLAT3H, PLAT4H, PLAT5H, PLAT6H, PLAT7H, PLAT8H, PLAT9H, PLAT10H, PLAT11H, PLAT12H,
          PLAT13H, PLAT14H, PLAT15H, PLAT16H, BOSSPLAT1H, BOSSPLAT2H, BOSSPLAT3H, BOSSPLAT4H, BOSSPLAT5H]
platrects = [plat0Rect, plat1Rect, plat2Rect, plat3Rect, plat4Rect, plat5Rect, plat6Rect, plat7Rect, plat8Rect,
             plat9Rect, plat10Rect, plat11Rect, plat12Rect, plat13Rect, plat14Rect, plat15Rect, plat16Rect,
             bossPlat1Rect, bossPlat2Rect, bossPlat3Rect, bossPlat4Rect, bossPlat5Rect]

ogplatxs = [-1000, 500, 300, 0, 580, 1200, 1600, 2020, 1870, 2360, 2520, 2680, 2520, 3000, 3200, 3340, 3320, -500, -10,
            -10, -990, -990]
ogplatys = [590, 560, 400, 560, 260, 500, 500, 380, 270, 330, 290, 250, 40, 170, 170, 170, 580, -258, -408, -150, -408,
            -150]
ogtrapxs = [2680, 3310, 3230]
ogkeyxs = [1895, 2730, 3300]
ogvillainxs = [700, 700, 1760, 2030, 1000]
ogvillainys = [520, 220, 460, 230, -490]
ogpwrupy = [500, -500]
ogpwrupx = [1300, 200]
# Trap lists

trapsx = [trap1x, trap2x, trap3x]
trapsy = [trap1y, trap2y, trap3y]
trapsw = [TRAP1W, TRAP2W, TRAP3W]
trapsh = [TRAP1H, TRAP2H, TRAP3H]
traprects = [trap1Rect, trap2Rect, trap3Rect]

# Key lists

keyxs = [key1x, key2x, key3x]
keyys = [key1y, key2y, key3y]
keyRects = [key1Rect, key2Rect, key3Rect]

# Powrup lists
pwrrects = [pwr1Rect, pwr2Rect]  # , pwr3Rect]


# Defining Collision functions for Platforms ( relative to Player )

def collisionBottom():
    for i in range(len(platys)):
        if playerx < platrects[i].right and (playerx + PLAYERW) > platrects[i].left:
            if (playery + PLAYERH) > platrects[i].top and playery < platrects[i].top:
                return True
    return False


def collisionBottomValue():
    for i in range(len(platys)):
        if playerx < platrects[i].right and (playerx + PLAYERW) > platrects[i].left:
            if (playery + PLAYERH) > platrects[i].top and playery < platrects[i].top:
                return i
    return -1


def collisionTop():
    for i in range(len(platys)):
        if playerx < platrects[i].right and (playerx + PLAYERW) > platrects[i].left:
            if playery < platrects[i].bottom and (playery + PLAYERH) > platrects[i].bottom:
                return True
    return False


def collisionRight():
    for i in range(len(platxs)):
        if (playerx + PLAYERW) == platrects[i].left:
            if (playery + PLAYERH) > platrects[i].top and (playery < platrects[i].bottom):
                return True
    return False


def collisionLeft():
    for i in range(len(platxs)):
        if playerx == platrects[i].right:
            if ((playery + PLAYERH) > platrects[i].top) and (playery < platrects[i].bottom):
                return True
    return False


# Defining Collision functions for Traps ( relative to Player )

def trapCollisionBottom():
    for i in range(len(trapsy)):
        if playerx < (traprects[i].right) and (playerx + PLAYERW) > traprects[i].left:
            if (playery + PLAYERH) > traprects[i].top and playery < traprects[i].top:
                return True
                # sys.exit(0)
    return False


def trapCollisionRight():
    for i in range(len(trapsx)):
        if (playerx + PLAYERW) == traprects[i].left:
            if (playery + PLAYERH) > (traprects[i].top) and (playery < traprects[i].bottom):
                return True
                # sys.exit(0)
    return False


def trapCollisionLeft():
    for i in range(len(trapsx)):
        if playerx == (traprects[i].right):
            if ((playery + PLAYERH) > traprects[i].top) and (playery < traprects[i].bottom):
                return True
                # sys.exit(0)
    return False


def trapCollision():
    b = trapCollisionBottom()
    r = trapCollisionRight()
    l = trapCollisionLeft()

    if b or r or l:
        return True
    return False


# Defining Collision functions for Villains ( relative to Villain )

def villainCollisionRight():
    # checking right side of the villain
    for i in range(len(villainxs)):
        if playerx < villainrects[i].right and (playerx + PLAYERW) > villainrects[i].left:
            if ((playery + PLAYERH) > villainrects[i].top) and playery < villainrects[i].bottom:
                print("hit the right side of the villain")
                return True
    return False


def villainCollisionLeft():
    # checkin left side of the villain
    for i in range(len(villainxs)):
        if (playerx + PLAYERW) > villainrects[i].left and playerx < villainrects[i].right:
            if (playery + PLAYERH) > (villainrects[i].top) and (playery < villainrects[i].bottom):
                print('hit the left side of the villian', i)
                return True
    return False

    # for i in range(len(villainxs)):
    #     if (playerx + PLAYERW) == villainrects[i].left:
    #         if (playery + PLAYERH) > (villainrects[i].top) and (playery < villainrects[i].bottom):
    #             print('hit the left side of the villian')
    #             return True
    # return True


def villainCollisionTop():
    # checking the top of the villain
    for i in range(len(villainrects)):
        if playerx < (villainrects[i].right) and (playerx + PLAYERW) > villainrects[i].left:
            if (playery + PLAYERH) > villainrects[i].top and playery < villainrects[i].top:
                if i == 4:
                    return True
                villainrects[i].top = -500
                print(villainrects[i].top)
                return True
    return False


def villainCollisionBottom():
    # Checking the bottom of the villain
    # most likey unnecessary
    for i in range(len(villainys)):
        if playerx < villainrects[i].right and (playerx + PLAYERW) > villainrects[i].left:
            if playery < villainrects[i].bottom and (playery + PLAYERH) > villainrects[i].bottom:
                # print('top collision')
                return True
    return False


def villainCollision():
    b = villainCollisionBottom()
    t = villainCollisionTop()
    r = villainCollisionRight()
    l = villainCollisionLeft()
    bt = bossCollisionTop()
    if b:
        print("DEAD bottom")
        return True
        # sys.exit(0)
    if t:
        print("DEAD top")
        return
    # if t != 4:
    #     villainrects[t].top = -500
    #     #     print(villainrects[i].top)
    #     # sys.exit(0)
    #     return
    if bt:
        print("DEAD bosstop")
        return True

    if r:
        print("DEAD right")
        return True
        # sys.exit(0)
    if l:
        print("DEAD left")
        return True
        # sys.exit(0)
    return False


def bossCollisionTop():  # player collision with top of boss
    if playerx < (bossRect.right) and (playerx + PLAYERW) > bossRect.left:
        if (playery + PLAYERH) > bossRect.top and playery < bossRect.top:
            return True
    return False


def bossCollisionBottom():  # boss collision with top of rects
    for i in range(len(platys)):
        if bossRect.left < platrects[i].right and (bossRect.right) > platrects[i].left:
            if (bossRect.bottom) > platrects[i].top and bossRect.top < platrects[i].top:
                return True
    return False


# bullet collisions
#player bullet
def playerBulletCollision():
    if bossRect.left < playerBullet.right and bossRect.right > playerBullet.left:
        if bossRect.bottom > playerBullet.top and bossRect.top < playerBullet.top:
            print("hit")
            return True
    return False


# 2nd bullet
def bulletCollisionTop():
    if playerx < bullet2.right and (playerx + PLAYERW) > bullet2.left:
        if (playery + PLAYERH) > bullet2.top and playery < bullet2.top:
            #print("hit the top of the bullet")
            return True
    return False


# bossBullet
def bulletCollisionRight():
    if playerx < bossBullet.right and (playerx + PLAYERW) > bossBullet.left:
        if (playery + PLAYERH) > bossBullet.top and playery < bossBullet.top:
            #print("hit the right of the bullet")
            return True
    return False

#1st bullet
def bulletCollisionLeft():
    if playerx < bullet.right and (playerx + PLAYERW) > bullet.left:
        if (playery + PLAYERH) > bullet.top and playery < bullet.top:
            #print("hit the left of the bullet")
            return True
    return False


def bulletCollision():
    t = bulletCollisionTop()
    r = bulletCollisionRight()
    l = bulletCollisionLeft()

    if r or l or t:
        return True
    return False


def pwrupCollisionBottom():
    for i in range(len(pwrrects)):
        if playerx < pwrrects[i].right and (playerx + PLAYERW) > pwrrects[i].left:
            if (playery + PLAYERH) > pwrrects[i].top and playery < pwrrects[i].top:
                return i
    return -1


def pwrupCollisionRight():
    for i in range(len(pwrrects)):
        if (playerx + PLAYERW) >= pwrrects[i].left and playerx < pwrrects[i].right:
            if (playery + PLAYERH) > pwrrects[i].top and (playery < pwrrects[i].bottom):
                return i
    return -1


def pwrupCollisionLeft():
    for i in range(len(pwrrects)):
        # if playerx == pwrrects[i].right:
        if playerx <= pwrrects[i].right and (playerx + PLAYERW) >= pwrrects[i].left:
            if ((playery + PLAYERH) > pwrrects[i].top) and (playery < pwrrects[i].bottom):
                return i
    return -1


def pwrupCollision():
    b = pwrupCollisionBottom()
    r = pwrupCollisionRight()
    l = pwrupCollisionLeft()

    if b == -1 or r == -1 or l == -1:
        return

    return max(b, r, l)  # i


# Checking if the player has collected a powerup

def havepwrup():
    global pwrCount
    left = False
    right = False
    bottom = False
    for i in range(len(pwrrects)):
        # checkin collision with players right
        if (playerx + PLAYERW) == pwrrects[i].left:
            if (playery + PLAYERH) > pwrrects[i].top and (playery < pwrrects[i].top + (radius * 2)):
                print("left hit")
                left = True
        # checkin collision with players left
        if playerx == (pwrrects[i].left + (radius * 2)):
            if ((playery + PLAYERH) > pwrrects[i].top) and (playery < (pwrrects[i].top + (radius * 2))):
                print("right hit")
                right = True

        # checkin collision with players bottom
        if playerx < (pwrrects[i].left + (radius * 2)) and (playerx + PLAYERW) > pwrrects[i].left:
            if (playery + PLAYERH) > pwrrects[i].top and playery < pwrrects[i].top:
                print("bottom hit")
                bottom = True

        # returning True if any collision happened, and keeping count of collected keys
        if bottom or right or left:
            pwrCount += 1
            # moving the collided key to avoid the count increasing constantly
            pwrrects[i].left = -500
            return True
    return False


# Checking if the player has collected a Key

def haveKey():
    global keyCount
    left = False
    right = False
    bottom = False
    for i in range(len(keyxs)):
        # checkin collision with players right
        if (playerx + PLAYERW) == keyRects[i].left:
            if (playery + PLAYERH) > keyRects[i].top and (playery < keyRects[i].top + (radius * 2)):
                print("left hit")
                left = True
        # checkin collision with players left
        if playerx == (keyRects[i].left + (radius * 2)):
            if ((playery + PLAYERH) > keyRects[i].top) and (playery < (keyRects[i].top + (radius * 2))):
                print("right hit")
                right = True

        # checkin collision with players bottom
        if playerx < (keyRects[i].left + (radius * 2)) and (playerx + PLAYERW) > keyRects[i].left:
            if (playery + PLAYERH) > keyRects[i].top and playery < keyRects[i].top:
                print("bottom hit")
                bottom = True

        # returning True if any collision happened, and keeping count of collected keys
        if bottom or right or left:
            keyCount += 1
            # moving the collided key to avoid the count increasing constantly
            keyRects[i].left = -500
            return True
    return False


# Checkin if the player has enough Keys to unlock the door

def doorUnlock():
    if doorRect.left < playerx and (playerx + PLAYERW) <= doorRect.right:
        if doorRect.centery < playery < doorRect.bottom:
            if haveKey and keyCount == 3:
                return True
            if not haveKey():
                return False


# Prompt message for door Unlocking

def doorText():
    noKey = "You need three more keys to enter the Boss level"
    oneKey = "You need two more keys to enter the Boss level"
    twoKey = "You need one more key to enter the Boss level"
    threeKey = "You have enough keys to enter the Boss level"
    buttonPrompt = "Press Enter to proceed to Boss level"

    # while True:
    if doorUnlock():
        text = gamefont.render(threeKey, True, (0, 255, 0))
        text2 = gamefont.render(buttonPrompt, True, (0, 255, 0))
        textRect = text.get_rect(center=(WIDTH / 2, 60))
        text2Rect = text2.get_rect(center=(WIDTH / 2, 120))
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
    else:

        # Shows a different message, depending on the number of Keys the player has
        if keyCount == 1:
            text = gamefont.render(oneKey, True, (255, 0, 0))
            textRect = text.get_rect(center=(WIDTH / 2, 60))
            screen.blit(text, textRect)
        elif keyCount == 2:
            text = gamefont.render(twoKey, True, (255, 0, 0))
            textRect = text.get_rect(center=(WIDTH / 2, 60))
            screen.blit(text, textRect)
        elif keyCount == 0:
            text = gamefont.render(noKey, True, (255, 0, 0))
            textRect = text.get_rect(center=(WIDTH / 2, 60))
            screen.blit(text, textRect)


# Scrolling the environment when the player is moving right

def rightScrolling():
    for i in range(len(platxs)):
        platxs[i] -= xvelocity
        platrects[i].left -= xvelocity

    for i in range(len(villainxs)):
        villainxs[i] -= xvelocity
        villainrects[i].left -= xvelocity
        # print(platxs[i])
        #
        # print('right side of plat1', plat1Rect.right)
        # print('left side of plat1', plat1Rect.left)
    for i in range(len(trapsx)):
        trapsx[i] -= xvelocity
        traprects[i].left -= xvelocity

    # find a way to get rid of global variables
    global doorx
    doorx -= xvelocity
    doorRect.left -= xvelocity

    global key1x, key2x, key3x
    key1x -= xvelocity
    key2x -= xvelocity
    key3x -= xvelocity

    # background scrolling
    # global back1x, backBx, back2x, back3x, back4x, back5x, back6x, back7x, back8x, back9x
    # back1x -= xvelocity
    # backBx -= xvelocity
    # back2x -= xvelocity
    # back3x -= xvelocity
    # back4x -= xvelocity
    # back5x -= xvelocity
    # back6x -= xvelocity
    # back7x -= xvelocity
    # back8x -= xvelocity
    # back9x -= xvelocity
    for i in range(len(backxs)):
        backxs[i] -= xvelocity
    global back17x
    back17x -= xvelocity

    for i in range(len(keyxs)):
        keyRects[i].left -= xvelocity


# Scrolling the environment when the player is moving left

def leftScrolling():
    for i in range(len(platxs)):
        platxs[i] += xvelocity
        platrects[i].left += xvelocity

    for i in range(len(villainxs)):
        villainxs[i] += xvelocity
        villainrects[i].left += xvelocity

    for i in range(len(trapsx)):
        trapsx[i] += xvelocity
        traprects[i].left += xvelocity

    # find a way to get rid of global variables
    global doorx
    doorx += xvelocity
    doorRect.left += xvelocity

    global key1x, key2x, key3x
    key1x += xvelocity
    key2x += xvelocity
    key3x += xvelocity

    for i in range(len(backxs)):
        backxs[i] += xvelocity
    global back17x
    back17x += xvelocity
    for i in range(len(keyxs)):
        keyRects[i].left += xvelocity


# Shooting function used for villains or powerups(?) ( incomplete )

def shoot():
    # Making a villain shoot
    global bullet
    bulletrdy = True

    bulletx = 720
    bullety = 540

    if bulletrdy:
        bullet = pygame.Rect(bulletx, bullety, 10, 10)
        print(bullet)
        bulletrdy = False

    for i in range(100):
        if i % 10 == 0:
            bullet.left -= 10
            print(bullet.left)

            pygame.draw.rect(screen, (255, 255, 255), bullet)


# Boss level ( incomplete )

def bossFight():
    reset()
    remove()
    keyCount = 3
    # detect that the player got the keys and pressed enter to go thru the door

    # find a way to get rid of global variables
    global playerx, playery, jumping, yvelocity, direction, bossx, bossJump, vyvelocity, bossBulletair, bossBulletrdy, bossBullet, counter, pwr, pwrup, jmppwr, movepwr, shootpwr
    global playerBulletair, playerBullet, playerBulletrdy, bossDist, playerRect, hlthbar, hlthbarx
    running = True
    plat17y = 590
    plat17x = -500

    counter = 120
    # pwrCount = 0
    pwr = False
    jmppwr = False
    movepwr = False
    trigger2 = False
    pwr = False
    hlthbarx = 500
    hlthbar = pygame.Rect(990, 0, hlthbarx, 20)
    bossBulletair = False
    playerBulletair = False
    #  plat17Rect.top = 590
    #  plat17Rect.left = -500

    while running:
        # timer
        counter -= 0.03333

        if int(counter) == 0:
            end()

        # checking for program closure
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                sys.exit(0)

        # Checking if player fell off
        if playery > HEIGHT:
            print("DEAD")

        # Moving the player
        if pygame.key.get_pressed()[pygame.locals.K_LEFT] or pygame.key.get_pressed()[pygame.locals.K_a] and not collisionLeft():
            playerx -= xvelocity
            if movepwr == True:
                playerx -= xvelocity * 1.4

        if pygame.key.get_pressed()[pygame.locals.K_RIGHT] or pygame.key.get_pressed()[pygame.locals.K_d] and not collisionRight():
            playerx += xvelocity
            if movepwr == True:
                playerx += xvelocity * 1.4

        if pygame.key.get_pressed()[pygame.locals.K_SPACE] and jumping == False:
            yvelocity = 28
            if jmppwr == True:
                yvelocity = 40
            jumping = True

        # # Moving the Boss
        # Boss moves towards player, slower than other villalins
        if (playerx + PLAYERW) < bossRect.left:
            direction = -1
        if playerx > bossRect.right:
            direction = 1
        # bossx += vxvelocity * direction*0.5
        bossRect.left += vxvelocity * direction * 0.5

        if bossRect.left < 450:
            vyvelocity -= gravity
            bossRect.top -= vyvelocity

        if bossRect.right > 550:
            vyvelocity -= gravity
            bossRect.top -= vyvelocity

        if bossRect.bottom > 590:
            bossRect.bottom = 590
        if vyvelocity < -20 and bossRect.left % 100 == 0:
            vyvelocity = 20

        # shooting
        if bossBulletair:
            if bulletCollision():
                bossBulletair = False
                jmppwr = False
                movepwr = False
                end()
                # return

        bossDist = playerx - bossRect.left

        if abs(bossDist) < 500:
            bossBulletrdy = True
        else:
            bossBulletrdy = False

        if bossBulletrdy and not bossBulletair:
            bossBullet.x = bossRect.centerx
            bossBullet.y = bossRect.centery
            bossBullet = pygame.Rect(bossBullet.x, bossBullet.y, 10, 10)
            bossBulletrdy = False
            bossBulletair = True

        if bossBulletair and bossDist < 0:
            bossBullet.left -= 20
        if bossBulletair and bossDist > 0:
            bossBullet.left += 20
        if bossBulletair and bossDist == 0:
            bossBulletair = False

        if bossBullet.left < 0 or bossBullet.left > 1500:
            bossBulletair = False


        # player shooting
        mouse1 = pygame.mouse.get_pos()
        mouse2 = pygame.mouse.get_pressed()[0]

        if mouse2:
            playerBulletrdy = True
        else:
            playerBulletrdy = False

        if playerBulletrdy and not playerBulletair:
            playerBullet.x = playerRect.centerx
            playerBullet.y = playerRect.centery
            playerBullet = pygame.Rect(playerBullet.x, playerBullet.y, 10, 10)
            playerBulletrdy = False
            playerBulletair = True

        if playerBulletair and mouse1[0] < playerRect.centerx:
            playerBullet.left -= 20
        if playerBulletair and mouse1[0] > playerRect.centerx:
            playerBullet.left += 20
        if playerBulletair and mouse1[0] == playerRect.centerx:
            playerBulletair = False

        if playerBullet.left < 0 or playerBullet.left > 1500:
            playerBulletair = False

        if playerBulletair:
            if playerBulletCollision():
                playerBulletair = False
                hlthbarx -= 50
                hlthbar = pygame.Rect(990, 0, hlthbarx, 20)
                if hlthbarx == 0:
                    win()
        if pygame.key.get_pressed()[pygame.locals.K_l]:
            win()

        # triggerJump = False
        # if bossRect.left > 350 and bossRect.right < 500:
        #     triggerJump = True
        # else:
        #     triggerJump = False

        # if bossJump == False:#pygame.key.get_pressed()[pygame.locals.K_c] and bossJump == False:
        #     vyvelocity = 28
        #     bossJump = True
        # Powerups
        # if int(counter) % 15 == 0:
        #     pwrup = pwr1Rect
        #     pwr = True
        # if int(counter) % 35 == 0:
        #     pwrup = pwr2Rect
        #     pwr = True
        # # if int(counter) % 25 == 0:
        # #     pwrup = pwr3Rect
        # #     pwr = True
        #
        # if pwrupCollision() == 0:
        #     pwr = False
        #     jmppwr = True
        # if pwrupCollision() == 1:
        #     pwr = False
        #     movepwr = True
        # if pwrupCollision() == 2:
        #     pwr = False
        #     movepwr = True

        # print(bossCollisionBottom())
        # print(bossRect.top, bossRect.left, bossJump)
        print(keyCount)
        # if villani1 is killed boss disappears for some reason

        # Collisions
        if collisionBottom() is False:
            yvelocity -= gravity
            playery -= yvelocity
        if collisionBottom():
            yvelocity = 0
            jumping = False
        if collisionTop():
            yvelocity = -yvelocity

        if collisionBottom():
            i = collisionBottomValue()
            playery = platys[i] - PLAYERH

        if villainCollision():
            print("Boss death")
            end()
        if bossCollisionTop():
            print("Boss top death")
            end()

        if playerx < 0:
            playerx = 0
        if (playerx + PLAYERW) > WIDTH:
            playerx = WIDTH - PLAYERW
        if playery < 0:
            # playery = 0
            yvelocity = -yvelocity

        # Drawing screen
        screen.fill((65, 65, 65))

        playerRect = pygame.Rect(playerx, playery, PLAYERW, PLAYERH)
        player = pygame.draw.rect(screen, (255, 178, 102), playerRect)

        boss = pygame.draw.rect(screen, (102, 178, 255), bossRect)

        platform0 = pygame.draw.rect(screen, (255, 0, 0), plat0Rect)
        bplatform1 = pygame.draw.rect(screen, (255, 0, 0), bossPlat1Rect)
        bplatform2 = pygame.draw.rect(screen, (255, 0, 0), bossPlat2Rect)
        bplatform3 = pygame.draw.rect(screen, (255, 0, 0), bossPlat3Rect)
        bplatform4 = pygame.draw.rect(screen, (255, 0, 0), bossPlat4Rect)
        bplatform5 = pygame.draw.rect(screen, (255, 0, 0), bossPlat5Rect)
        screen.blit(backgroundbase, (backxs[0], 590))

        # drawing powerup

        if not havepwrup():
            if pwrCount == 0:
                currentpwr = pygame.draw.circle(screen, (0, 255, 0),
                                                ((pwr1Rect.left + radius), (pwr1Rect.top + radius)), radius)
                print("green drawn")

            if pwrCount == 1:
                jmppwr = True
            if pwrCount == 2:
                movepwr = True

            # show the second powerup if the first is collected and time less than 100
            if pwrCount == 1 and counter < 100:
                currentpwr = pygame.draw.circle(screen, (0, 0, 255),
                                                ((pwr2Rect.left + radius), (pwr2Rect.top + radius)), radius)
                pwr2Rect.top = 100

        # drawing bullet
        if bossBulletair:
            bssBullet = pygame.draw.rect(screen, (255, 255, 255), bossBullet)

        if playerBulletair:
            plyrBullet = pygame.draw.rect(screen, (255, 255, 255), playerBullet)

        timerwrd = gamefont.render('Timer: ', True, (255, 255, 255))
        screen.blit(timerwrd, (0, 0))

        timer = gamefont.render(str(int(counter)), True, (255, 255, 255))
        if int(counter) <= 10:
            timer = gamefont.render(str(int(counter)), True, (255, 0, 0))
        screen.blit(timer, (110, 0))

        bosswrd = gamefont.render('Boss: ', True, (255, 255, 255))

        screen.blit(bosswrd, (900, 0))
        bar = pygame.draw.rect(screen, (102, 178, 255), hlthbar)

        pygame.display.flip()
        clock.tick(30)


# Resetting the environment so the player can restart without closing the program

def reset():
    # find a way to get rid of global variables
    global playerx, playery, villain1x, villain2x, doorx, keyCount, bulletair1, bulletair2, pwrCount
    # if playerx != 250:
    #     playerx = 250
    # if playery != 400:
    #     playery = 400
    playerx, playery = 250, 400
    villain1x = 700
    villain2x = 700
    doorx = 3740
    doorRect.left = 3740
    keyCount = 0
    pwrCount = 0

    bulletair1 = False
    bulletair2 = False

    for i in range(len(backxs)):
        if backxs[i] != ogbackxs[i]:
            backxs[i] = ogbackxs[i]

    for i in range(len(platxs)):
        if platxs[i] != ogplatxs[i]:
            platxs[i] = ogplatxs[i]

    for i in range(len(platys)):
        if platys[i] != ogplatys[i]:
            platys[i] = ogplatys[i]

    for i in range(len(platxs)):
        if platrects[i].left != ogplatxs[i]:
            platrects[i].left = ogplatxs[i]
        if platrects[i].top != ogplatys[i]:
            platrects[i].top = ogplatys[i]

    # for i in range(len(villainxs)):
    #     if villainxs[i] != ogvillainxs[i]:
    #         villainxs[i] = ogvillainxs[i]
    #     if villainys[i] != ogvillainys[i]:
    #         villainys[i] = ogvillainys[i]

    for i in range(len(villainrects)):
        if villainrects[i].left != ogvillainxs[i]:
            villainrects[i].left = ogvillainxs[i]
        if villainrects[i].top != ogvillainys[i]:
            villainrects[i].top = ogvillainys[i]

    for i in range(len(trapsx)):
        if trapsx[i] != ogtrapxs[i]:
            trapsx[i] = ogtrapxs[i]

    for i in range(len(trapsx)):
        if traprects[i].left != ogtrapxs[i]:
            traprects[i].left = ogtrapxs[i]

    # collision for keys is being reset but the drawings arent
    for i in range(len(keyxs)):
        if keyxs[i] != ogkeyxs[i]:
            keyxs[i] = ogkeyxs[i]

    for i in range(len(keyxs)):
        if keyRects[i].left != ogkeyxs[i]:
            keyRects[i].left = ogkeyxs[i]

    for i in range(len(ogpwrupy)):
        if pwrrects[i].top != ogpwrupy[i]:
            pwrrects[i].top = ogpwrupy[i]
        if pwrrects[i].left != ogpwrupx[i]:
            pwrrects[i].left = ogpwrupx[i]

    # removing all phase one platforms before calling bossFight


def remove():
    for i in range(len(platxs)):
        # So that the 0th Platform ( floor ) isn't removed
        if i == 0:
            continue
        #elif i == 17 or i == 18 or i == 19 or i == 20 or i == 21:
        #    platxs[i] *= -1
        else:
            platxs[i] = -500

    for i in range(len(platys)):
        if i == 0:
            continue
        #elif i == 17 or i == 18 or i == 19 or i == 20 or i == 21:
        #    platys[i] *= -1
        else:
            platys[i] = -500

    for i in range(len(platxs)):
        if i == 0:
            continue
        #elif i == 17 or i == 18 or i == 19 or i == 20 or i == 21:
        #    platrects[i].left *= -1
        #    platrects[i].top *= -1
        else:
            platrects[i].left = -500
            platrects[i].top = -500

    # for i in range(2):#len(villainrects)):
    for i in range(len(villainrects)):  # so that the boss isnt removed will find a better way for it later
        villainrects[i].top = -500
        if i == 4:
            villainrects[i].top *= -1  # 490
    for i in range(len(trapsx)):
        trapsx[i] = -500

    for i in range(len(trapsx)):
        traprects[i].left = -500

    # collision for keys is being reset but the drawings arent
    for i in range(len(keyxs)):
        keyxs[i] = -500

    for i in range(len(keyxs)):
        keyRects[i].left = -500


# Credits screen, when user presses CREDITS

def credits():
    creds = Titlefont.render("CREDITS", True, (255, 255, 255))
    graphics = gamefont.render("GRAPHICS", True, (255, 255, 255))
    gameMech = gamefont.render("GAME MECHANICS", True, (255, 255, 255))
    siName = gamefont.render("Siyoung Oh", True, (255, 255, 255))
    ahName = gamefont.render("Ahmed Benbyad", True, (255, 255, 255))
    yoName = gamefont.render("Youssef Fayed", True, (255, 255, 255))
    muName = gamefont.render("Mustafa Abdalla", True, (255, 255, 255))

    back = gamefont.render("←", True, (255, 255, 255))

    while True:

        # clearing previous screen ( creating a clean screen )
        screen.fill((65, 65, 65))

        # showing the credit screen
        credsRect = creds.get_rect(center=(WIDTH / 2, 100))
        screen.blit(creds, credsRect)
        # Graphics credits
        graphicsRect = graphics.get_rect(center=(WIDTH / 2, 200))
        screen.blit(graphics, graphicsRect)
        siNameRect = siName.get_rect(center=(WIDTH / 2, 250))
        screen.blit(siName, siNameRect)
        ahNameRect = ahName.get_rect(center=(WIDTH / 2, 300))
        screen.blit(ahName, ahNameRect)

        # Game Mechanics credits
        gameMechRect = gameMech.get_rect(center=(WIDTH / 2, 400))
        yoNameRect = yoName.get_rect(center=(WIDTH / 2, 450))
        screen.blit(yoName, yoNameRect)
        muNameRect = muName.get_rect(center=(WIDTH / 2, 500))
        screen.blit(muName, muNameRect)
        screen.blit(gameMech, gameMechRect)

        # Back button
        backRect = back.get_rect(topleft=(0, 0))
        screen.blit(back, backRect)

        # checking for program closure
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(0)

            # Back button control
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= backRect.width and 0 <= mouse[1] <= backRect.height:
                    return

        pygame.display.update()  # unnecessary?
        pygame.display.flip()


# Info / About screen displayed when the user presses the i on the top-left corner

def info():
    text0 = "Welcome to Fred!"
    text1 = "Your objective is to traverse this universe, avoiding enemies,"
    text2 = "collecting keys and powers"
    text3 = "Once you collect 3 keys you are able to open the door that leads to the final Boss"
    text4 = "Beat the Boss and you beat the Game"
    text5 = "CONTROLS:"
    text6 = "Move Left ← or A"
    text7 = "Move Right → or D"
    text8 = "Jump [SPACEBAR]"
    text9 = "Shoot MOUSEBUTTON"
    text10 = "Press Esc at anytime to exit the Game"

    while True:

        screen.fill((65, 65, 65))
        intro0 = gamefont.render(text0, True, (255, 255, 255))
        screen.blit(intro0, (0, 30))
        intro1 = gamefont.render(text1, True, (255, 255, 255))
        screen.blit(intro1, (0, 70))
        intro2 = gamefont.render(text2, True, (255, 255, 255))
        screen.blit(intro2, (0, 110))
        intro3 = gamefont.render(text3, True, (255, 255, 255))
        screen.blit(intro3, (0, 150))
        intro4 = gamefont.render(text4, True, (255, 255, 255))
        screen.blit(intro4, (0, 190))
        intro5 = gamefont.render(text5, True, (255, 255, 255))
        screen.blit(intro5, (0, 250))
        intro6 = gamefont.render(text6, True, (255, 255, 255))
        screen.blit(intro6, (0, 290))
        intro7 = gamefont.render(text7, True, (255, 255, 255))
        screen.blit(intro7, (0, 330))
        intro8 = gamefont.render(text8, True, (255, 255, 255))
        screen.blit(intro8, (0, 370))
        intro9 = gamefont.render(text9, True, (255, 255, 255))
        screen.blit(intro9, (0, 410))
        intro10 = gamefont.render(text10, True, (255, 255, 255))
        screen.blit(intro10, (0, 470))
        back = gamefont.render("←", True, (255, 255, 255))
        # Back button
        backRect = back.get_rect(topleft=(0, 0))
        screen.blit(back, backRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(0)
            # Back button control
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= backRect.width and 0 <= mouse[1] <= backRect.height:
                    return

        pygame.display.flip()


# animating letters one at a time
def endAnimation(string):

    messagefont = pygame.font.Font("Font.ttf", 150)
    messagefont2 = pygame.font.Font("Font.ttf", 30)

    text = ""
    for i in range(len(string)):
        screen.fill((65, 65, 65))
        text = text + string[i]
        message = messagefont.render(text, True, (254,39,18))
        text_rect = message.get_rect()
        text_rect.center = (752, 166)
        screen.blit(message, text_rect)
        pygame.display.update()
        pygame.time.wait(150)

def winAnimation(string):

    messagefont = pygame.font.Font("Font.ttf", 150)
    messagefont2 = pygame.font.Font("Font.ttf", 30)

    text = ""
    for i in range(len(string)):
        screen.fill((65, 65, 65))
        text = text + string[i]
        message = messagefont.render(text, True, (144,238,144))
        text_rect = message.get_rect()
        text_rect.center = (752, 166)
        screen.blit(message, text_rect)
        pygame.display.update()
        pygame.time.wait(150)


# End screen displayed when the player dies ( villain or trap collision , falling off ... )

def end():
    # our font for message
    messagefont = pygame.font.Font("Font.ttf", 150)
    messagefont2 = pygame.font.Font("Font.ttf", 30)

    # 3 message for YOU DIED, r and i button

    message = messagefont.render("YOU DIED", True, (254,39,18))
    message2 = messagefont2.render("- Press R to Restart -", True, (255, 255, 255))
    message3 = messagefont2.render("- Press M to go to Main Menu -", True, (255, 255, 255))

    endAnimation("YOU DIED")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if bossRect.top > 0:
                        reset()
                        bossFight()
                        endAnimation("YOU DIED")
                        # if event.key == pygame.K_m:
                        #     return

                    else:
                        reset()
                        game()
                        endAnimation("YOU DIED")

                    #    endAnimation("YOU DIED")
                    # reset()
                    # game()
                    # if bossRect.top > 0:
                    #    bossFight()
                    #    if event.key == pygame.K_m:
                    #        return

                    # else :
                    #    reset()
                    #    game()
                    #    endAnimation("YOU DIED")

                if event.key == pygame.K_m:
                    main()

        screen.fill((65, 65, 65))

        screen.blit(message, (400, 100))
        screen.blit(message2, (560, 420))
        screen.blit(message3, (488, 510))
        pygame.display.update()


# win end screen
def win():
    # our font for message
    messagefont = pygame.font.Font("Font.ttf", 150)
    messagefont2 = pygame.font.Font("Font.ttf", 30)

    # 3 message for YOU DIED, r and i button

    message = messagefont.render("YOU WON!", True, (144,238,144))
    message3 = messagefont2.render("- Press M to go to Main Menu -", True, (255, 255, 255))

    winAnimation("YOU WON!")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_r:
                    #if bossRect.top > 0:
                    #   bossFight()
                       # if event.key == pygame.K_m:
                       #     return

                    #else :
                    #   reset()
                    #   game()
                    #    endAnimation("YOU DIED")
                    # reset()
                    # game()
                    # if bossRect.top > 0:
                    #    bossFight()
                    #    if event.key == pygame.K_m:
                    #        return

                    # else :
                    #    reset()
                    #    game()
                    #    endAnimation("YOU DIED")

                if event.key == pygame.K_m:
                    main()

        screen.fill((65, 65, 65))

        screen.blit(message, (400, 100))
        screen.blit(message3, (488, 510))
        pygame.display.update()



# Game function with most of the functionality and drawing

def game():
    global villain2x, villain4x, playery, playerx, jumping, yvelocity, villain2Rect, direction, direction2, plat2x, plat2y, bulletrdy1, bulletair1, bullet, bulletair2, bulletrdy2, bullet2
    running = True

    # resetting the platforms works and the collisions arent affected
    # resetting the villains works visually but the collisions dont work
    # they work as if the villains have been scrolled, and when theyre resetted
    # the collision part of them doesnt, although both the j and the rect.left are being reset

    # reset()
    # keyCounter()
    while running:
        # checking for closure of program
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                # running = False
                sys.exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_b:
                    bossFight()

        # Checking if player fell off
        if playery > HEIGHT:
            print("DEAD")

            running = False
            # sys.exit(0)

        # Moving the player
        if (pygame.key.get_pressed()[pygame.locals.K_LEFT] or pygame.key.get_pressed()[pygame.locals.K_a]) and not collisionLeft():
            playerx -= xvelocity
            if playerx < 200:
                playerx = 200
                leftScrolling()
        if (pygame.key.get_pressed()[pygame.locals.K_RIGHT] or pygame.key.get_pressed()[pygame.locals.K_d])and not collisionRight():
            playerx += xvelocity
            if playerx > (WIDTH * 0.6):
                playerx = (WIDTH * 0.6)
                rightScrolling()

        if pygame.key.get_pressed()[pygame.locals.K_SPACE] and jumping == False:
            yvelocity = 28
            jumping = True

        # Collisions
        if collisionBottom() is False:
            yvelocity -= gravity
            playery -= yvelocity
            # print("velocity im if= " + str(yvelocity))
        if collisionBottom():
            yvelocity = 0
            jumping = False
        if collisionTop():
            yvelocity = -yvelocity

        if villainCollision():
            return

        if trapCollision():
            return

        doorUnlock()

        # shooting
        if bulletair2 or bulletair1:
            if bulletCollision():
                bulletair2 = False
                bulletair1 = False
                return

        dist = playerx - villain1Rect.left

        if abs(dist) < 400 and playery > 400:
            bulletrdy1 = True
        else:
            bulletrdy1 = False

        if bulletrdy1 and not bulletair1:
            bulletx = villain1Rect.centerx
            bullety = villain1Rect.centery
            bullet = pygame.Rect(bulletx, bullety, 10, 10)
            bulletrdy1 = False
            bulletair1 = True

        if bulletair1 and dist < 0:
            bullet.left -= 20
        if bulletair1 and dist > 0:
            bullet.left += 20
        if bulletair1 and dist == 0:
            bulletair1 = False

        if bullet.left < 0 or bullet.left > 1500:
            bulletair1 = False

        dist2 = playerx - villain3Rect.left

        if abs(dist2) < 400:
            bulletrdy2 = True
        else:
            bulletrdy2 = False

        if bulletrdy2 and not bulletair2:
            bullet2x = villain3Rect.centerx
            bullet2y = villain3Rect.centery
            bullet2 = pygame.Rect(bullet2x, bullet2y, 10, 10)
            bulletrdy2 = False
            bulletair2 = True

        if bulletair2 and dist2 < 0:
            bullet2.left -= 20
        if bulletair2 and dist2 > 0:
            bullet2.left += 20
        if bulletair2 and dist2 == 0:
            bulletair2 = False

        if bullet2.left < 0 or bullet2.left > 1500:
            bulletair2 = False

        # Moving Villains

        # bug occurred where if player and villain moving in same direction villain would get off the platform
        # quick and lazy fix
        rightdistance1 = plat4Rect.right - villain2Rect.right
        leftdistance1 = villain2Rect.left - plat4Rect.left
        vxvelocity = 10
        if pygame.key.get_pressed()[pygame.locals.K_LEFT] and direction == -1 and leftdistance1 < 5:
            vxvelocity = 0
        if pygame.key.get_pressed()[pygame.locals.K_RIGHT] and direction == 1 and rightdistance1 < 5:
            vxvelocity = 0

        rightdistance2 = plat8Rect.right - villain4Rect.right
        leftdistance2 = villain4Rect.left - plat4Rect.left
        vxvelocity2 = 10
        if pygame.key.get_pressed()[pygame.locals.K_LEFT] and direction2 == -1 and leftdistance2 < 5:
            vxvelocity2 = 0
        if pygame.key.get_pressed()[pygame.locals.K_RIGHT] and direction2 == 1 and rightdistance2 < 5:
            vxvelocity2 = 0

        villain2x += vxvelocity * direction
        villain2Rect.left += vxvelocity * direction

        if villain2Rect.right >= plat4Rect.right:
            direction = -1
        if villain2Rect.left <= plat4Rect.left:
            direction = 1

        villain4x += vxvelocity2 * direction2
        villain4Rect.left += vxvelocity * direction2
        if villain4Rect.right >= plat8Rect.right:
            direction2 = -1
        if villain4Rect.left <= plat8Rect.left:
            direction2 = 1

        # print(villain4x, villain4Rect.left)

        if collisionBottom():
            i = collisionBottomValue()
            playery = platys[i] - PLAYERH

        # Drawing the screen
        screen.fill((65, 65, 65))

        # checking if the player is infront of the door and pressed Enter
        if doorx < playerx and (playerx + PLAYERW) <= (doorx + DOORW):
            if (doory / 2) < playery < (doory + DOORH):
                doorText()
                if pygame.key.get_pressed()[pygame.locals.K_RETURN] or pygame.key.get_pressed()[
                    pygame.locals.K_KP_ENTER]:
                    bossFight()
                    return


        #door = pygame.draw.rect(screen, (50, 255, 50), doorRect)
        # drawing door
        screen.blit(background17, (backxs[17], 420))

        # Drawing the character (Rectangle for now)
        playerRect = pygame.Rect(playerx, playery, PLAYERW, PLAYERH)
        player = pygame.draw.rect(screen, (255, 178, 102), playerRect)

        # drawing a key counter on the top-left corner
        pygame.draw.circle(screen, (255, 255, 0), (radius + 10, radius + 10), radius)
        keyNums = gamefont.render(str(keyCount), True, (255, 255, 255))
        screen.blit(keyNums, ((radius * 2.5) + 10, radius))

        # Drawing villains
        villain1 = pygame.draw.rect(screen, (102, 178, 255), villain1Rect)
        villain2 = pygame.draw.rect(screen, (102, 178, 255), villain2Rect)
        villain3 = pygame.draw.rect(screen, (102, 178, 255), villain3Rect)
        villain4 = pygame.draw.rect(screen, (102, 178, 255), villain4Rect)

        # Drawing platforms
        platform0 = pygame.draw.rect(screen, (255, 255, 0), plat0Rect)
        platform1 = pygame.draw.rect(screen, (204, 0, 0), plat1Rect)
        platform2 = pygame.draw.rect(screen, (204, 0, 0), plat2Rect)
        platform3 = pygame.draw.rect(screen, (204, 0, 0), plat3Rect)
        platform4 = pygame.draw.rect(screen, (204, 0, 0), plat4Rect)
        platform5 = pygame.draw.rect(screen, (204, 0, 0), plat5Rect)
        platform6 = pygame.draw.rect(screen, (204, 0, 0), plat6Rect)
        platform7 = pygame.draw.rect(screen, (204, 0, 0), plat7Rect)
        platform8 = pygame.draw.rect(screen, (204, 0, 0), plat8Rect)
        platform9 = pygame.draw.rect(screen, (204, 0, 0), plat9Rect)
        platform10 = pygame.draw.rect(screen, (139, 69, 19), plat10Rect)
        platform11 = pygame.draw.rect(screen, (204, 0, 0), plat11Rect)
        platform12 = pygame.draw.rect(screen, (204, 0, 0), plat12Rect)
        trap1 = pygame.draw.polygon(screen, (211, 211, 211), ((trap1Rect.left, trap1Rect.bottom),
                                                              (trap1Rect.left + 15, trap1Rect.top),
                                                              (trap1Rect.left + 30, trap1Rect.bottom)))
        trap2 = pygame.draw.polygon(screen, (211, 211, 211), ((trap1Rect.left + 30, trap1Rect.bottom),
                                                              (trap1Rect.left + 45, trap1Rect.top),
                                                              (trap1Rect.right, trap1Rect.bottom)))
        platform13 = pygame.draw.rect(screen, (204, 0, 0), plat13Rect)
        platform14 = pygame.draw.rect(screen, (204, 0, 0), plat14Rect)
        platform15 = pygame.draw.rect(screen, (204, 0, 0), plat15Rect)
        platform16 = pygame.draw.rect(screen, (204, 0, 0), plat16Rect)
        trap3 = pygame.draw.polygon(screen, (211, 211, 211), ((trap2Rect.right, trap2Rect.top),
                                                              (trap2Rect.left, trap2Rect.top + 15),
                                                              (trap2Rect.right, trap2Rect.bottom)))
        trap4 = pygame.draw.polygon(screen, (211, 211, 211), ((trap3Rect.left, trap3Rect.top),
                                                              (trap3Rect.right, trap3Rect.top + 15),
                                                              (trap3Rect.left, trap3Rect.bottom)))
        if bulletair1:
            bullet1 = pygame.draw.rect(screen, (255, 255, 255), bullet)
        if bulletair2:
            bullet2 = pygame.draw.rect(screen, (255, 255, 255), bullet2)

        # Drawing the Background
        screen.blit(backgroundbase, (backxs[0], 590))
        screen.blit(background1, (backxs[1], 560))
        screen.blit(background2, (backxs[2], 400))
        screen.blit(background3, (backxs[3], 560))
        screen.blit(background4, (backxs[4], 260))
        screen.blit(background5, (backxs[5], 500))
        screen.blit(background6, (backxs[6], 500))
        screen.blit(background7, (backxs[7], 380))
        screen.blit(background8, (backxs[8], 270))
        screen.blit(background9, (backxs[9], 330))
        screen.blit(background10, (backxs[10], 290))
        screen.blit(background11, (backxs[11], 250))
        screen.blit(background12, (backxs[12], 40))
        screen.blit(background13, (backxs[13], 170))
        screen.blit(background14, (backxs[14], 170))
        screen.blit(background15, (backxs[15], 170))
        screen.blit(background16, (backxs[16], 580))
        # screen.blit(background17, (backxs[17], 420))

        # Draw the key if you dont have it and you havent collected any keys before
        if not haveKey():
            if keyCount == 0:
                key = pygame.draw.circle(screen, (255, 255, 0), ((key1Rect.left + radius), (key1Rect.top + radius)),
                                         radius)
            if keyCount == 1:
                key = pygame.draw.circle(screen, (255, 255, 0), ((key2Rect.left + radius), (key2Rect.top + radius)),
                                         radius)

            if keyCount == 2:
                key = pygame.draw.circle(screen, (255, 255, 0), ((key3Rect.left + radius), (key3Rect.top + radius)),
                                         radius)

        pygame.display.flip()

        clock.tick(30)


# main loop of the Start screen
def main():
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    reset()
                    game()
                    end()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quit button action
                if 650 <= mouse[0] <= 850 and 430 <= mouse[1] <= 480:
                    sys.exit(0)
                # Start button action
                if (650 <= mouse[0] <= 850 and 270 <= mouse[1] <= 320):
                    reset()
                    game()
                    end()

                # Credits button action
                if 650 <= mouse[0] <= 850 and 350 <= mouse[1] <= 400:
                    credits()

                # Info button action
                if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 40:
                    info()

        screen.fill((65, 65, 65))

        # Start Button
        if 650 <= mouse[0] <= 850 and 270 <= mouse[1] <= 320:
            pygame.draw.rect(screen, (50, 50, 50), (650, 270, 200, 50))
        else:
            pygame.draw.rect(screen, (170, 170, 170), (650, 270, 200, 50))
        # Credits Button
        if 650 <= mouse[0] <= 850 and 350 <= mouse[1] <= 400:
            pygame.draw.rect(screen, (50, 50, 50), (650, 350, 200, 50))
        else:
            pygame.draw.rect(screen, (170, 170, 170), (650, 350, 200, 50))
        # QUIT Button
        if 650 <= mouse[0] <= 850 and 430 <= mouse[1] <= 480:
            pygame.draw.rect(screen, (50, 50, 50), (650, 430, 200, 50))
        else:
            pygame.draw.rect(screen, (170, 170, 170), (650, 430, 200, 50))
        # Info button
        if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 40:
            pygame.draw.circle(screen, (255, 255, 255), (20, 20), 20, 4)

        screen.blit(Title, (450, 50))
        screen.blit(textstart, (709, 280))
        screen.blit(textcredits, (690, 360))
        screen.blit(textquit, (719, 440))
        pygame.draw.circle(screen, (255, 255, 255), (20, 20), 20, 2)
        screen.blit(infos, (12, 5))

        pygame.display.update()



main()