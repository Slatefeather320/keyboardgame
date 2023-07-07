import win32com.client as comclt, time, pygame, random 
window = pygame.display.set_mode((300,10))
pygame.display.set_caption("Sanil's Screenless Game V0.5")
wsh= comclt.Dispatch("WScript.Shell")
score = 0
turn = 0
tturns = 50 #total turns (change this number for longer game)
def lq():
    wsh.SendKeys("{NUMLOCK}")
def lw():
    wsh.SendKeys("{CAPSLOCK}")
def le():
    wsh.SendKeys("{SCROLLLOCK}")

def flash():
    le();lw();lq()
    time.sleep(0.3)
    le();lw();lq()
    time.sleep(0.3)
def qflash():
    le();lw();lq()
    time.sleep(0.05)
    le();lw();lq()
    time.sleep(0.05)

def start():
    time.sleep(0.5)
    flash()
    time.sleep(0.5)
    flash()
    time.sleep(1)

    le();lw();lq()
    time.sleep(0.3)
    le();lw();lq()
    time.sleep(1)
    lq();lw()
    time.sleep(0.3)
    lq();lw()
    time.sleep(1)
    lq()
    time.sleep(0.3)
    lq()
    time.sleep(1)
    flash()
def end():
    global randy
    if randy == 1:
        lq()
    elif randy == 2:
        lw()
    elif randy == 3:
        le()
    time.sleep(0.5)
    flash()
    time.sleep(0.5)
    flash()
    time.sleep(1)
    for i in range(0,4):
        lq()
        time.sleep(0.2)
        lw()
        time.sleep(0.2)
        le()
        time.sleep(0.2)
def scoring(d):
    if score < 25:
        le()
        time.sleep(d)
        le()
    elif score < 30:
        lw()
        time.sleep(d)
        lw()
    elif score < 35:
        le();lw()
        time.sleep(d)
        le();lw()
    elif score < 40:
        lq()
        time.sleep(d)
        lq()
    elif score < 45:
        lq();le()
        time.sleep(d)
        lq();le()
    elif score < 50:
        lq();lw()
        time.sleep(d)
        lq();lw()
    else:
        lq();lw();le()
        time.sleep(d)
        lq();lw();le()
#start 
start()
startTime = time.time()
active = True 
clear = True 
while active == True and turn < tturns:
    if clear == True:
        turn+=1
        randy = random.randint(1,3)
        if randy == 1:
            lq()
            clear = False
        elif randy == 2:
            lw()
            clear = False
        elif randy == 3:
            le()
        clear = False
        print("turn-",turn, "score-", score)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            if randy == 1:
                clear = True
                lq()
                qflash()
                score+=1
            else:
                score -= 1
        if event.key == pygame.K_w:
            if randy == 2:
                clear = True
                lw()
                qflash()
                score+=1
            else:
                score -= 1
        if event.key == pygame.K_e:
            if randy == 3:
                clear = True
                le()
                qflash()
                score+=1
            else:
                score -= 1

end()
endTime = time.time()
time.sleep(0.2)
scoring(3)
print("time taken:", round(endTime - startTime), "seconds")
