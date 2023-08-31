from operator import truediv
import cv2
import mediapipe as mp
import numpy as np
import time
import pygame
import os
import random
import pyautogui
from google.protobuf.json_format import MessageToDict
from win32api import GetSystemMetrics


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mpHands = mp.solutions.hands
# mp_holistic = mp.solutions.holistic
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
# os.environ['SDL_VIDEO_CENTERED'] = '0'

cap = cv2.VideoCapture(0)

# cv2.namedWindow("WebCam");
# cv2.moveWindow("WebCam", 700,20);


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
VIOLET = (153,0,153)
BLUE2 = (0,255,255)

# initializing the constructor
pygame.init()
size = width, height = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Thienthanmicle")
clock = pygame.time.Clock()


x1_menu=0
y1_menu = height - 50
g1_menu = True

x2_menu = width - 100
y2_menu = height - 80
g2_menu = True

x3_menu = 100
y3_menu = height - 110
g3_menu = True

x4_menu = width - 200
y4_menu = height - 140
g4_menu = True

x5_menu = 250
y5_menu = height - 170
g5_menu = True

#Đạn
x6_menu = 25
y6_menu = height - 20
x8_menu = 25
y8_menu = height - 50
x9_menu = 25
y9_menu = height - 80
x10_menu = 25
y10_menu = height - 110
x11_menu = 25
y11_menu = height - 130
bienchay1_menu = 0
bienchay3_menu = 0
bienchay4_menu = 0
bienchay5_menu = 0
bienchay6_menu = 0




color_menu = (255,255,255)
color1_menu = GREEN
color2_menu = GREEN
color3_menu = GREEN
color4_menu = GREEN
color5_menu = GREEN
color6_menu = GREEN
color_back_menu = GREEN


# width = screen.get_width()
# height = screen.get_height()
# smallfont = pygame.font.SysFont('Algerian',35)
title_font = pygame.font.SysFont('Jokerman',45)
# smallfont = pygame.font.SysFont('Gigi',35)
# smallfont = pygame.font.SysFont('Forte',35)
smallfont = pygame.font.SysFont('Chiller',35)
title_game = title_font.render('The Lonely Shooter' , True , color4_menu)
text = smallfont.render('START' , True , color1_menu)
text2 = smallfont.render('QUIT' , True , color3_menu)
hd = smallfont.render('GUIDE' , True , color2_menu)
hd2 = smallfont.render('- Dùng ngón giữa tay phải để di chuyển nhân vật' , True , color_menu)
back = smallfont.render('BACK' , True , color_back_menu)
h1 = True
h2 = False
h3 = False
h0 = False

mouse_player = pygame.image.load("mouse1.png").convert_alpha()
mouse_player = pygame.transform.scale(mouse_player, (64, 64))
# background_game = pygame.image.load("bg_test3.jpg").convert_alpha()
# background_game = pygame.transform.scale(background_game, (720, 720))
ufo = pygame.image.load("ufo3.png").convert_alpha()
ufo = pygame.transform.scale(ufo, (55, 35))
rocket = pygame.image.load("rocket.png").convert_alpha()
rocket_menu = pygame.transform.scale(rocket, (20,28))
rocket = pygame.transform.rotate(rocket_menu, 180)

shot = pygame.mixer.Sound("shot.wav")

bien1 = 0
bien2 = 0
bien3 = 0
bien4 = 0
bien5 = 0
bien6 = 0
bien7 = 0
bien8 = 0

ship_menu = pygame.image.load("player_re1.png").convert_alpha()
ship_menu = pygame.transform.scale(ship_menu, (35, 35))

xchar= 0
ychar = 150
rota = 0
qq = 0
qq1 = 0
qq2 = False

arr1 = []
arr2 = []
def read_reverse(file_name):
    with open(file_name, 'r') as read_obj:
        lines = read_obj.readlines()
        lines = [line.strip() for line in lines]
        lines = reversed(lines)
        return lines
    
bullets = []
bullets_wall = []
bullets_ran = []
bullets_ran2 = []
bullets_three1 = []
bullets_three2 = []
bullets_three3 = []

bullets_boss1 = []
bien_boss1 = 0
bullets_boss2 = []
bien_boss2 = 0

x=400 # Người chơi
y=500 # Người chơi
i=0 # for a target bullet
k=0 # Tính điểm
u=0 # thời gian cách nhau mỗi viên đạn
level = 10
change_bullet = True
change_bullet1 = False
target_bullet = 1 # Số đạn bắn mục tiêu
wall_bullet = 1 # Số đạn bắn gạch
xtarget = width/2
ytarget = 5
xtarget2 = width/2
ytarget2 = 5

color1 = BLACK
x1=0
y1 = 100
i1=0 # for a wall_bullet
g1 = True # Đụng tường chạy ngược lại
t1 = True # Set tốc độ của gạch


color2 = BLACK
x2 = width-50
y2 = 150
i2 = 0 
g2 = True
t2 = True


color3 = BLACK
x3 = 0
y3 = 200
i3 = 0 
g3 = True
t3 = True


color4 = BLACK
x4 = width-50
y4 = 250
i4 = 0 
g4 = True
t4 = True


color5 = BLACK
x5 = 0
y5 = 300
i5 = 0 
g5 = True
t5 = True


#Đạn
x6 = 25
y6 = 100
bienchay1 = 0
bienchay2 = 0
xg1 = 300
yg1 = 500
xg2 = 600
yg2 = 500

#Đạn
x8 = 25
y8 = 150
x9 = 25
y9 = 200
x10 = 25
y10 = 250
x11 = 25
y11 = 300
bienchay3 = 0
bienchay4 = 0
bienchay5 = 0
bienchay6 = 0
xg3 = 300
yg3 = 500
xg4 = 600
yg4 = 500

#-----dây điện---------
gd1 = True
gd2 = True
xd1 = 65
yd1 = 50
xd2 = 715
yd2 = 50
colord1 = RED
colord2 = RED
colord12 = RED
biend1 = False
biend2 = False
#-----dây điện---------


bienchay7 = 0
tt = False
dem1 = 0

y12 = -50
x12 = random.randint(10, width-10)
sizev12 = 1
colorv12 = WHITE

y13 = 0
x13 = random.randint(10, width-10)
colorv13 = GREEN

ifall = 0
xfall = random.randint(10, width - 10)
ifall2 = 0
xfall2 = random.randint(10, width - 10)


background = pygame.image.load("target2.png").convert_alpha()
background = pygame.transform.scale(background, (65, 50))
# ship = pygame.image.load("player_re1.png").convert_alpha()
# ship = pygame.transform.scale(ship, (64, 64))
ship = pygame.image.load("player3.png").convert_alpha()
ship = pygame.transform.scale(ship, (64,64))
bulletpicture = pygame.image.load("bullet_re1.png").convert_alpha()
bulletpicture = pygame.transform.scale(bulletpicture, (30, 38))
# ufo = pygame.image.load("ufo.png").convert_alpha()
# ufo = pygame.transform.scale(ufo, (50, 50))
white = pygame.image.load('white.png').convert_alpha()
white = pygame.transform.scale(white,(GetSystemMetrics(0),GetSystemMetrics(1)))

background_game = pygame.image.load("bg_game.png").convert_alpha()
background_game = pygame.transform.scale(background_game, (800,600))
bullet_fc = pygame.image.load("bullet_fc.jpg").convert_alpha()
bullet_fc = pygame.transform.scale(bullet_fc, (25,25))
# rocket = pygame.image.load("rocket.png").convert_alpha()
# rocket_menu = pygame.transform.scale(rocket, (20,28))
# rocket = pygame.transform.rotate(rocket_menu, 180)
bullet_target = pygame.image.load("bullet_target.png").convert_alpha()
bullet_target = pygame.transform.scale(bullet_target, (30,38))
turn_right = pygame.image.load("turn_right.png").convert_alpha()
turn_right = pygame.transform.scale(turn_right, (120,120))
turn_left = pygame.image.load("turn_left.png").convert_alpha()
turn_left = pygame.transform.scale(turn_left, (120,120))
fire_yellow = pygame.image.load("fire_yellow.png").convert_alpha()
fire_yellow = pygame.transform.scale(fire_yellow, (120,120))
fire_bullet = pygame.image.load("fire_bullet.png").convert_alpha()
fire_bullet = pygame.transform.scale(fire_bullet, (120,120))
fire_3tia = pygame.image.load("fire33.PNG").convert_alpha()
fire_3tia = pygame.transform.scale(fire_3tia, (120,120))
pausehand = pygame.image.load("pausehand.PNG").convert_alpha()
pausehand = pygame.transform.scale(pausehand, (240,120))

bullet_alein = pygame.image.load("bullet_alein2.png").convert_alpha()
bullet_alein = pygame.transform.scale(bullet_alein, (40,20))
bullet_alein1 = pygame.transform.rotate(bullet_alein, 90)

boom = pygame.image.load("boom.png").convert_alpha()
boom = pygame.transform.scale(boom, (50,30))

protect_image = pygame.image.load("khien1.png").convert_alpha()


shot = pygame.mixer.Sound("shot.wav")
notshot = pygame.mixer.Sound("notshot.wav")
level_complete = pygame.mixer.Sound("level_complete.wav")
lose_game = pygame.mixer.Sound("lose.wav")
bullet_ufo = pygame.mixer.Sound("bullet_ufo.wav")
bullet_func = pygame.mixer.Sound("bullet_func2.wav")
ufo_boom = pygame.mixer.Sound("ufo_boom.wav")


d = True
reset = 0

targetlv8 = False
target2lv8 = False
colortarget1 = BLACK
colortarget2 = BLACK

count_time = 0
count_time1 = 0

move = True
    
xlevel = -100

bien_lose = 0
lose = False
lose1 = False
s3 = 0
level_display = False

def music():
    pygame.mixer.music.load('intro_game2.wav')
    pygame.mixer.music.play(-1)
music()

pause = False
pause_display = False

color1_pause = GREEN
color2_pause = GREEN
color3_pause = GREEN

y7 = 0
x7 = random.randint(10, width-10)
xauto = 0
yauto = 200
sizev6 = 10
sizev7 = 1
colorv7 = WHITE
bienchay2 = 0
ttt = False
sizeauto = 32
sizefc2 = 25
bienauto = False

kk = 0
victory = False

ufo1_play = True
ufo1_time = 0
ufo1_bien = 0

ufo2_play = True
ufo2_time = 0
ufo2_bien = 0

ufo3_play = True
ufo3_time = 0
ufo3_bien = 0

ufo4_play = True
ufo4_time = 0
ufo4_bien = 0

ufo5_play = True
ufo5_time = 0
ufo5_bien = 0

run_boss1 = True
run_boss2 = False

yc=[]
ycr=[]
yc1=[]
yc2=[]
ycc=[]
hh=[]

i1_space=0
i2_space=0
quantity_three = 5
bien_three = 0
biendem_three = False

bienx1_die = 0
x1_die = 0
bienx2_die = 0
x2_die = 0
bienx3_die = 0
x3_die = 0
bienx4_die = 0
x4_die = 0
bienx5_die = 0
x5_die = 0

ximage_add = random.randint(10, width-10)
yimage_add = -50
bien_add = False
bien_add2 = False
biendem_add = 0
biendem_add2 = 0

bien_three2 = 0
biendem_three2 = False

bien_pause = False
bien_pause2 = 0

bienfire = False

colorchange_ufo1 = GREEN
colorchange_ufo2 = RED

colorchange_bg1 = GREEN
colorchange_bg2 = RED

protect0 = False
protect1 = False
protect2 = False
protect3 = 0
protect4 = 0
protect5 = 0
protect6 = 0
protect7 = False
color_ship = BLACK
ximage_protect = random.randint(10, width-10)
yimage_protect = -50
color_protect = GREEN

colorbg_cv1 = 0
colorbg_cv2 = 1
colorcv0 = True
colorcv1 = False
colorcv2 = False

target1_display = True
target2_display = True

ox1 = 20
oy1 = 70
ox2 = 50
oy2 = 100

ox3=60
oy3=70
ox4=90
oy4=100

ox5=100
oy5=70
ox6=130
oy6=100

protect_size = 0

u1 = 0
u11 = False
u1_s = 0
u11_s = False
u2 = 0
u22 = False
u2_s = 0
u22_s = False
u3 = 0
u33 = False

finger_color1 = (255,0,255)
finger_color2 = (255,0,255)
finger_color3 = (255,0,255)
finger_color4 = (255,0,255)

GREEN_color = GREEN

with mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hand_track:
    while d:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False

        screen.fill(BLACK)
        screen.blit(background_game, (0,0))
        screen.blit(title_game , (width/2-title_game.get_width()/2,50))
                
        title_game = title_font.render('The Lonely Shooter' , True , color4_menu)
        if qq % 150 == 0:
            qq2 = True
        if qq2 == True:
            color4_menu = BLACK
            qq1 += 1
            if qq1 > 40:
                qq1 = 0
                qq2 = False
        else:
            color4_menu = GREEN
        qq += 1
        text = smallfont.render('START' , True , color1_menu)
        hd = smallfont.render('GUIDE' , True , color2_menu)
        scores = smallfont.render('SCORE' , True , color3_menu)
        quitt = smallfont.render('QUIT' , True , color5_menu)
            
            
            

        start = time.time()
        success, img = cap.read()
        img = cv2.resize(img, (570, 430))
        imgg = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(imgg, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False
        results = hand_track.process(imgRGB)
        imgRGB.flags.writeable = True
        # imgRGB = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
        
        if colorcv1 == True:
            imgRGB = np.empty(imgRGB.shape)
            imgRGB.fill(0)
        elif colorcv2 == True:
            imgRGB = np.empty(imgRGB.shape)
            imgRGB.fill(1)
        else:
            imgRGB = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
                    

        # cv2.rectangle(imgRGB,(140,70),(170,100),BLUE,-1)
        # cv2.rectangle(imgRGB,(180,70),(210,100),WHITE,-1)
        
        fingerCount = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label
                
                h, w, c = imgRGB.shape

                xt, yt = hand_landmarks.landmark[9].x*w, hand_landmarks.landmark[9].y*h

                xt1, yt1 = hand_landmarks.landmark[12].x*w, hand_landmarks.landmark[12].y*h
                
                xt11, yt11 = hand_landmarks.landmark[11].x*w, hand_landmarks.landmark[11].y*h

                xs, ys = hand_landmarks.landmark[4].x*w, hand_landmarks.landmark[4].y*h

                xs1, ys1 = hand_landmarks.landmark[8].x*w, hand_landmarks.landmark[8].y*h
                

                # cv2.circle(imgRGB, (int(xt), int(yt)), 9, (255,255,0), -1)
                # cv2.circle(imgRGB, (int(xt1), int(yt1)), 9, (255,0,255), -1)
                
                cv2.circle(imgRGB, (int(xt1), int(yt1)), 9, finger_color4, -1)
                cv2.circle(imgRGB, (int(xs), int(ys)), 9, finger_color1, -1)
                cv2.circle(imgRGB, (int(xs1), int(ys1)), 9, finger_color2, -1)
                
                finger_color1 = (255,0,255)
                finger_color2 = (255,0,255)
                
                finger_color4 = (255,0,255)
                
                font = cv2.FONT_HERSHEY_SIMPLEX
                
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label
                handLandmarks = []
                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])
                if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    fingerCount = fingerCount+1
                elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    fingerCount = fingerCount+1
                if handLandmarks[8][1] < handLandmarks[6][1]:       #Index finger
                    fingerCount = fingerCount+1
                if handLandmarks[12][1] < handLandmarks[10][1]:     #Middle finger
                    fingerCount = fingerCount+1
                if handLandmarks[16][1] < handLandmarks[14][1]:     #Ring finger
                    fingerCount = fingerCount+1
                if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
                    fingerCount = fingerCount+1

                if handLabel == "Right":
                    GREEN_color = GREEN
                else:
                    GREEN_color = RED

                # if len(results.multi_handedness) == 1:
                #     pyautogui.moveTo(xt1*2, yt1*2)
                
                # xt11 = int(xt1)
                # yt11 = int(yt1)
                cv2.rectangle(imgRGB,(ox1,oy1),(ox1+30,oy1+30),BLUE,1)
                cv2.line(imgRGB,(ox1+30,oy1),(ox1,oy1+30),BLUE,1)
                cv2.rectangle(imgRGB,(ox3,oy3),(ox3+30,oy3+30),BLACK,-1)
                cv2.rectangle(imgRGB,(ox5,oy5),(ox5+30,oy5+30),WHITE,-1)
                if ox1 <= xt1 <= ox1+30 and oy1 <= yt1 <= oy1+30 and len(results.multi_handedness) == 1:
                        if abs(ys - ys1) < 20 and abs(xs - xs1) < 20 and len(results.multi_handedness) == 1:
                            colorcv1 = False
                            colorcv2 = False
                        if abs(yt1 - ys1) < 15 and abs(xt1 - xs1) < 15 and len(results.multi_handedness) == 1:
                            ox1 = int(xt1-15)
                            oy1 = int(yt1-15)
                if ox3 <= xt1 <= ox3+30 and oy3 <= yt1 <= oy3+30 and len(results.multi_handedness) == 1:
                        if abs(ys - ys1) < 20 and abs(xs - xs1) < 20 and len(results.multi_handedness) == 1:
                            colorcv1 = True
                            colorcv2 = False
                        if abs(yt1 - ys1) < 15 and abs(xt1 - xs1) < 15 and len(results.multi_handedness) == 1:
                            ox3 = int(xt1-15)
                            oy3 = int(yt1-15)
                if ox5 <= xt1 <= ox5+30 and oy5 <= yt1 <= oy5+30 and len(results.multi_handedness) == 1:
                        if abs(ys - ys1) < 20 and abs(xs - xs1) < 20 and len(results.multi_handedness) == 1:
                            colorcv1 = False
                            colorcv2 = True
                        if abs(yt1 - ys1) < 15 and abs(xt1 - xs1) < 15 and len(results.multi_handedness) == 1:
                            ox5 = int(xt1-15)
                            oy5 = int(yt1-15)

                if h1 == True:
                    if len(results.multi_handedness) == 1:
                        # pyautogui.moveTo(xt1*2, yt1*2)
                        screen.blit(mouse_player, (xt1*2,yt1*2))
                        # pygame.draw.rect(screen, RED, (xt1*2,yt1*2,64,46),2)
                        # select = pygame.draw.circle(screen, GREEN, (xt1*2,yt1*2), 10)
                    
                    
                    finger_color1 = (255,0,255)
                    finger_color2 = (255,0,255)
                    finger_color4 = (255,0,255)
                    
                    screen.blit(ufo, (x1_menu,y1_menu))
                    screen.blit(ufo, (x2_menu,y2_menu))
                    screen.blit(ufo, (x3_menu,y3_menu))
                    screen.blit(ufo, (x4_menu,y4_menu))
                    screen.blit(ufo, (x5_menu,y5_menu))
                    
                    bienchay1_menu += 1
                    bienchay3_menu += 1
                    bienchay4_menu += 1
                    bienchay5_menu += 1
                    bienchay6_menu += 1
                    if bienchay1_menu == 1:
                        x6_menu = x1_menu + 25
                    if bienchay3_menu == 1:
                        x8_menu = x2_menu + 25
                    if bienchay4_menu == 1:
                        x9_menu = x3_menu + 25
                    if bienchay5_menu == 1:
                        x10_menu = x4_menu + 25
                    if bienchay6_menu == 1:
                        x11_menu = x5_menu + 25
                        
                    screen.blit(rocket_menu, (x6_menu, y6_menu))
                    screen.blit(rocket_menu, (x8_menu, y8_menu))
                    screen.blit(rocket_menu, (x9_menu, y9_menu))
                    screen.blit(rocket_menu, (x10_menu, y10_menu))
                    screen.blit(rocket_menu, (x11_menu, y11_menu))

                    if y6_menu < 0:
                        y6_menu = height - 20
                        bienchay1_menu = 0

                    if y8_menu < 0:
                        y8_menu = height - 50
                        bienchay3_menu = 0

                    if y9_menu < 0:
                        y9_menu = height - 80
                        bienchay4_menu = 0

                    if y10_menu < 0:
                        y10_menu = height - 110
                        bienchay5_menu = 0

                    if y11_menu < 0:
                        y11_menu = height - 130
                        bienchay6_menu = 0
                    y6_menu-=1
                    y8_menu-=1
                    y9_menu-=1
                    y10_menu-=1
                    y11_menu-=1
                    
                    if g1_menu == True:
                        x1_menu += 1
                    if g1_menu == False:
                        x1_menu -= 1
                    if x1_menu>width-50:
                        g1_menu = False
                        x1_menu = width-50
                    if x1_menu < 0:
                        g1_menu = True
                        x1_menu = 0
                        
                    if g2_menu == True:
                        x2_menu -= 1.5
                    if g2_menu == False:
                        x2_menu += 1.5
                    if x2_menu>width-50:
                        g2_menu = True
                        x2_menu = width-50
                    if x2_menu < 0:
                        g2_menu = False
                        x2_menu = 0
                        
                    if g3_menu == True:
                        x3_menu += 2
                    if g3_menu == False:
                        x3_menu -= 2
                    if x3_menu>width-50:
                        g3_menu = False
                        x3_menu = width-50
                    if x3_menu < 0:
                        g3_menu = True
                        x3_menu = 0
                        
                    if g4_menu == True:
                        x4_menu -= 2.5
                    if g4_menu == False:
                        x4_menu += 2.5
                    if x4_menu>width-50:
                        g4_menu = True
                        x4_menu = width-50
                    if x4_menu < 0:
                        g4_menu = False
                        x4_menu = 0
                        
                    if g5_menu == True:
                        x5_menu += 3
                    if g5_menu == False:
                        x5_menu -= 3
                    if x5_menu>width-50:
                        g5_menu = False
                        x5_menu = width-50
                    if x5_menu < 0:
                        g5_menu = True
                        x5_menu = 0
                    
                    mouse = pygame.mouse.get_pos()
                    left, middle, right = pygame.mouse.get_pressed()
                    
                    if width/2-90 <= xt1*2 <= width/2+90 and height/2-100 <= yt1*2+32 <= height/2-60 and len(results.multi_handedness) == 1:
                    # if select.colliderect(pygame.draw.rect(screen, BLACK, [width/2-90, height/2-100, 180, 40],2)):
                        pygame.draw.rect(screen, RED, [width/2-90, height/2-100, 180, 40],2)
                        bien1 += 1
                        if bien1 == 1:
                            shot.play(0)
                        color1_menu = RED
                        if len(results.multi_handedness) == 1 and abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                            h0 = True
                            h1 = False
                            h2 = False
                            h3 = False
                            finger_color1 = WHITE
                            finger_color2 = WHITE
                    else:
                        bien1 = 0
                        color1_menu = GREEN

                    if width/2-90 <= xt1*2 <= width/2+90 and height/2-50 <= yt1*2+32 <= height/2-10 and len(results.multi_handedness) == 1:
                    # if select.colliderect(pygame.draw.rect(screen, BLACK, [width/2-90, height/2-50, 180, 40],2)):
                        pygame.draw.rect(screen, RED, [width/2-90, height/2-50, 180, 40],2)
                        bien2 += 1
                        if bien2 == 1:
                            shot.play(0)
                        color2_menu = RED
                        if len(results.multi_handedness) == 1 and abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                            h2 = True
                            h1 = False
                            h3 = False
                            h0 = False
                    else:
                        bien2 = 0
                        color2_menu = GREEN

                    if width/2-90 <= xt1*2 <= width/2+90 and height/2 <= yt1*2+32 <= height/2+40 and len(results.multi_handedness) == 1:
                    # if select.colliderect(pygame.draw.rect(screen, BLACK, [width/2-90, height/2, 180, 40],2)):
                        pygame.draw.rect(screen, RED, [width/2-90, height/2, 180, 40],2)
                        bien3 += 1
                        if bien3 == 1:
                            shot.play(0)
                        color3_menu = RED
                        if len(results.multi_handedness) == 1 and abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                            h3 = True
                            h1 = False
                            h2 = False
                            h0 = False
                    else:
                        bien3 = 0
                        color3_menu = GREEN
                        
                    if width/2-90 <= xt1*2 <= width/2+90 and height/2+50 <= yt1*2+32 <= height/2+90 and len(results.multi_handedness) == 1:
                    # if select.colliderect(pygame.draw.rect(screen, BLACK, [width/2-90, height/2+50, 180, 40],2)):
                        pygame.draw.rect(screen, RED, [width/2-90, height/2+50, 180, 40],2)
                        bien4 += 1
                        if bien4 == 1:
                            shot.play(0)
                        color5_menu = RED
                        if len(results.multi_handedness) == 1 and abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                            pygame.quit()
                            finger_color1 = WHITE
                            finger_color2 = WHITE
                    else:
                        bien4 = 0
                        color5_menu = GREEN
                    
                    screen.blit(text , (width/2-text.get_width()/2,height/2-100))
                    screen.blit(hd , (width/2-hd.get_width()/2,height/2-50))
                    screen.blit(scores, (width/2-scores.get_width()/2, height/2))
                    screen.blit(quitt, (width/2-quitt.get_width()/2, height/2+50))
                    ship_menup = pygame.transform.rotate(ship_menu, rota)
                    screen.blit(ship_menup, (xchar,ychar))
                    rota += 0.8
                    xchar += 1
                    if xchar > width:
                        xchar = -40
                        ychar = random.randint(10,height/2-100)
                    
                    pygame.display.update()
                    pygame.display.flip()
                    clock.tick(60)
                    
                    
                    
                    
                            
                if h2 == True:
                    # if len(results.multi_handedness) == 1:
                    #     pyautogui.moveTo(xt1*2, yt1*2)
                    if len(results.multi_handedness) == 1:
                        screen.blit(mouse_player, (xt1*2,yt1*2))
                        # select = pygame.draw.circle(screen, GREEN, (xt1*2,yt1*2), 10)
                        
                    finger_color1 = (255,0,255)
                    finger_color2 = (255,0,255)
                    finger_color4 = (255,0,255)
                    
                    back = smallfont.render('BACK' , True , color_back_menu)
                    smallfont_guide = pygame.font.SysFont('Chiller',20)
                    hd2 = smallfont_guide.render('- Game using hand gestures to move the character, the difficulty increases with levels (1-10)' , True , color_menu)
                    hd3 = smallfont_guide.render('To the right' , True , color_menu)
                    hd4 = smallfont_guide.render('To the left' , True , color_menu)
                    hd5 = smallfont_guide.render('Shot the normal bullet' , True , color_menu)
                    hd6 = smallfont_guide.render('Shot the target bullet' , True , color_menu)
                    hd7 = smallfont_guide.render('Shot the function bullet' , True , color_menu)
                    hd8 = smallfont_guide.render('Pause game' , True , color_menu)
                    hd9 = smallfont_guide.render("Don't touch" , True , color_menu)
                    hd10 = smallfont_guide.render('Functional bullets' , True , color_menu)
                    hd11 = smallfont_guide.render("Defend" , True , color_menu)
                    hd12 = smallfont_guide.render('Add the normal bullets' , True , color_menu)
                    mouse = pygame.mouse.get_pos()
                    left, mid, right = pygame.mouse.get_pressed()
                    if width/2-90 <= xt1*2 <= width/2+90 and height/2+200 <= yt1*2+32 <= height/2+240 and len(results.multi_handedness) == 1:
                    # if select.colliderect(pygame.draw.rect(screen, BLACK, [width/2-90, height/2+200, 180, 40],2)):
                        pygame.draw.rect(screen, RED, [width/2-90, height/2+200, 180, 40],2)
                        bien5 += 1
                        if bien5 == 1:
                            shot.play(0)
                        if len(results.multi_handedness) == 1 and abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                            h2 = False
                            h3 = False
                            h0 = False
                            h1 = True
                            finger_color1 = WHITE
                            finger_color2 = WHITE
                        color_back_menu = RED
                    else:
                        bien5 = 0
                        color_back_menu = GREEN
                    screen.blit(turn_right, (10, 200))
                    screen.blit(turn_left, (10, 350))
                    screen.blit(fire_bullet, (160, 200))
                    screen.blit(fire_yellow, (160, 350))
                    screen.blit(fire_3tia, (310, 200))
                    screen.blit(pausehand, (310, 350))
                    screen.blit(hd2, (10, 140))
                    screen.blit(hd3, (10+30, 320))
                    screen.blit(hd4, (10+30, 470))
                    screen.blit(hd5, (160, 320))
                    screen.blit(hd6, (160, 470))
                    screen.blit(hd7, (310, 320))
                    screen.blit(hd8, (400, 470))
                    
                    screen.blit(rocket, (570, 250))
                    screen.blit(bullet_fc, (570, 300))
                    screen.blit(protect_image, (570, 350))
                    screen.blit(bullet_alein1, (570, 400))
                    screen.blit(hd9, (620, 250))
                    screen.blit(hd10, (620, 300))
                    screen.blit(hd11, (620, 350))
                    screen.blit(hd12, (630, 400))
                    screen.blit(back, (width/2-back.get_width()/2, height/2+200))
                    pygame.display.update()
                    
                
                
                if h3 == True:
                    # if len(results.multi_handedness) == 1:
                    #     pyautogui.moveTo(xt1*2, yt1*2)
                    if len(results.multi_handedness) == 1:
                        screen.blit(mouse_player, (xt1*2,yt1*2))
                        # select = pygame.draw.circle(screen, GREEN, (xt1*2,yt1*2), 10)
                        
                    finger_color1 = (255,0,255)
                    finger_color2 = (255,0,255)
                    finger_color4 = (255,0,255)
                    
                    score_font = pygame.font.SysFont('Chiller', 60)
                    diem_time = score_font.render('TIME' , True , color_menu)
                    diem_level = score_font.render('LEVEL' , True , color_menu)
                    back = smallfont.render('BACK' , True , color_back_menu)
                    mouse = pygame.mouse.get_pos()
                    left, mid, right = pygame.mouse.get_pressed()
                    if width/2-90 <= xt1*2 <= width/2+90 and height/2+200 <= yt1*2+32 <= height/2+240 and len(results.multi_handedness) == 1:
                    # if select.colliderect(pygame.draw.rect(screen, BLACK, [width/2-90, height/2+200, 180, 40],2)):
                        pygame.draw.rect(screen, RED, [width/2-90, height/2+200, 180, 40],2)
                        bien5 += 1
                        if bien5 == 1:
                            shot.play(0)
                        if len(results.multi_handedness) == 1 and abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                            h2 = False
                            h3 = False
                            h1 = True
                            finger_color1 = WHITE
                            finger_color2 = WHITE
                        color_back_menu = RED
                    else:
                        bien5 = 0
                        color_back_menu = GREEN
                    screen.blit(diem_time, (width/2 - 130 - diem_time.get_width()/2, height/2-130))
                    screen.blit(diem_level, (width/2 + 130 - diem_level.get_width()/2, height/2-130))
                    
                    
                    score_font = pygame.font.SysFont('Gigi',30)
                    textt = score_font.render("1.     ", True, WHITE)
                    screen.blit(textt,(width/2 - 250 - textt.get_width()/2, height/2-50))
                    textt = score_font.render("2.     ", True, WHITE)
                    screen.blit(textt,(width/2 - 250 - textt.get_width()/2, height/2-20))
                    textt = score_font.render("3.     ", True, WHITE)
                    screen.blit(textt,(width/2 - 250 - textt.get_width()/2, height/2+10))
                    textt = score_font.render("4.     ", True, WHITE)
                    screen.blit(textt,(width/2 - 250 - textt.get_width()/2, height/2+40))
                    textt = score_font.render("5.     ", True, WHITE)
                    screen.blit(textt,(width/2 - 250 - textt.get_width()/2, height/2+70))
                    lines_in_reverse_order = read_reverse('time_his.txt')
                    for line in lines_in_reverse_order:
                        arr1.append(line)
                    lines_in_reverse_order2 = read_reverse('level_his.txt')
                    for line in lines_in_reverse_order2:
                        arr2.append(line)
                    textt = score_font.render(arr1[0], True, WHITE)
                    screen.blit(textt,(width/2 - 130 - textt.get_width()/2, height/2-50))
                    textt = score_font.render(arr1[1], True, WHITE)
                    screen.blit(textt,(width/2 - 130 - textt.get_width()/2, height/2-20))
                    textt = score_font.render(arr1[2], True, WHITE)
                    screen.blit(textt,(width/2 - 130 - textt.get_width()/2, height/2+10))
                    textt = score_font.render(arr1[3], True, WHITE)
                    screen.blit(textt,(width/2 - 130 - textt.get_width()/2, height/2+40))
                    textt = score_font.render(arr1[4], True, WHITE)
                    screen.blit(textt,(width/2 - 130 - textt.get_width()/2, height/2+70))
                    
                    textt = score_font.render(arr2[0], True, WHITE)
                    screen.blit(textt,(width/2 + 130 - textt.get_width()/2, height/2-50))
                    textt = score_font.render(arr2[1], True, WHITE)
                    screen.blit(textt,(width/2 + 130 - textt.get_width()/2, height/2-20))
                    textt = score_font.render(arr2[2], True, WHITE)
                    screen.blit(textt,(width/2 + 130 - textt.get_width()/2, height/2+10))
                    textt = score_font.render(arr2[3], True, WHITE)
                    screen.blit(textt,(width/2 + 130 - textt.get_width()/2, height/2+40))
                    textt = score_font.render(arr2[4], True, WHITE)
                    screen.blit(textt,(width/2 + 130 - textt.get_width()/2, height/2+70))
                    
                    
                    screen.blit(back, (width/2-back.get_width()/2, height/2+200))
                    pygame.display.update()
                
                

                if h0 == True:
                    
                    screen.fill(BLACK)
                    screen.blit(background_game, (0,0))
                    
                    cv2.circle(imgRGB, (int(xt), int(yt)), 9, finger_color3, -1)
                    finger_color3 = (255,0,255)
                    
                    for b in range(100):
                        yc.append(random.randint(-GetSystemMetrics(1),-10))
                        ycc.append(random.randint(0,GetSystemMetrics(0)))
                    for b in range(100):
                        if b%3==0:
                            h1=2
                        elif b%2==0 and b%3!=0:
                            h1=1.5
                        else:
                            h1=1
                        hh.append(h1)
                        pygame.draw.circle(screen,WHITE,(ycc[b],yc[b]),hh[b])
                        yc[b]+=i1_space
                        ycc[b]+=i2_space
                    for b in range(100):
                        if yc[b]> GetSystemMetrics(1):
                            yc[b]=random.randint(-300,0)
                            ycc[b]=random.randint(0,GetSystemMetrics(0))
                    i1_space = 8
                    i2_space = 0
                    # b = pygame.key.get_pressed()
                    # if b[pygame.K_UP]: i1-=3
                    # if b[pygame.K_DOWN]: i1+=3
                    # if b[pygame.K_LEFT]: i2-=3
                    # if b[pygame.K_RIGHT]: i2+=3
                    
                    # if target1_display == True:
                    #     screen.blit(background, (xtarget,ytarget))
                    #     target_box = (xtarget,ytarget,65,50)
                    #     target = pygame.draw.rect(screen,colortarget1,target_box,2)
                    
                    # screen.blit(ship, (x, y))
                    ship_box = (x,y,64,64)
                    shipp = pygame.draw.rect(screen,color_ship,ship_box,2)
                    # xtarget = width/2
                    
                    if lose1 == False:
                        if run_boss1 == True:
                            if victory == False:
                                xtarget += 1
                            if xtarget > 620:
                                run_boss1 = False
                        if run_boss1 == False:
                            if victory == False:
                                xtarget -= 1
                            if xtarget < 150:
                                run_boss1 = True
                    
                    if target1_display == True:
                        if bien_boss1 % 100 == 0:
                            bullets_boss1.append([xtarget+30,ytarget])
                        for b in range(len(bullets_boss1)):
                            if lose1 == False:
                                bullets_boss1[b][1] += 5
                            # if lose1 == True:
                            #     bullets_boss1[b][1] -= 5
                        for bullet in bullets_boss1[:]:
                            if bullet[1] > height:
                                bullets_boss1.remove(bullet)
                        for bullet in bullets_boss1:
                            a = screen.blit(rocket, (bullet[0], bullet[1]))
                        for bullet in bullets_boss1:
                            box_boss1 = (bullet[0],bullet[1],20,28)
                            n_boss1 = pygame.draw.rect(screen,BLACK,box_boss1,2)
                            if protect0 == False:
                                if n_boss1.colliderect(shipp):
                                    lose1 = True
                                    lose = True
                        if lose1 == False:
                            bien_boss1 += 1
                        # if lose1 == True:
                        #     bien_boss1 -= 1
                    
                    if target1_display == True:
                        screen.blit(background, (xtarget,ytarget))
                        target_box = (xtarget,ytarget,65,50)
                        target = pygame.draw.rect(screen,colortarget1,target_box,2)
                                    
                    if level > 0:
                        if ufo1_play == True:
                            screen.blit(ufo, (x1,y1))
                            v1=pygame.draw.rect(screen,color1,(x1,y1,55,35),1)
                            bienx1_die = 0
                        if level == 1:
                            screen.blit(ufo, (x2,y2))
                            screen.blit(ufo, (x3,y3))
                            screen.blit(ufo, (x4,y4))
                            screen.blit(ufo, (x5,y5))
                        if ufo1_play == False:
                            ufo1_bien += 1
                            bienx1_die += 1
                            if bienx1_die == 1:
                                x1_die = x1
                            if ufo1_bien > 0 and ufo1_bien < 50:
                                screen.blit(boom, (x1_die,y1))
                            if ufo1_bien > 400:
                                ufo1_play = True
                                ufo1_time = 0
                                ufo1_bien = 0
                                color1 = BLACK
                                t1 = True
                                bienchay1 = 0
                                y6 = 100
                                bienx1_die = 0
                            if lose1 == True:
                                ufo1_bien -= 1
                    if level > 1:
                        if ufo2_play == True:
                            screen.blit(ufo, (x2,y2))
                            v2=pygame.draw.rect(screen,color2,(x2,y2,55,35),1)
                            bienx2_die = 0
                        if level == 2:
                            screen.blit(ufo, (x3,y3))
                            screen.blit(ufo, (x4,y4))
                            screen.blit(ufo, (x5,y5))
                        if ufo2_play == False:
                            ufo2_bien += 1
                            bienx2_die += 1
                            if bienx2_die == 1:
                                x2_die = x2
                            if ufo2_bien > 0 and ufo2_bien < 50:
                                screen.blit(boom, (x2_die,y2))
                            if ufo2_bien > 600:
                                ufo2_play = True
                                ufo2_time = 0
                                ufo2_bien = 0
                                color2 = BLACK
                                t2 = True
                                bienchay3 = 0
                                y8 = 150
                                bienx2_die = 0
                            if lose1 == True:
                                ufo2_bien -= 1
                    if level > 2:
                        if ufo3_play == True:
                            screen.blit(ufo, (x3,y3))
                            v3=pygame.draw.rect(screen,color3,(x3,y3,55,35),1)
                            bienx3_die = 0
                        if level == 3:
                            screen.blit(ufo, (x4,y4))
                            screen.blit(ufo, (x5,y5))
                        if ufo3_play == False:
                            ufo3_bien += 1
                            bienx3_die += 1
                            if bienx3_die == 1:
                                x3_die = x3
                            if ufo3_bien > 0 and ufo3_bien < 50:
                                screen.blit(boom, (x3_die,y3))
                            if ufo3_bien > 800:
                                ufo3_play = True
                                ufo3_time = 0
                                ufo3_bien = 0
                                color3 = BLACK
                                t3 = True
                                bienchay4 = 0
                                y9 = 200
                                bienx3_die = 0
                            if lose1 == True:
                                ufo3_bien -= 1
                    if level > 3:
                        if ufo4_play == True:
                            screen.blit(ufo, (x4,y4))
                            v4=pygame.draw.rect(screen,color4,(x4,y4,55,35),1)
                            bienx4_die = 0
                        if level == 4:
                            screen.blit(ufo, (x5,y5))
                        if ufo4_play == False:
                            ufo4_bien += 1
                            bienx4_die += 1
                            if bienx4_die == 1:
                                x4_die = x4
                            if ufo4_bien > 0 and ufo4_bien < 50:
                                screen.blit(boom, (x4_die,y4))
                            if ufo4_bien > 1000:
                                ufo4_play = True
                                ufo4_time = 0
                                ufo4_bien = 0
                                color4 = BLACK
                                t4 = True
                                bienchay5 = 0
                                y10 = 250
                                bienx4_die = 0
                            if lose1 == True:
                                ufo4_bien -= 1
                        
                    if level > 4:
                        if ufo5_play == True:
                            screen.blit(ufo, (x5,y5))
                            v5=pygame.draw.rect(screen,color5,(x5,y5,55,35),1)
                            bienx5_die = 0
                        if ufo5_play == False:
                            ufo5_bien += 1
                            bienx5_die += 1
                            if bienx5_die == 1:
                                x5_die = x5
                            if ufo5_bien > 0 and ufo5_bien < 50:
                                screen.blit(boom, (x5_die,y5))
                            if ufo5_bien > 1200:
                                ufo5_play = True
                                ufo5_time = 0
                                ufo5_bien = 0
                                color5 = BLACK
                                t5 = True
                                bienchay6 = 0
                                y11 = 300
                                bienx5_die = 0
                            if lose1 == True:
                                ufo5_bien -= 1
                        
                    if level > 5:
                        if ufo1_play == True:
                            bienchay1 += 1
                            if bienchay1 == 1:
                                x6 = x1 + 25
                            screen.blit(rocket, (x6, y6))
                            v6=pygame.draw.rect(screen,BLACK,(x6, y6, 20, 28),1)
                            if protect0 == False:
                                if v6.colliderect(shipp):
                                    lose = True
                                    lose1 = True
                            if y6 > 600:
                                y6 = 100
                                bienchay1 = 0
                            if lose1 == False:
                                y6+=2
                            # if lose1 == True:
                            #     y6-=2
                        
                        if ufo2_play == True:
                            bienchay3 += 1
                            if bienchay3 == 1:
                                x8 = x2 + 25
                            screen.blit(rocket, (x8, y8))
                            v8=pygame.draw.rect(screen,BLACK,(x8, y8, 20, 28),1)
                            if protect0 == False:
                                if v8.colliderect(shipp):
                                    lose = True
                                    lose1 = True
                            if y8 > 600:
                                y8 = 150
                                bienchay3 = 0
                            if lose1 == False:
                                y8+=2
                            # if lose1 == True:
                            #     y8-=2
                        
                        if ufo3_play == True:
                            bienchay4 += 1
                            if bienchay4 == 1:
                                x9 = x3 + 25
                            screen.blit(rocket, (x9, y9))
                            v9=pygame.draw.rect(screen,BLACK,(x9, y9, 20, 28),1)
                            if protect0 == False:
                                if v9.colliderect(shipp):
                                    lose = True
                                    lose1 = True
                            if y9 > 600:
                                y9 = 200
                                bienchay4 = 0
                                
                            if lose1 == False:
                                y9+=2
                            # if lose1 == True:
                            #     y9-=2
                        
                        if ufo4_play == True:
                            bienchay5 += 1
                            if bienchay5 == 1:
                                x10 = x4 + 25
                            screen.blit(rocket, (x10, y10))
                            v10=pygame.draw.rect(screen,BLACK,(x10, y10, 20, 28),1)
                            if protect0 == False:
                                if v10.colliderect(shipp):
                                    lose = True
                                    lose1 = True
                            if y10 > 600:
                                y10 = 250
                                bienchay5 = 0
                                
                            if lose1 == False:
                                y10+=2
                            # if lose1 == True:
                            #     y10-=2
                        
                        if ufo5_play == True:
                            bienchay6 += 1
                            if bienchay6 == 1:
                                x11 = x5 + 25
                            screen.blit(rocket, (x11, y11))
                            v11=pygame.draw.rect(screen,BLACK,(x11, y11, 20, 28),1)
                            if protect0 == False:
                                if v11.colliderect(shipp):
                                    lose = True
                                    lose1 = True
                            if y11 > 600:
                                y11 = 300
                                bienchay6 = 0
                            if lose1 == False:
                                y11+=2
                            # if lose1 == True:
                            #     y11-=2
                        
                            
                    # screen.blit(bullet_alein1, (300,300))
                    # screen.blit(player2, (width/2,height/2))
                        
                    if level > 6:
                        d1=pygame.draw.rect(screen,colord1,(xd1, yd1, 20, 20))
                        pygame.draw.circle(screen, GREEN, (xd1+10,yd1+10), 2)
                        d2=pygame.draw.rect(screen,colord2,(xd2, yd2, 20, 20))
                        pygame.draw.circle(screen, GREEN, (xd2+10,yd2+10), 2)
                        d3=pygame.draw.rect(screen,colord12,(xd1+20, yd1+9, xd2-(xd1+20), 2))
                        
                        if biend1 == True and biend2 == True:
                            colord12 = GREEN
                            
                    if level > 7:
                        # 2 target
                        target_bullet = 2
                        # xtarget = width/2 - 150
                        # xtarget2 = width/2 + 150
                        
                        # if target2_display == True:
                        #     screen.blit(background, (xtarget2,ytarget2))
                        #     target_box2 = (xtarget2,ytarget2,65,50)
                        #     target2 = pygame.draw.rect(screen,colortarget2,target_box2,2)
                        
                        if target2_display == True:
                            if bien_boss2 % 100 == 0:
                                bullets_boss2.append([xtarget2+30,ytarget2])
                            for b in range(len(bullets_boss2)):
                                if lose1 == False:
                                    bullets_boss2[b][1] += 5
                                # if lose1 == True:
                                #     bullets_boss2[b][1] -= 5
                            for bullet in bullets_boss2[:]:
                                if bullet[1] > height:
                                    bullets_boss2.remove(bullet)
                            for bullet in bullets_boss2:
                                a = screen.blit(rocket, (bullet[0], bullet[1]))
                            for bullet in bullets_boss2:
                                box_boss2 = (bullet[0],bullet[1],20,28)
                                n_boss2 = pygame.draw.rect(screen,BLACK,box_boss2,2)
                                if protect0 == False:
                                    if n_boss2.colliderect(shipp):
                                        lose1 = True
                                        lose = True
                            if lose1 == False:
                                bien_boss2 += 1
                            # if lose1 == True:
                            #     bien_boss2 -= 1
                        
                        if lose1 == False:
                            if run_boss2 == True:
                                if victory == False:
                                    xtarget2 += 1
                                if xtarget2 > 620:
                                    run_boss2 = False
                            if run_boss2 == False:
                                if victory == False:
                                    xtarget2 -= 1
                                if xtarget2 < 150:
                                    run_boss2 = True
                                
                        if target2_display == True:
                            screen.blit(background, (xtarget2,ytarget2))
                            target_box2 = (xtarget2,ytarget2,65,50)
                            target2 = pygame.draw.rect(screen,colortarget2,target_box2,2)
                        # function bullet
                        bullet_fc = pygame.transform.scale(bullet_fc, (25,25))
                        if biendem_three2 == True:
                            if tt == False:
                                screen.blit(bullet_fc, (x12,y12))
                                v12=pygame.draw.rect(screen,colorv12,(x12,y12,25,25), sizev12) #3
                        
                        if biendem_three2 == True:
                            if tt == False:
                                if shipp.colliderect(v12): #3
                                    # bienchay7 += 1
                                    # colorv12 = BLACK
                                    tt = True
                                    # sizev12 = 0
                                    bullet_func.play(0)
                                
                        # Dùng thời gian để bắn đạn 3 tia sau khi lấy chức năng
                        # if tt == True:
                        #     dem1 += 1

                        # if tt == True:
                        #     b = pygame.key.get_pressed()
                        #     if u%10==0:
                        #         if b[pygame.K_z]:
                        #             bullets_three1.append([x+16,y])
                        #             bullets_three2.append([x+16,y])
                        #             bullets_three3.append([x+16,y])
                        
                        if tt == True:
                            b = pygame.key.get_pressed()
                            # if u%10==0:
                            if move == True:
                                if quantity_three > 0:
                                    # if fingerCount == 4:
                                    #     if handLabel == 'Right' and abs(yt - yt1) < 10:
                                    if len(results.multi_handedness) == 1 and abs(xt1 - xs1) < 20:
                                        if u33 == False:
                                                shot.play(0)
                                                bullets_three1.append([x+16,y])
                                                bullets_three2.append([x+16,y])
                                                bullets_three3.append([x+16,y])
                                                quantity_three -= 1
                                                u33 = True
                                        finger_color2 = WHITE
                                        finger_color4 = WHITE
                        if u33 == True:
                            u3 += 1
                        if u3 > 10:
                            u3 = 0
                            u33 = False

                        for b in range(len(bullets_three1)):
                            if lose1 == False:
                                bullets_three1[b][1] -= 5
                                bullets_three1[b][0] -= 3
                        for b in range(len(bullets_three2)):
                            if lose1 == False:
                                bullets_three2[b][1] -= 5
                        for b in range(len(bullets_three3)):
                            if lose1 == False:
                                bullets_three3[b][1] -= 5
                                bullets_three3[b][0] += 3
                        for bullet in bullets_three1[:]:
                            if bullet[1] < -30:
                                bullets_three1.remove(bullet)
                        for bullet in bullets_three2[:]:
                            if bullet[1] < -30:
                                bullets_three2.remove(bullet)
                        for bullet in bullets_three3[:]:
                            if bullet[1] < -30:
                                bullets_three3.remove(bullet)
                        for bullet in bullets_three1:
                            a = screen.blit(bullet_alein1, (bullet[0], bullet[1]))
                        for bullet in bullets_three2:
                            a = screen.blit(bullet_alein1, (bullet[0], bullet[1]))
                        for bullet in bullets_three3:
                            a = screen.blit(bullet_alein1, (bullet[0], bullet[1]))
                        for bullet in bullets_three1:
                            box = (bullet[0],bullet[1],20,40)
                            n = pygame.draw.rect(screen,BLACK,box,2)
                            if ufo1_play == True:
                                if n.colliderect(v1):
                                    ufo1_time += 1
                                    if ufo1_time == 3:
                                        ufo_boom.play(0)
                                        ufo1_play = False
                                    color1 = GREEN
                                    t1 = False
                                    if ufo1_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three1.remove(bullet)
                                    continue
                            if ufo2_play == True:
                                if n.colliderect(v2):
                                    ufo2_time += 1
                                    if ufo2_time == 3:
                                        ufo_boom.play(0)
                                        ufo2_play = False
                                    color2 = GREEN
                                    t2 = False
                                    if ufo2_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three1.remove(bullet)
                                    continue
                            if ufo3_play == True:
                                if n.colliderect(v3):
                                    ufo3_time += 1
                                    if ufo3_time == 3:
                                        ufo_boom.play(0)
                                        ufo3_play = False
                                    color3 = GREEN
                                    t3 = False
                                    if ufo3_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three1.remove(bullet)
                                    continue
                            if ufo4_play == True:
                                if n.colliderect(v4):
                                    ufo4_time += 1
                                    if ufo4_time == 3:
                                        ufo_boom.play(0)
                                        ufo4_play = False
                                    color4 = GREEN
                                    t4 = False
                                    if ufo4_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three1.remove(bullet)
                                    continue
                            if ufo5_play == True:
                                if n.colliderect(v5):
                                    ufo5_time += 1
                                    if ufo5_time == 3:
                                        ufo_boom.play(0)
                                        ufo5_play = False
                                    color5 = GREEN
                                    t5 = False
                                    if ufo5_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three1.remove(bullet)
                                    continue
                            if n.colliderect(d1):
                                bullet_ufo.play(0)
                                colord1 = GREEN
                                biend1 = True
                                bullets_three1.remove(bullet)
                            elif n.colliderect(d2):
                                bullet_ufo.play(0)
                                colord2 = GREEN
                                biend2 = True
                                bullets_three1.remove(bullet)
                            if n.colliderect(v1) or n.colliderect(v2) or n.colliderect(v3) or n.colliderect(v4) or n.colliderect(v5) or n.colliderect(d1) or n.colliderect(d2):
                                bullet_ufo.play(0)
                        for bullet in bullets_three2:
                            box = (bullet[0],bullet[1],20,40)
                            n = pygame.draw.rect(screen,BLACK,box,2)
                            if ufo1_play == True:
                                if n.colliderect(v1):
                                    ufo1_time += 1
                                    if ufo1_time == 3:
                                        ufo_boom.play(0)
                                        ufo1_play = False
                                    color1 = GREEN
                                    t1 = False
                                    if ufo1_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three2.remove(bullet)
                                    continue
                            if ufo2_play == True:
                                if n.colliderect(v2):
                                    ufo2_time += 1
                                    if ufo2_time == 3:
                                        ufo_boom.play(0)
                                        ufo2_play = False
                                    color2 = GREEN
                                    t2 = False
                                    if ufo2_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three2.remove(bullet)
                                    continue
                            if ufo3_play == True:
                                if n.colliderect(v3):
                                    ufo3_time += 1
                                    if ufo3_time == 3:
                                        ufo_boom.play(0)
                                        ufo3_play = False
                                    color3 = GREEN
                                    t3 = False
                                    if ufo3_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three2.remove(bullet)
                                    continue
                            if ufo4_play == True:
                                if n.colliderect(v4):
                                    ufo4_time += 1
                                    if ufo4_time == 3:
                                        ufo_boom.play(0)
                                        ufo4_play = False
                                    color4 = GREEN
                                    t4 = False
                                    if ufo4_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three2.remove(bullet)
                                    continue
                            if ufo5_play == True:
                                if n.colliderect(v5):
                                    ufo5_time += 1
                                    if ufo5_time == 3:
                                        ufo_boom.play(0)
                                        ufo5_play = False
                                    color5 = GREEN
                                    t5 = False
                                    if ufo5_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three2.remove(bullet)
                                    continue
                            if n.colliderect(d1):
                                bullet_ufo.play(0)
                                colord1 = GREEN
                                biend1 = True
                                bullets_three2.remove(bullet)
                            elif n.colliderect(d2):
                                bullet_ufo.play(0)
                                colord2 = GREEN
                                biend2 = True
                                bullets_three2.remove(bullet)
                            if n.colliderect(v1) or n.colliderect(v2) or n.colliderect(v3) or n.colliderect(v4) or n.colliderect(v5) or n.colliderect(d1) or n.colliderect(d2):
                                bullet_ufo.play(0)
                        for bullet in bullets_three3:
                            
                            box = (bullet[0],bullet[1],20,40)
                            n = pygame.draw.rect(screen,BLACK,box,2)
                            if ufo1_play == True:
                                if n.colliderect(v1):
                                    ufo1_time += 1
                                    if ufo1_time == 3:
                                        ufo_boom.play(0)
                                        ufo1_play = False
                                    color1 = GREEN
                                    t1 = False
                                    if ufo1_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three3.remove(bullet)
                                    continue
                            if ufo2_play == True:
                                if n.colliderect(v2):
                                    ufo2_time += 1
                                    if ufo2_time == 3:
                                        ufo_boom.play(0)
                                        ufo2_play = False
                                    color2 = GREEN
                                    t2 = False
                                    if ufo2_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three3.remove(bullet)
                                    continue
                            if ufo3_play == True:
                                if n.colliderect(v3):
                                    ufo3_time += 1
                                    if ufo3_time == 3:
                                        ufo_boom.play(0)
                                        ufo3_play = False
                                    color3 = GREEN
                                    t3 = False
                                    if ufo3_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three3.remove(bullet)
                                    continue
                            if ufo4_play == True:
                                if n.colliderect(v4):
                                    ufo4_time += 1
                                    if ufo4_time == 3:
                                        ufo_boom.play(0)
                                        ufo4_play = False
                                    color4 = GREEN
                                    t4 = False
                                    if ufo4_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three3.remove(bullet)
                                    continue
                            if ufo5_play == True:
                                if n.colliderect(v5):
                                    ufo5_time += 1
                                    if ufo5_time == 3:
                                        ufo_boom.play(0)
                                        ufo5_play = False
                                    color5 = GREEN
                                    t5 = False
                                    if ufo5_play == True:
                                        bullet_ufo.play(0)
                                    bullets_three3.remove(bullet)
                                    continue
                            if n.colliderect(d1):
                                bullet_ufo.play(0)
                                colord1 = GREEN
                                biend1 = True
                                bullets_three3.remove(bullet)
                            elif n.colliderect(d2):
                                bullet_ufo.play(0)
                                colord2 = GREEN
                                biend2 = True
                                bullets_three3.remove(bullet)
                            if n.colliderect(v1) or n.colliderect(v2) or n.colliderect(v3) or n.colliderect(v4) or n.colliderect(v5) or n.colliderect(d1) or n.colliderect(d2):
                                bullet_ufo.play(0)
                        
                        # Dùng thời gian
                        # if dem1 > 200:
                        #     y12 = -50
                        #     x12 = random.randint(0, width)
                        #     dem1 = 0
                        #     tt = False
                        
                        bien_three2 += 1
                        if bien_three2 == 200:
                            biendem_three2 = True
                        
                        if quantity_three == 0:
                            # bien_three2 += 1
                            y12 = -50
                            x12 = random.randint(0, width)
                            # dem1 = 0
                            # tt = False
                            biendem_three = True
                            # dem1 += 1
                        if biendem_three == True:
                            bien_three += 1
                        if bien_three == 300:
                            bien_three = 0
                            tt = False
                            biendem_three = False
                            quantity_three = 5

                        if biendem_three2 == True:
                            if tt == False:
                                if lose1 == False:
                                    y12+=2
                                # if lose1 == True:
                                #     y12-=2

                        if y12 > height:
                            sizev12 = 1
                            y12 = -50
                            x12 = random.randint(0, width)
                    else:
                        target_bullet = 1
                        
                    if level > 8:
                        if ifall == 0:
                            xfall = random.randint(10, width-10)
                            
                        if ifall > 0 and ifall < 70:
                            listran = random.choice([BLACK,RED])
                            boxran = (xfall,0,20,20)
                            pygame.draw.rect(screen,listran,boxran)
                            
                        if ifall == 70:
                            bullets_ran.append([xfall, -50])
                            
                        for b in range(len(bullets_ran)):
                            if lose1 == False:
                                bullets_ran[b][1] += 10
                            # if lose1 == True:
                            #     bullets_ran[b][1] -= 10

                        for bullet in bullets_ran[:]:
                            # if level < 10:
                            if bullet[1] == height/2:
                                ifall = -1
                            # else:
                            #     if bullet[1] == -30:
                            #         ifall = -1
                            if bullet[1] > height:
                                bullets_ran.remove(bullet)
                        for bullet in bullets_ran:
                            # bulletpicture2 = pygame.transform.rotate(bulletpicture, 180)
                            a = screen.blit(rocket, (bullet[0], bullet[1]))
                        for bullet in bullets_ran:
                            box = (bullet[0],bullet[1],20,28)
                            nran = pygame.draw.rect(screen,BLACK,box,2)
                            if protect0 == False:
                                if nran.colliderect(shipp):
                                    lose = True
                                    lose1 = True
                                # bullets_ran.remove(bullet)
                        # if lose1 == False
                        ifall += 1
                        
                    if level > 9:
                        if ifall2 == 0:
                            xfall2 = random.randint(10, width-10)
                        if ifall2 > 0 and ifall2 < 70:
                            listran2 = random.choice([BLACK,RED])
                            boxran2 = (xfall2,0,20,20)
                            pygame.draw.rect(screen,listran2,boxran2)
                        if ifall2 == 70:
                            bullets_ran2.append([xfall2, -50])
                            
                        for b in range(len(bullets_ran2)):
                            if lose1 == False:
                                bullets_ran2[b][1] += 20
                            # if lose1 == True:
                            #     bullets_ran2[b][1] -= 20
                        for bullet in bullets_ran2[:]:
                            if bullet[1] == -30:
                                ifall2 = -1
                            if bullet[1] > height:
                                bullets_ran2.remove(bullet)
                        for bullet in bullets_ran2:
                            a = screen.blit(rocket, (bullet[0], bullet[1]))
                        for bullet in bullets_ran2:
                            box = (bullet[0],bullet[1],20,28)
                            nran2 = pygame.draw.rect(screen,BLACK,box,2)
                            if protect0 == False:
                                if nran2.colliderect(shipp):
                                    lose = True
                                    lose1 = True
                                # bullets_ran2.remove(bullet)
                        ifall2 += 1
                        
                    # if level > 9:  
                    #     bullet_fc2 = pygame.transform.scale(bullet_target, (20, 25))
                    #     screen.blit(bullet_fc2, (x7, y7))
                    #     v7=pygame.draw.rect(screen,colorv7,(x7,y7,20,25),sizev7)
                    #     if shipp.colliderect(v7):
                    #         bienauto = True
                    #         bienchay2 += 1
                    #         sizev7 = 0
                    #         colorv7 = BLACK
                    #         ttt = True

                    #     if bienchay2 == 1:
                    #         xauto = x + 16
                    #         yauto = y - 35
                                    
                    #     b = pygame.key.get_pressed()               
                    #     if b[pygame.K_a]: xauto-=3
                    #     if b[pygame.K_d]: xauto+=3
                    #     if b[pygame.K_w]: yauto-=3
                    #     if b[pygame.K_s]: yauto+=3

                    #     if ttt == True:
                    #         bullet_move = pygame.transform.scale(bullet_target, (sizefc2, 30))
                    #         screen.blit(bullet_move, (xauto, yauto))
                    #         boxx2 = (xauto,yauto,sizefc2,30)
                    #         n2 = pygame.draw.rect(screen,BLACK,boxx2,2)
                    #         if n2.colliderect(target):
                    #             bullet_ufo.play(0)
                    #             colortarget1 = GREEN
                    #             targetlv8 = True
                    #             sizefc2 = 0
                    #             xauto = 20000
                    #         if n2.colliderect(target2):
                    #             bullet_ufo.play(0)
                    #             colortarget2 = GREEN
                    #             target2lv8 = True
                    #             sizefc2 = 0
                    #             xauto = 20000
                    #         if n2.colliderect(v1) or  n2.colliderect(v2) or n2.colliderect(v3) or n2.colliderect(v4) or n2.colliderect(v5) or n2.colliderect(d1) or n2.colliderect(d2) or n2.colliderect(d3):
                    #             sizefc2 = 0
                    #             xauto = 20000
                                
                    #     if bienauto == False:
                    #         if y7 > height:
                    #             y7 = 0
                    #             x7 = random.randint(10, width-10)
                    #     y7 += 3
                    #     if lose1 == True:
                    #         y7 -= 3
                    
                    if level > 0:
                        if bien_add == True:
                            image_add = pygame.transform.scale(bullet_alein1, (20, 30))
                            screen.blit(image_add, (ximage_add, yimage_add))
                            vadd=pygame.draw.rect(screen,WHITE,(ximage_add,yimage_add,20,30), 1)
                            
                            if shipp.colliderect(vadd):
                                bullet_func.play(0)
                                biendem_add += 1
                                bien_add = False
                                yimage_add = -50
                                ximage_add = random.randint(10, width-10)
                                if biendem_add == 1:
                                    i1 -= 10
                                    
                            if yimage_add > height:
                                yimage_add = 0
                                ximage_add = random.randint(10, width-10)
                                    
                            if lose1 == False:
                                yimage_add += 3
                            # if lose1 == True:
                            #     yimage_add -= 3
                        
                        if wall_bullet*4-i1 == 0:
                            if bien_add == False:
                                if lose1 == False:
                                    biendem_add2 += 1
                                # if lose1 == True:
                                #     biendem_add2 -= 1
                            
                        if level < 6:
                            if biendem_add2 == 200:
                                biendem_add2 = 0
                                bien_add = True
                                biendem_add = 0
                        else:
                            if biendem_add2 == 400:
                                biendem_add2 = 0
                                bien_add = True
                                biendem_add = 0
                                
                    b = pygame.key.get_pressed()
                    if move == True:
                        if len(results.multi_handedness) == 1 and xt1 - xt > 10:
                            x += 6
                        if len(results.multi_handedness) == 1 and xt - xt1 > 10:
                            x -= 6
                                
                                
                    if level > 5:
                        # color_ship = BLACK
                        if protect1 == False:
                            if protect7 == True:
                                screen.blit(protect_image, (ximage_protect, yimage_protect))
                                vprotect=pygame.draw.rect(screen,WHITE,(ximage_protect,yimage_protect,28,28), 1)
                                
                                if vprotect.colliderect(shipp):
                                    bullet_func.play(0)
                                    # color_ship = GREEN
                                    protect1 = True
                                    protect0 = True
                            
                        if level == 6:
                            if protect6 > 300:
                                protect7 = True
                        if level == 7:
                            if protect6 > 500:
                                protect7 = True
                        if level == 8:
                            if protect6 > 700:
                                protect7 = True
                        if level == 9:
                            if protect6 > 900:
                                protect7 = True
                        if level == 10:
                            if protect6 > 1000:
                                protect7 = True
                        if lose1 == False:
                            protect6 += 1
                                                
                        if protect1 == True:
                            if lose1 == False:
                                protect3 += 1
                                
                        if protect0 == False:
                            color_ship = BLACK
                            
                        if protect0 == True:
                            color_protect = GREEN
                            if protect3 > 400 and protect3 < 500:
                                color_protect = random.choice([BLACK,GREEN])
                            if protect_size > 40:
                                protect_size = 40
                            pygame.draw.circle(screen,color_protect,(x+32,y+38),protect_size,2)
                            protect_size+=1

                        if protect3 == 500:
                            protect2 = True
                            protect0 = False
                            # color_ship = BLACK
                            ximage_protect = random.randint(0, width-28)
                            yimage_protect = -50
                            protect_size = 0
                            
                        
                            
                        # if protect3 > 400 and protect3 < 500:
                        #     color_ship = random.choice([BLACK,GREEN])
                        
                        if protect2 == True:
                            if lose1 == False:
                                protect4 += 1
                            if level == 6:
                                if protect4 == 500:
                                    protect3 = 0
                                    protect4 = 0
                                    protect2 = False
                                    protect1 = False
                            if level == 7:
                                if protect4 == 1000:
                                    protect3 = 0
                                    protect4 = 0
                                    protect2 = False
                                    protect1 = False
                            if level == 8:
                                if protect4 == 1300:
                                    protect3 = 0
                                    protect4 = 0
                                    protect2 = False
                                    protect1 = False
                            if level == 9:
                                if protect4 == 1500:
                                    protect3 = 0
                                    protect4 = 0
                                    protect2 = False
                                    protect1 = False
                            if level == 10:
                                if protect4 == 2000:
                                    protect3 = 0
                                    protect4 = 0
                                    protect2 = False
                                    protect1 = False
                            
                        # if protect
                        
                        if yimage_protect > height:
                            ximage_protect = random.randint(0, width-28)
                            yimage_protect = -50
                        
                        if protect1 == False:
                            if lose1 == False:
                                if protect7 == True:
                                    yimage_protect += 2   
                                
                        
                        
                    
                    # b = pygame.key.get_pressed()
                    # if move == True:
                    #     if handLabel == "Right" and xt1 - xt > 10:
                    #         x += 6
                    #     if handLabel == "Right" and xt - xt1 > 10:
                    #         x -= 6
                        
                    # if level < 10:
                    if lose == False and lose1 == False:
                        if fingerCount == 10:
                            bien_pause = True
                        else:
                            bien_pause = False
                    if bien_pause == True:
                        bien_pause2 += 1
                        if bien_pause2 == 20:
                            lose1 = True
                            pause = True
                    if bien_pause2 > 50:
                        bien_pause = False
                        bien_pause2 = 0
                            
                        
                        # if b[pygame.K_KP_ENTER]:
                        #     ship = pygame.image.load("player2.png").convert_alpha()
                        #     ship = pygame.transform.scale(ship, (64,64))
                        # if b[pygame.K_BACKSPACE]:
                        #     ship = pygame.image.load("player3.png").convert_alpha()
                        #     ship = pygame.transform.scale(ship, (64,64))
                        


                    if x < 0:
                        x = 0
                    if x > 736:
                        x = 736
                        
                    
                     
                    # Thêm chức năng thay đổi hình dáng phi thuyền và background với tay trái
                    
                    if lose1 == True:
                        cv2.putText(imgRGB, 'Chose shape player', (0, 150),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 255, 0), 2)
                        cv2.circle(imgRGB, (100, 200), 20, colorchange_ufo1, -1)
                        cv2.putText(imgRGB, '1', (92, 208),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                WHITE, 2)
                        cv2.circle(imgRGB, (100, 250), 20, colorchange_ufo2, -1)
                        cv2.putText(imgRGB, '2', (92, 258),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                YELLOW, 2)
                        if 80 <= xt1 <= 120 and 180 <= yt1 <= 220 and handLabel == "Left" and len(results.multi_handedness) == 1:
                            colorchange_ufo1 = BLACK
                            if abs(ys - ys1) < 20 and handLabel == "Left" and len(results.multi_handedness) == 1:
                                ship = pygame.image.load("player2.png").convert_alpha()
                                ship = pygame.transform.scale(ship, (64,64))
                        else:
                            colorchange_ufo1 = GREEN
                        if 80 <= xt1 <= 120 and 230 <= yt1 <= 270 and handLabel == "Left" and len(results.multi_handedness) == 1:
                            colorchange_ufo2 = BLACK
                            if abs(ys - ys1) < 20 and handLabel == "Left" and len(results.multi_handedness) == 1:
                                ship = pygame.image.load("player3.png").convert_alpha()
                                ship = pygame.transform.scale(ship, (64,64))
                        else:
                            colorchange_ufo2 = RED
                            
                        
                        
                        cv2.putText(imgRGB, 'Chose background', (400, 150),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 255, 0), 2)
                        cv2.circle(imgRGB, (500, 200), 20, colorchange_bg1, -1)
                        cv2.putText(imgRGB, '1', (492, 208),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                WHITE, 2)
                        cv2.circle(imgRGB, (500, 250), 20, colorchange_bg2, -1)
                        cv2.putText(imgRGB, '2', (492, 258),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                YELLOW, 2)
                        if 480 <= xt1 <= 520 and 180 <= yt1 <= 220 and handLabel == "Left" and len(results.multi_handedness) == 1:
                            colorchange_bg1 = BLACK
                            if abs(ys - ys1) < 20 and handLabel == "Left" and len(results.multi_handedness) == 1:
                                background_game = pygame.image.load("bg_test66.jpg").convert_alpha()
                                background_game = pygame.transform.scale(background_game, (800,600))
                        else:
                            colorchange_bg1 = GREEN
                        if 480 <= xt1 <= 520 and 230 <= yt1 <= 270 and handLabel == "Left" and len(results.multi_handedness) == 1:
                            colorchange_bg2 = BLACK
                            if abs(ys - ys1) < 20 and handLabel == "Left" and len(results.multi_handedness) == 1:
                                background_game = pygame.image.load("bg_game.png").convert_alpha()
                                background_game = pygame.transform.scale(background_game, (800,600))
                        else:
                            colorchange_bg2 = RED

                    # ------------------------------------- 
                

                    # if change_bullet == True:
                    #     if b[pygame.K_e]:
                    #         change_bullet1 = True
                    #         change_bullet = False
                    # if change_bullet == False:
                    #     if b[pygame.K_q]:
                    #         change_bullet1 = False
                    #         change_bullet = True

                    

                    if change_bullet1 == False:
                        # pygame.draw.rect(screen,GREEN,(x + 70,520,10,10))
                        screen.blit(bullet_target, (x+60,y))
                        # if u%8==0:
                        if move == True:
                            if len(results.multi_handedness) == 1:
                                if abs(yt - yt1) < 10 and abs(xt - xt1) < 20:
                                        if u22 == False:
                                            if i<target_bullet*2:
                                                shot.play(0)
                                                bullets.append([x+30,y])
                                                i+=1
                                                u22 = True
                                        if i>=target_bullet*2:
                                            if u22_s == False:
                                                notshot.play(0)
                                                u22_s = True
                                        finger_color3 = WHITE
                                        finger_color4 = WHITE
                        
                        if u22 == True:
                            u2 += 1
                        if u2 > 10:
                            u2 = 0
                            u22 = False
                        if u22_s == True:
                            u2_s += 1
                        if u2_s > 10:
                            u2_s = 0
                            u22_s = False         
                                            
                            

                        for b in range(len(bullets)):
                            if lose1 == False:
                                bullets[b][1] -= 5

                        for bullet in bullets[:]:
                            if bullet[1] < 0:
                                bullets.remove(bullet)
                        for bullet in bullets:
                            a = screen.blit(bullet_target, (bullet[0], bullet[1]))
                        # screen.blit(ship, (x, y))
                            
                        for bullet in bullets:
                            box = (bullet[0],bullet[1],30,38)
                            n = pygame.draw.rect(screen,BLACK,box,2)
                            
                            if level > 0:
                                if ufo1_play == True:
                                    if n.colliderect(v1):
                                        bullets.remove(bullet)
                            if level > 1:
                                if ufo2_play == True:
                                    v2=pygame.draw.rect(screen,color2,(x2,y2,55,35), 1)
                                    if n.colliderect(v2):
                                        bullets.remove(bullet)
                            if level > 2:
                                if ufo3_play == True:
                                    v3=pygame.draw.rect(screen,color3,(x3,y3,55,35), 1)
                                    if n.colliderect(v3):
                                        bullets.remove(bullet)
                            if level > 3:
                                if ufo4_play == True:
                                    v4=pygame.draw.rect(screen,color4,(x4,y4,55,35), 1)
                                    if n.colliderect(v4):
                                        bullets.remove(bullet)
                            if level > 4:
                                if ufo5_play == True:
                                    v5=pygame.draw.rect(screen,color5,(x5,y5,55,35), 1)
                                    if n.colliderect(v5):
                                        bullets.remove(bullet)
                            if level > 6:
                                d1=pygame.draw.rect(screen,colord1,(xd1, yd1, 20, 20))
                                d2=pygame.draw.rect(screen,colord2,(xd2, yd2, 20, 20))
                                d3=pygame.draw.rect(screen,colord12,(xd1+20, yd1+9, xd2-(xd1+20), 2))
                                if biend1 == False or biend2 == False:
                                    if n.colliderect(d1) or n.colliderect(d2) or n.colliderect(d3):
                                        bullets.remove(bullet)
                                elif biend1 == True and biend2 == True:
                                    colord12 = GREEN
                            
                            if level <= 7:
                                if n.colliderect(target):
                                    bullet_ufo.play(0)
                                    level_display = True
                                    bullets.remove(bullet)
                                    i = 0 # target_bullet
                                    i1 = 0 # wall_bullet
                                    level += 1
                                    k+=1 # Score
                                    reset = 0 # Display reset
                                    
                                    bullets_wall.clear()
                                    bullets.clear()
                                    bullets_three1.clear()
                                    bullets_three2.clear()
                                    bullets_three3.clear()
                                    bullets_boss1.clear()
                                    bien_boss1 = 0
                                    bien_boss2 = 0
                                    run_boss1 = True
                                    run_boss2 = False
                                    
                                    ufo1_play = True
                                    ufo1_time = 0
                                    ufo1_bien = 0
                                    
                                    ufo2_play = True
                                    ufo2_time = 0
                                    ufo2_bien = 0
                                    
                                    ufo3_play = True
                                    ufo3_time = 0
                                    ufo3_bien = 0
                                    
                                    ufo4_play = True
                                    ufo4_time = 0
                                    ufo4_bien = 0
                                    
                                    ufo5_play = True
                                    ufo5_time = 0
                                    ufo5_bien = 0
                                    
                                    xtarget = width/2
                                    xtarget2 = width/2
                                    
                                    ximage_add = random.randint(10, width-10)
                                    yimage_add = -50
                                    bien_add = False
                                    bien_add2 = False
                                    biendem_add = 0
                                    biendem_add2 = 0
                                    
                                    x = width/2
                                    
                                    protect_size = 0
                                    
                                    u1 = 0
                                    u11 = False
                                    u1_s = 0
                                    u11_s = False
                                    u2 = 0
                                    u22 = False
                                    u2_s = 0
                                    u22_s = False
                                    u3 = 0
                                    u33 = False
                                    
                                    protect0 = False
                                    protect1 = False
                                    protect2 = False
                                    protect3 = 0
                                    protect4 = 0
                                    protect5 = 0
                                    protect6 = 0
                                    protect7 = False
                                    color_ship = BLACK
                                    ximage_protect = random.randint(10, width-10)
                                    yimage_protect = -50
                                    color_protect = GREEN

                                    if level > 0:
                                        i1 = 0
                                        t1 = True
                                        color1 = BLACK
                                        g1 = True
                                        x1 = 0
                                    
                                    if level > 1:
                                        i2 = 0
                                        t2 = True
                                        color2 = BLACK
                                        g2 = True
                                        x2 = width
                                    if level > 2:
                                        i3 = 0
                                        t3 = True
                                        color3 = BLACK
                                        g3 = True
                                        x3 = 0
                                    if level > 3:
                                        i4 = 0
                                        t4 = True
                                        color4 = BLACK
                                        g4 = True
                                        x4 = width
                                    if level > 4:
                                        i5 = 0
                                        t5 = True
                                        color5 = BLACK
                                        g5 = True
                                        x5 = 0
                                    if level > 5:
                                        y6 = 100
                                        y8 = 150
                                        y9 = 200
                                        y10 = 250
                                        y11 = 300
                                        bienchay1 = 0
                                        bienchay3 = 0
                                        bienchay4 = 0
                                        bienchay5 = 0
                                        bienchay6 = 0
                                    if level > 6:
                                        biend1 = False
                                        biend2 = False
                                        colord1 = RED
                                        colord2 = RED
                                        colord12 = RED
                                    level_complete.play(0)
                            elif level > 7:
                                if target1_display == True:
                                    target_box = (xtarget,ytarget,65,50)
                                    target = pygame.draw.rect(screen,BLACK,target_box,2)
                                if target2_display == True:
                                    target_box2 = (xtarget2,ytarget2,65,50)
                                    target2 = pygame.draw.rect(screen,BLACK,target_box2,2)
                                if n.colliderect(target):
                                    if target1_display == True:
                                        bullet_ufo.play(0)
                                        colortarget1 = GREEN
                                        target1_display = False
                                        bullets.remove(bullet)
                                        targetlv8 = True
                                elif n.colliderect(target2):
                                    if target2_display == True:
                                        bullet_ufo.play(0)
                                        colortarget2 = GREEN
                                        target2_display = False
                                        bullets.remove(bullet)
                                        target2lv8 = True
                                if targetlv8 == True and target2lv8 == True:
                                    level_complete.play(0)
                                    i = 0 # target_bullet
                                    i1 = 0 # wall_bullet
                                    level += 1
                                    level_display = True
                                    k+=1 # Score
                                    reset = 0 # Display reset
                                    colortarget1 = BLACK
                                    colortarget2 = BLACK
                                    targetlv8 = False
                                    target2lv8 = False
                                    xtarget = width/2
                                    xtarget2 = width/2
                                    bien_boss1 = 0
                                    bien_boss2 = 0
                                    run_boss1 = True
                                    run_boss2 = False
                                    
                                    quantity_three = 5
                                    bien_three = 0
                                    bien_three2 = 0
                                    biendem_three = False
                                    biendem_three2 = False
                                    
                                    target1_display = True
                                    target2_display = True
                                    
                                    x = width/2
                                    
                                    protect_size = 0
                                    
                                    u1 = 0
                                    u11 = False
                                    u1_s = 0
                                    u11_s = False
                                    u2 = 0
                                    u22 = False
                                    u2_s = 0
                                    u22_s = False
                                    u3 = 0
                                    u33 = False
                                    
                                    ufo1_play = True
                                    ufo1_time = 0
                                    ufo1_bien = 0
                                    
                                    ufo2_play = True
                                    ufo2_time = 0
                                    ufo2_bien = 0
                                    
                                    ufo3_play = True
                                    ufo3_time = 0
                                    ufo3_bien = 0
                                    
                                    ufo4_play = True
                                    ufo4_time = 0
                                    ufo4_bien = 0
                                    
                                    ufo5_play = True
                                    ufo5_time = 0
                                    ufo5_bien = 0
                                    if level > 10:
                                        victory = True
                                        lose = True
                                        lose1 = True
                                    
                                    bullets_wall.clear()
                                    bullets.clear()
                                    bullets_three1.clear()
                                    bullets_three2.clear()
                                    bullets_three3.clear()
                                    bullets_ran.clear()
                                    bullets_ran2.clear()
                                    bullets_boss1.clear()
                                    bullets_boss2.clear()
                                    bien_boss1 = 0
                                    bien_boss2 = 0
                                    
                                    xtarget = width/2
                                    xtarget2 = width/2
                                    
                                    protect0 = False
                                    protect1 = False
                                    protect2 = False
                                    protect3 = 0
                                    protect4 = 0
                                    protect5 = 0
                                    protect6 = 0
                                    protect7 = False
                                    color_ship = BLACK
                                    ximage_protect = random.randint(10, width-10)
                                    yimage_protect = -50
                                    color_protect = GREEN
                                    
                                    ximage_add = random.randint(10, width-10)
                                    yimage_add = -50
                                    bien_add = False
                                    bien_add2 = False
                                    biendem_add = 0
                                    biendem_add2 = 0
                                    
                                    ifall = 0
                                    ifall2 = 0

                                    if level > 0:
                                        i1 = 0
                                        t1 = True
                                        color1 = BLACK
                                        g1 = True
                                        x1 = 0
                                    
                                    if level > 1:
                                        i2 = 0
                                        t2 = True
                                        color2 = BLACK
                                        g2 = True
                                        x2 = width
                                    if level > 2:
                                        i3 = 0
                                        t3 = True
                                        color3 = BLACK
                                        g3 = True
                                        x3 = 0
                                    if level > 3:
                                        i4 = 0
                                        t4 = True
                                        color4 = BLACK
                                        g4 = True
                                        x4 = width
                                    if level > 4:
                                        i5 = 0
                                        t5 = True
                                        color5 = BLACK
                                        g5 = True
                                        x5 = 0
                                    if level > 5:
                                        y6 = 100
                                        y8 = 150
                                        y9 = 200
                                        y10 = 250
                                        y11 = 300
                                        bienchay1 = 0
                                        bienchay3 = 0
                                        bienchay4 = 0
                                        bienchay5 = 0
                                        bienchay6 = 0
                                    if level > 6:
                                        biend1 = False
                                        biend2 = False
                                        colord1 = RED
                                        colord2 = RED
                                        colord12 = RED
                                    if level > 7:
                                        y12 = -50
                                        tt = False
                                        ttt = False
                                    
                    if level_display == True:
                        if victory == False:
                            if level <= 10:
                                font = pygame.font.SysFont("Forte", 30)
                                text = font.render("LEVEL UP", True, GREEN)
                                screen.blit(text,(xlevel, height/2))
                                if xlevel > width/2-150 and xlevel < width/2:
                                    xlevel -= 13
                                xlevel += 15
                                if xlevel > width:
                                    level_display = False
                                    xlevel = -100
                       
                    wall_bullet = level
                    if change_bullet1 == False:
                        # if quantity_three > 0: # Hiển thị đạn chức nắng khi bắn được đạn đó
                        #     screen.blit(bullet_alein1, (x-20,y))
                        screen.blit(bullet_alein1, (x-20,y))
                        for xx in range(1,level+1):
                            if level == xx:
                                wall_bullet = xx
                        # if u%8==0:
                        if move == True:
                            if len(results.multi_handedness) == 1:
                                if abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                                    if u11 == False:
                                        if i1<wall_bullet*4:
                                            shot.play(0)
                                            bullets_wall.append([x,y])
                                            i1+=1
                                            u11 = True
                                    if i1>=wall_bullet*4:
                                        if u11_s == False:
                                            notshot.play(0)
                                            u11_s = True
                                    finger_color1 = WHITE
                                    finger_color2 = WHITE
                                            
                        if u11 == True:
                            u1 += 1
                        if u1 > 10:
                            u1 = 0
                            u11 = False
                        if u11_s == True:
                            u1_s += 1
                        if u1_s > 10:
                            u1_s = 0
                            u11_s = False 

                        for b in range(len(bullets_wall)):
                            if lose1 == False:
                                bullets_wall[b][1] -= 5

                        for bullet in bullets_wall[:]:
                            if bullet[1] < 0:
                                bullets_wall.remove(bullet)
                        for bullet in bullets_wall:
                            a = screen.blit(bullet_alein1, (bullet[0], bullet[1]))
                        for bullet in bullets_wall:
                            box = (bullet[0],bullet[1],20,40)
                            n = pygame.draw.rect(screen,BLACK,box,2)
                            if level > 0:
                                if ufo1_play == True:
                                    if n.colliderect(v1):
                                        ufo1_time += 1
                                        if level < 6:
                                            if ufo1_time == 2:
                                                ufo_boom.play(0)
                                                ufo1_play = False
                                        else:
                                            if ufo1_time == 3:
                                                ufo_boom.play(0)
                                                ufo1_play = False
                                        color1 = GREEN
                                        t1 = False
                                        if ufo1_play == True:
                                            bullet_ufo.play(0)
                                        bullets_wall.remove(bullet)
                                        continue
                            if level > 1:
                                if ufo2_play == True:
                                    v2=pygame.draw.rect(screen,color2,(x2,y2,55,35),1)
                                    if n.colliderect(v2):
                                        ufo2_time += 1
                                        if level < 6:
                                            if ufo2_time == 2:
                                                ufo_boom.play(0)
                                                ufo2_play = False
                                        else:
                                            if ufo2_time == 3:
                                                ufo_boom.play(0)
                                                ufo2_play = False
                                        color2 = GREEN
                                        t2 = False
                                        if ufo2_play == True:
                                            bullet_ufo.play(0)
                                        bullets_wall.remove(bullet)
                                        continue

                            if level > 2:
                                if ufo3_play == True:
                                    v3=pygame.draw.rect(screen,color3,(x3,y3,55,35),1)
                                    if n.colliderect(v3):
                                        ufo3_time += 1
                                        if level < 6:
                                            if ufo3_time == 2:
                                                ufo_boom.play(0)
                                                ufo3_play = False
                                        else:
                                            if ufo3_time == 3:
                                                ufo_boom.play(0)
                                                ufo3_play = False
                                        color3 = GREEN
                                        t3 = False
                                        if ufo3_play == True:
                                            bullet_ufo.play(0)
                                        bullets_wall.remove(bullet)
                                        continue
                            if level > 3:
                                if ufo4_play == True:
                                    v4=pygame.draw.rect(screen,color4,(x4,y4,55,35),1)
                                    if n.colliderect(v4):
                                        ufo4_time += 1
                                        if level < 6:
                                            if ufo4_time == 2:
                                                ufo_boom.play(0)
                                                ufo4_play = False
                                        else:
                                            if ufo4_time == 3:
                                                ufo_boom.play(0)
                                                ufo4_play = False
                                        color4 = GREEN
                                        t4 = False
                                        if ufo4_play == True:
                                            bullet_ufo.play(0)
                                        bullets_wall.remove(bullet)
                                        continue
                            if level > 4:
                                if ufo5_play == True:
                                    v5=pygame.draw.rect(screen,color5,(x5,y5,55,35),1)
                                    if n.colliderect(v5):
                                        ufo5_time += 1
                                        if level < 6:
                                            if ufo5_time == 2:
                                                ufo_boom.play(0)
                                                ufo5_play = False
                                        else:
                                            if ufo5_time == 3:
                                                ufo_boom.play(0)
                                                ufo5_play = False
                                        color5 = GREEN
                                        t5 = False
                                        if ufo5_play == True:
                                            bullet_ufo.play(0)
                                        bullets_wall.remove(bullet)
                                        continue
                                    
                            if level > 6:
                                d1=pygame.draw.rect(screen,colord1,(xd1, yd1, 20, 20))
                                d2=pygame.draw.rect(screen,colord2,(xd2, yd2, 20, 20))
                                # d3=pygame.draw.rect(screen,colord12,(xd1+20, yd1+9, xd2-(xd1+20), 2))
                                if n.colliderect(d1):
                                    colord1 = GREEN
                                    biend1 = True
                                    bullet_ufo.play(0)
                                    bullets_wall.remove(bullet)
                                if n.colliderect(d2):
                                    colord2 = GREEN
                                    biend2 = True
                                    bullet_ufo.play(0)
                                    bullets_wall.remove(bullet)

                    screen.blit(ship, (x, y))
                    
                    if level > 10:
                        level = 10
                        
                    if lose1 == False:
                        if t1 == True:
                            if g1 == True:
                                x1 += 6
                                if level > 7:
                                    x1 += 2
                                if level > 9:
                                    x1 += 2
                        if t1 == False:  # Bắn trúng tường set lại tốc độ
                            if g1 == True:
                                x1 += 2
                                if level > 7:
                                    x1 += 2
                                if level > 9:
                                    x1 += 2
                        if t1 == True:
                            if g1 == False:
                                x1 -= 6
                                if level > 7:
                                    x1 -= 2
                                if level > 9:
                                    x1 -= 2
                        if t1 == False:
                            if g1 == False:
                                x1 -= 2
                                if level > 7:
                                    x1 -= 2
                                if level > 9:
                                    x1 -= 2
                        if x1>750:
                            g1 = False
                            x1 = 750
                        if x1 < 0:
                            g1 = True
                            x1 = 0

                        if level > 1:
                            if t2 == True:
                                if g2 == True:
                                    x2 -= 8
                                    if level > 7:
                                        x2 -= 2
                                    if level > 9:
                                        x2 -= 2
                            if t2 == False:
                                if g2 == True:
                                    x2 -= 2
                                    if level > 7:
                                        x2 -= 2
                                    if level > 9:
                                        x2 -= 2
                            if t2 == True:
                                if g2 == False:
                                    x2 += 8
                                    if level > 7:
                                        x2 += 2
                                    if level > 9:
                                        x2 += 2
                            if t2 == False:
                                if g2 == False:
                                    x2 += 2
                                    if level > 7:
                                        x2 += 2
                                    if level > 9:
                                        x2 += 2
                            if x2>750:
                                g2 = True
                                x2 = 750
                            if x2 < 0:
                                g2 = False
                                x2 = 0

                        if level > 2:
                            if t3 == True:
                                if g3 == True:
                                    x3 += 10
                                    if level > 7:
                                        x3 += 2
                                    if level > 9:
                                        x3 += 2
                            if t3 == False:  # Bắn trúng tường set lại tốc độ
                                if g3 == True:
                                    x3 += 2
                                    if level > 7:
                                        x3 += 2
                                    if level > 9:
                                        x3 += 2
                            if t3 == True:
                                if g3 == False:
                                    x3 -= 10
                                    if level > 7:
                                        x3 -= 2
                                    if level > 9:
                                        x3 -= 2
                            if t3 == False:
                                if g3 == False:
                                    x3 -= 2
                                    if level > 7:
                                        x3 -= 2
                                    if level > 9:
                                        x3 -= 2
                            if x3>750:
                                g3 = False
                                x3 = 750
                            if x3 < 0:
                                g3 = True
                                x3 = 0

                        if level > 3:
                            if t4 == True:
                                if g4 == True:
                                    x4 -= 12
                                    if level > 7:
                                        x4 -= 2
                                    if level > 9:
                                        x4 -= 2
                            if t4 == False:
                                if g4 == True:
                                    x4 -= 2
                                    if level > 7:
                                        x4 -= 2
                                    if level > 9:
                                        x4 -= 2
                            if t4 == True:
                                if g4 == False:
                                    x4 += 12
                                    if level > 7:
                                        x4 += 2
                                    if level > 9:
                                        x4 += 2
                            if t4 == False:
                                if g4 == False:
                                    x4 += 2
                                    if level > 7:
                                        x4 += 2
                                    if level > 9:
                                        x4 += 2
                            if x4>750:
                                g4 = True
                                x4 = 750
                            if x4 < 0:
                                g4 = False
                                x4 = 0

                        if level > 4:
                            if t5 == True:
                                if g5 == True:
                                    x5 += 14
                                    if level > 7:
                                        x5 += 2
                                    if level > 9:
                                        x5 += 2
                            if t5 == False:  # Bắn trúng tường set lại tốc độ ko,l.
                                if g5 == True:
                                    x5 += 2
                                    if level > 7:
                                        x5 += 2
                                    if level > 9:
                                        x5 += 2
                            if t5 == True:
                                if g5 == False:
                                    x5 -= 14
                                    if level > 7:
                                        x5 -= 2
                                    if level > 9:
                                        x5 -= 2
                            if t5 == False:
                                if g5 == False:
                                    x5 -= 2
                                    if level > 7:
                                        x5 -= 2
                                    if level > 9:
                                        x5 -= 2
                            if x5>750:
                                g5 = False
                                x5 = 750
                            if x5 < 0:
                                g5 = True
                                x5 = 0
                            
                        if level > 6:
                            if gd1 == True:
                                xd1 -= 2
                            if gd1 == False:
                                xd1 += 2
                            if xd1>150:
                                gd1 = True
                                xd1 = 150
                            if xd1 < 0:
                                gd1 = False
                                xd1 = 0

                            if gd2 == True:
                                xd2 += 2
                            if gd2 == False:
                                xd2 -= 2
                            if xd2>width - 20:
                                gd2 = False
                                xd2 = width - 20
                            if xd2 < width - 170:
                                gd2 = True
                                xd2 = width - 170

                    if lose == True:
                        # y6 = 100
                        # y8 = 150
                        # y9 = 200
                        # y10= 250
                        # y11 = 300
                        bien_lose += 1
                    if bien_lose == 1:   
                        if victory == False:
                            lose_game.play(0) 
                        with open('time_his.txt', 'a') as f:
                            f.write(str(count_time/1000)+'\n')
                        with open('level_his.txt', 'a') as f:
                            f.write(str(level)+'\n')
                    
                        
                    if lose1 == True:
                        if len(results.multi_handedness) == 1:
                            screen.blit(mouse_player, (xt1*2,yt1*2))
                        move = False
                        white.set_alpha(s3)
                        screen.blit(white,(0,0))
                        # font = pygame.font.SysFont("Comicsansms", 20)
                        font = pygame.font.SysFont("Forte", 20)
                        font_player = pygame.font.SysFont("Forte", 25)
                        font_win = pygame.font.SysFont("Forte", 50)
                        winner = font_win.render('VICTORY' , True , GREEN)
                        level_player = font_player.render('Level: ' + str(level) , True , GREEN)
                        time_player = font_player.render('Time: ' + str(count_time/1000) , True , GREEN)
                        gach_ngang = font_player.render('--------------------------------------', True , GREEN)
                        reback = font.render('PLAY AGAIN' , True , GREEN)
                        reback_menu = font.render('MENU' , True , GREEN)
                        resume = font.render('RESUME' , True , GREEN)
                        mouse = pygame.mouse.get_pos()
                        left, mid, right = pygame.mouse.get_pressed()
                        if width/2-90 <= xt1*2 <= width/2+90 and height/2+50 <= yt1*2+32 <= height/2+90 and len(results.multi_handedness) == 1:
                            bien6 += 1
                            if bien6 == 1:
                                shot.play(0)
                            pygame.draw.rect(screen, RED, [width/2-90, height/2+50, 180, 40],2)
                            if abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                                x1 = x3 = x5 = 0
                                x2 = x4 = width-50
                                y6 = 100
                                y8 = 150
                                y9 = 200
                                y10= 250
                                y11 = 300
                                colortarget1 = BLACK
                                colortarget2 = BLACK
                                xtarget = width/2
                                xtarget2 = width/2
                                targetlv8 = False
                                target2lv8 = False
                                bullets_wall.clear()
                                bullets.clear()
                                bullets_three1.clear()
                                bullets_three2.clear()
                                bullets_three3.clear()
                                bullets_ran.clear()
                                bullets_ran2.clear()
                                bullets_boss1.clear()
                                bullets_boss2.clear()
                                bien_boss1 = 0
                                bien_boss2 = 0
                                run_boss1 = True
                                run_boss2 = False
                                level_display = False
                                ifall = 0
                                ifall2 = 0
                                x = width/2
                                ximage_add = random.randint(10, width-10)
                                yimage_add = -50
                                bien_add = False
                                bien_add2 = False
                                biendem_add = 0
                                biendem_add2 = 0
                                move = True
                                level = 1
                                lose = False
                                lose1 = False
                                pause = False
                                biend1 = False
                                biend2 = False
                                colord12 = RED
                                y12 = -50
                                i = 0
                                i1 = 0
                                bien_lose = 0
                                count_time = 0
                                y7 = 0
                                x7 = random.randint(10, width-10)
                                xauto = 0
                                yauto = 200
                                sizev6 = 10
                                sizev7 = 1
                                colorv7 = WHITE
                                bienchay2 = 0
                                ttt = False
                                tt = False
                                quantity_three = 5
                                bien_three = 0
                                bien_three2 = 0
                                biendem_three = False
                                biendem_three2 = False
                                sizeauto = 32
                                sizefc2 = 25
                                bienauto = False
                                
                                protect0 = False
                                protect1 = False
                                protect2 = False
                                protect3 = 0
                                protect4 = 0
                                protect5 = 0
                                protect6 = 0
                                protect7 = False
                                color_ship = BLACK
                                ximage_protect = random.randint(10, width-10)
                                yimage_protect = -50
                                color_protect = GREEN
                                
                                target1_display = True
                                target2_display = True
                                
                                protect_size = 0
                                
                                victory = False
                                
                                u1 = 0
                                u11 = False
                                u1_s = 0
                                u11_s = False
                                u2 = 0
                                u22 = False
                                u2_s = 0
                                u22_s = False
                                u3 = 0
                                u33 = False
                                
                                s3 = 0
                                
                                ufo1_play = True
                                ufo1_time = 0
                                ufo1_bien = 0
                                
                                ufo2_play = True
                                ufo2_time = 0
                                ufo2_bien = 0
                                
                                ufo3_play = True
                                ufo3_time = 0
                                ufo3_bien = 0
                                
                                ufo4_play = True
                                ufo4_time = 0
                                ufo4_bien = 0
                                
                                ufo5_play = True
                                ufo5_time = 0
                                ufo5_bien = 0
                                if level > 0:
                                    i1 = 0
                                    t1 = True
                                    color1 = BLACK
                                    g1 = True
                                    x1 = 0
                                if level > 1:
                                    i2 = 0
                                    t2 = True
                                    color2 = BLACK
                                    g2 = True
                                    x2 = width
                                    
                                if level > 2:
                                    i3 = 0
                                    t3 = True
                                    color3 = BLACK
                                    g3 = True
                                    x3 = 0
                                if level > 3:
                                    i4 = 0
                                    t4 = True
                                    color4 = BLACK
                                    g4 = True
                                    x4 = width
                                if level > 4:
                                    i5 = 0
                                    t5 = True
                                    color5 = BLACK
                                    g5 = True
                                    x5 = 0
                                if level > 5:
                                    y6 = 100
                                    y8 = 150
                                    y9 = 200
                                    y10 = 250
                                    y11 = 300
                                    bienchay1 = 0
                                    bienchay3 = 0
                                    bienchay4 = 0
                                    bienchay5 = 0
                                    bienchay6 = 0
                                if level > 6:
                                    biend1 = False
                                    biend2 = False
                                    colord1 = RED
                                    colord2 = RED
                                    colord12 = RED
                                if level > 7:
                                    y12 = -50
                        else:
                            bien6 = 0            
                        
                                    
                        if width/2-90 <= xt1*2 <= width/2+90 and height/2+100 <= yt1*2+32 <= height/2+140 and len(results.multi_handedness) == 1:
                            bien7 += 1
                            if bien7 == 1:
                                shot.play(0)
                            pygame.draw.rect(screen, RED, [width/2-90, height/2+100, 180, 40],2)
                            if abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                                h1 = True
                                h2 = False
                                h3 = False
                                h0 = False
                                y6 = 100
                                y8 = 150
                                y9 = 200
                                y10= 250
                                y11 = 300
                                x1 = x3 = x5 = 0
                                x2 = x4 = width-50
                                colortarget1 = BLACK
                                colortarget2 = BLACK
                                targetlv8 = False
                                target2lv8 = False
                                bullets_wall.clear()
                                bullets.clear()
                                bullets_three1.clear()
                                bullets_three2.clear()
                                bullets_three3.clear()
                                bullets_ran.clear()
                                bullets_ran2.clear()
                                bullets_boss1.clear()
                                bullets_boss2.clear()
                                bien_boss1 = 0
                                bien_boss2 = 0
                                run_boss1 = True
                                run_boss2 = False
                                xtarget = width/2
                                ifall = 0
                                ifall2 = 0
                                x = width/2
                                level_display = False
                                ximage_add = random.randint(10, width-10)
                                yimage_add = -50
                                bien_add = False
                                bien_add2 = False
                                biendem_add = 0
                                biendem_add2 = 0
                                move = True
                                level = 1
                                lose = False
                                lose1 = False
                                pause = False
                                biend1 = False
                                biend2 = False
                                colord12 = RED
                                y12 = -50
                                i = 0
                                i1 = 0
                                bien_lose = 0
                                count_time = 0
                                y7 = 0
                                x7 = random.randint(10, width-10)
                                xauto = 0
                                yauto = 200
                                sizev6 = 10
                                sizev7 = 1
                                colorv7 = WHITE
                                bienchay2 = 0
                                ttt = False
                                tt = False
                                quantity_three = 5
                                bien_three = 0
                                bien_three2 = 0
                                biendem_three = False
                                biendem_three2 = False
                                sizeauto = 32
                                sizefc2 = 25
                                bienauto = False
                                
                                protect0 = False
                                protect1 = False
                                protect2 = False
                                protect3 = 0
                                protect4 = 0
                                protect5 = 0
                                protect6 = 0
                                protect7 = False
                                color_ship = BLACK
                                ximage_protect = random.randint(10, width-10)
                                yimage_protect = -50
                                color_protect = GREEN
                                
                                target1_display = True
                                target2_display = True
                                
                                protect_size = 0
                                
                                victory = False
                                
                                u1 = 0
                                u11 = False
                                u1_s = 0
                                u11_s = False
                                u2 = 0
                                u22 = False
                                u2_s = 0
                                u22_s = False
                                u3 = 0
                                u33 = False
                                
                                s3 = 0
                                
                                ufo1_play = True
                                ufo1_time = 0
                                ufo1_bien = 0
                                
                                ufo2_play = True
                                ufo2_time = 0
                                ufo2_bien = 0
                                
                                ufo3_play = True
                                ufo3_time = 0
                                ufo3_bien = 0
                                
                                ufo4_play = True
                                ufo4_time = 0
                                ufo4_bien = 0
                                
                                ufo5_play = True
                                ufo5_time = 0
                                ufo5_bien = 0
                                if level > 0:
                                    i1 = 0
                                    t1 = True
                                    color1 = BLACK
                                    g1 = True
                                    x1 = 0
                                if level > 1:
                                    i2 = 0
                                    t2 = True
                                    color2 = BLACK
                                    g2 = True
                                    x2 = width
                                    
                                if level > 2:
                                    i3 = 0
                                    t3 = True
                                    color3 = BLACK
                                    g3 = True
                                    x3 = 0
                                if level > 3:
                                    i4 = 0
                                    t4 = True
                                    color4 = BLACK
                                    g4 = True
                                    x4 = width
                                if level > 4:
                                    i5 = 0
                                    t5 = True
                                    color5 = BLACK
                                    g5 = True
                                    x5 = 0
                                if level > 5:
                                    y6 = 100
                                    y8 = 150
                                    y9 = 200
                                    y10 = 250
                                    y11 = 300
                                    bienchay1 = 0
                                    bienchay3 = 0
                                    bienchay4 = 0
                                    bienchay5 = 0
                                    bienchay6 = 0
                                if level > 6:
                                    biend1 = False
                                    biend2 = False
                                    colord1 = RED
                                    colord2 = RED
                                    colord12 = RED
                                if level > 7:
                                    y12 = -50
                        else:
                            bien7 = 0
                                    
                        if pause == True:
                            if width/2-90 <= xt1*2 <= width/2+90 and height/2+150 <= yt1*2+32 <= height/2+190 and len(results.multi_handedness) == 1:
                                bien8 += 1
                                if bien8 == 1:
                                    shot.play(0)
                                pygame.draw.rect(screen, RED, [width/2-90, height/2+150, 180, 40],2)
                                if abs(ys - ys1) < 20 and abs(xs - xs1) < 20:
                                    move = True
                                    lose1 = False
                                    lose = False
                                    pause = False
                                    s3 = 0
                            else:
                                bien8 = 0
                                    
                        # screen.blit(reback, (width/2-reback.get_width()/2, height/2-reback.get_height()/2))
                        if victory == True:
                            screen.blit(winner, (width/2-winner.get_width()/2, height/2-200))
                        screen.blit(time_player, (width/2-time_player.get_width()/2, height/2-50))
                        screen.blit(level_player, (width/2-level_player.get_width()/2, height/2))
                        screen.blit(gach_ngang, (width/2-gach_ngang.get_width()/2, height/2+15))
                        screen.blit(reback, (width/2-reback.get_width()/2, height/2+50+reback.get_height()/2))
                        # screen.blit(reback_menu, (width/2-reback.get_width()/2, height/2-reback.get_height()/2+50))
                        screen.blit(reback_menu, (width/2-reback_menu.get_width()/2, height/2+100+reback_menu.get_height()/2))
                        if pause == True:
                            screen.blit(resume, (width/2-resume.get_width()/2, height/2+150+resume.get_height()/2))
                        s3+=1
                        if s3 > 100:
                            s3 = 100
                            
                            
                    font = pygame.font.SysFont("comicsansms", 12)
                    text = font.render("Level: " + str(level), True, (0, 128, 0))
                    screen.blit(text,(width-80, 0))
                    
                    text2 = font.render(str(wall_bullet*4-i1), True, (0, 128, 0))
                    screen.blit(text2,(18, 5))
                    bulletpicture3 = pygame.transform.scale(bullet_alein1, (12, 15))
                    screen.blit(bulletpicture3, (5, 5))
                    
                    text3 = font.render(str(target_bullet*2-i), True, (0, 128, 0))
                    screen.blit(text3,(76, 5))
                    ship2 = pygame.transform.scale(bullet_target, (12, 15))
                    screen.blit(ship2, (60, 5))
                    
                    mouse = pygame.mouse.get_pos()
                    left, mid, right = pygame.mouse.get_pressed()
                    # if width-50 <= mouse[0] <= width-10 and 450 <= mouse[1] <= 470:
                    #     pygame.draw.rect(screen, RED, [width-50, 450, 40, 20],2)
                    #     if left:
                    #         lose1 = True
                    #         pause = True
                    # text = font.render("Pause", True, (0, 128, 0))
                    # screen.blit(text,(width-50, 450))

                    u+=1

                    if lose1 == False:
                        count_time += 15
                    # count_time1 += 10
                    time_display = font.render("Time: " + str(count_time/1000), True, (0, 128, 0))
                    screen.blit(time_display,(width-80, 20))
                    
                    pygame.display.update()
                    pygame.display.flip()
                    clock.tick(60)
                    

                # if h2 == True:
                #     if len(results.multi_handedness) == 1 and abs(xs - xs1) > 70:
                #         screen.fill((0,0,0))

                # if len(results.multi_handedness) == 2:
                #     cv2.putText(imgRGB, 'Both Hands', (250, 50),
                #                 cv2.FONT_HERSHEY_COMPLEX, 0.9,
                #                 (0, 255, 0), 2)
                # else:
                #     for ii in results.multi_handedness:         
                #         label = MessageToDict(ii)[
                #             'classification'][0]['label']
        
                #         if label == 'Left':
                #             cv2.putText(imgRGB, label+' Hand', (20, 50),
                #                         cv2.FONT_HERSHEY_COMPLEX, 0.9,
                #                         (0, 255, 0), 2)
        
                #         if label == 'Right':
                #             cv2.putText(imgRGB, label+' Hand', (460, 50),
                #                         cv2.FONT_HERSHEY_COMPLEX,
                #                         0.9, (0, 255, 0), 2)

                mp_drawing.draw_landmarks(
                    imgRGB,
                    hand_landmarks,
                    mpHands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=GREEN_color, thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=VIOLET, thickness=2, circle_radius=2))

                # mp_drawing.draw_landmarks(imgRGB, results2.face_landmarks, mp_holistic.FACE_CONNECTIONS)

        end = time.time()
        fps = 1/(end-start)
        # cv2.putText(imgRGB, 'FPS: ' + str(round(fps,3)), (350, 100),
        #                                 cv2.FONT_HERSHEY_COMPLEX,
        #                                 0.9, (0, 255, 0), 2)
        
        # cv2.putText(imgRGB, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)
        cv2.imshow("WebCam", imgRGB)
        cv2.waitKey(1)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        # t.fill((207, 181, 180))
        # b = pygame.draw.circle(t, (255,0,0), (x,y), 6)
        # v = pygame.draw.circle(t, (155,155,155), (500,y1), 10)
        # z = pygame.draw.line(t, (255,0,0), (xgg, ygg), (xgg, ygg1), 3)
        # z1 = pygame.draw.line(t, (255,0,0), (xgg, ygg1 + 50), (xgg, height), 3)
        # if b.colliderect(v): h = True
        # if b.colliderect(z): c = False
        # if b.colliderect(z1): c = False
        # if h:
        #     h = False

        # if x > 800:
        #     x = 800
        # if x < 0:
        #     x = 0
        # if y > 600:
        #     y = 600
        # if y < 0:
        #     y = 0

        # if xgg < 0:
        #     xgg = width
        #     ygg1 = random.randint(20,580)
        # xgg -= 10

        # if h2 == True:
        #     pygame.display.flip()
        #     pygame.display.update()
        #     clock.tick()

cap.release()
cv2.destroyAllWindows()
